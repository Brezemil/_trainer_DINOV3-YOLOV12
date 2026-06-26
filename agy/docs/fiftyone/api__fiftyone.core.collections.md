---
source_url: https://docs.voxel51.com/api/fiftyone.core.collections.html
---

# fiftyone.core.collections#

Interface for sample collections.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`view_stage`(func) |   
---|---  
`aggregation`(func) |   
  
**Classes:**

`SaveContext`(sample_collection[,Â batch_size,Â ...]) | Context that saves samples from a collection according to a configurable batching strategy.  
---|---  
`SampleCollection`() | Abstract class representing an ordered collection of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances in a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").  
  
fiftyone.core.collections.view_stage(_func_)#
    

fiftyone.core.collections.aggregation(_func_)#
    

class fiftyone.core.collections.SaveContext(_sample_collection_ , _batch_size =None_, _batching_strategy =None_, _async_writes =False_)#
    

Bases: `object`

Context that saves samples from a collection according to a configurable batching strategy.

Parameters:
    

  * **sample_collection** â a `fiftyone.core.collections.SampleCollection`

  * **batch_size** (_None_) â the batch size to use. If a `batching_strategy` is provided, this parameter configures the strategy as described below. If no `batching_strategy` is provided, this can either be an integer specifying the number of samples to save in a batch (in which case `batching_strategy` is implicitly set to `"static"`) or a float number of seconds between batched saves (in which case `batching_strategy` is implicitly set to `"latency"`)

  * **batching_strategy** (_None_) â 

the batching strategy to use for each save operation. Supported values are:

    * `"static"`: a fixed sample batch size for each save

    * `"size"`: a target batch size, in bytes, for each save

    * `"latency"`: a target latency, in seconds, between saves

By default, `fo.config.default_batcher` is used

  * **async_writes** (_False_) â whether to perform batch writes asynchronously in a background thread




**Methods:**

`save`(sample) | Registers the sample for saving in the next batch.  
---|---  
  
save(_sample_)#
    

Registers the sample for saving in the next batch.

Parameters:
    

**sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

class fiftyone.core.collections.SampleCollection#
    

Bases: `object`

Abstract class representing an ordered collection of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances in a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").

**Attributes:**

`name` | The name of the collection.  
---|---  
`media_type` | The media type of the collection.  
`group_field` | The group field of the collection, or None if the collection is not grouped.  
`group_slice` | The current group slice of the collection, or None if the collection is not grouped.  
`group_slices` | The list of group slices of the collection, or None if the collection is not grouped.  
`group_media_types` | A dict mapping group slices to media types, or None if the collection is not grouped.  
`default_group_slice` | The default group slice of the collection, or None if the collection is not grouped.  
`tags` | The list of tags of the underlying dataset.  
`description` | A description of the underlying dataset.  
`info` | The info dict of the underlying dataset.  
`app_config` | Dataset-specific settings that customize how this collection is visualized in the [FiftyOne App](user_guide__app.md#fiftyone-app).  
`classes` | The classes of the underlying dataset.  
`default_classes` | The default classes of the underlying dataset.  
`mask_targets` | The mask targets of the underlying dataset.  
`default_mask_targets` | The default mask targets of the underlying dataset.  
`skeletons` | The keypoint skeletons of the underlying dataset.  
`default_skeleton` | The default keypoint skeleton of the underlying dataset.  
`camera_intrinsics` | The camera intrinsics of the underlying dataset.  
`static_transforms` | The static transforms of the underlying dataset.  
`has_evaluations` | Whether this collection has any evaluation results.  
`has_brain_runs` | Whether this collection has any brain runs.  
`has_runs` | Whether this collection has any runs.  
`has_annotation_runs` | Whether this collection has any annotation runs.  
  
**Methods:**

`has_classes`(field) | Determines whether this collection has a classes list for the given field.  
---|---  
`get_classes`(field) | Gets the classes list for the given field, or None if no classes are available.  
`has_mask_targets`(field) | Determines whether this collection has mask targets for the given field.  
`get_mask_targets`(field) | Gets the mask targets for the given field, or None if no mask targets are available.  
`has_skeleton`(field) | Determines whether this collection has a keypoint skeleton for the given field.  
`get_skeleton`(field) | Gets the keypoint skeleton for the given field, or None if no skeleton is available.  
`summary`() | Returns a string summary of the collection.  
`sync_last_modified_at`([include_frames]) | Syncs the `last_modified_at` property(s) of the dataset.  
`stats`([include_media,Â include_indexes,Â ...]) | Returns stats about the collection on disk.  
`first`() | Returns the first sample in the collection.  
`last`() | Returns the last sample in the collection.  
`head`([num_samples]) | Returns a list of the first few samples in the collection.  
`tail`([num_samples]) | Returns a list of the last few samples in the collection.  
`one`(expr[,Â exact]) | Returns a single sample in this collection matching the expression.  
`view`() | Returns a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the collection.  
`iter_samples`([progress,Â autosave,Â ...]) | Returns an iterator over the samples in the collection.  
`iter_groups`([group_slices,Â progress,Â ...]) | Returns an iterator over the groups in the collection.  
`get_group`(group_id[,Â group_slices]) | Returns a dict containing the samples for the given group ID.  
`save_context`([batch_size,Â batching_strategy]) | Returns a context that can be used to save samples from this collection according to a configurable batching strategy.  
`get_field`(path[,Â ftype,Â embedded_doc_type,Â ...]) | Returns the field instance of the provided path, or `None` if one does not exist.  
`get_field_schema`([ftype,Â embedded_doc_type,Â ...]) | Returns a schema dictionary describing the fields of the samples in the collection.  
`get_frame_field_schema`([ftype,Â ...]) | Returns a schema dictionary describing the fields of the frames in the collection.  
`get_dynamic_field_schema`([fields,Â recursive]) | Returns a schema dictionary describing the dynamic fields of the samples in the collection.  
`get_dynamic_frame_field_schema`([fields,Â ...]) | Returns a schema dictionary describing the dynamic fields of the frames in the collection.  
`make_unique_field_name`([root]) | Makes a unique field name with the given root name for the collection.  
`has_field`(path) | Determines whether the collection has a field with the given name.  
`has_sample_field`(path) | Determines whether the collection has a sample field with the given name.  
`has_frame_field`(path) | Determines whether the collection has a frame-level field with the given name.  
`validate_fields_exist`(fields[,Â include_private]) | Validates that the collection has field(s) with the given name(s).  
`validate_field_type`(path[,Â ftype,Â ...]) | Validates that the collection has a field of the given type.  
`tag_samples`(tags) | Adds the tag(s) to all samples in this collection, if necessary.  
`untag_samples`(tags) | Removes the tag(s) from all samples in this collection, if necessary.  
`count_sample_tags`() | Counts the occurrences of sample tags in this collection.  
`tag_labels`(tags[,Â label_fields]) | Adds the tag(s) to all labels in the specified label field(s) of this collection, if necessary.  
`untag_labels`(tags[,Â label_fields]) | Removes the tag from all labels in the specified label field(s) of this collection, if necessary.  
`count_label_tags`([label_fields]) | Counts the occurrences of all label tags in the specified label field(s) of this collection.  
`split_labels`(in_field,Â out_field[,Â filter]) | Splits the labels from the given input field into the given output field of the collection.  
`merge_labels`(in_field,Â out_field) | Merges the labels from the given input field into the given output field of the collection.  
`set_values`(field_name,Â values[,Â key_field,Â ...]) | Sets the field or embedded field on each sample or frame in the collection to the given values.  
`set_label_values`(field_name,Â values[,Â ...]) | Sets the fields of the specified labels in the collection to the given values.  
`compute_metadata`([overwrite,Â num_workers,Â ...]) | Populates the `metadata` field of all samples in the collection.  
`generate_label_schemas`([fields,Â scan_samples]) | Generates label schemas for the `fiftyone.core.collections.SampleCollection`.  
`apply_model`(model[,Â label_field,Â ...]) | Applies the model to the samples in the collection.  
`compute_embeddings`(model[,Â ...]) | Computes embeddings for the samples in the collection using the given model.  
`compute_patch_embeddings`(model,Â patches_field) | Computes embeddings for the image patches defined by `patches_field` of the samples in the collection using the given model.  
`evaluate_regressions`(pred_field[,Â gt_field,Â ...]) | Evaluates the regression predictions in this collection with respect to the specified ground truth values.  
`evaluate_classifications`(pred_field[,Â ...]) | Evaluates the classification predictions in this collection with respect to the specified ground truth labels.  
`evaluate_detections`(pred_field[,Â gt_field,Â ...]) | Evaluates the specified predicted detections in this collection with respect to the specified ground truth detections.  
`evaluate_segmentations`(pred_field[,Â ...]) | Evaluates the specified semantic segmentation masks in this collection with respect to the specified ground truth masks.  
`has_evaluation`(eval_key) | Whether this collection has an evaluation with the given key.  
`list_evaluations`([type,Â method]) | Returns a list of evaluation keys on this collection.  
`map_samples`(map_fcn[,Â save,Â skip_failures,Â ...]) | Applies the given function to each sample in the collection and returns the results as a generator.  
`update_samples`(update_fcn[,Â skip_failures,Â ...]) | Applies the given function to each sample in the collection and saves the resulting sample edits.  
`rename_evaluation`(eval_key,Â new_eval_key) | Replaces the key for the given evaluation with a new key.  
`get_evaluation_info`(eval_key) | Returns information about the evaluation with the given key on this collection.  
`load_evaluation_results`(eval_key[,Â cache]) | Loads the results for the evaluation with the given key on this collection.  
`load_evaluation_view`(eval_key[,Â select_fields]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified evaluation was performed on this collection.  
`delete_evaluation`(eval_key) | Deletes the evaluation results associated with the given evaluation key from this collection.  
`delete_evaluations`() | Deletes all evaluation results from this collection.  
`has_brain_run`(brain_key) | Whether this collection has a brain method run with the given key.  
`list_brain_runs`([type,Â method]) | Returns a list of brain keys on this collection.  
`rename_brain_run`(brain_key,Â new_brain_key) | Replaces the key for the given brain run with a new key.  
`get_brain_info`(brain_key) | Returns information about the brain method run with the given key on this collection.  
`load_brain_results`(brain_key[,Â cache,Â load_view]) | Loads the results for the brain method run with the given key on this collection.  
`load_brain_view`(brain_key[,Â select_fields]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified brain method run was performed on this collection.  
`delete_brain_run`(brain_key) | Deletes the brain method run with the given key from this collection.  
`delete_brain_runs`() | Deletes all brain method runs from this collection.  
`has_run`(run_key) | Whether this collection has a run with the given key.  
`list_runs`(**kwargs) | Returns a list of run keys on this collection.  
`init_run`(**kwargs) | Initializes a config instance for a new run.  
`register_run`(run_key,Â config[,Â results,Â ...]) | Registers a run under the given key on this collection.  
`rename_run`(run_key,Â new_run_key) | Replaces the key for the given run with a new key.  
`get_run_info`(run_key) | Returns information about the run with the given key on this collection.  
`update_run_config`(run_key,Â config) | Updates the run config for the run with the given key.  
`init_run_results`(run_key,Â **kwargs) | Initializes a results instance for the run with the given key.  
`save_run_results`(run_key,Â results[,Â ...]) | Saves run results for the run with the given key.  
`load_run_results`(run_key[,Â cache,Â load_view]) | Loads the results for the run with the given key on this collection.  
`load_run_view`(run_key[,Â select_fields]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified run was performed on this collection.  
`delete_run`(run_key) | Deletes the run with the given key from this collection.  
`delete_runs`() | Deletes all runs from this collection.  
`list_view_stages`() | Returns a list of all available methods on this collection that apply [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") operations to this collection.  
`add_stage`(stage) | Applies the given [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") to the collection.  
`concat`(samples) | Concatenates the contents of the given `SampleCollection` to this collection.  
`exclude`(sample_ids) | Excludes the samples with the given IDs from the collection.  
`exclude_by`(field,Â values) | Excludes the samples with the given field values from the collection.  
`exclude_fields`([field_names,Â meta_filter,Â ...]) | Excludes the fields with the given names from the samples in the collection.  
`exclude_frames`(frame_ids[,Â omit_empty]) | Excludes the frames with the given IDs from the video collection.  
`exclude_groups`(group_ids) | Excludes the groups with the given IDs from the grouped collection.  
`exclude_group_slices`([slices,Â media_type]) | Excludes the specified group slice(s) from the grouped collection.  
`exclude_labels`([labels,Â ids,Â instance_ids,Â ...]) | Excludes the specified labels from the collection.  
`exists`(field[,Â bool]) | Returns a view containing the samples in the collection that have (or do not have) a non-`None` value for the given field or embedded field.  
`filter_field`(field,Â filter[,Â only_matches]) | Filters the values of a field or embedded field of each sample in the collection.  
`filter_labels`(field,Â filter[,Â only_matches,Â ...]) | Filters the [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field of each sample in the collection.  
`filter_keypoints`(field[,Â filter,Â labels,Â ...]) | Filters the individual [`fiftyone.core.labels.Keypoint.points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points") elements in the specified keypoints field of each sample in the collection.  
`flatten`([stages]) | Returns a flattened view that contains all samples in the dynamic grouped collection.  
`geo_near`(point[,Â location_field,Â ...]) | Sorts the samples in the collection by their proximity to a specified geolocation.  
`geo_within`(boundary[,Â location_field,Â ...]) | Filters the samples in this collection to only include samples whose geolocation is within a specified boundary.  
`group_by`(field_or_expr[,Â order_by,Â reverse,Â ...]) | Creates a view that groups the samples in the collection by a specified field or expression.  
`limit`(limit) | Returns a view with at most the given number of samples.  
`limit_labels`(field,Â limit) | Limits the number of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances in the specified labels list field of each sample in the collection.  
`map_labels`(field,Â map) | Maps the `label` values of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field to new values for each sample in the collection.  
`map_values`(field,Â map) | Maps the values in the given field to new values for each sample in the collection.  
`set_field`(field,Â expr[,Â _allow_missing]) | Sets a field or embedded field on each sample in a collection by evaluating the given expression.  
`match`(filter) | Filters the samples in the collection by the given filter.  
`match_frames`(filter[,Â omit_empty]) | Filters the frames in the video collection by the given filter.  
`match_labels`([labels,Â ids,Â instance_ids,Â ...]) | Selects the samples from the collection that contain (or do not contain) at least one label that matches the specified criteria.  
`match_tags`(tags[,Â bool,Â all]) | Returns a view containing the samples in the collection that have or don't have any/all of the given tag(s).  
`mongo`(pipeline[,Â _needs_frames,Â _group_slices]) | Adds a view stage defined by a raw MongoDB aggregation pipeline.  
`select`(sample_ids[,Â ordered]) | Selects the samples with the given IDs from the collection.  
`select_by`(field,Â values[,Â ordered]) | Selects the samples with the given field values from the collection.  
`select_fields`([field_names,Â meta_filter,Â ...]) | Selects only the fields with the given names from the samples in the collection.  
`select_frames`(frame_ids[,Â omit_empty]) | Selects the frames with the given IDs from the video collection.  
`select_groups`(group_ids[,Â ordered]) | Selects the groups with the given IDs from the grouped collection.  
`select_group_slices`([slices,Â media_type,Â ...]) | Selects the specified group slice(s) from the grouped collection.  
`select_labels`([labels,Â ids,Â instance_ids,Â ...]) | Selects only the specified labels from the collection.  
`shuffle`([seed]) | Randomly shuffles the samples in the collection.  
`skip`(skip) | Omits the given number of samples from the head of the collection.  
`sort_by`(field_or_expr[,Â reverse,Â create_index]) | Sorts the samples in the collection by the given field(s) or expression(s).  
`sort_by_similarity`(query[,Â k,Â reverse,Â ...]) | Sorts the collection by similarity to a specified query.  
`take`(size[,Â seed]) | Randomly samples the given number of samples from the collection.  
`to_patches`(field,Â **kwargs) | Creates a view that contains one sample per object patch in the specified field of the collection.  
`to_evaluation_patches`(eval_key,Â **kwargs) | Creates a view based on the results of the evaluation with the given key that contains one sample for each true positive, false positive, and false negative example in the collection, respectively.  
`to_clips`(field_or_expr,Â **kwargs) | Creates a view that contains one sample per clip defined by the given field or expression in the video collection.  
`to_trajectories`(field,Â **kwargs) | Creates a view that contains one clip for each unique object trajectory defined by their `(label, index)` in a frame-level field of a video collection.  
`to_frames`(**kwargs) | Creates a view that contains one sample per frame in the video collection.  
`list_aggregations`() | Returns a list of all available methods on this collection that apply [`fiftyone.core.aggregations.Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") operations to this collection.  
`bounds`(field_or_expr[,Â expr,Â safe]) | Computes the bounds of a numeric field of the collection.  
`count`([field_or_expr,Â expr,Â safe]) | Counts the number of field values in the collection.  
`count_values`(field_or_expr[,Â expr,Â safe]) | Counts the occurrences of field values in the collection.  
`distinct`(field_or_expr[,Â expr,Â safe]) | Computes the distinct values of a field in the collection.  
`histogram_values`(field_or_expr[,Â expr,Â ...]) | Computes a histogram of the field values in the collection.  
`min`(field_or_expr[,Â expr,Â safe]) | Computes the minimum of a numeric field of the collection.  
`max`(field_or_expr[,Â expr,Â safe]) | Computes the maximum of a numeric field of the collection.  
`mean`(field_or_expr[,Â expr,Â safe]) | Computes the arithmetic mean of the field values of the collection.  
`quantiles`(field_or_expr,Â quantiles[,Â expr,Â safe]) | Computes the quantile(s) of the field values of a collection.  
`schema`(field_or_expr[,Â expr,Â dynamic_only,Â ...]) | Extracts the names and types of the attributes of a specified embedded document field across all samples in the collection.  
`list_schema`(field_or_expr[,Â expr]) | Extracts the value type(s) in a specified list field across all samples in the collection.  
`std`(field_or_expr[,Â expr,Â safe,Â sample]) | Computes the standard deviation of the field values of the collection.  
`sum`(field_or_expr[,Â expr,Â safe]) | Computes the sum of the field values of the collection.  
`values`(field_or_expr[,Â expr,Â missing_value,Â ...]) | Extracts the values of a field from all samples in the collection.  
`draw_labels`(output_dir[,Â rel_dir,Â ...]) | Renders annotated versions of the media in the collection with the specified label data overlaid to the given directory.  
`export`([export_dir,Â dataset_type,Â ...]) | Exports the samples in the collection to disk.  
`to_torch`(get_item[,Â vectorize,Â ...]) | Constructs a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") that loads data from this collection via the provided [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance.  
`annotate`(anno_key[,Â label_schema,Â ...]) | Exports the samples and optional label field(s) in this collection to the given annotation backend.  
`has_annotation_run`(anno_key) | Whether this collection has an annotation run with the given key.  
`list_annotation_runs`([type,Â method]) | Returns a list of annotation keys on this collection.  
`rename_annotation_run`(anno_key,Â new_anno_key) | Replaces the key for the given annotation run with a new key.  
`get_annotation_info`(anno_key) | Returns information about the annotation run with the given key on this collection.  
`load_annotation_results`(anno_key[,Â cache]) | Loads the results for the annotation run with the given key on this collection.  
`load_annotation_view`(anno_key[,Â select_fields]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified annotation run was performed on this collection.  
`load_annotations`(anno_key[,Â dest_field,Â ...]) | Downloads the labels from the given annotation run from the annotation backend and merges them into this collection.  
`delete_annotation_run`(anno_key) | Deletes the annotation run with the given key from this collection.  
`delete_annotation_runs`() | Deletes all annotation runs from this collection.  
`list_indexes`() | Returns the list of index names on this collection.  
`get_index_information`([include_stats,Â ...]) | Returns a dictionary of information about the indexes on this collection.  
`create_index`(field_or_spec[,Â unique,Â force,Â ...]) | Creates an index on the given field or with the given specification, if necessary.  
`drop_index`(field_or_name) | Drops the index for the given field or name, if necessary.  
`reload`() | Reloads the collection from the database.  
`to_dict`([rel_dir,Â include_private,Â ...]) | Returns a JSON dictionary representation of the collection.  
`to_json`([rel_dir,Â include_private,Â ...]) | Returns a JSON string representation of the collection.  
`write_json`(json_path[,Â rel_dir,Â ...]) | Writes the collection to disk in JSON format.  
`aggregate`(aggregations[,Â _mongo]) | Aggregates one or more [`fiftyone.core.aggregations.Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") instances.  
  
property name#
    

The name of the collection.

property media_type#
    

The media type of the collection.

property group_field#
    

The group field of the collection, or None if the collection is not grouped.

property group_slice#
    

The current group slice of the collection, or None if the collection is not grouped.

property group_slices#
    

The list of group slices of the collection, or None if the collection is not grouped.

property group_media_types#
    

A dict mapping group slices to media types, or None if the collection is not grouped.

property default_group_slice#
    

The default group slice of the collection, or None if the collection is not grouped.

property tags#
    

The list of tags of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.tags()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.tags "fiftyone.core.dataset.Dataset.tags") for more information.

property description#
    

A description of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.description()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.description "fiftyone.core.dataset.Dataset.description") for more information.

property info#
    

The info dict of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.info()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.info "fiftyone.core.dataset.Dataset.info") for more information.

property app_config#
    

Dataset-specific settings that customize how this collection is visualized in the [FiftyOne App](user_guide__app.md#fiftyone-app).

property classes#
    

The classes of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.classes()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.classes "fiftyone.core.dataset.Dataset.classes") for more information.

property default_classes#
    

The default classes of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.default_classes()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_classes "fiftyone.core.dataset.Dataset.default_classes") for more information.

has_classes(_field_)#
    

Determines whether this collection has a classes list for the given field.

Classes may be defined either in `classes()` or `default_classes()`.

Parameters:
    

**field** â a field name

Returns:
    

True/False

get_classes(_field_)#
    

Gets the classes list for the given field, or None if no classes are available.

Classes are first retrieved from `classes()` if they exist, otherwise from `default_classes()`.

Parameters:
    

**field** â a field name

Returns:
    

a list of classes, or None

property mask_targets#
    

The mask targets of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.mask_targets()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.mask_targets "fiftyone.core.dataset.Dataset.mask_targets") for more information.

property default_mask_targets#
    

The default mask targets of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.default_mask_targets()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_mask_targets "fiftyone.core.dataset.Dataset.default_mask_targets") for more information.

has_mask_targets(_field_)#
    

Determines whether this collection has mask targets for the given field.

Mask targets may be defined either in `mask_targets()` or `default_mask_targets()`.

Parameters:
    

**field** â a field name

Returns:
    

True/False

get_mask_targets(_field_)#
    

Gets the mask targets for the given field, or None if no mask targets are available.

Mask targets are first retrieved from `mask_targets()` if they exist, otherwise from `default_mask_targets()`.

Parameters:
    

**field** â a field name

Returns:
    

a list of classes, or None

property skeletons#
    

The keypoint skeletons of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.skeletons()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.skeletons "fiftyone.core.dataset.Dataset.skeletons") for more information.

property default_skeleton#
    

The default keypoint skeleton of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.default_skeleton()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_skeleton "fiftyone.core.dataset.Dataset.default_skeleton") for more information.

property camera_intrinsics#
    

The camera intrinsics of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.camera_intrinsics()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.camera_intrinsics "fiftyone.core.dataset.Dataset.camera_intrinsics") for more information.

property static_transforms#
    

The static transforms of the underlying dataset.

See [`fiftyone.core.dataset.Dataset.static_transforms()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.static_transforms "fiftyone.core.dataset.Dataset.static_transforms") for more information.

has_skeleton(_field_)#
    

Determines whether this collection has a keypoint skeleton for the given field.

Keypoint skeletons may be defined either in `skeletons()` or `default_skeleton()`.

Parameters:
    

**field** â a field name

Returns:
    

True/False

get_skeleton(_field_)#
    

Gets the keypoint skeleton for the given field, or None if no skeleton is available.

Skeletons are first retrieved from `skeletons()` if they exist, otherwise from `default_skeleton()`.

Parameters:
    

**field** â a field name

Returns:
    

a list of classes, or None

summary()#
    

Returns a string summary of the collection.

Returns:
    

a string summary

sync_last_modified_at(_include_frames =True_)#
    

Syncs the `last_modified_at` property(s) of the dataset.

Updates the `last_modified_at` property of the dataset if necessary to incorporate any modification/deletion timestamps to its samples.

If `include_frames==True`, the `last_modified_at` property of each video sample is first updated if necessary to incorporate any modification timestamps to its frames.

Parameters:
    

**include_frames** (_True_) â whether to update the `last_modified_at` property of video samples. Only applicable to datasets that contain videos

stats(_include_media =False_, _include_indexes =False_, _compressed =False_)#
    

Returns stats about the collection on disk.

The `samples` keys refer to the sample documents stored in the database.

For video datasets, the `frames` keys refer to the frame documents stored in the database.

The `media` keys refer to the raw media associated with each sample on disk.

The `index[es]` keys refer to the indexes associated with the dataset.

Note that dataset-level metadata such as annotation runs are not included in this computation.

Parameters:
    

  * **include_media** (_False_) â whether to include stats about the size of the raw media in the collection

  * **include_indexes** (_False_) â whether to include stats on the datasetâs indexes

  * **compressed** (_False_) â whether to return the sizes of collections in their compressed form on disk (True) or the logical uncompressed size of the collections (False). This option is only supported for datasets (not views)



Returns:
    

a stats dict

first()#
    

Returns the first sample in the collection.

Returns:
    

a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

last()#
    

Returns the last sample in the collection.

Returns:
    

a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

head(_num_samples =3_)#
    

Returns a list of the first few samples in the collection.

If fewer than `num_samples` samples are in the collection, only the available samples are returned.

Parameters:
    

**num_samples** (_3_) â the number of samples

Returns:
    

a list of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects

tail(_num_samples =3_)#
    

Returns a list of the last few samples in the collection.

If fewer than `num_samples` samples are in the collection, only the available samples are returned.

Parameters:
    

**num_samples** (_3_) â the number of samples

Returns:
    

a list of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects

one(_expr_ , _exact =False_)#
    

Returns a single sample in this collection matching the expression.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Get a sample by filepath
    #
    
    # A random filepath in the dataset
    filepath = dataset.take(1).first().filepath
    
    # Get sample by filepath
    sample = dataset.one(F("filepath") == filepath)
    
    #
    # Dealing with multiple matches
    #
    
    # Get a sample whose image is JPEG
    sample = dataset.one(F("filepath").ends_with(".jpg"))
    
    # Raises an error since there are multiple JPEGs
    dataset.one(F("filepath").ends_with(".jpg"), exact=True)
    

Parameters:
    

  * **expr** â a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that evaluates to `True` for the sample to match

  * **exact** (_False_) â whether to raise an error if multiple samples match the expression



Raises:
    

  * **ValueError** â if no samples match the expression or if `exact=True`

  * **and multiple samples match the expression** â 



Returns:
    

a [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

view()#
    

Returns a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the collection.

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

iter_samples(_progress =False_, _autosave =False_, _batch_size =None_, _batching_strategy =None_)#
    

Returns an iterator over the samples in the collection.

Parameters:
    

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **autosave** (_False_) â whether to automatically save changes to samples emitted by this iterator

  * **batch_size** (_None_) â the batch size to use when autosaving samples. If a `batching_strategy` is provided, this parameter configures the strategy as described below. If no `batching_strategy` is provided, this can either be an integer specifying the number of samples to save in a batch (in which case `batching_strategy` is implicitly set to `"static"`) or a float number of seconds between batched saves (in which case `batching_strategy` is implicitly set to `"latency"`)

  * **batching_strategy** (_None_) â 

the batching strategy to use for each save operation when autosaving samples. Supported values are:

    * `"static"`: a fixed sample batch size for each save

    * `"size"`: a target batch size, in bytes, for each save

    * `"latency"`: a target latency, in seconds, between saves

By default, `fo.config.default_batcher` is used



Returns:
    

an iterator over [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

iter_groups(_group_slices =None_, _progress =False_, _autosave =False_, _batch_size =None_, _batching_strategy =None_)#
    

Returns an iterator over the groups in the collection.

Parameters:
    

  * **group_slices** (_None_) â an optional subset of group slices to load

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **autosave** (_False_) â whether to automatically save changes to samples emitted by this iterator

  * **batch_size** (_None_) â the batch size to use when autosaving samples. If a `batching_strategy` is provided, this parameter configures the strategy as described below. If no `batching_strategy` is provided, this can either be an integer specifying the number of samples to save in a batch (in which case `batching_strategy` is implicitly set to `"static"`) or a float number of seconds between batched saves (in which case `batching_strategy` is implicitly set to `"latency"`)

  * **batching_strategy** (_None_) â 

the batching strategy to use for each save operation when autosaving samples. Supported values are:

    * `"static"`: a fixed sample batch size for each save

    * `"size"`: a target batch size, in bytes, for each save

    * `"latency"`: a target latency, in seconds, between saves

By default, `fo.config.default_batcher` is used



Returns:
    

an iterator that emits dicts mapping group slice names to [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances, one per group

get_group(_group_id_ , _group_slices =None_)#
    

Returns a dict containing the samples for the given group ID.

Parameters:
    

  * **group_id** â a group ID

  * **group_slices** (_None_) â an optional subset of group slices to load



Returns:
    

a dict mapping group names to [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

Raises:
    

**KeyError** â if the group ID is not found

save_context(_batch_size =None_, _batching_strategy =None_)#
    

Returns a context that can be used to save samples from this collection according to a configurable batching strategy.

Examples:
    
    
    import random as r
    import string as s
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("cifar10", split="test")
    
    def make_label():
        return "".join(r.choice(s.ascii_letters) for i in range(10))
    
    # No save context
    for sample in dataset.iter_samples(progress=True):
        sample.ground_truth.label = make_label()
        sample.save()
    
    # Save using default batching strategy
    with dataset.save_context() as context:
        for sample in dataset.iter_samples(progress=True):
            sample.ground_truth.label = make_label()
            context.save(sample)
    
    # Save in batches of 10
    with dataset.save_context(batch_size=10) as context:
        for sample in dataset.iter_samples(progress=True):
            sample.ground_truth.label = make_label()
            context.save(sample)
    
    # Save every 0.5 seconds
    with dataset.save_context(batch_size=0.5) as context:
        for sample in dataset.iter_samples(progress=True):
            sample.ground_truth.label = make_label()
            context.save(sample)
    

Parameters:
    

  * **batch_size** (_None_) â the batch size to use. If a `batching_strategy` is provided, this parameter configures the strategy as described below. If no `batching_strategy` is provided, this can either be an integer specifying the number of samples to save in a batch (in which case `batching_strategy` is implicitly set to `"static"`) or a float number of seconds between batched saves (in which case `batching_strategy` is implicitly set to `"latency"`)

  * **batching_strategy** (_None_) â 

the batching strategy to use for each save operation. Supported values are:

    * `"static"`: a fixed sample batch size for each save

    * `"size"`: a target batch size, in bytes, for each save

    * `"latency"`: a target latency, in seconds, between saves

By default, `fo.config.default_batcher` is used



Returns:
    

a `SaveContext`

get_field(_path_ , _ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _include_private =False_, _leaf =False_)#
    

Returns the field instance of the provided path, or `None` if one does not exist.

Parameters:
    

  * **path** â a field path

  * **ftype** (_None_) â an optional field type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to enforce. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **read_only** (_None_) â whether to optionally enforce that the field is read-only (True) or not read-only (False)

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema

  * **leaf** (_False_) â whether to return the subfield of list fields



Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instance or `None`

Raises:
    

**ValueError** â if the field does not match provided constraints

get_field_schema(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Returns a schema dictionary describing the fields of the samples in the collection.

Parameters:
    

  * **ftype** (_None_) â an optional field type or iterable of types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **read_only** (_None_) â whether to restrict to (True) or exclude (False) read-only fields. By default, all fields are included

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema

  * **flat** (_False_) â whether to return a flattened schema where all embedded document fields are included as top-level keys

  * **unwind** (_True_) â whether to traverse into list fields. Only applicable when `flat=True`

  * **mode** (_None_) â whether to apply the above constraints before and/or after flattening the schema. Only applicable when `flat=True`. Supported values are `("before", "after", "both")`. The default is `"after"`



Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances

get_frame_field_schema(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Returns a schema dictionary describing the fields of the frames in the collection.

Only applicable for collections that contain videos.

Parameters:
    

  * **ftype** (_None_) â an optional field type to which to restrict the returned schema. Must be a subclass of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type to which to restrict the returned schema. Must be a subclass of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **read_only** (_None_) â whether to restrict to (True) or exclude (False) read-only fields. By default, all fields are included

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema

  * **flat** (_False_) â whether to return a flattened schema where all embedded document fields are included as top-level keys

  * **unwind** (_True_) â whether to traverse into list fields. Only applicable when `flat=True`

  * **mode** (_None_) â whether to apply the above constraints before and/or after flattening the schema. Only applicable when `flat=True`. Supported values are `("before", "after", "both")`. The default is `"after"`



Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances, or `None` if the collection does not contain videos

get_dynamic_field_schema(_fields =None_, _recursive =True_)#
    

Returns a schema dictionary describing the dynamic fields of the samples in the collection.

Dynamic fields are embedded document fields with at least one non-None value that have not been declared on the datasetâs schema.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields for which to return dynamic fields. By default, all fields are considered

  * **recursive** (_True_) â whether to recursively inspect nested lists and embedded documents



Returns:
    

a dict mapping field paths to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or lists of them

get_dynamic_frame_field_schema(_fields =None_, _recursive =True_)#
    

Returns a schema dictionary describing the dynamic fields of the frames in the collection.

Dynamic fields are embedded document fields with at least one non-None value that have not been declared on the datasetâs schema.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields for which to return dynamic fields. By default, all fields are considered

  * **recursive** (_True_) â whether to recursively inspect nested lists and embedded documents



Returns:
    

a dict mapping field paths to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or lists of them, or `None` if the collection does not contain videos

make_unique_field_name(_root =''_)#
    

Makes a unique field name with the given root name for the collection.

Parameters:
    

**root** â an optional root for the output field name

Returns:
    

the field name

has_field(_path_)#
    

Determines whether the collection has a field with the given name.

Parameters:
    

**path** â the field name or `embedded.field.name`

Returns:
    

True/False

has_sample_field(_path_)#
    

Determines whether the collection has a sample field with the given name.

Parameters:
    

**path** â the field name or `embedded.field.name`

Returns:
    

True/False

has_frame_field(_path_)#
    

Determines whether the collection has a frame-level field with the given name.

Parameters:
    

**path** â the field name or `embedded.field.name`

Returns:
    

True/False

validate_fields_exist(_fields_ , _include_private =False_)#
    

Validates that the collection has field(s) with the given name(s).

If embedded field names are provided, only the root field is checked.

Parameters:
    

  * **fields** â a field name or iterable of field names

  * **include_private** (_False_) â whether to include private fields when checking for existence



Raises:
    

**ValueError** â if one or more of the fields do not exist

validate_field_type(_path_ , _ftype =None_, _embedded_doc_type =None_, _subfield =None_)#
    

Validates that the collection has a field of the given type.

Parameters:
    

  * **path** â a field name or `embedded.field.name`

  * **ftype** (_None_) â an optional field type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to enforce. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")



Raises:
    

**ValueError** â if the field does not exist or does not have the expected type

tag_samples(_tags_)#
    

Adds the tag(s) to all samples in this collection, if necessary.

Parameters:
    

**tags** â a tag or iterable of tags

untag_samples(_tags_)#
    

Removes the tag(s) from all samples in this collection, if necessary.

Parameters:
    

**tags** â a tag or iterable of tags

count_sample_tags()#
    

Counts the occurrences of sample tags in this collection.

Returns:
    

a dict mapping tags to counts

tag_labels(_tags_ , _label_fields =None_)#
    

Adds the tag(s) to all labels in the specified label field(s) of this collection, if necessary.

Parameters:
    

  * **tags** â a tag or iterable of tags

  * **label_fields** (_None_) â an optional name or iterable of names of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields. By default, all label fields are used




untag_labels(_tags_ , _label_fields =None_)#
    

Removes the tag from all labels in the specified label field(s) of this collection, if necessary.

Parameters:
    

  * **tags** â a tag or iterable of tags

  * **label_fields** (_None_) â an optional name or iterable of names of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields. By default, all label fields are used




count_label_tags(_label_fields =None_)#
    

Counts the occurrences of all label tags in the specified label field(s) of this collection.

Parameters:
    

**label_fields** (_None_) â an optional name or iterable of names of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields. By default, all label fields are used

Returns:
    

a dict mapping tags to counts

split_labels(_in_field_ , _out_field_ , _filter =None_)#
    

Splits the labels from the given input field into the given output field of the collection.

This method is typically invoked on a view that has filtered the contents of the specified input field, so that the labels in the view are moved to the output field and the remaining labels are left in-place.

Alternatively, you can provide a `filter` expression that selects the labels of interest to move in this collection.

Parameters:
    

  * **in_field** â the name of the input label field

  * **out_field** â the name of the output label field, which will be created if necessary

  * **filter** (_None_) â a boolean [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") to apply to each label in the input field to determine whether to move it (True) or leave it (False)




merge_labels(_in_field_ , _out_field_)#
    

Merges the labels from the given input field into the given output field of the collection.

If this collection is a dataset, the input field is deleted after the merge.

If this collection is a view, the input field will still exist on the underlying dataset but will only contain the labels not present in this view.

Parameters:
    

  * **in_field** â the name of the input label field

  * **out_field** â the name of the output label field, which will be created if necessary




set_values(_field_name_ , _values_ , _key_field =None_, _skip_none =False_, _expand_schema =True_, _dynamic =False_, _validate =True_, _progress =False_, __allow_missing =False_, __sample_ids =None_, __frame_ids =None_)#
    

Sets the field or embedded field on each sample or frame in the collection to the given values.

You can use this method in two ways:

  * **Dict syntax (recommended):** provide `values` as a dict whose keys specify the `key_field` values of the samples whose `field_name` you want to set to the corresponding values

  * **List syntax:** provide `values` as a list, one for each sample in the collection on which you are invoking this method




Note

The most performant strategy for setting large numbers of field values is to use the dict syntax with `key_field="id"` when setting sample fields and `key_field="frames.id"` when setting frame fields. All other syntaxes internally convert to these IDs before ultimately performing the updates.

When setting a sample field `embedded.field.name` via the list `values` syntax, this function is an efficient implementation of the following loop:
    
    
    for sample, value in zip(sample_collection, values):
        sample.embedded.field.name = value
        sample.save()
    

When setting an embedded field that contains an array, say `embedded.array.field.name`, via the list `values` syntax, this function is an efficient implementation of the following loop:
    
    
    for sample, array_values in zip(sample_collection, values):
        for doc, value in zip(sample.embedded.array, array_values):
            doc.field.name = value
    
        sample.save()
    

When setting a frame field `frames.embedded.field.name` via the list `values` syntax, this function is an efficient implementation of the following loop:
    
    
    for sample, frame_values in zip(sample_collection, values):
        for frame, value in zip(sample.frames.values(), frame_values):
            frame.embedded.field.name = value
    
        sample.save()
    

When setting an embedded frame field that contains an array, say `frames.embedded.array.field.name`, via the list `values` syntax, this function is an efficient implementation of the following loop:
    
    
    for sample, frame_values in zip(sample_collection, values):
        for frame, array_values in zip(sample.frames.values(), frame_values):
            for doc, value in zip(frame.embedded.array, array_values):
                doc.field.name = value
    
        sample.save()
    

When setting a sample field `embedded.field.name` via the dict `values` syntax, this function is an efficient implementation of the following loop:
    
    
    for key, value in values.items():
        sample = sample_collection.one(F(key_field) == key)
        sample.embedded.field.name = value
        sample.save()
    

When setting frame fields using the dict `values` syntax with a frame-level `key_field`, this function is an efficient implementation of the following loop:
    
    
    frames = sample_collection.to_frames(...)
    for key, value in values.items():
        frame = frames.one(F(key_field) == key)
        frame.embedded.field.name = value
        frame.save()
    

When setting frame fields using the dict `values` syntax with a sample-level `key_field`, each value in `values` may either be a list corresponding to the frames of the sample matching the given key, or each value may itself be a dict mapping frame numbers to values. In the latter case, this function is an efficient implementation of the following loop:
    
    
    for key, frame_values in values.items():
        sample = sample_collection.one(F(key_field) == key)
        for frame_number, value in frame_values.items():
            frame = sample[frame_number]
            frame.embedded.field.name = value
    
        sample.save()
    

You can also update list fields using the dict `values` syntaxes, in which case this method is an efficient implementation of the natural nested list modifications of the above sample/frame loops.

The dual function of `set_values()` is `values()`, which can be used to efficiently extract the values of a field or embedded field of all samples in a collection as lists of values.

Note

If you are setting attributes of a nested list of labels, such as attributes of the objects in a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field, then consider using `set_label_values()` instead for greater efficiency.

Note

If the values you are setting can be described by a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") applied to the existing dataset contents, then consider using `set_field()` \+ [`save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") for an even more efficient alternative to explicitly iterating over the dataset or calling `values()` \+ `set_values()` to perform the update in-memory.

Examples:
    
    
    import random
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Create a new sample field
    #
    
    # list syntax
    values = [random.random() for _ in range(len(dataset))]
    
    dataset.set_values("random", values)
    
    print(dataset.bounds("random"))
    
    #
    # Edit a frame field
    #
    
    # dict syntax
    sample_ids = dataset.values("id")
    values = {id: random.random() for id in sample_ids}
    
    dataset.set_values("random", values, key_field="id")
    
    print(dataset.bounds("random"))
    
    #
    # Add a tag to all low confidence labels
    #
    
    view = dataset.filter_labels("predictions", F("confidence") < 0.06)
    
    # list syntax on a filtered view
    tags = view.values("predictions.detections.tags")
    for sample_tags in tags:
        for detection_tags in sample_tags:
            detection_tags.append("low_confidence")
    
    view.set_values("predictions.detections.tags", tags)
    
    print(view.count("predictions.detections"))  # 447
    print(dataset.count_label_tags())  # 447
    
    #
    # Create a new frame field
    #
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    # list syntax
    values = []
    for sample in dataset:
        values.append([random.random() for _ in sample.frames])
    
    dataset.set_values("frames.random", values)
    
    print(dataset.bounds("frames.random"))
    
    #
    # Edit a frame field
    #
    
    # dict syntax
    frame_ids = dataset.values("frames.id", unwind=True)
    values = {id: random.random() for id in frame_ids}
    
    dataset.set_values("frames.random", values, key_field="frames.id")
    
    print(dataset.bounds("frames.random"))
    

Parameters:
    

  * **field_name** â a field or `embedded.field.name`

  * **values** â 

the field values to set, provided in either of the following formats:

    * **list syntax** : an iterable of values, one for each sample in the collection. If `field_name` contains array fields, the corresponding elements of `values` must be arrays of the same lengths. When setting frame fields, each element can either be an iterable of values (one for each existing frame of the sample) or a dict mapping frame numbers to values

    * **dict syntax** : a dict whose keys specify the `key_field` values of the samples for which to set `field_name` to the corresponding values. When setting frame fields, you can either provide a sample-level `key_field`, in which case each corresponding value in `values` must be a list or dict of per-frame field values to set as described in the previous bullet, or you can provide a frame-level `key_field`, in which case each key-value pair in `values` represents a per-frame update

  * **key_field** (_None_) â a key field to use when choosing which samples to update when `values` is a dict

  * **skip_none** (_False_) â whether to treat None data in `values` as missing data that should not be set

  * **expand_schema** (_True_) â whether to dynamically add new sample/frame fields encountered to the dataset schema. If False, an error is raised if the root `field_name` does not exist

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **validate** (_True_) â whether to validate that the values are compliant with the dataset schema before adding them

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




set_label_values(_field_name_ , _values_ , _dynamic =False_, _skip_none =False_, _validate =True_, _progress =False_)#
    

Sets the fields of the specified labels in the collection to the given values.

You can use this method in two ways:

  * **List syntax (recommended):** provide a list of dicts of the form `{"sample_id": sample_id, "label_id": label_id, "value": value}` specifying the sample IDs and label IDs of each label you want to edit

  * **Dict syntax:** provide a dict mapping label IDs to values




Note

This method is most efficient when you use the list syntax, which includes the sample/frame ID of each label that you are modifying.

Note

This method is appropriate when you have the IDs of the labels you wish to modify. See `set_values()` and `set_field()` if your updates are not keyed by label ID.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Populate a new boolean attribute on all high confidence labels
    #
    
    view = dataset.filter_labels("predictions", F("confidence") > 0.99)
    
    # Option 1 (recommended): provide label IDs and sample IDs
    
    values = []
    sample_ids, label_ids = view.values(["id", "predictions.detections.id"])
    for sid, lids in zip(sample_ids, label_ids):
        for lid in lids:
            values.append({"sample_id": sid, "label_id": lid, "value": True})
    
    dataset.set_label_values("predictions.detections.high_conf", values)
    
    print(dataset.count("predictions.detections"))
    print(len(values))
    print(dataset.count_values("predictions.detections.high_conf"))
    
    # Option 2: provide only label IDs
    
    label_ids = view.values("predictions.detections.id", unwind=True)
    values = {_id: True for _id in label_ids}
    
    dataset.set_label_values("predictions.detections.high_conf", values)
    
    print(dataset.count("predictions.detections"))
    print(len(label_ids))
    print(dataset.count_values("predictions.detections.high_conf"))
    

Parameters:
    

  * **field_name** â a field or `embedded.field.name`

  * **values** â 

the label values to set, in one of the following formats:

    * a list of dicts of the form `{"sample_id": sample_id, "label_id": label_id, "value": value}` when setting sample-level labels

    * a list of dicts of the form `{"frame_id": frame_id, "label_id": label_id, "value": value}` when setting frame-level labels

    * a dict mapping label IDs to values

  * **skip_none** (_False_) â whether to treat None data in `values` as missing data that should not be set

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **validate** (_True_) â whether to validate that the values are compliant with the dataset schema before adding them

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




compute_metadata(_overwrite =False_, _num_workers =None_, _skip_failures =True_, _warn_failures =True_, _progress =None_)#
    

Populates the `metadata` field of all samples in the collection.

Any samples with existing metadata are skipped, unless `overwrite == True`.

Parameters:
    

  * **overwrite** (_False_) â whether to overwrite existing metadata

  * **num_workers** (_None_) â a suggested number of threads to use

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if metadata cannot be computed for a sample

  * **warn_failures** (_True_) â whether to log a warning if metadata cannot be computed for a sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




generate_label_schemas(_fields =None_, _scan_samples =True_)#
    

Generates label schemas for the `fiftyone.core.collections.SampleCollection`.

A label schema is defined by a `type` and `component` with respect to a field. Further settings depend on the `type` and `component` combination as outlined below.

The `type` value for a field is inferred from the collectionâs field schema. See `fiftyone.core.collections.SampleCollection.get_field_schema()`

Currently supported media types for the collection are `image` and `3d`. See `fiftyone.core.collections.SampleCollection.media_type`

**Primitives and components**

Supported primitive types are:

>   * `bool`: [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")
> 
>   * `date`: [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")
> 
>   * `datetime`: [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")
> 
>   * `dict`: [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")
> 
>   * `float`: [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")
> 
>   * `id`: [`fiftyone.core.fields.ObjectIdField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ObjectIdField "fiftyone.core.fields.ObjectIdField") or [`fiftyone.core.fields.UUIDField`](api__fiftyone.core.fields.md#fiftyone.core.fields.UUIDField "fiftyone.core.fields.UUIDField")
> 
>   * `int`: [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField") or [`fiftyone.core.fields.FrameNumberField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FrameNumberField "fiftyone.core.fields.FrameNumberField")
> 
>   * `list<int>`: [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") of [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")
> 
>   * `list<float>`: [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") of [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")
> 
>   * `list<str>`: [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") of [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")
> 
>   * `str`: [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")
> 
> 


Supported `bool` components are:

>   * `checkbox`
> 
>   * `toggle` \- the default
> 
> 


`date` and `datetime` only support the `datepicker` component.

`dict` only supports the `json` component.

Supported `float` and `int` components are:

>   * `dropdown`
> 
>   * `radio`
> 
>   * `slider`: the default when `scan_samples` is `True` and distinct finite bounds are found that define a `range`
> 
>   * `text`: the default when `scan_samples` is `False` or distinct finite bounds are not found
> 
> 


Supported `list<float>` and `list<int>` components are:

>   * `checkboxes`
> 
>   * `dropdown`
> 
>   * `text` \- the default
> 
> 


Supported `list<str>` components are:

>   * `checkboxes`: the default if `<=5` values are scanned
> 
>   * `dropdown`: the default if `>5` and `<=1000` values are scanned
> 
>   * `text`: the default if `0` values or `>1000` values are scanned, or `scan_samples` is `False`
> 
> 


Supported `str` type components are:

>   * `dropdown`: the default if `>5` and `<=1000` values are scanned
> 
>   * `radio`: the default if `<=5` values are scanned
> 
>   * `text`: the default if `0` values or `>1000` values are scanned, or `scan_samples` is `False`
> 
> 


`float` types support a `precision` setting when a `text` component is configured for the number of digits to allow after the decimal.

All types support a `read_only` flag. `id` types must be `read_only`. If a field is `read_only` in the field schema, then the `read_only` label schema setting must be `True`, e.g. `created_at` and `last_modified_at` must be read only.

All components support `values` except `json`, `slider`, and `toggle` excepting `id` restrictions.

`checkboxes` and `dropdown` require the `values` setting.

`slider` requires the `range: [min, max]` setting.

**Labels**

The `label` subfield of all label types are configured via `classes` and support the same settings as a `str` type. See the example output below for `detections` fields in the quickstart dataset. If the label type has a visual representation, that field is handled by the Appâs builtin annotation UI, e.g. `bounding_box` for a `detection`. Primitive attributes of label types are configured via the `attributes` list.

When a label is marked as `read_only`, all its attributes inherit the setting as well.

All [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types are resolved by this method except [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation"), [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations"), [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection"), and [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections") when provided in the `fields` argument, otherwise only App supported fields are resolved. For label types supported by the App for annotation, see [`fiftyone.core.annotation.utils.get_supported_app_annotation_fields()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.get_supported_app_annotation_fields "fiftyone.core.annotation.utils.get_supported_app_annotation_fields").

All attributes and the label class itself support a `default` setting that applies when creating a new label.

**Embedded documents**

One level of nesting is supported via `dot.notation` for `fiftyone.core.fields.EmbeddedDocumentField`` fields for the default `metadata` field and the `fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument`` document type. All label and primitive types are supported. See [here](https://docs.voxel51.com/user_guide/using_datasets.html#dynamic-attributes) for more details on adding dynamic attributes.

Example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    fo.pprint(dataset.generate_label_schemas(scan_samples=False))
    

Output:
    
    
    {
        "created_at": {
            "type": "datetime",
            "component": "datepicker",
            "read_only": True,
        },
        "filepath": {"type": "str", "component": "text"},
        "ground_truth": {
            "attributes": [
                {
                    "name": "attributes",
                    "type": "dict",
                    "component": "json",
                },
                {
                    "name": "confidence",
                    "type": "float",
                    "component": "text",
                },
                {
                    "name": "id",
                    "type": "id",
                    "component": "text",
                    "read_only": True,
                },
                {"name": "index", "type": "int", "component": "text"},
                {
                    "name": "mask_path",
                    "type": "str",
                    "component": "text",
                },
                {
                    "name": "tags",
                    "type": "list<str>",
                    "component": "text",
                },
            ],
            "component": "text",
            "type": "detections",
        },
        "id": {"type": "id", "component": "text", "read_only": True},
        "last_modified_at": {
            "type": "datetime",
            "component": "datepicker",
            "read_only": True,
        },
        "metadata.height": {"type": "int", "component": "text"},
        "metadata.mime_type": {"type": "str", "component": "text"},
        "metadata.num_channels": {"type": "int", "component": "text"},
        "metadata.size_bytes": {"type": "int", "component": "text"},
        "metadata.width": {"type": "int", "component": "text"},
        "predictions": {
            "attributes": [
                {
                    "name": "attributes",
                    "type": "dict",
                    "component": "json",
                },
                {
                    "name": "confidence",
                    "type": "float",
                    "component": "text",
                },
                {
                    "name": "id",
                    "type": "id",
                    "component": "text",
                    "read_only": True,
                },
                {"name": "index", "type": "int", "component": "text"},
                {
                    "name": "mask_path",
                    "type": "str",
                    "component": "text",
                },
                {
                    "name": "tags",
                    "type": "list<str>",
                    "component": "text",
                },
            ],
            "component": "text",
            "type": "detections",
        },
        "tags": {"type": "list<str>", "component": "text"},
        "uniqueness": {"type": "float", "component": "text"},
    }
    

Parameters:
    

  * **fields** (_None_) â a field name, `embedded.field.name` or iterable of such values

  * **scan_samples** (_True_) â whether to scan the collection to populate component settings based on actual field values (ranges, values, etc). If False, the label schema is generated from _only_ the statically available information in the datasetâs field schema



Raises:
    

**ValueError** â if the sample collection or field is not supported

Returns:
    

a label schemas `dict`, or an individual fieldâs label schema `dict` if only one field is provided

apply_model(_model_ , _label_field ='predictions'_, _confidence_thresh =None_, _classes =None_, _store_logits =False_, _batch_size =None_, _num_workers =None_, _skip_failures =True_, _output_dir =None_, _rel_dir =None_, _progress =None_, _** kwargs_)#
    

Applies the model to the samples in the collection.

This method supports all of the following cases:

  * Applying an image model to an image collection

  * Applying an image model to the frames of a video collection

  * Applying a video model to a video collection




Parameters:
    

  * **model** â a [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model"), Hugging Face transformers model, Ultralytics model, SuperGradients model, or Lightning Flash model

  * **label_field** (_"predictions"_) â the name of the field in which to store the model predictions. When performing inference on video frames, the âframes.â prefix is optional

  * **confidence_thresh** (_None_) â an optional confidence threshold to apply to any applicable labels generated by the model

  * **classes** (_None_) â an optional iterable of classes to which to restrict any applicable labels generated by the model

  * **store_logits** (_False_) â whether to store logits for the model predictions. This is only supported when the provided `model` has logits, `model.has_logits == True`

  * **batch_size** (_None_) â an optional batch size to use, if the model supports batching

  * **num_workers** (_None_) â the number of workers for the [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)") to use. Only applicable for Torch-based models

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if predictions cannot be generated for a sample. Only applicable to [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instances

  * **output_dir** (_None_) â an optional output directory in which to write segmentation images. Only applicable if the model generates segmentations. If none is provided, the segmentations are stored in the database

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each segmentation image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional model-specific keyword arguments passed through to the underlying inference implementation




compute_embeddings(_model_ , _embeddings_field =None_, _batch_size =None_, _num_workers =None_, _skip_failures =True_, _progress =None_, _** kwargs_)#
    

Computes embeddings for the samples in the collection using the given model.

This method supports all the following cases:

  * Using an image model to compute embeddings for an image collection

  * Using an image model to compute frame embeddings for a video collection

  * Using a video model to compute embeddings for a video collection




The `model` must expose embeddings, i.e., [`fiftyone.core.models.Model.has_embeddings()`](api__fiftyone.core.models.md#fiftyone.core.models.Model.has_embeddings "fiftyone.core.models.Model.has_embeddings") must return `True`.

If an `embeddings_field` is provided, the embeddings are saved to the samples; otherwise, the embeddings are returned in-memory.

Parameters:
    

  * **model** â a [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model"), Hugging Face Transformers model, Ultralytics model, SuperGradients model, or Lightning Flash model

  * **embeddings_field** (_None_) â the name of a field in which to store the embeddings. When computing video frame embeddings, the âframes.â prefix is optional

  * **batch_size** (_None_) â an optional batch size to use, if the model supports batching

  * **num_workers** (_None_) â the number of workers for the [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)") to use. Only applicable for Torch-based models

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if embeddings cannot be generated for a sample. Only applicable to [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instances

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional model-specific keyword arguments passed through to the underlying inference implementation



Returns:
    

  * `None`, if an `embeddings_field` is provided

  * a `num_samples x num_dim` array of embeddings, when computing embeddings for image/video collections with image/video models, respectively, and no `embeddings_field` is provided. If `skip_failures` is `True` and any errors are detected, a list of length `num_samples` is returned instead containing all successfully computed embedding vectors along with `None` entries for samples for which embeddings could not be computed

  * a dictionary mapping sample IDs to `num_frames x num_dim` arrays of embeddings, when computing frame embeddings for video collections using an image model. If `skip_failures` is `True` and any errors are detected, the values of this dictionary will contain arrays of embeddings for all frames 1, 2, â¦ until the error occurred, or `None` if no embeddings were computed at all




Return type:
    

one of the following

compute_patch_embeddings(_model_ , _patches_field_ , _embeddings_field =None_, _force_square =False_, _alpha =None_, _handle_missing ='skip'_, _batch_size =None_, _num_workers =None_, _skip_failures =True_, _progress =None_)#
    

Computes embeddings for the image patches defined by `patches_field` of the samples in the collection using the given model.

This method supports all the following cases:

  * Using an image model to compute patch embeddings for an image collection

  * Using an image model to compute frame patch embeddings for a video collection




The `model` must expose embeddings, i.e., [`fiftyone.core.models.Model.has_embeddings()`](api__fiftyone.core.models.md#fiftyone.core.models.Model.has_embeddings "fiftyone.core.models.Model.has_embeddings") must return `True`.

If an `embeddings_field` is provided, the embeddings are saved to the samples; otherwise, the embeddings are returned in-memory.

Parameters:
    

  * **model** â a [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model"), Hugging Face Transformers model, Ultralytics model, SuperGradients model, or Lightning Flash model

  * **patches_field** â the name of the field defining the image patches in each sample to embed. Must be of type [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"). When computing video frame embeddings, the âframes.â prefix is optional

  * **embeddings_field** (_None_) â the name of a label attribute in which to store the embeddings

  * **force_square** (_False_) â whether to minimally manipulate the patch bounding boxes into squares prior to extraction

  * **alpha** (_None_) â an optional expansion/contraction to apply to the patches before extracting them, in `[-1, inf)`. If provided, the length and width of the box are expanded (or contracted, when `alpha < 0`) by `(100 * alpha)%`. For example, set `alpha = 0.1` to expand the boxes by 10%, and set `alpha = -0.1` to contract the boxes by 10%

  * **handle_missing** (_"skip"_) â 

how to handle images with no patches. Supported values are:

    * âskipâ: skip the image and assign its embedding as `None`

    * âimageâ: use the whole image as a single patch

    * âerrorâ: raise an error

  * **batch_size** (_None_) â an optional batch size to use, if the model supports batching

  * **num_workers** (_None_) â the number of workers for the [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)") to use. Only applicable for Torch-based models

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if embeddings cannot be generated for a sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

  * `None`, if an `embeddings_field` is provided

  * a dict mapping sample IDs to `num_patches x num_dim` arrays of patch embeddings, when computing patch embeddings for image collections and no `embeddings_field` is provided. If `skip_failures` is `True` and any errors are detected, this dictionary will contain `None` values for any samples for which embeddings could not be computed

  * a dict of dicts mapping sample IDs to frame numbers to `num_patches x num_dim` arrays of patch embeddings, when computing patch embeddings for the frames of video collections and no `embeddings_field` is provided. If `skip_failures` is `True` and any errors are detected, this nested dict will contain missing or `None` values to indicate uncomputable embeddings




Return type:
    

one of the following

evaluate_regressions(_pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _missing =None_, _method =None_, _progress =None_, _** kwargs_)#
    

Evaluates the regression predictions in this collection with respect to the specified ground truth values.

You can customize the evaluation method by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"simple"`: [`fiftyone.utils.eval.regression.SimpleEvaluationConfig`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig "fiftyone.utils.eval.regression.SimpleEvaluationConfig")




If an `eval_key` is specified, then this method will record some statistics on each sample:

  * When evaluating sample-level fields, an `eval_key` field will be populated on each sample recording the error of that sampleâs prediction.

  * When evaluating frame-level fields, an `eval_key` field will be populated on each frame recording the error of that frameâs prediction. In addition, an `eval_key` field will be populated on each sample that records the average error of the frame predictions of the sample.




Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") instances

  * **eval_key** (_None_) â a string key to use to refer to this evaluation

  * **missing** (_None_) â a missing value. Any None-valued regressions are given this value for results purposes

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.regression_backends.keys()` and the default is `fo.evaluation_config.regression_default_backend`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the [`fiftyone.utils.eval.regression.RegressionEvaluationConfig`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig "fiftyone.utils.eval.regression.RegressionEvaluationConfig") being used



Returns:
    

a [`fiftyone.utils.eval.regression.RegressionResults`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults "fiftyone.utils.eval.regression.RegressionResults")

evaluate_classifications(_pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _classes =None_, _missing =None_, _method =None_, _progress =None_, _** kwargs_)#
    

Evaluates the classification predictions in this collection with respect to the specified ground truth labels.

By default, this method simply compares the ground truth and prediction for each sample, but other strategies such as binary evaluation and top-k matching can be configured via the `method` parameter.

You can customize the evaluation method by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"simple"`: [`fiftyone.utils.eval.classification.SimpleEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig "fiftyone.utils.eval.classification.SimpleEvaluationConfig")

  * `"top-k"`: [`fiftyone.utils.eval.classification.TopKEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig "fiftyone.utils.eval.classification.TopKEvaluationConfig")

  * `"binary"`: [`fiftyone.utils.eval.classification.BinaryEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig "fiftyone.utils.eval.classification.BinaryEvaluationConfig")




If an `eval_key` is specified, then this method will record some statistics on each sample:

  * When evaluating sample-level fields, an `eval_key` field will be populated on each sample recording whether that sampleâs prediction is correct.

  * When evaluating frame-level fields, an `eval_key` field will be populated on each frame recording whether that frameâs prediction is correct. In addition, an `eval_key` field will be populated on each sample that records the average accuracy of the frame predictions of the sample.




Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances

  * **eval_key** (_None_) â a string key to use to refer to this evaluation

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used

  * **missing** (_None_) â a missing label string. Any None-valued labels are given this label for results purposes

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.classification_backends.keys()` and the default is `fo.evaluation_config.classification_default_backend`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the [`fiftyone.utils.eval.classification.ClassificationEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig "fiftyone.utils.eval.classification.ClassificationEvaluationConfig") being used



Returns:
    

a [`fiftyone.utils.eval.classification.ClassificationResults`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults "fiftyone.utils.eval.classification.ClassificationResults")

evaluate_detections(_pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _classes =None_, _missing =None_, _method =None_, _iou =0.5_, _use_masks =False_, _use_boxes =False_, _classwise =True_, _dynamic =True_, _progress =None_, _** kwargs_)#
    

Evaluates the specified predicted detections in this collection with respect to the specified ground truth detections.

This method supports evaluating the following spatial data types:

  * Object detections in [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") format

  * Instance segmentations in [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") format with their `mask` attributes populated

  * Polygons in [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") format

  * Keypoints in [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") format

  * Temporal detections in [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections") format




For spatial object detection evaluation, this method uses COCO-style evaluation by default.

When evaluating keypoints, âIoUsâ are computed via [object keypoint similarity](https://cocodataset.org/#keypoints-eval).

For temporal segment detection, this method uses ActivityNet-style evaluation by default.

You can use the `method` parameter to select a different method, and you can optionally customize the method by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"coco"`: [`fiftyone.utils.eval.coco.COCOEvaluationConfig`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig "fiftyone.utils.eval.coco.COCOEvaluationConfig")

  * `"open-images"`: [`fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig "fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig")

  * `"activitynet"`: [`fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig "fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig")




If an `eval_key` is provided, a number of fields are populated at the object- and sample-level recording the results of the evaluation:

  * True positive (TP), false positive (FP), and false negative (FN) counts for the each sample are saved in top-level fields of each sample:
        
        TP: sample.<eval_key>_tp
        FP: sample.<eval_key>_fp
        FN: sample.<eval_key>_fn
        

In addition, when evaluating frame-level objects, TP/FP/FN counts are recorded for each frame:
        
        TP: frame.<eval_key>_tp
        FP: frame.<eval_key>_fp
        FN: frame.<eval_key>_fn
        

  * The fields listed below are populated on each individual object; these fields tabulate the TP/FP/FN status of the object, the ID of the matching object (if any), and the matching IoU:
        
        TP/FP/FN: object.<eval_key>
              ID: object.<eval_key>_id
             IoU: object.<eval_key>_iou
        




Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections")

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections")

  * **eval_key** (_None_) â a string key to use to refer to this evaluation

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used

  * **missing** (_None_) â a missing label string. Any unmatched objects are given this label for results purposes

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.detection_backends.keys()` and the default is `fo.evaluation_config.detection_default_backend`

  * **iou** (_0.50_) â the IoU threshold to use to determine matches

  * **use_masks** (_False_) â whether to compute IoUs using the instances masks in the `mask` attribute of the provided objects, which must be [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") instances

  * **use_boxes** (_False_) â whether to compute IoUs using the bounding boxes of the provided [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") instances rather than using their actual geometries

  * **classwise** (_True_) â whether to only match objects with the same class label (True) or allow matches between classes (False)

  * **dynamic** (_True_) â whether to declare the dynamic object-level attributes that are populated on the datasetâs schema

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the [`fiftyone.utils.eval.detection.DetectionEvaluationConfig`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig "fiftyone.utils.eval.detection.DetectionEvaluationConfig") being used



Returns:
    

a [`fiftyone.utils.eval.detection.DetectionResults`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults "fiftyone.utils.eval.detection.DetectionResults")

evaluate_segmentations(_pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _mask_targets =None_, _method =None_, _progress =None_, _** kwargs_)#
    

Evaluates the specified semantic segmentation masks in this collection with respect to the specified ground truth masks.

If the size of a predicted mask does not match the ground truth mask, it is resized to match the ground truth.

By default, this method simply performs pixelwise evaluation of the full masks, but other strategies such as boundary-only evaluation can be configured by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"simple"`: [`fiftyone.utils.eval.segmentation.SimpleEvaluationConfig`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig "fiftyone.utils.eval.segmentation.SimpleEvaluationConfig")




If an `eval_key` is provided, the accuracy, precision, and recall of each sample is recorded in top-level fields of each sample:
    
    
     Accuracy: sample.<eval_key>_accuracy
    Precision: sample.<eval_key>_precision
       Recall: sample.<eval_key>_recall
    

In addition, when evaluating frame-level masks, the accuracy, precision, and recall of each frame if recorded in the following frame-level fields:
    
    
     Accuracy: frame.<eval_key>_accuracy
    Precision: frame.<eval_key>_precision
       Recall: frame.<eval_key>_recall
    

Note

The mask values `0` and `#000000` are treated as a background class for the purposes of computing evaluation metrics like precision and recall.

Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") instances

  * **eval_key** (_None_) â a string key to use to refer to this evaluation

  * **mask_targets** (_None_) â a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to semantic label strings. If not provided, the observed values are used as labels

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.segmentation_backends.keys()` and the default is `fo.evaluation_config.segmentation_default_backend`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the [`fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig "fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig") being used



Returns:
    

a [`fiftyone.utils.eval.segmentation.SegmentationResults`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults "fiftyone.utils.eval.segmentation.SegmentationResults")

property has_evaluations#
    

Whether this collection has any evaluation results.

has_evaluation(_eval_key_)#
    

Whether this collection has an evaluation with the given key.

Parameters:
    

**eval_key** â an evaluation key

Returns:
    

True/False

list_evaluations(_type =None_, _method =None_, _** kwargs_)#
    

Returns a list of evaluation keys on this collection.

Parameters:
    

  * **type** (_None_) â 

a specific evaluation type to match, which can be:

    * a string `fiftyone.core.evaluations.EvaluationMethodConfig.type`

    * a `fiftyone.core.evaluations.EvaluationMethod` class or its fully-qualified class name string

  * **method** (_None_) â a specific `fiftyone.core.evaluations.EvaluationMethodConfig.method` string to match

  * ****kwargs** â optional config parameters to match



Returns:
    

a list of evaluation keys

map_samples(_map_fcn_ , _save =False_, _skip_failures =False_, _parallelize_method =None_, _num_workers =None_, _batch_method =None_, _batch_size =None_, _progress =None_)#
    

Applies the given function to each sample in the collection and returns the results as a generator.

By default, a multiprocessing pool is used to parallelize the work, unless this method is called in a daemon process (subprocess), in which case no workers are used.

This function effectively performs the following map operation with the outer loop in parallel:
    
    
    for batch_view in fou.iter_slices(sample_collection, batch_size):
        for sample in batch_view.iter_samples(autosave=save):
            sample_output = map_fcn(sample)
            yield sample.id, sample_output
    

Example:
    
    
    from collections import Counter
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("cifar10", split="train")
    view = dataset.select_fields("ground_truth")
    
    def map_fcn(sample):
        return sample.ground_truth.label.upper()
    
    counter = Counter()
    for _, label in view.map_samples(map_fcn):
        counter[label] += 1
    
    print(dict(counter))
    

Parameters:
    

  * **map_fcn** â a function to apply to each sample in the collection

  * **save** (_False_) â whether to save any sample edits applied by `map_fcn`

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if the update function raises an exception for a sample

  * **parallelize_method** (_None_) â the parallelization method to use. Supported values are `{"process", "thread"}`. The default is `fiftyone.config.default_parallelization_method`

  * **num_workers** (_None_) â the number of workers to use. When using process parallelism, this defaults to `fiftyone.config.default_process_pool_workers` if the value is set, else [`fiftyone.core.utils.recommend_process_pool_workers()`](api__fiftyone.core.utils.md#fiftyone.core.utils.recommend_process_pool_workers "fiftyone.core.utils.recommend_process_pool_workers") workers are used. If this value is <= 1, all work is done in the main process

  * **batch_method** (_None_) â whether to use IDs (`"id"`) or slices (`"slice"`) to assign samples to workers

  * **batch_size** (_None_) â an optional number of samples to distribute to each worker at a time. By default, samples are evenly distributed to workers with one batch per worker

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead, or âworkersâ to render per-worker progress bars



Returns:
    

a generator that emits `(sample_id, map_output)` tuples

update_samples(_update_fcn_ , _skip_failures =True_, _parallelize_method =None_, _num_workers =None_, _batch_method =None_, _batch_size =None_, _progress =None_)#
    

Applies the given function to each sample in the collection and saves the resulting sample edits.

By default, a multiprocessing pool is used to parallelize the work, unless this method is called in a daemon process (subprocess), in which case no workers are used.

This function effectively performs the following map operation with the outer loop in parallel:
    
    
    for batch_view in fou.iter_slices(sample_collection, batch_size):
        for sample in batch_view.iter_samples(autosave=True):
            map_fcn(sample)
    

Example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("cifar10", split="train")
    view = dataset.select_fields("ground_truth")
    
    def update_fcn(sample):
        sample.ground_truth.label = sample.ground_truth.label.upper()
    
    view.update_samples(update_fcn)
    
    print(dataset.count_values("ground_truth.label"))
    

Parameters:
    

  * **update_fcn** â a function to apply to each sample in the collection

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if the update function raises an exception for a sample

  * **parallelize_method** (_None_) â the parallelization method to use. Supported values are `{"process", "thread"}`. The default is `fiftyone.config.default_parallelization_method`

  * **num_workers** (_None_) â the number of workers to use. When using process parallelism, this defaults to `fiftyone.config.default_process_pool_workers` if the value is set, else [`fiftyone.core.utils.recommend_process_pool_workers()`](api__fiftyone.core.utils.md#fiftyone.core.utils.recommend_process_pool_workers "fiftyone.core.utils.recommend_process_pool_workers") workers are used. If this value is <= 1, all work is done in the main process

  * **batch_method** (_None_) â whether to use IDs (`"id"`) or slices (`"slice"`) to assign samples to workers

  * **batch_size** (_None_) â an optional number of samples to distribute to each worker at a time. By default, samples are evenly distributed to workers with one batch per worker

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead, or âworkersâ to render per-worker progress bars




rename_evaluation(_eval_key_ , _new_eval_key_)#
    

Replaces the key for the given evaluation with a new key.

Parameters:
    

  * **eval_key** â an evaluation key

  * **new_anno_key** â a new evaluation key




get_evaluation_info(_eval_key_)#
    

Returns information about the evaluation with the given key on this collection.

Parameters:
    

**eval_key** â an evaluation key

Returns:
    

an [`fiftyone.core.evaluation.EvaluationInfo`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationInfo "fiftyone.core.evaluation.EvaluationInfo")

load_evaluation_results(_eval_key_ , _cache =True_, _** kwargs_)#
    

Loads the results for the evaluation with the given key on this collection.

Parameters:
    

  * **eval_key** â an evaluation key

  * **cache** (_True_) â whether to cache the results on the collection

  * ****kwargs** â keyword arguments for the runâs [`fiftyone.core.evaluation.EvaluationMethodConfig.load_credentials()`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig.load_credentials "fiftyone.core.evaluation.EvaluationMethodConfig.load_credentials") method



Returns:
    

a [`fiftyone.core.evaluation.EvaluationResults`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationResults "fiftyone.core.evaluation.EvaluationResults")

load_evaluation_view(_eval_key_ , _select_fields =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified evaluation was performed on this collection.

Parameters:
    

  * **eval_key** â an evaluation key

  * **select_fields** (_False_) â whether to exclude fields involved in other evaluations



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

delete_evaluation(_eval_key_)#
    

Deletes the evaluation results associated with the given evaluation key from this collection.

Parameters:
    

**eval_key** â an evaluation key

delete_evaluations()#
    

Deletes all evaluation results from this collection.

property has_brain_runs#
    

Whether this collection has any brain runs.

has_brain_run(_brain_key_)#
    

Whether this collection has a brain method run with the given key.

Parameters:
    

**brain_key** â a brain key

Returns:
    

True/False

list_brain_runs(_type =None_, _method =None_, _** kwargs_)#
    

Returns a list of brain keys on this collection.

Parameters:
    

  * **type** (_None_) â 

a specific brain run type to match, which can be:

    * a string [`fiftyone.core.brain.BrainMethodConfig.type`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainMethodConfig.type "fiftyone.core.brain.BrainMethodConfig.type")

    * a [`fiftyone.core.brain.BrainMethod`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainMethod "fiftyone.core.brain.BrainMethod") class or its fully-qualified class name string

  * **method** (_None_) â a specific [`fiftyone.core.brain.BrainMethodConfig.method`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainMethodConfig.method "fiftyone.core.brain.BrainMethodConfig.method") string to match

  * ****kwargs** â optional config parameters to match



Returns:
    

a list of brain keys

rename_brain_run(_brain_key_ , _new_brain_key_)#
    

Replaces the key for the given brain run with a new key.

Parameters:
    

  * **brain_key** â a brain key

  * **new_brain_key** â a new brain key




get_brain_info(_brain_key_)#
    

Returns information about the brain method run with the given key on this collection.

Parameters:
    

**brain_key** â a brain key

Returns:
    

a [`fiftyone.core.brain.BrainInfo`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainInfo "fiftyone.core.brain.BrainInfo")

load_brain_results(_brain_key_ , _cache =True_, _load_view =True_, _** kwargs_)#
    

Loads the results for the brain method run with the given key on this collection.

Parameters:
    

  * **brain_key** â a brain key

  * **cache** (_True_) â whether to cache the results on the collection

  * **load_view** (_True_) â whether to load the view on which the results were computed (True) or the full dataset (False)

  * ****kwargs** â keyword arguments for the runâs [`fiftyone.core.brain.BrainMethodConfig.load_credentials()`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainMethodConfig.load_credentials "fiftyone.core.brain.BrainMethodConfig.load_credentials") method



Returns:
    

a [`fiftyone.core.brain.BrainResults`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainResults "fiftyone.core.brain.BrainResults")

load_brain_view(_brain_key_ , _select_fields =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified brain method run was performed on this collection.

Parameters:
    

  * **brain_key** â a brain key

  * **select_fields** (_False_) â whether to exclude fields involved in other brain method runs



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

delete_brain_run(_brain_key_)#
    

Deletes the brain method run with the given key from this collection.

Parameters:
    

**brain_key** â a brain key

delete_brain_runs()#
    

Deletes all brain method runs from this collection.

property has_runs#
    

Whether this collection has any runs.

has_run(_run_key_)#
    

Whether this collection has a run with the given key.

Parameters:
    

**run_key** â a run key

Returns:
    

True/False

list_runs(_** kwargs_)#
    

Returns a list of run keys on this collection.

Parameters:
    

****kwargs** â optional config parameters to match

Returns:
    

a list of run keys

init_run(_** kwargs_)#
    

Initializes a config instance for a new run.

Parameters:
    

****kwargs** â JSON serializable config parameters

Returns:
    

a [`fiftyone.core.runs.RunConfig`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunConfig "fiftyone.core.runs.RunConfig")

register_run(_run_key_ , _config_ , _results =None_, _overwrite =False_, _cleanup =True_, _cache =True_)#
    

Registers a run under the given key on this collection.

Parameters:
    

  * **run_key** â a run key

  * **config** â a [`fiftyone.core.runs.RunConfig`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunConfig "fiftyone.core.runs.RunConfig")

  * **results** (_None_) â an optional [`fiftyone.core.runs.RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults")

  * **overwrite** (_False_) â whether to allow overwriting an existing run of the same type

  * **cleanup** (_True_) â whether to execute an existing runâs [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup") method when overwriting it

  * **cache** (_True_) â whether to cache the results on the collection




rename_run(_run_key_ , _new_run_key_)#
    

Replaces the key for the given run with a new key.

Parameters:
    

  * **run_key** â a run key

  * **new_run_key** â a new run key




get_run_info(_run_key_)#
    

Returns information about the run with the given key on this collection.

Parameters:
    

**run_key** â a run key

Returns:
    

a [`fiftyone.core.runs.RunInfo`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunInfo "fiftyone.core.runs.RunInfo")

update_run_config(_run_key_ , _config_)#
    

Updates the run config for the run with the given key.

Parameters:
    

  * **run_key** â a run key

  * **config** â a [`fiftyone.core.runs.RunConfig`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunConfig "fiftyone.core.runs.RunConfig")




init_run_results(_run_key_ , _** kwargs_)#
    

Initializes a results instance for the run with the given key.

Parameters:
    

  * **run_key** â a run key

  * ****kwargs** â JSON serializable data



Returns:
    

a [`fiftyone.core.runs.RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults")

save_run_results(_run_key_ , _results_ , _overwrite =True_, _cache =True_)#
    

Saves run results for the run with the given key.

Parameters:
    

  * **run_key** â a run key

  * **results** â a [`fiftyone.core.runs.RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults")

  * **overwrite** (_True_) â whether to overwrite an existing result with the same key

  * **cache** (_True_) â whether to cache the results on the collection




load_run_results(_run_key_ , _cache =True_, _load_view =True_, _** kwargs_)#
    

Loads the results for the run with the given key on this collection.

Parameters:
    

  * **run_key** â a run key

  * **cache** (_True_) â whether to cache the results on the collection

  * **load_view** (_True_) â whether to load the view on which the results were computed (True) or the full dataset (False)

  * ****kwargs** â keyword arguments for the runâs [`fiftyone.core.runs.RunConfig.load_credentials()`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunConfig.load_credentials "fiftyone.core.runs.RunConfig.load_credentials") method



Returns:
    

a [`fiftyone.core.runs.RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults")

load_run_view(_run_key_ , _select_fields =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified run was performed on this collection.

Parameters:
    

  * **run_key** â a run key

  * **select_fields** (_False_) â whether to exclude fields involved in other runs



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

delete_run(_run_key_)#
    

Deletes the run with the given key from this collection.

Parameters:
    

**run_key** â a run key

delete_runs()#
    

Deletes all runs from this collection.

classmethod list_view_stages()#
    

Returns a list of all available methods on this collection that apply [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") operations to this collection.

Returns:
    

a list of `SampleCollection` method names

add_stage(_stage_)#
    

Applies the given [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") to the collection.

Parameters:
    

**stage** â a [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage")

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

concat(_samples_)#
    

Concatenates the contents of the given `SampleCollection` to this collection.

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
    
    view = view1.concat(view2)
    
    print(view1)
    print(view2)
    print(view)
    
    #
    # Concatenate two patches views
    #
    
    gt_objects = dataset.to_patches("ground_truth")
    
    patches1 = gt_objects[:50]
    patches2 = gt_objects[-50:]
    patches = patches1.concat(patches2)
    
    print(patches1)
    print(patches2)
    print(patches)
    

Parameters:
    

**samples** â a `SampleCollection` whose contents to append to this collection

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude(_sample_ids_)#
    

Excludes the samples with the given IDs from the collection.

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
    view = dataset.exclude(sample_id)
    
    #
    # Exclude the first and last samples from the dataset
    #
    
    sample_ids = [dataset.first().id, dataset.last().id]
    view = dataset.exclude(sample_ids)
    

Parameters:
    

**sample_ids** â 

the samples to exclude. Can be any of the following:

  * a sample ID

  * an iterable of sample IDs

  * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

  * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

  * a `fiftyone.core.collections.SampleCollection`




Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude_by(_field_ , _values_)#
    

Excludes the samples with the given field values from the collection.

This stage is typically used to work with categorical fields (strings, ints, and bools). If you want to exclude samples based on floating point fields, use `match()`.

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
    
    view = dataset.exclude_by("int", [1, 9, 3, 7, 5])
    print(view.head(5))
    
    #
    # Create a view excluding samples whose `str` field have the given
    # values
    #
    
    view = dataset.exclude_by("str", ["1", "9", "3", "7", "5"])
    print(view.head(5))
    

Parameters:
    

  * **field** â a field or `embedded.field.name`

  * **values** â a value or iterable of values to exclude by



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude_fields(_field_names =None_, _meta_filter =None_, __allow_missing =False_)#
    

Excludes the fields with the given names from the samples in the collection.

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
    
    view = dataset.exclude_fields("predictions")
    
    #
    # Exclude the `mood` attribute from all classifications in the
    # `predictions` field
    #
    
    view = dataset.exclude_fields("predictions.mood")
    

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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude_frames(_frame_ids_ , _omit_empty =True_)#
    

Excludes the frames with the given IDs from the video collection.

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
    
    view = dataset.exclude_frames(frame_ids)
    
    print(dataset.count("frames"))
    print(view.count("frames"))
    

Parameters:
    

  * **frame_ids** â 

the frames to exclude. Can be any of the following:

    * a frame ID

    * an iterable of frame IDs

    * a [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") or [`fiftyone.core.frame.FrameView`](api__fiftyone.core.frame.md#fiftyone.core.frame.FrameView "fiftyone.core.frame.FrameView")

    * an iterable of [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") or [`fiftyone.core.frame.FrameView`](api__fiftyone.core.frame.md#fiftyone.core.frame.FrameView "fiftyone.core.frame.FrameView") instances

    * a `fiftyone.core.collections.SampleCollection` whose frames to exclude

  * **omit_empty** (_True_) â whether to omit samples that have no frames after excluding the specified frames



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude_groups(_group_ids_)#
    

Excludes the groups with the given IDs from the grouped collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-groups")
    
    #
    # Exclude some specific groups by ID
    #
    
    view = dataset.take(2)
    group_ids = view.values("group.id")
    other_groups = dataset.exclude_groups(group_ids)
    
    assert len(set(group_ids) & set(other_groups.values("group.id"))) == 0
    

Parameters:
    

**groups_ids** â 

the groups to exclude. Can be any of the following:

  * a group ID

  * an iterable of group IDs

  * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

  * a group dict returned by `get_group()`

  * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

  * an iterable of group dicts returned by `get_group()`

  * a `fiftyone.core.collections.SampleCollection`




Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude_group_slices(_slices =None_, _media_type =None_)#
    

Excludes the specified group slice(s) from the grouped collection.

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
    # Exclude the samples from the "ego" group slice
    #
    
    view = dataset.exclude_group_slices("ego")
    
    #
    # Exclude the samples from the "left" or "right" group slices
    #
    
    view = dataset.exclude_group_slices(["left", "right"])
    
    #
    # Exclude all image slices
    #
    
    view = dataset.exclude_group_slices(media_type="image")
    

Parameters:
    

  * **slices** (_None_) â a group slice or iterable of group slices to exclude

  * **media_type** (_None_) â a media type or iterable of media types whose slice(s) to exclude



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exclude_labels(_labels =None_, _ids =None_, _instance_ids =None_, _tags =None_, _fields =None_, _omit_empty =True_)#
    

Excludes the specified labels from the collection.

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
    
    view = dataset.exclude_labels(labels=session.selected_labels)
    
    #
    # Exclude labels with the specified IDs
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    view = dataset.exclude_labels(ids=ids)
    
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
    view = dataset.exclude_labels(tags="test")
    
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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

exists(_field_ , _bool =None_)#
    

Returns a view containing the samples in the collection that have (or do not have) a non-`None` value for the given field or embedded field.

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
    # Only include samples that have a value in their `predictions`
    # field
    #
    
    view = dataset.exists("predictions")
    
    #
    # Only include samples that do NOT have a value in their
    # `predictions` field
    #
    
    view = dataset.exists("predictions", False)
    
    #
    # Only include samples that have prediction confidences
    #
    
    view = dataset.exists("predictions.confidence")
    

Parameters:
    

  * **field** â the field name or `embedded.field.name`

  * **bool** (_None_) â whether to check if the field exists (None or True) or does not exist (False)



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

filter_field(_field_ , _filter_ , _only_matches =True_)#
    

Filters the values of a field or embedded field of each sample in the collection.

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
    
    view = dataset.filter_field("predictions", F("label") == "cat")
    
    #
    # Only include samples whose `numeric_field` value is positive
    #
    
    view = dataset.filter_field("numeric_field", F() > 0)
    

Parameters:
    

  * **field** â the field name or `embedded.field.name`

  * **filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

  * **only_matches** (_True_) â whether to only include samples that match the filter (True) or include all samples (False)



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

filter_labels(_field_ , _filter_ , _only_matches =True_, _trajectories =False_)#
    

Filters the [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field of each sample in the collection.

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
    
    view = dataset.filter_labels("predictions", F("confidence") > 0.8)
    
    #
    # Only include classifications in the `predictions` field whose
    # `label` is "cat" or "dog"
    #
    
    view = dataset.filter_labels(
        "predictions", F("label").is_in(["cat", "dog"])
    )
    

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
    # Only include detections in the `predictions` field whose
    # `confidence` is greater than 0.8
    #
    
    view = dataset.filter_labels("predictions", F("confidence") > 0.8)
    
    #
    # Only include detections in the `predictions` field whose `label`
    # is "cat" or "dog"
    #
    
    view = dataset.filter_labels(
        "predictions", F("label").is_in(["cat", "dog"])
    )
    
    #
    # Only include detections in the `predictions` field whose bounding
    # box area is smaller than 0.2
    #
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    view = dataset.filter_labels("predictions", bbox_area < 0.2)
    

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
    
    view = dataset.filter_labels("predictions", F("filled") == True)
    
    #
    # Only include polylines in the `predictions` field whose `label`
    # is "lane"
    #
    
    view = dataset.filter_labels("predictions", F("label") == "lane")
    
    #
    # Only include polylines in the `predictions` field with at least
    # 3 vertices
    #
    
    num_vertices = F("points").map(F().length()).sum()
    view = dataset.filter_labels("predictions", num_vertices >= 3)
    

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
    # Only include keypoints in the `predictions` field whose `label`
    # is "house"
    #
    
    view = dataset.filter_labels("predictions", F("label") == "house")
    
    #
    # Only include keypoints in the `predictions` field with less than
    # four points
    #
    
    view = dataset.filter_labels("predictions", F("points").length() < 4)
    

Parameters:
    

  * **field** â the label field to filter

  * **filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

  * **only_matches** (_True_) â whether to only include samples with at least one label after filtering (True) or include all samples (False)

  * **trajectories** (_False_) â whether to match entire object trajectories for which the object matches the given filter on at least one frame. Only applicable to datasets that contain videos and frame-level label fields whose objects have their `index` attributes populated



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

filter_keypoints(_field_ , _filter =None_, _labels =None_, _only_matches =True_)#
    

Filters the individual [`fiftyone.core.labels.Keypoint.points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points") elements in the specified keypoints field of each sample in the collection.

Note

Use `filter_labels()` if you simply want to filter entire [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects in a field.

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
    
    view = dataset.filter_keypoints(
        "predictions", filter=F("confidence") > 0.9
    )
    
    #
    # Only include keypoints in the `predictions` field with less than
    # four points
    #
    
    view = dataset.filter_keypoints(
        "predictions", labels=["left eye", "right eye"]
    )
    

Parameters:
    

  * **field** â the [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") field to filter

  * **filter** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean, like `F("confidence") > 0.5` or `F("occluded") == False`, to apply elementwise to the specified field, which must be a list of same length as [`fiftyone.core.labels.Keypoint.points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points")

  * **labels** (_None_) â a label or iterable of keypoint skeleton labels to keep

  * **only_matches** (_True_) â whether to only include keypoints/samples with at least one point after filtering (True) or include all keypoints/samples (False)



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

flatten(_stages =None_)#
    

Returns a flattened view that contains all samples in the dynamic grouped collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("cifar10", split="test")
    
    # Group samples by ground truth label
    grouped_view = dataset.take(1000).group_by("ground_truth.label")
    print(len(grouped_view))  # 10
    
    # Return a flat view that contains 10 samples from each class
    flat_view = grouped_view.flatten(fo.Limit(10))
    print(len(flat_view))  # 100
    

Parameters:
    

**stages** (_None_) â a [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") or list of [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") instances to apply to each groupâs samples while flattening

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

geo_near(_point_ , _location_field =None_, _min_distance =None_, _max_distance =None_, _query =None_, _create_index =False_)#
    

Sorts the samples in the collection by their proximity to a specified geolocation.

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
    
    view = dataset.geo_near(TIMES_SQUARE, create_index=True)
    
    #
    # Sort the samples by their proximity to Times Square, and only
    # include samples within 5km
    #
    
    view = dataset.geo_near(
        TIMES_SQUARE,
        max_distance=5000,
        create_index=True,
    )
    
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
    
    view = dataset.geo_near(
        TIMES_SQUARE,
        location_field="location",
        query=in_manhattan,
        create_index=True,
    )
    

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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

geo_within(_boundary_ , _location_field =None_, _strict =True_, _create_index =False_)#
    

Filters the samples in this collection to only include samples whose geolocation is within a specified boundary.

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
    
    view = dataset.geo_within(MANHATTAN)
    

Parameters:
    

  * **boundary** â a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation"), [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations"), GeoJSON dict, or list of coordinates that define a `Polygon` or `MultiPolygon` to search within

  * **location_field** (_None_) â 

the location data of each sample to use. Can be any of the following:

    * The name of a `fiftyone.core.fields.GeoLocation` field whose `point` attribute to use as location data

    * An `embedded.field.name` that directly contains the GeoJSON location data to use

    * `None`, in which case there must be a single `fiftyone.core.fields.GeoLocation` field on the samples, which is used by default

  * **strict** (_True_) â whether a sampleâs location data must strictly fall within boundary (True) in order to match, or whether any intersection suffices (False)

  * **create_index** (_False_) â whether to create a spherical index, if necessary, to optimize the query



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

group_by(_field_or_expr_ , _order_by =None_, _reverse =False_, _flat =False_, _match_expr =None_, _sort_expr =None_, _create_index =False_, _order_by_key =None_)#
    

Creates a view that groups the samples in the collection by a specified field or expression.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("cifar10", split="test")
    
    #
    # Take 1000 samples at random and group them by ground truth label
    #
    
    view = dataset.take(1000).group_by("ground_truth.label")
    
    for group in view.iter_dynamic_groups():
        group_value = group.first().ground_truth.label
        print("%s: %d" % (group_value, len(group)))
    
    #
    # Variation of above operation that arranges the groups in
    # decreasing order of size and immediately flattens them
    #
    
    from itertools import groupby
    
    view = dataset.take(1000).group_by(
        "ground_truth.label",
        flat=True,
        sort_expr=F().length(),
        reverse=True,
    )
    
    rle = lambda v: [(k, len(list(g))) for k, g in groupby(v)]
    for label, count in rle(view.values("ground_truth.label")):
        print("%s: %d" % (label, count))
    

Parameters:
    

  * **field_or_expr** â the field or `embedded.field.name` to group by, or a list of field names defining a compound group key, or a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines the value to group by

  * **order_by** (_None_) â an optional field by which to order the samples in each group

  * **reverse** (_False_) â whether to return the results in descending order Applies both to `order_by` and `sort_expr`

  * **flat** (_False_) â whether to return a grouped collection (False) or a flattened collection (True)

  * **match_expr** (_None_) â 

an optional [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines which groups to include in the output view. If provided, this expression will be evaluated on the list of samples in each group. Only applicable when `flat=True`

  * **sort_expr** (_None_) â 

an optional [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines how to sort the groups in the output view. If provided, this expression will be evaluated on the list of samples in each group. Only applicable when `flat=True`

  * **create_index** (_False_) â whether to create an index, if necessary, to optimize the grouping. Only applicable when grouping by field(s), not expressions

  * **order_by_key** (_None_) â an optional fixed `order_by` value representing the first sample in a group. Required for optimized performance. See [this guide](user_guide__app.md#app-query-performant-stages) for more details



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

limit(_limit_)#
    

Returns a view with at most the given number of samples.

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
    
    view = dataset.limit(2)
    

Parameters:
    

**limit** â the maximum number of samples to return. If a non-positive number is provided, an empty view is returned

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

limit_labels(_field_ , _limit_)#
    

Limits the number of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances in the specified labels list field of each sample in the collection.

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
    # Only include the first detection in the `predictions` field of
    # each sample
    #
    
    view = dataset.limit_labels("predictions", 1)
    

Parameters:
    

  * **field** â the labels list field to filter

  * **limit** â the maximum number of labels to include in each labels list. If a non-positive number is provided, all lists will be empty



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

map_labels(_field_ , _map_)#
    

Maps the `label` values of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field to new values for each sample in the collection.

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
    
    view = dataset.map_labels("weather", {"partly cloudy": "cloudy"})
    
    #
    # Map "rabbit" and "squirrel" predictions to "other"
    #
    
    view = dataset.map_labels(
        "predictions", {"rabbit": "other", "squirrel": "other"}
    )
    

Parameters:
    

  * **field** â the labels field to map

  * **map** â a dict mapping label values to new label values



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

map_values(_field_ , _map_)#
    

Maps the values in the given field to new values for each sample in the collection.

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
    
    view = dataset.map_values("str_field", mapping)
    
    print(view.count_values("str_field"))
    # {"animal": 200}
    
    view = dataset.map_values("list_field", mapping)
    
    print(view.count_values("list_field"))
    # {"animal": 200}
    
    #
    # Map values in nested fields
    #
    
    view = dataset.map_values("ground_truth.detections.label", mapping)
    
    print(view.count_values("ground_truth.detections.label"))
    # {"animal": 183, ...}
    
    view = dataset.map_values("ground_truth.detections.tags", mapping)
    
    print(view.count_values("ground_truth.detections.tags"))
    # {"animal": 183, ...}
    

Parameters:
    

  * **field** â the field or `embedded.field.name` to map

  * **map** â a dict mapping values to new values



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

set_field(_field_ , _expr_ , __allow_missing =False_)#
    

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
    # Replace all values of the `uniqueness` field that are less than
    # 0.5 with `None`
    #
    
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.5).if_else(F("uniqueness"), None)
    )
    print(view.bounds("uniqueness"))
    
    #
    # Lower bound all object confidences in the `predictions` field at
    # 0.5
    #
    
    view = dataset.set_field(
        "predictions.detections.confidence", F("confidence").max(0.5)
    )
    print(view.bounds("predictions.detections.confidence"))
    
    #
    # Add a `num_predictions` property to the `predictions` field that
    # contains the number of objects in the field
    #
    
    view = dataset.set_field(
        "predictions.num_predictions",
        F("$predictions.detections").length(),
    )
    print(view.bounds("predictions.num_predictions"))
    
    #
    # Set an `is_animal` field on each object in the `predictions` field
    # that indicates whether the object is an animal
    #
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    view = dataset.set_field(
        "predictions.detections.is_animal", F("label").is_in(ANIMALS)
    )
    print(view.count_values("predictions.detections.is_animal"))
    

Parameters:
    

  * **field** â the field or `embedded.field.name` to set

  * **expr** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines the field value to set



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

match(_filter_)#
    

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
    
    view = dataset.match(F("filepath").ends_with(".jpg"))
    
    #
    # Only include samples whose `weather` field is "sunny"
    #
    
    view = dataset.match(F("weather.label") == "sunny")
    
    #
    # Only include samples with at least 2 objects in their
    # `predictions` field
    #
    
    view = dataset.match(F("predictions.detections").length() >= 2)
    
    #
    # Only include samples whose `predictions` field contains at least
    # one object with area smaller than 0.2
    #
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox = F("bounding_box")
    bbox_area = bbox[2] * bbox[3]
    
    small_boxes = F("predictions.detections").filter(bbox_area < 0.2)
    view = dataset.match(small_boxes.length() > 0)
    

Parameters:
    

**filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

match_frames(_filter_ , _omit_empty =True_)#
    

Filters the frames in the video collection by the given filter.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    #
    # Match frames with at least 10 detections
    #
    
    num_objects = F("detections.detections").length()
    view = dataset.match_frames(num_objects > 10)
    
    print(dataset.count())
    print(view.count())
    
    print(dataset.count("frames"))
    print(view.count("frames"))
    

Parameters:
    

  * **filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

  * **omit_empty** (_True_) â whether to omit samples with no frame labels after filtering



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

match_labels(_labels =None_, _ids =None_, _instance_ids =None_, _tags =None_, _filter =None_, _fields =None_, _bool =None_)#
    

Selects the samples from the collection that contain (or do not contain) at least one label that matches the specified criteria.

Note that, unlike `select_labels()` and `filter_labels()`, this stage will not filter the labels themselves; it only selects the corresponding samples.

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
    
    view = dataset.match_labels(labels=session.selected_labels)
    
    #
    # Only include samples that contain labels with the specified IDs
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    view = dataset.match_labels(ids=ids)
    
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
    view = dataset.match_labels(tags="test")
    
    print(len(view))
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    
    #
    # Only include samples that contain labels matching a filter
    #
    
    filter = F("confidence") > 0.99
    view = dataset.match_labels(filter=filter, fields="predictions")
    
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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

match_tags(_tags_ , _bool =None_, _all =False_)#
    

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
    
    view = dataset.match_tags("test")
    
    #
    # Only include samples that do not have the "test" tag
    #
    
    view = dataset.match_tags("test", bool=False)
    
    #
    # Only include samples that have the "test" or "train" tags
    #
    
    view = dataset.match_tags(["test", "train"])
    
    #
    # Only include samples that have the "test" and "train" tags
    #
    
    view = dataset.match_tags(["test", "train"], all=True)
    
    #
    # Only include samples that do not have the "test" or "train" tags
    #
    
    view = dataset.match_tags(["test", "train"], bool=False)
    
    #
    # Only include samples that do not have the "test" and "train" tags
    #
    
    view = dataset.match_tags(["test", "train"], bool=False, all=True)
    

Parameters:
    

  * **tags** â the tag or iterable of tags to match

  * **bool** (_None_) â whether to match samples that have (None or True) or do not have (False) the given tags

  * **all** (_False_) â whether to match samples that have (or donât have) all (True) or any (False) of the given tags



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

mongo(_pipeline_ , __needs_frames =None_, __group_slices =None_)#
    

Adds a view stage defined by a raw MongoDB aggregation pipeline.

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
    # Extract a view containing the second and third samples in the
    # dataset
    #
    
    view = dataset.mongo([{"$skip": 1}, {"$limit": 2}])
    
    #
    # Sort by the number of objects in the `precictions` field
    #
    
    view = dataset.mongo([
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
    

Parameters:
    

**pipeline** â a MongoDB aggregation pipeline (list of dicts)

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select(_sample_ids_ , _ordered =False_)#
    

Selects the samples with the given IDs from the collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Create a view containing the currently selected samples in the App
    #
    
    session = fo.launch_app(dataset)
    
    # Select samples in the App...
    
    view = dataset.select(session.selected)
    

Parameters:
    

**sample_ids** â 

the samples to select. Can be any of the following:

  * a sample ID

  * an iterable of sample IDs

  * an iterable of booleans of same length as the collection encoding which samples to select

  * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

  * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

  * a `fiftyone.core.collections.SampleCollection`




ordered (False): whether to sort the samples in the returned view to
    

match the order of the provided IDs

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select_by(_field_ , _values_ , _ordered =False_)#
    

Selects the samples with the given field values from the collection.

This stage is typically used to work with categorical fields (strings, ints, and bools). If you want to select samples based on floating point fields, use `match()`.

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
    
    view = dataset.select_by("int", [1, 51, 11, 41, 21, 31])
    print(view.head(6))
    
    #
    # Create a view containing samples whose `str` field have the given
    # values, in order
    #
    
    view = dataset.select_by(
        "str", ["1", "51", "11", "41", "21", "31"], ordered=True
    )
    print(view.head(6))
    

Parameters:
    

  * **field** â a field or `embedded.field.name`

  * **values** â a value or iterable of values to select by

  * **ordered** (_False_) â whether to sort the samples in the returned view to match the order of the provided values



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select_fields(_field_names =None_, _meta_filter =None_, __allow_missing =False_)#
    

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
    
    view = dataset.select_fields()
    
    #
    # Include only the `uniqueness` field (and the default fields) on
    # each sample
    #
    
    view = dataset.select_fields("uniqueness")
    
    #
    # Include only the `mood` attribute (and the default attributes) of
    # each `Detection` in the `ground_truth` field
    #
    
    view = dataset.select_fields("ground_truth.detections.mood")
    

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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select_frames(_frame_ids_ , _omit_empty =True_)#
    

Selects the frames with the given IDs from the video collection.

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
    
    view = dataset.select_frames(frame_ids)
    
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

    * a `fiftyone.core.collections.SampleCollection` whose frames to select

  * **omit_empty** (_True_) â whether to omit samples that have no frames after selecting the specified frames



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select_groups(_group_ids_ , _ordered =False_)#
    

Selects the groups with the given IDs from the grouped collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-groups")
    
    #
    # Select some specific groups by ID
    #
    
    group_ids = dataset.take(10).values("group.id")
    
    view = dataset.select_groups(group_ids)
    
    assert set(view.values("group.id")) == set(group_ids)
    
    view = dataset.select_groups(group_ids, ordered=True)
    
    assert view.values("group.id") == group_ids
    

Parameters:
    

  * **groups_ids** â 

the groups to select. Can be any of the following:

    * a group ID

    * an iterable of group IDs

    * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

    * a group dict returned by `get_group()`

    * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

    * an iterable of group dicts returned by `get_group()`

    * a `fiftyone.core.collections.SampleCollection`

  * **ordered** (_False_) â whether to sort the groups in the returned view to match the order of the provided IDs



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select_group_slices(_slices =None_, _media_type =None_, _flat =True_, __allow_mixed =False_, __force_mixed =False_)#
    

Selects the specified group slice(s) from the grouped collection.

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
    
    view = dataset.select_group_slices("ego")
    
    #
    # Retrieve the samples from the "left" or "right" group slices
    #
    
    view = dataset.select_group_slices(["left", "right"])
    
    #
    # Select only the "left" and "right" group slices
    #
    
    view = dataset.select_group_slices(["left", "right"], flat=False)
    
    #
    # Retrieve all image samples
    #
    
    view = dataset.select_group_slices(media_type="image")
    

Parameters:
    

  * **slices** (_None_) â a group slice or iterable of group slices to select. If neither argument is provided, a flattened list of all samples is returned

  * **media_type** (_None_) â a media type or iterable of media types whose slice(s) to select

  * **flat** (_True_) â whether to return a flattened collection (True) or a grouped collection (False)



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

select_labels(_labels =None_, _ids =None_, _instance_ids =None_, _tags =None_, _fields =None_, _omit_empty =True_)#
    

Selects only the specified labels from the collection.

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
    
    view = dataset.select_labels(labels=session.selected_labels)
    
    #
    # Only include labels with the specified IDs
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    view = dataset.select_labels(ids=ids)
    
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
    
    print(dataset.count_label_tags())
    
    # Retrieve the labels via their tag
    view = dataset.select_labels(tags="test")
    
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

  * **labels** (_None_) â a list of dicts specifying the labels to select in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels")

  * **ids** (_None_) â an ID or iterable of IDs of the labels to select

  * **instance_ids** (_None_) â an instance ID or iterable of instance IDs of the labels to select

  * **tags** (_None_) â a tag or iterable of tags of labels to select

  * **fields** (_None_) â a field or iterable of fields from which to select

  * **omit_empty** (_True_) â whether to omit samples that have no labels after filtering



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

shuffle(_seed =None_)#
    

Randomly shuffles the samples in the collection.

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
    
    view = dataset.shuffle()
    
    #
    # Shuffle the samples with a fixed random seed
    #
    
    view = dataset.shuffle(seed=51)
    

Parameters:
    

**seed** (_None_) â an optional random seed to use when shuffling the samples

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

skip(_skip_)#
    

Omits the given number of samples from the head of the collection.

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
    
    view = dataset.skip(2)
    

Parameters:
    

**skip** â the number of samples to skip. If a non-positive number is provided, no samples are omitted

Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

sort_by(_field_or_expr_ , _reverse =False_, _create_index =False_)#
    

Sorts the samples in the collection by the given field(s) or expression(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Sort the samples by their `uniqueness` field in ascending order
    #
    
    view = dataset.sort_by("uniqueness", reverse=False)
    
    #
    # Sorts the samples in descending order by the number of detections
    # in their `predictions` field whose bounding box area is less than
    # 0.2
    #
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox = F("bounding_box")
    bbox_area = bbox[2] * bbox[3]
    
    small_boxes = F("predictions.detections").filter(bbox_area < 0.2)
    view = dataset.sort_by(small_boxes.length(), reverse=True)
    
    #
    # Performs a compound sort where samples are first sorted in
    # descending or by number of detections and then in ascending order
    # of uniqueness for samples with the same number of predictions
    #
    
    view = dataset.sort_by(
        [
            (F("predictions.detections").length(), -1),
            ("uniqueness", 1),
        ]
    )
    
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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

sort_by_similarity(_query_ , _k =None_, _reverse =False_, _dist_field =None_, _brain_key =None_)#
    

Sorts the collection by similarity to a specified query.

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
    
    view = dataset.sort_by_similarity(query_id, k=5)
    
    #
    # Sort samples by their similarity to a manually computed vector
    #
    
    model = foz.load_zoo_model("clip-vit-base32-torch")
    embeddings = dataset.take(2, seed=51).compute_embeddings(model)
    query = embeddings.mean(axis=0)
    
    view = dataset.sort_by_similarity(query, k=5)
    
    #
    # Sort samples by their similarity to a text prompt
    #
    
    query = "kites high in the air"
    
    view = dataset.sort_by_similarity(query, k=5)
    

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



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

take(_size_ , _seed =None_)#
    

Randomly samples the given number of samples from the collection.

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
    
    view = dataset.take(2)
    
    #
    # Take two random samples from the dataset with a fixed seed
    #
    
    view = dataset.take(2, seed=51)
    

Parameters:
    

  * **size** â the number of samples to return. If a non-positive number is provided, an empty view is returned

  * **seed** (_None_) â an optional random seed to use when selecting the samples



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

to_patches(_field_ , _** kwargs_)#
    

Creates a view that contains one sample per object patch in the specified field of the collection.

Fields other than `field` and the default sample fields will not be included in the returned view. A `sample_id` field will be added that records the sample ID from which each patch was taken.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    session = fo.launch_app(dataset)
    
    #
    # Create a view containing the ground truth patches
    #
    
    view = dataset.to_patches("ground_truth")
    print(view)
    
    session.view = view
    

Parameters:
    

  * **field** â the patches field, which must be of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **other_fields** (_None_) â 

controls whether fields other than `field` and the default sample fields are included. Can be any of the following:

    * a field or list of fields to include

    * `True` to include all other fields

    * `None`/`False` to include no other fields

  * **keep_label_lists** (_False_) â whether to store the patches in label list fields of the same type as the input collection rather than using their single label variants

  * **include_indexes** (_False_) â whether to recreate any custom indexes on `field` and `other_fields` on the patches view (True) or a list of specific indexes or index prefixes to recreate. By default, no custom indexes are recreated



Returns:
    

a [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")

to_evaluation_patches(_eval_key_ , _** kwargs_)#
    

Creates a view based on the results of the evaluation with the given key that contains one sample for each true positive, false positive, and false negative example in the collection, respectively.

True positive examples will result in samples with both their ground truth and predicted fields populated, while false positive/negative examples will only have one of their corresponding predicted/ground truth fields populated, respectively.

If multiple predictions are matched to a ground truth object (e.g., if the evaluation protocol includes a crowd attribute), then all matched predictions will be stored in the single sample along with the ground truth object.

The returned dataset will also have top-level `type` and `iou` fields populated based on the evaluation results for that example, as well as a `sample_id` field recording the sample ID of the example, and a `crowd` field if the evaluation protocol defines a crowd attribute.

Note

The returned view will contain patches for the contents of this collection, which may differ from the view on which the `eval_key` evaluation was performed. This may exclude some labels that were evaluated and/or include labels that were not evaluated.

If you would like to see patches for the exact view on which an evaluation was performed, first call `load_evaluation_view()` to load the view and then convert to patches.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.evaluate_detections("predictions", eval_key="eval")
    
    session = fo.launch_app(dataset)
    
    #
    # Create a patches view for the evaluation results
    #
    
    view = dataset.to_evaluation_patches("eval")
    print(view)
    
    session.view = view
    

Parameters:
    

  * **eval_key** â an evaluation key that corresponds to the evaluation of ground truth/predicted fields that are of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **other_fields** (_None_) â 

controls whether fields other than the ground truth/predicted fields and the default sample fields are included. Can be any of the following:

    * a field or list of fields to include

    * `True` to include all other fields

    * `None`/`False` to include no other fields

  * **include_indexes** (_False_) â whether to recreate any custom indexes on the ground truth/predicted fields and `other_fields` on the patches view (True) or a list of specific indexes or index prefixes to recreate. By default, no custom indexes are recreated



Returns:
    

a [`fiftyone.core.patches.EvaluationPatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.EvaluationPatchesView "fiftyone.core.patches.EvaluationPatchesView")

to_clips(_field_or_expr_ , _** kwargs_)#
    

Creates a view that contains one sample per clip defined by the given field or expression in the video collection.

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
    
    clips = (
        dataset
        .filter_labels("frames.detections", F("label") == "road sign")
        .to_clips("frames.detections")
    )
    print(clips)
    
    #
    # Create a clips view that contains one clip for each contiguous
    # segment that contains at least two road signs in every frame
    #
    
    signs = F("detections.detections").filter(F("label") == "road sign")
    clips = dataset.to_clips(signs.length() >= 2)
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

  * **other_fields** (_None_) â 

controls whether sample fields other than the default sample fields are included. Can be any of the following:

    * a field or list of fields to include

    * `True` to include all other fields

    * `None`/`False` to include no other fields

  * **include_indexes** (_False_) â whether to recreate any custom indexes on `field_or_expr` and `other_fields` on the clips view (True) or a list of specific indexes or index prefixes to recreate. By default, no custom indexes are recreated

  * **tol** (_0_) â the maximum number of false frames that can be overlooked when generating clips. Only applicable when `field_or_expr` is a frame-level list field or expression

  * **min_len** (_0_) â the minimum allowable length of a clip, in frames. Only applicable when `field_or_expr` is a frame-level list field or an expression

  * **trajectories** (_False_) â whether to create clips for each unique object trajectory defined by their `(label, index)`. Only applicable when `field_or_expr` is a frame-level field



Returns:
    

a [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView")

to_trajectories(_field_ , _** kwargs_)#
    

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
    
    trajectories = (
        dataset
        .filter_labels("frames.detections", F("label") == "vehicle")
        .to_trajectories("frames.detections")
    )
    
    print(trajectories)
    

Parameters:
    

  * **field** â 

a frame-level label list field of any of the following types:

    * [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

    * [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

    * [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **other_fields** (_None_) â 

controls whether sample fields other than the default sample fields are included. Can be any of the following:

    * a field or list of fields to include

    * `True` to include all other fields

    * `None`/`False` to include no other fields

  * **include_indexes** (_False_) â whether to recreate any custom indexes on `other_fields` on the clips view (True) or a list of specific indexes or index prefixes to recreate. By default, no custom indexes are recreated

  * **tol** (_0_) â the maximum number of false frames that can be overlooked when generating clips

  * **min_len** (_0_) â the minimum allowable length of a clip, in frames



Returns:
    

a [`fiftyone.core.clips.TrajectoriesView`](api__fiftyone.core.clips.md#fiftyone.core.clips.TrajectoriesView "fiftyone.core.clips.TrajectoriesView")

to_frames(_** kwargs_)#
    

Creates a view that contains one sample per frame in the video collection.

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
    
    frames = dataset.to_frames(sample_frames=True)
    print(frames)
    
    session.view = frames
    
    #
    # Create a frames view that only contains frames with at least 10
    # objects, sampled at a maximum frame rate of 1fps
    #
    
    num_objects = F("detections.detections").length()
    view = dataset.match_frames(num_objects > 10)
    
    frames = view.to_frames(max_fps=1)
    print(frames)
    
    session.view = frames
    

Parameters:
    

  * **sample_frames** (_False_) â whether to assume that the frame images have already been sampled at locations stored in the `filepath` field of each frame (False), or whether to sample the video frames now according to the specified parameters (True)

  * **fps** (_None_) â an optional frame rate at which to sample each videoâs frames

  * **max_fps** (_None_) â an optional maximum frame rate at which to sample. Videos with frame rate exceeding this value are downsampled

  * **size** (_None_) â an optional `(width, height)` at which to sample frames. A dimension can be -1, in which case the aspect ratio is preserved. Only applicable when `sample_frames=True`

  * **min_size** (_None_) â an optional minimum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint. Only applicable when `sample_frames=True`

  * **max_size** (_None_) â an optional maximum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint. Only applicable when `sample_frames=True`

  * **sparse** (_False_) â whether to only sample frame images for frame numbers for which [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") instances exist in the input collection. This parameter has no effect when `sample_frames==False` since frames must always exist in order to have `filepath` information use

  * **output_dir** (_None_) â an optional output directory in which to write the sampled frames. By default, the frames are written in folders with the same basename of each video

  * **rel_dir** (_None_) â a relative directory to remove from the filepath of each video, if possible. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path"). This argument can be used in conjunction with `output_dir` to cause the sampled frames to be written in a nested directory structure within `output_dir` matching the shape of the input videoâs folder structure

  * **frames_patt** (_None_) â a pattern specifying the filename/format to use to write or check or existing sampled frames, e.g., `"%%06d.jpg"`. The default value is `fiftyone.config.default_sequence_idx + fiftyone.config.default_image_ext`

  * **force_sample** (_False_) â whether to resample videos whose sampled frames already exist. Only applicable when `sample_frames=True`

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if a video cannot be sampled

  * **verbose** (_False_) â whether to log information about the frames that will be sampled, if any

  * **include_indexes** (_False_) â whether to recreate any custom frame indexes on the frames view (True) or a list of specific indexes or index prefixes to recreate. By default, no custom indexes are recreated



Returns:
    

a [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView")

classmethod list_aggregations()#
    

Returns a list of all available methods on this collection that apply [`fiftyone.core.aggregations.Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") operations to this collection.

Returns:
    

a list of `SampleCollection` method names

bounds(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Computes the bounds of a numeric field of the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the bounds of a numeric field
    #
    
    bounds = dataset.bounds("numeric_field")
    print(bounds)  # (min, max)
    
    #
    # Compute the bounds of a numeric list field
    #
    
    bounds = dataset.bounds("numeric_list_field")
    print(bounds)  # (min, max)
    
    #
    # Compute the bounds of a transformation of a numeric field
    #
    
    bounds = dataset.bounds(2 * (F("numeric_field") + 1))
    print(bounds)  # (min, max)
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the `(min, max)` bounds

count(_field_or_expr =None_, _expr =None_, _safe =False_)#
    

Counts the number of field values in the collection.

`None`-valued fields are ignored.

If no field is provided, the samples themselves are counted.

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
                        fo.Detection(label="cat"),
                        fo.Detection(label="dog"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="rabbit"),
                        fo.Detection(label="squirrel"),
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
    # Count the number of samples in the dataset
    #
    
    count = dataset.count()
    print(count)  # the count
    
    #
    # Count the number of samples with `predictions`
    #
    
    count = dataset.count("predictions")
    print(count)  # the count
    
    #
    # Count the number of objects in the `predictions` field
    #
    
    count = dataset.count("predictions.detections")
    print(count)  # the count
    
    #
    # Count the number of objects in samples with > 2 predictions
    #
    
    count = dataset.count(
        (F("predictions.detections").length() > 2).if_else(
            F("predictions.detections"), None
        )
    )
    print(count)  # the count
    

Parameters:
    

  * **field_or_expr** (_None_) â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. If neither `field_or_expr` or `expr` is provided, the samples themselves are counted. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the count

count_values(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Counts the occurrences of field values in the collection.

This aggregation is typically applied to _countable_ field types (or lists of such types):

  * [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                tags=["sunny"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="dog"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                tags=["cloudy"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="rabbit"),
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
    # Compute the tag counts in the dataset
    #
    
    counts = dataset.count_values("tags")
    print(counts)  # dict mapping values to counts
    
    #
    # Compute the predicted label counts in the dataset
    #
    
    counts = dataset.count_values("predictions.detections.label")
    print(counts)  # dict mapping values to counts
    
    #
    # Compute the predicted label counts after some normalization
    #
    
    counts = dataset.count_values(
        F("predictions.detections.label").map_values(
            {"cat": "pet", "dog": "pet"}
        ).upper()
    )
    print(counts)  # dict mapping values to counts
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to treat nan/inf values as None when dealing with floating point values



Returns:
    

a dict mapping values to counts

distinct(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Computes the distinct values of a field in the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _countable_ field types (or lists of such types):

  * [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                tags=["sunny"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="dog"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                tags=["sunny", "cloudy"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="rabbit"),
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
    # Get the distinct tags in a dataset
    #
    
    values = dataset.distinct("tags")
    print(values)  # list of distinct values
    
    #
    # Get the distinct predicted labels in a dataset
    #
    
    values = dataset.distinct("predictions.detections.label")
    print(values)  # list of distinct values
    
    #
    # Get the distinct predicted labels after some normalization
    #
    
    values = dataset.distinct(
        F("predictions.detections.label").map_values(
            {"cat": "pet", "dog": "pet"}
        ).upper()
    )
    print(values)  # list of distinct values
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

a sorted list of distinct values

histogram_values(_field_or_expr_ , _expr =None_, _bins =None_, _range =None_, _auto =False_)#
    

Computes a histogram of the field values in the collection.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = []
    for idx in range(100):
        samples.append(
            fo.Sample(
                filepath="/path/to/image%d.png" % idx,
                numeric_field=np.random.randn(),
                numeric_list_field=list(np.random.randn(10)),
            )
        )
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    def plot_hist(counts, edges):
        counts = np.asarray(counts)
        edges = np.asarray(edges)
        left_edges = edges[:-1]
        widths = edges[1:] - edges[:-1]
        plt.bar(left_edges, counts, width=widths, align="edge")
    
    #
    # Compute a histogram of a numeric field
    #
    
    counts, edges, other = dataset.histogram_values(
        "numeric_field", bins=50, range=(-4, 4)
    )
    
    plot_hist(counts, edges)
    plt.show(block=False)
    
    #
    # Compute the histogram of a numeric list field
    #
    
    counts, edges, other = dataset.histogram_values(
        "numeric_list_field", bins=50
    )
    
    plot_hist(counts, edges)
    plt.show(block=False)
    
    #
    # Compute the histogram of a transformation of a numeric field
    #
    
    counts, edges, other = dataset.histogram_values(
        2 * (F("numeric_field") + 1), bins=50
    )
    
    plot_hist(counts, edges)
    plt.show(block=False)
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **bins** (_None_) â can be either an integer number of bins to generate or a monotonically increasing sequence specifying the bin edges to use. By default, 10 bins are created. If `bins` is an integer and no `range` is specified, bin edges are automatically distributed in an attempt to evenly distribute the counts in each bin

  * **range** (_None_) â a `(lower, upper)` tuple specifying a range in which to generate equal-width bins. Only applicable when `bins` is an integer

  * **auto** (_False_) â whether to automatically choose bin edges in an attempt to evenly distribute the counts in each bin. If this option is chosen, `bins` will only be used if it is an integer, and the `range` parameter is ignored



Returns:
    

a tuple of

  * counts: a list of counts in each bin

  * edges: an increasing list of bin edges of length `len(counts) + 1`. Note that each bin is treated as having an inclusive lower boundary and exclusive upper boundary, `[lower, upper)`, including the rightmost bin

  * other: the number of items outside the bins




min(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Computes the minimum of a numeric field of the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the minimum of a numeric field
    #
    
    min = dataset.min("numeric_field")
    print(min)  # the min
    
    #
    # Compute the minimum of a numeric list field
    #
    
    min = dataset.min("numeric_list_field")
    print(min)  # the min
    
    #
    # Compute the minimum of a transformation of a numeric field
    #
    
    min = dataset.min(2 * (F("numeric_field") + 1))
    print(min)  # the min
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the minimum value

max(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Computes the maximum of a numeric field of the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the maximum of a numeric field
    #
    
    max = dataset.max("numeric_field")
    print(max)  # the max
    
    #
    # Compute the maximum of a numeric list field
    #
    
    max = dataset.max("numeric_list_field")
    print(max)  # the max
    
    #
    # Compute the maximum of a transformation of a numeric field
    #
    
    max = dataset.max(2 * (F("numeric_field") + 1))
    print(max)  # the max
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the maximum value

mean(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Computes the arithmetic mean of the field values of the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the mean of a numeric field
    #
    
    mean = dataset.mean("numeric_field")
    print(mean)  # the mean
    
    #
    # Compute the mean of a numeric list field
    #
    
    mean = dataset.mean("numeric_list_field")
    print(mean)  # the mean
    
    #
    # Compute the mean of a transformation of a numeric field
    #
    
    mean = dataset.mean(2 * (F("numeric_field") + 1))
    print(mean)  # the mean
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the mean

quantiles(_field_or_expr_ , _quantiles_ , _expr =None_, _safe =False_)#
    

Computes the quantile(s) of the field values of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the quantiles of a numeric field
    #
    
    quantiles = dataset.quantiles("numeric_field", [0.1, 0.5, 0.9])
    print(quantiles)  # the quantiles
    
    #
    # Compute the quantiles of a numeric list field
    #
    
    quantiles = dataset.quantiles("numeric_list_field", [0.1, 0.5, 0.9])
    print(quantiles)  # the quantiles
    
    #
    # Compute the mean of a transformation of a numeric field
    #
    
    quantiles = dataset.quantiles(2 * (F("numeric_field") + 1), [0.1, 0.5, 0.9])
    print(quantiles)  # the quantiles
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **quantiles** â the quantile or iterable of quantiles to compute. Each quantile must be a numeric value in `[0, 1]`

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the quantile or list of quantiles

schema(_field_or_expr_ , _expr =None_, _dynamic_only =False_, __doc_type =None_, __include_private =False_)#
    

Extracts the names and types of the attributes of a specified embedded document field across all samples in the collection.

Schema aggregations are useful for detecting the presence and types of dynamic attributes of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields across a collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    
    sample1 = fo.Sample(
        filepath="image1.png",
        ground_truth=fo.Detections(
            detections=[
                fo.Detection(
                    label="cat",
                    bounding_box=[0.1, 0.1, 0.4, 0.4],
                    foo="bar",
                    hello=True,
                ),
                fo.Detection(
                    label="dog",
                    bounding_box=[0.5, 0.5, 0.4, 0.4],
                    hello=None,
                )
            ]
        )
    )
    
    sample2 = fo.Sample(
        filepath="image2.png",
        ground_truth=fo.Detections(
            detections=[
                fo.Detection(
                    label="rabbit",
                    bounding_box=[0.1, 0.1, 0.4, 0.4],
                    foo=None,
                ),
                fo.Detection(
                    label="squirrel",
                    bounding_box=[0.5, 0.5, 0.4, 0.4],
                    hello="there",
                ),
            ]
        )
    )
    
    dataset.add_samples([sample1, sample2])
    
    #
    # Get schema of all dynamic attributes on the detections in a
    # `Detections` field
    #
    
    print(dataset.schema("ground_truth.detections", dynamic_only=True))
    # {'foo': StringField, 'hello': [BooleanField, StringField]}
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **dynamic_only** (_False_) â whether to only include dynamically added attributes



Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances. If a fieldâs values takes multiple non-None types, the list of observed types will be returned

list_schema(_field_or_expr_ , _expr =None_)#
    

Extracts the value type(s) in a specified list field across all samples in the collection.

Examples:
    
    
    from datetime import datetime
    import fiftyone as fo
    
    dataset = fo.Dataset()
    
    sample1 = fo.Sample(
        filepath="image1.png",
        ground_truth=fo.Classification(
            label="cat",
            info=[
                fo.DynamicEmbeddedDocument(
                    task="initial_annotation",
                    author="Alice",
                    timestamp=datetime(1970, 1, 1),
                    notes=["foo", "bar"],
                ),
                fo.DynamicEmbeddedDocument(
                    task="editing_pass",
                    author="Bob",
                    timestamp=datetime.utcnow(),
                ),
            ],
        ),
    )
    
    sample2 = fo.Sample(
        filepath="image2.png",
        ground_truth=fo.Classification(
            label="dog",
            info=[
                fo.DynamicEmbeddedDocument(
                    task="initial_annotation",
                    author="Bob",
                    timestamp=datetime(2018, 10, 18),
                    notes=["spam", "eggs"],
                ),
            ],
        ),
    )
    
    dataset.add_samples([sample1, sample2])
    
    # Determine that `ground_truth.info` contains embedded documents
    print(dataset.list_schema("ground_truth.info"))
    # fo.EmbeddedDocumentField
    
    # Determine the fields of the embedded documents in the list
    print(dataset.schema("ground_truth.info[]"))
    # {'task': StringField, ..., 'notes': ListField}
    
    # Determine the type of the values in the nested `notes` list field
    # Since `ground_truth.info` is not yet declared on the dataset's
    # schema, we must manually include `[]` to unwind the info lists
    print(dataset.list_schema("ground_truth.info[].notes"))
    # fo.StringField
    
    # Declare the `ground_truth.info` field
    dataset.add_sample_field(
        "ground_truth.info",
        fo.ListField,
        subfield=fo.EmbeddedDocumentField,
        embedded_doc_type=fo.DynamicEmbeddedDocument,
    )
    
    # Now we can inspect the nested `notes` field without unwinding
    print(dataset.list_schema("ground_truth.info.notes"))
    # fo.StringField
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating



Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") or list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances describing the value type(s) in the list

std(_field_or_expr_ , _expr =None_, _safe =False_, _sample =False_)#
    

Computes the standard deviation of the field values of the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the standard deviation of a numeric field
    #
    
    std = dataset.std("numeric_field")
    print(std)  # the standard deviation
    
    #
    # Compute the standard deviation of a numeric list field
    #
    
    std = dataset.std("numeric_list_field")
    print(std)  # the standard deviation
    
    #
    # Compute the standard deviation of a transformation of a numeric field
    #
    
    std = dataset.std(2 * (F("numeric_field") + 1))
    print(std)  # the standard deviation
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values

  * **sample** (_False_) â whether to compute the sample standard deviation rather than the population standard deviation



Returns:
    

the standard deviation

sum(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Computes the sum of the field values of the collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the sum of a numeric field
    #
    
    total = dataset.sum("numeric_field")
    print(total)  # the sum
    
    #
    # Compute the sum of a numeric list field
    #
    
    total = dataset.sum("numeric_list_field")
    print(total)  # the sum
    
    #
    # Compute the sum of a transformation of a numeric field
    #
    
    total = dataset.sum(2 * (F("numeric_field") + 1))
    print(total)  # the sum
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values



Returns:
    

the sum

values(_field_or_expr_ , _expr =None_, _missing_value =None_, _unwind =False_, __allow_missing =False_, __big_result =True_, __raw =False_, __field =None_, __enforce_natural_order =True_)#
    

Extracts the values of a field from all samples in the collection.

Values aggregations are useful for efficiently extracting a slice of field or embedded field values across all samples in a collection. See the examples below for more details.

The dual function of `values()` is `set_values()`, which can be used to efficiently set a field or embedded field of all samples in a collection by providing lists of values of same structure returned by this aggregation.

Note

Unlike other aggregations, `values()` does not automatically unwind list fields, which ensures that the returned values match the potentially-nested structure of the documents.

You can opt-in to unwinding specific list fields using the `[]` syntax, or you can pass the optional `unwind=True` parameter to unwind all supported list fields. See [Aggregating list fields](https://docs.voxel51.com/user_guide/using_aggregations.html#aggregations-list-fields) for more information.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Get all values of a field
    #
    
    values = dataset.values("numeric_field")
    print(values)  # [1.0, 4.0, None]
    
    #
    # Get all values of a list field
    #
    
    values = dataset.values("numeric_list_field")
    print(values)  # [[1, 2, 3], [1, 2], None]
    
    #
    # Get all values of transformed field
    #
    
    values = dataset.values(2 * (F("numeric_field") + 1))
    print(values)  # [4.0, 10.0, None]
    
    #
    # Get values from a label list field
    #
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # list of `Detections`
    detections = dataset.values("ground_truth")
    
    # list of lists of `Detection` instances
    detections = dataset.values("ground_truth.detections")
    
    # list of lists of detection labels
    labels = dataset.values("ground_truth.detections.label")
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. This can also be a list or tuple of such arguments, in which case a tuple of corresponding aggregation results (each receiving the same additional keyword arguments, if any) will be returned

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **missing_value** (_None_) â a value to insert for missing or `None`-valued fields

  * **unwind** (_False_) â whether to automatically unwind all recognized list fields (True) or unwind all list fields except the top-level sample field (-1)



Returns:
    

the list of values

draw_labels(_output_dir_ , _rel_dir =None_, _label_fields =None_, _overwrite =False_, _config =None_, _progress =None_, _** kwargs_)#
    

Renders annotated versions of the media in the collection with the specified label data overlaid to the given directory.

The filenames of the sample media are maintained, unless a name conflict would occur in `output_dir`, in which case an index of the form `"-%d" % count` is appended to the base filename.

Images are written in format `fo.config.default_image_ext`, and videos are written in format `fo.config.default_video_ext`.

Parameters:
    

  * **output_dir** â the directory to write the annotated media

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each annotated media. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **label_fields** (_None_) â a label field or list of label fields to render. By default, all [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields are drawn

  * **overwrite** (_False_) â whether to delete `output_dir` if it exists before rendering

  * **config** (_None_) â an optional [`fiftyone.utils.annotations.DrawConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.DrawConfig "fiftyone.utils.annotations.DrawConfig") configuring how to draw the labels

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments specifying parameters of the default [`fiftyone.utils.annotations.DrawConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.DrawConfig "fiftyone.utils.annotations.DrawConfig") to override



Returns:
    

the list of paths to the rendered media

export(_export_dir =None_, _dataset_type =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _dataset_exporter =None_, _label_field =None_, _frame_labels_field =None_, _overwrite =False_, _progress =None_, _** kwargs_)#
    

Exports the samples in the collection to disk.

You can perform exports with this method via the following basic patterns:

  1. Provide `export_dir` and `dataset_type` to export the content to a directory in the default layout for the specified format, as documented in [this page](user_guide__export_datasets.md#exporting-datasets)

  2. Provide `dataset_type` along with `data_path`, `labels_path`, and/or `export_media` to directly specify where to export the source media and/or labels (if applicable) in your desired format. This syntax provides the flexibility to, for example, perform workflows like labels-only exports

  3. Provide a `dataset_exporter` to which to feed samples to perform a fully-customized export




In all workflows, the remaining parameters of this method can be provided to further configure the export.

See [this page](user_guide__export_datasets.md#exporting-datasets) for more information about the available export formats and examples of using this method.

See [this guide](user_guide__export_datasets.md#custom-dataset-exporter) for more details about exporting datasets in custom formats by defining your own [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter").

This method will automatically coerce the data to match the requested export in the following cases:

  * When exporting in either an unlabeled image or image classification format, if a spatial label field is provided ([`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")), then the **image patches** of the provided samples will be exported

  * When exporting in labeled image dataset formats that expect list-type labels ([`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")), if a label field contains labels in non-list format (e.g., [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")), the labels will be automatically upgraded to single-label lists

  * When exporting in labeled image dataset formats that expect [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") labels, if a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") field is provided, the labels will be automatically upgraded to detections that span the entire images




Parameters:
    

  * **export_dir** (_None_) â 

the directory to which to export the samples in format `dataset_type`. This parameter may be omitted if you have provided appropriate values for the `data_path` and/or `labels_path` parameters. Alternatively, this can also be an archive path with one of the following extensions:
        
        .zip, .tar, .tar.gz, .tgz, .tar.bz, .tbz
        

If an archive path is specified, the export is performed in a directory of same name (minus extension) and then automatically archived and the directory then deleted

  * **dataset_type** (_None_) â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type to write. If not specified, the default type for `label_field` is used

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media for certain export formats. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the media

    * an absolute directory path in which to export the media. In this case, the `export_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of a JSON manifest file in `export_dir` generated when `export_media` is `"manifest"`

    * an absolute filepath specifying the location to write the JSON manifest file when `export_media` is `"manifest"`. In this case, `export_dir` has no effect on the location of the data

If None, a default value of this parameter will be chosen based on the value of the `export_media` parameter. Note that this parameter is not applicable to certain export formats such as binary types like TF records

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Only applicable when exporting in certain labeled dataset formats. Can be any of the following:

    * a type-specific folder name like `"labels"` or `"labels/"` or a filename like `"labels.json"` or `"labels.xml"` specifying the location in `export_dir` in which to export the labels

    * an absolute directory or filepath in which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

For labeled datasets, the default value of this parameter will be chosen based on the export format so that the labels will be exported into `export_dir`

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media. This option is only useful when exporting labeled datasets whose label format stores sufficient information to locate the associated media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, an appropriate default value of this parameter will be chosen based on the value of the `data_path` parameter. Note that some dataset formats may not support certain values for this parameter (e.g., when exporting in binary formats such as TF records, âsymlinkâ is not an option)

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **dataset_exporter** (_None_) â a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") to use to export the samples. When provided, parameters such as `export_dir`, `dataset_type`, `data_path`, and `labels_path` have no effect

  * **label_field** (_None_) â 

controls the label field(s) to export. Only applicable to labeled datasets. Can be any of the following:

    * the name of a label field to export

    * a glob pattern of label field(s) to export

    * a list or tuple of label field(s) to export

    * a dictionary mapping label field names to keys to use when constructing the label dictionaries to pass to the exporter

Note that multiple fields can only be specified when the exporter used can handle dictionaries of labels. By default, the first field of compatible type for the exporter is used. When exporting labeled video datasets, this argument may contain frame fields prefixed by `"frames."`

  * **frame_labels_field** (_None_) â 

controls the frame label field(s) to export. The `"frames."` prefix is optional. Only applicable to labeled video datasets. Can be any of the following:

    * the name of a frame label field to export

    * a glob pattern of frame label field(s) to export

    * a list or tuple of frame label field(s) to export

    * a dictionary mapping frame label field names to keys to use when constructing the frame label dictionaries to pass to the exporter

Note that multiple fields can only be specified when the exporter used can handle dictionaries of frame labels. By default, the first field of compatible type for the exporter is used

  * **overwrite** (_False_) â whether to delete existing directories before performing the export (True) or to merge the export with existing files and directories (False)

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments to pass to the dataset exporterâs constructor. If you are exporting image patches, this can also contain keyword arguments for [`fiftyone.utils.patches.ImagePatchesExtractor`](api__fiftyone.utils.patches.md#fiftyone.utils.patches.ImagePatchesExtractor "fiftyone.utils.patches.ImagePatchesExtractor")




to_torch(_get_item_ , _vectorize =False_, _skip_failures =False_, _local_process_group =None_)#
    

Constructs a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") that loads data from this collection via the provided [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance.

Parameters:
    

  * **get_item** â a [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem")

  * **vectorize** (_False_) â whether to load and cache the required fields from the sample collection upfront (True) or lazily load the values from each sample when items are retrieved (False). Vectorizing gives faster data loading times, but you must have enough memory to store the required field values for the entire sample collection. When `vectorize=True`, all field values must be serializable; ie `pickle.dumps(field_value)` must not raise an error

  * **skip_failures** (_False_) â whether to skip failures that occur when calling `get_item`. If True, the exception will be returned rather than the intended field values

  * **local_process_group** (_None_) â the local process group. Only used during distributed training



Returns:
    

a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)")

annotate(_anno_key_ , _label_schema =None_, _label_field =None_, _label_type =None_, _classes =None_, _attributes =True_, _mask_targets =None_, _allow_additions =True_, _allow_deletions =True_, _allow_label_edits =True_, _allow_index_edits =True_, _allow_spatial_edits =True_, _media_field ='filepath'_, _backend =None_, _launch_editor =False_, _** kwargs_)#
    

Exports the samples and optional label field(s) in this collection to the given annotation backend.

The `backend` parameter controls which annotation backend to use. Depending on the backend you use, you may want/need to provide extra keyword arguments to this function for the constructor of the backendâs [`fiftyone.utils.annotations.AnnotationBackendConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackendConfig "fiftyone.utils.annotations.AnnotationBackendConfig") class.

The natively provided backends and their associated config classes are:

  * `"cvat"`: [`fiftyone.utils.cvat.CVATBackendConfig`](api__fiftyone.utils.cvat.md#fiftyone.utils.cvat.CVATBackendConfig "fiftyone.utils.cvat.CVATBackendConfig")

  * `"labelstudio"`: [`fiftyone.utils.labelstudio.LabelStudioBackendConfig`](api__fiftyone.utils.labelstudio.md#fiftyone.utils.labelstudio.LabelStudioBackendConfig "fiftyone.utils.labelstudio.LabelStudioBackendConfig")

  * `"labelbox"`: [`fiftyone.utils.labelbox.LabelboxBackendConfig`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxBackendConfig "fiftyone.utils.labelbox.LabelboxBackendConfig")




See [this page](integrations__annotation.md#requesting-annotations) for more information about using this method, including how to define label schemas and how to configure login credentials for your annotation provider.

Parameters:
    

  * **anno_key** â a string key to use to refer to this annotation run

  * **label_schema** (_None_) â a dictionary defining the label schema to use. If this argument is provided, it takes precedence over the other schema-related arguments

  * **label_field** (_None_) â a string indicating a new or existing label field to annotate

  * **label_type** (_None_) â 

a string indicating the type of labels to annotate. The possible values are:

    * `"classification"`: a single classification stored in [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") fields

    * `"classifications"`: multilabel classifications stored in [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields

    * `"detections"`: object detections stored in [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields

    * `"instances"`: instance segmentations stored in [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields with their [`mask`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection.mask "fiftyone.core.labels.Detection.mask") attributes populated

    * `"polylines"`: polylines stored in [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `False`

    * `"polygons"`: polygons stored in [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `True`

    * `"keypoints"`: keypoints stored in [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") fields

    * `"segmentation"`: semantic segmentations stored in [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") fields

    * `"scalar"`: scalar labels stored in [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField"), [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField"), [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField"), or [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField") fields

All new label fields must have their type specified via this argument or in `label_schema`. Note that annotation backends may not support all label types

  * **classes** (_None_) â a list of strings indicating the class options for `label_field` or all fields in `label_schema` without classes specified. All new label fields must have a class list provided via one of the supported methods. For existing label fields, if classes are not provided by this argument nor `label_schema`, they are retrieved from `get_classes()` if possible, or else the observed labels on your dataset are used

  * **attributes** (_True_) â 

specifies the label attributes of each label field to include (other than their `label`, which is always included) in the annotation export. Can be any of the following:

    * `True`: export all label attributes

    * `False`: donât export any custom label attributes

    * a list of label attributes to export

    * a dict mapping attribute names to dicts specifying the `type`, `values`, and `default` for each attribute

If a `label_schema` is also provided, this parameter determines which attributes are included for all fields that do not explicitly define their per-field attributes (in addition to any per-class attributes)

  * **mask_targets** (_None_) â a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to semantic label strings. Only applicable when annotating semantic segmentations. All new label fields must have mask targets provided via one of the supported methods. For existing label fields, if mask targets are not provided by this argument nor `label_schema`, any applicable mask targets stored on your dataset will be used, if available

  * **allow_additions** (_True_) â whether to allow new labels to be added. Only applicable when editing existing label fields

  * **allow_deletions** (_True_) â whether to allow labels to be deleted. Only applicable when editing existing label fields

  * **allow_label_edits** (_True_) â whether to allow the `label` attribute of existing labels to be modified. Only applicable when editing existing fields with `label` attributes

  * **allow_index_edits** (_True_) â whether to allow the `index` attribute of existing video tracks to be modified. Only applicable when editing existing frame fields with `index` attributes

  * **allow_spatial_edits** (_True_) â whether to allow edits to the spatial properties (bounding boxes, vertices, keypoints, masks, etc) of labels. Only applicable when editing existing spatial label fields

  * **media_field** (_"filepath"_) â the field containing the paths to the media files to upload

  * **backend** (_None_) â the annotation backend to use. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

  * **launch_editor** (_False_) â whether to launch the annotation backendâs editor after uploading the samples

  * ****kwargs** â keyword arguments for the [`fiftyone.utils.annotations.AnnotationBackendConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackendConfig "fiftyone.utils.annotations.AnnotationBackendConfig")



Returns:
    

an `fiftyone.utils.annotations.AnnnotationResults`

property has_annotation_runs#
    

Whether this collection has any annotation runs.

has_annotation_run(_anno_key_)#
    

Whether this collection has an annotation run with the given key.

Parameters:
    

**anno_key** â an annotation key

Returns:
    

True/False

list_annotation_runs(_type =None_, _method =None_, _** kwargs_)#
    

Returns a list of annotation keys on this collection.

Parameters:
    

  * **type** (_None_) â 

a specific annotation run type to match, which can be:

    * a string `fiftyone.core.annotations.AnnotationMethodConfig.type`

    * a `fiftyone.core.annotations.AnnotationMethod` class or its fully-qualified class name string

  * **method** (_None_) â a specific `fiftyone.core.annotations.AnnotationMethodConfig.method` string to match

  * ****kwargs** â optional config parameters to match



Returns:
    

a list of annotation keys

rename_annotation_run(_anno_key_ , _new_anno_key_)#
    

Replaces the key for the given annotation run with a new key.

Parameters:
    

  * **anno_key** â an annotation key

  * **new_anno_key** â a new annotation key




get_annotation_info(_anno_key_)#
    

Returns information about the annotation run with the given key on this collection.

Parameters:
    

**anno_key** â an annotation key

Returns:
    

a [`fiftyone.core.annotation.AnnotationInfo`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationInfo "fiftyone.core.annotation.AnnotationInfo")

load_annotation_results(_anno_key_ , _cache =True_, _** kwargs_)#
    

Loads the results for the annotation run with the given key on this collection.

The [`fiftyone.utils.annotations.AnnotationResults`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults "fiftyone.utils.annotations.AnnotationResults") object returned by this method will provide a variety of backend-specific methods allowing you to perform actions such as checking the status and deleting this run from the annotation backend.

Use `load_annotations()` to load the labels from an annotation run onto your FiftyOne dataset.

Parameters:
    

  * **anno_key** â an annotation key

  * **cache** (_True_) â whether to cache the results on the collection

  * ****kwargs** â keyword arguments for runâs [`fiftyone.core.annotation.AnnotationMethodConfig.load_credentials()`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationMethodConfig.load_credentials "fiftyone.core.annotation.AnnotationMethodConfig.load_credentials") method



Returns:
    

a [`fiftyone.utils.annotations.AnnotationResults`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults "fiftyone.utils.annotations.AnnotationResults")

load_annotation_view(_anno_key_ , _select_fields =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") on which the specified annotation run was performed on this collection.

Parameters:
    

  * **anno_key** â an annotation key

  * **select_fields** (_False_) â whether to exclude fields involved in other annotation runs



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

load_annotations(_anno_key_ , _dest_field =None_, _unexpected ='prompt'_, _cleanup =False_, _progress =None_, _** kwargs_)#
    

Downloads the labels from the given annotation run from the annotation backend and merges them into this collection.

See [this page](integrations__annotation.md#loading-annotations) for more information about using this method to import annotations that you have scheduled by calling `annotate()`.

Parameters:
    

  * **anno_key** â an annotation key

  * **dest_field** (_None_) â an optional name of a new destination field into which to load the annotations, or a dict mapping field names in the runâs label schema to new destination field names

  * **unexpected** (_"prompt"_) â 

how to deal with any unexpected labels that donât match the runâs label schema when importing. The supported values are:

    * `"prompt"`: present an interactive prompt to direct/discard unexpected labels

    * `"ignore"`: automatically ignore any unexpected labels

    * `"keep"`: automatically keep all unexpected labels in a field whose name matches the label type

    * `"return"`: return a dict containing all unexpected labels, or `None` if there arenât any

  * **cleanup** (_False_) â whether to delete any information regarding this run from the annotation backend after loading the annotations

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â keyword arguments for the runâs [`fiftyone.core.annotation.AnnotationMethodConfig.load_credentials()`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationMethodConfig.load_credentials "fiftyone.core.annotation.AnnotationMethodConfig.load_credentials") method



Returns:
    

`None`, unless `unexpected=="return"` and unexpected labels are found, in which case a dict containing the extra labels is returned

delete_annotation_run(_anno_key_)#
    

Deletes the annotation run with the given key from this collection.

Calling this method only deletes the **record** of the annotation run from the collection; it will not delete any annotations loaded onto your dataset via `load_annotations()`, nor will it delete any associated information from the annotation backend.

Use `load_annotation_results()` to programmatically manage/delete a run from the annotation backend.

Parameters:
    

**anno_key** â an annotation key

delete_annotation_runs()#
    

Deletes all annotation runs from this collection.

Calling this method only deletes the **records** of the annotation runs from this collection; it will not delete any annotations loaded onto your dataset via `load_annotations()`, nor will it delete any associated information from the annotation backend.

Use `load_annotation_results()` to programmatically manage/delete runs in the annotation backend.

list_indexes()#
    

Returns the list of index names on this collection.

Single-field indexes are referenced by their field name, while compound indexes are referenced by more complicated strings. See [`pymongo.collection.Collection.index_information()`](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.index_information "\(in PyMongo v4.17.0\)") for details on the compound format.

Returns:
    

the list of index names

get_index_information(_include_stats =False_, __keep_index_names =False_)#
    

Returns a dictionary of information about the indexes on this collection.

See [`pymongo.collection.Collection.index_information()`](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.index_information "\(in PyMongo v4.17.0\)") for details on the structure of this dictionary.

Parameters:
    

**include_stats** (_False_) â whether to include the size, usage, and build status of each index

Returns:
    

a dict mapping index names to info dicts

create_index(_field_or_spec_ , _unique =False_, _force =False_, _wait =True_, _** kwargs_)#
    

Creates an index on the given field or with the given specification, if necessary.

Indexes enable efficient sorting, merging, and other such operations.

Frame-level fields can be indexed by prepending `"frames."` to the field name.

Note

If a matching non-unique index exists and you request a unique index, the existing index will be converted to a unique index.

If a matching unique index exists and you request a non-unique index, the existing index will **only** be converted to a non-unique index if you specify `force=True`.

Note

If an index with the same field(s) but different order(s) already exists, the existing index will **only** be replaced with a new index if you specify `force=True`.

Parameters:
    

  * **field_or_spec** â the field name, `embedded.field.name`, or index specification list. See [`pymongo.collection.Collection.create_index()`](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index "\(in PyMongo v4.17.0\)") for supported values

  * **unique** (_False_) â whether to add a uniqueness constraint to the index

  * **force** (_False_) â whether to convert an existing unique index to a non-unique index or replace an existing index with different orderings with a new index. By default, existing indexes will not be modified in these cases

  * **wait** (_True_) â whether to wait for index creation to finish

  * ****kwargs** â optional keyword arguments for [`pymongo.collection.Collection.create_index()`](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index "\(in PyMongo v4.17.0\)")



Returns:
    

the name of the index

drop_index(_field_or_name_)#
    

Drops the index for the given field or name, if necessary.

Parameters:
    

**field_or_name** â a field name, `embedded.field.name`, or compound index name. Use `list_indexes()` to see the available indexes

reload()#
    

Reloads the collection from the database.

to_dict(_rel_dir =None_, _include_private =False_, _include_frames =False_, _frame_labels_dir =None_, _pretty_print =False_, _progress =None_)#
    

Returns a JSON dictionary representation of the collection.

Parameters:
    

  * **rel_dir** (_None_) â a relative directory to remove from the `filepath` of each sample, if possible. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path"). The typical use case for this argument is that your source data lives in a single directory and you wish to serialize relative, rather than absolute, paths to the data within that directory

  * **include_private** (_False_) â whether to include private fields

  * **include_frames** (_False_) â whether to include the frame labels for video samples

  * **frame_labels_dir** (_None_) â a directory in which to write per-sample JSON files containing the frame labels for video samples. If omitted, frame labels will be included directly in the returned JSON dict (which can be quite quite large for video datasets containing many frames). Only applicable to datasets that contain videos when `include_frames` is True

  * **pretty_print** (_False_) â whether to render frame labels JSON in human readable format with newlines and indentations. Only applicable to datasets that contain videos when a `frame_labels_dir` is provided

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a JSON dict

to_json(_rel_dir =None_, _include_private =False_, _include_frames =False_, _frame_labels_dir =None_, _pretty_print =False_)#
    

Returns a JSON string representation of the collection.

The samples will be written as a list in a top-level `samples` field of the returned dictionary.

Parameters:
    

  * **rel_dir** (_None_) â a relative directory to remove from the `filepath` of each sample, if possible. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path"). The typical use case for this argument is that your source data lives in a single directory and you wish to serialize relative, rather than absolute, paths to the data within that directory

  * **include_private** (_False_) â whether to include private fields

  * **include_frames** (_False_) â whether to include the frame labels for video samples

  * **frame_labels_dir** (_None_) â a directory in which to write per-sample JSON files containing the frame labels for video samples. If omitted, frame labels will be included directly in the returned JSON dict (which can be quite quite large for video datasets containing many frames). Only applicable to datasets that contain videos when `include_frames` is True

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations



Returns:
    

a JSON string

write_json(_json_path_ , _rel_dir =None_, _include_private =False_, _include_frames =False_, _frame_labels_dir =None_, _pretty_print =False_)#
    

Writes the collection to disk in JSON format.

Parameters:
    

  * **json_path** â the path to write the JSON

  * **rel_dir** (_None_) â a relative directory to remove from the `filepath` of each sample, if possible. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path"). The typical use case for this argument is that your source data lives in a single directory and you wish to serialize relative, rather than absolute, paths to the data within that directory

  * **include_private** (_False_) â whether to include private fields

  * **include_frames** (_False_) â whether to include the frame labels for video samples

  * **frame_labels_dir** (_None_) â a directory in which to write per-sample JSON files containing the frame labels for video samples. If omitted, frame labels will be included directly in the returned JSON dict (which can be quite quite large for video datasets containing many frames). Only applicable to datasets that contain videos when `include_frames` is True

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




aggregate(_aggregations_ , __mongo =False_)#
    

Aggregates one or more [`fiftyone.core.aggregations.Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") instances.

Note that it is best practice to group aggregations into a single call to `aggregate()`, as this will be more efficient than performing multiple aggregations in series.

Parameters:
    

**aggregations** â an [`fiftyone.core.aggregations.Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") or iterable of [`fiftyone.core.aggregations.Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") instances

Returns:
    

Aggregation result(s) corresponding to the input aggregation(s). Returns a single result for a single aggregation, a list of results for multiple aggregations, or a generator for lazy aggregations

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
