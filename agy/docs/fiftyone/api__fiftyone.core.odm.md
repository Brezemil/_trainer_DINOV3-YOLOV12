---
source_url: https://docs.voxel51.com/api/fiftyone.core.odm.html
---

# fiftyone.core.odm#

  * [fiftyone.core.odm.database](api__fiftyone.core.odm.database.md)
    * [`DatabaseConfigDocument`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.DatabaseConfigDocument)
      * [`DatabaseConfigDocument.version`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.DatabaseConfigDocument.version)
      * [`DatabaseConfigDocument.type`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.DatabaseConfigDocument.type)
      * [`DatabaseConfigDocument.save()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.DatabaseConfigDocument.save)
    * [`get_db_config()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_db_config)
    * [`establish_db_conn()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.establish_db_conn)
    * [`aggregate()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.aggregate)
    * [`ensure_connection()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.ensure_connection)
    * [`get_db_client()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_db_client)
    * [`get_db_conn()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_db_conn)
    * [`get_db_version()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_db_version)
    * [`get_async_db_client()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_async_db_client)
    * [`get_async_db_conn()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_async_db_conn)
    * [`drop_database()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_database)
    * [`sync_database()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.sync_database)
    * [`list_collections()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.list_collections)
    * [`drop_collection()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_collection)
    * [`drop_orphan_collections()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_collections)
    * [`drop_orphan_saved_views()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_saved_views)
    * [`drop_orphan_generated_datasets()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_generated_datasets)
    * [`drop_orphan_workspaces()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_workspaces)
    * [`drop_orphan_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_runs)
    * [`drop_orphan_delegated_ops()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_delegated_ops)
    * [`drop_orphan_stores()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.drop_orphan_stores)
    * [`stream_collection()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.stream_collection)
    * [`get_collection_stats()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_collection_stats)
    * [`count_documents()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.count_documents)
    * [`export_document()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.export_document)
    * [`export_collection()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.export_collection)
    * [`import_document()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.import_document)
    * [`import_collection()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.import_collection)
    * [`insert_documents()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.insert_documents)
    * [`bulk_write()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.bulk_write)
    * [`list_datasets()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.list_datasets)
    * [`load_dataset()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.load_dataset)
    * [`patch_saved_views()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.patch_saved_views)
    * [`patch_workspaces()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.patch_workspaces)
    * [`patch_annotation_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.patch_annotation_runs)
    * [`patch_brain_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.patch_brain_runs)
    * [`patch_evaluations()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.patch_evaluations)
    * [`patch_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.patch_runs)
    * [`delete_dataset()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_dataset)
    * [`delete_saved_view()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_saved_view)
    * [`delete_saved_views()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_saved_views)
    * [`delete_workspace()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_workspace)
    * [`delete_workspaces()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_workspaces)
    * [`delete_annotation_run()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_annotation_run)
    * [`delete_annotation_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_annotation_runs)
    * [`delete_brain_run()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_brain_run)
    * [`delete_brain_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_brain_runs)
    * [`delete_evaluation()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_evaluation)
    * [`delete_evaluations()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_evaluations)
    * [`delete_run()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_run)
    * [`delete_runs()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_runs)
    * [`get_indexed_values()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.get_indexed_values)
  * [fiftyone.core.odm.dataset](api__fiftyone.core.odm.dataset.md)
    * [`SampleFieldDocument`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument)
      * [`SampleFieldDocument.name`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.name)
      * [`SampleFieldDocument.ftype`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.ftype)
      * [`SampleFieldDocument.embedded_doc_type`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.embedded_doc_type)
      * [`SampleFieldDocument.subfield`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.subfield)
      * [`SampleFieldDocument.fields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.fields)
      * [`SampleFieldDocument.db_field`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.db_field)
      * [`SampleFieldDocument.description`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.description)
      * [`SampleFieldDocument.info`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.info)
      * [`SampleFieldDocument.read_only`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.read_only)
      * [`SampleFieldDocument.created_at`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.created_at)
      * [`SampleFieldDocument.to_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.to_field)
      * [`SampleFieldDocument.from_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.from_field)
      * [`SampleFieldDocument.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.STRICT)
      * [`SampleFieldDocument.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.clean)
      * [`SampleFieldDocument.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.clear_field)
      * [`SampleFieldDocument.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.copy)
      * [`SampleFieldDocument.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.fancy_repr)
      * [`SampleFieldDocument.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.field_names)
      * [`SampleFieldDocument.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.field_to_mongo)
      * [`SampleFieldDocument.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.field_to_python)
      * [`SampleFieldDocument.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.from_dict)
      * [`SampleFieldDocument.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.from_json)
      * [`SampleFieldDocument.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.get_field)
      * [`SampleFieldDocument.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.get_text_score)
      * [`SampleFieldDocument.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.has_field)
      * [`SampleFieldDocument.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.iter_fields)
      * [`SampleFieldDocument.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.merge)
      * [`SampleFieldDocument.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.my_metaclass)
      * [`SampleFieldDocument.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.set_field)
      * [`SampleFieldDocument.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.to_dict)
      * [`SampleFieldDocument.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.to_json)
      * [`SampleFieldDocument.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.to_mongo)
      * [`SampleFieldDocument.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument.validate)
    * [`SidebarGroupDocument`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument)
      * [`SidebarGroupDocument.name`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.name)
      * [`SidebarGroupDocument.paths`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.paths)
      * [`SidebarGroupDocument.expanded`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.expanded)
      * [`SidebarGroupDocument.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.STRICT)
      * [`SidebarGroupDocument.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.clean)
      * [`SidebarGroupDocument.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.clear_field)
      * [`SidebarGroupDocument.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.copy)
      * [`SidebarGroupDocument.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.fancy_repr)
      * [`SidebarGroupDocument.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.field_names)
      * [`SidebarGroupDocument.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.field_to_mongo)
      * [`SidebarGroupDocument.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.field_to_python)
      * [`SidebarGroupDocument.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.from_dict)
      * [`SidebarGroupDocument.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.from_json)
      * [`SidebarGroupDocument.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.get_field)
      * [`SidebarGroupDocument.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.get_text_score)
      * [`SidebarGroupDocument.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.has_field)
      * [`SidebarGroupDocument.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.iter_fields)
      * [`SidebarGroupDocument.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.merge)
      * [`SidebarGroupDocument.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.my_metaclass)
      * [`SidebarGroupDocument.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.set_field)
      * [`SidebarGroupDocument.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.to_dict)
      * [`SidebarGroupDocument.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.to_json)
      * [`SidebarGroupDocument.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.to_mongo)
      * [`SidebarGroupDocument.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SidebarGroupDocument.validate)
    * [`ActiveFields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields)
      * [`ActiveFields.exclude`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.exclude)
      * [`ActiveFields.paths`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.paths)
      * [`ActiveFields.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.STRICT)
      * [`ActiveFields.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.clean)
      * [`ActiveFields.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.clear_field)
      * [`ActiveFields.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.copy)
      * [`ActiveFields.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.fancy_repr)
      * [`ActiveFields.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.field_names)
      * [`ActiveFields.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.field_to_mongo)
      * [`ActiveFields.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.field_to_python)
      * [`ActiveFields.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.from_dict)
      * [`ActiveFields.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.from_json)
      * [`ActiveFields.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.get_field)
      * [`ActiveFields.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.get_text_score)
      * [`ActiveFields.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.has_field)
      * [`ActiveFields.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.iter_fields)
      * [`ActiveFields.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.merge)
      * [`ActiveFields.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.my_metaclass)
      * [`ActiveFields.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.set_field)
      * [`ActiveFields.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.to_dict)
      * [`ActiveFields.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.to_json)
      * [`ActiveFields.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.to_mongo)
      * [`ActiveFields.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ActiveFields.validate)
    * [`ColorScheme`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme)
      * [`ColorScheme.id`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.id)
      * [`ColorScheme.color_pool`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.color_pool)
      * [`ColorScheme.color_by`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.color_by)
      * [`ColorScheme.fields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.fields)
      * [`ColorScheme.label_tags`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.label_tags)
      * [`ColorScheme.multicolor_keypoints`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.multicolor_keypoints)
      * [`ColorScheme.opacity`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.opacity)
      * [`ColorScheme.show_skeletons`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.show_skeletons)
      * [`ColorScheme.default_mask_targets_colors`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.default_mask_targets_colors)
      * [`ColorScheme.colorscales`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.colorscales)
      * [`ColorScheme.default_colorscale`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.default_colorscale)
      * [`ColorScheme.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.STRICT)
      * [`ColorScheme.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.clean)
      * [`ColorScheme.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.clear_field)
      * [`ColorScheme.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.copy)
      * [`ColorScheme.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.fancy_repr)
      * [`ColorScheme.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.field_names)
      * [`ColorScheme.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.field_to_mongo)
      * [`ColorScheme.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.field_to_python)
      * [`ColorScheme.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.from_dict)
      * [`ColorScheme.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.from_json)
      * [`ColorScheme.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.get_field)
      * [`ColorScheme.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.get_text_score)
      * [`ColorScheme.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.has_field)
      * [`ColorScheme.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.iter_fields)
      * [`ColorScheme.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.merge)
      * [`ColorScheme.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.my_metaclass)
      * [`ColorScheme.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.set_field)
      * [`ColorScheme.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.to_dict)
      * [`ColorScheme.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.to_json)
      * [`ColorScheme.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.to_mongo)
      * [`ColorScheme.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme.validate)
    * [`KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton)
      * [`KeypointSkeleton.labels`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.labels)
      * [`KeypointSkeleton.edges`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.edges)
      * [`KeypointSkeleton.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.STRICT)
      * [`KeypointSkeleton.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.clean)
      * [`KeypointSkeleton.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.clear_field)
      * [`KeypointSkeleton.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.copy)
      * [`KeypointSkeleton.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.fancy_repr)
      * [`KeypointSkeleton.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.field_names)
      * [`KeypointSkeleton.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.field_to_mongo)
      * [`KeypointSkeleton.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.field_to_python)
      * [`KeypointSkeleton.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.from_dict)
      * [`KeypointSkeleton.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.from_json)
      * [`KeypointSkeleton.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.get_field)
      * [`KeypointSkeleton.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.get_text_score)
      * [`KeypointSkeleton.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.has_field)
      * [`KeypointSkeleton.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.iter_fields)
      * [`KeypointSkeleton.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.merge)
      * [`KeypointSkeleton.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.my_metaclass)
      * [`KeypointSkeleton.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.set_field)
      * [`KeypointSkeleton.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.to_dict)
      * [`KeypointSkeleton.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.to_json)
      * [`KeypointSkeleton.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.to_mongo)
      * [`KeypointSkeleton.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton.validate)
    * [`DatasetAppConfig`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig)
      * [`DatasetAppConfig.active_fields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.active_fields)
      * [`DatasetAppConfig.color_scheme`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.color_scheme)
      * [`DatasetAppConfig.disable_frame_filtering`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.disable_frame_filtering)
      * [`DatasetAppConfig.dynamic_groups_target_frame_rate`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.dynamic_groups_target_frame_rate)
      * [`DatasetAppConfig.grid_media_field`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.grid_media_field)
      * [`DatasetAppConfig.media_fallback`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.media_fallback)
      * [`DatasetAppConfig.media_fields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.media_fields)
      * [`DatasetAppConfig.modal_media_field`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.modal_media_field)
      * [`DatasetAppConfig.plugins`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.plugins)
      * [`DatasetAppConfig.sidebar_groups`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.sidebar_groups)
      * [`DatasetAppConfig.default_active_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.default_active_fields)
      * [`DatasetAppConfig.default_sidebar_groups()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.default_sidebar_groups)
      * [`DatasetAppConfig.is_custom()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.is_custom)
      * [`DatasetAppConfig.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.STRICT)
      * [`DatasetAppConfig.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.clean)
      * [`DatasetAppConfig.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.clear_field)
      * [`DatasetAppConfig.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.copy)
      * [`DatasetAppConfig.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.fancy_repr)
      * [`DatasetAppConfig.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.field_names)
      * [`DatasetAppConfig.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.field_to_mongo)
      * [`DatasetAppConfig.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.field_to_python)
      * [`DatasetAppConfig.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.from_dict)
      * [`DatasetAppConfig.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.from_json)
      * [`DatasetAppConfig.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.get_field)
      * [`DatasetAppConfig.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.get_text_score)
      * [`DatasetAppConfig.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.has_field)
      * [`DatasetAppConfig.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.iter_fields)
      * [`DatasetAppConfig.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.merge)
      * [`DatasetAppConfig.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.my_metaclass)
      * [`DatasetAppConfig.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.set_field)
      * [`DatasetAppConfig.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.to_dict)
      * [`DatasetAppConfig.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.to_json)
      * [`DatasetAppConfig.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.to_mongo)
      * [`DatasetAppConfig.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.validate)
    * [`DatasetDocument`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument)
      * [`DatasetDocument.name`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.name)
      * [`DatasetDocument.slug`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.slug)
      * [`DatasetDocument.version`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.version)
      * [`DatasetDocument.created_at`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.created_at)
      * [`DatasetDocument.last_modified_at`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.last_modified_at)
      * [`DatasetDocument.last_deletion_at`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.last_deletion_at)
      * [`DatasetDocument.last_loaded_at`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.last_loaded_at)
      * [`DatasetDocument.sample_collection_name`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.sample_collection_name)
      * [`DatasetDocument.frame_collection_name`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.frame_collection_name)
      * [`DatasetDocument.persistent`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.persistent)
      * [`DatasetDocument.media_type`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.media_type)
      * [`DatasetDocument.group_field`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.group_field)
      * [`DatasetDocument.group_media_types`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.group_media_types)
      * [`DatasetDocument.default_group_slice`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.default_group_slice)
      * [`DatasetDocument.tags`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.tags)
      * [`DatasetDocument.description`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.description)
      * [`DatasetDocument.info`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.info)
      * [`DatasetDocument.app_config`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.app_config)
      * [`DatasetDocument.classes`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.classes)
      * [`DatasetDocument.default_classes`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.default_classes)
      * [`DatasetDocument.mask_targets`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.mask_targets)
      * [`DatasetDocument.default_mask_targets`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.default_mask_targets)
      * [`DatasetDocument.skeletons`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.skeletons)
      * [`DatasetDocument.default_skeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.default_skeleton)
      * [`DatasetDocument.camera_intrinsics`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.camera_intrinsics)
      * [`DatasetDocument.static_transforms`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.static_transforms)
      * [`DatasetDocument.sample_fields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.sample_fields)
      * [`DatasetDocument.frame_fields`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.frame_fields)
      * [`DatasetDocument.saved_views`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.saved_views)
      * [`DatasetDocument.workspaces`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.workspaces)
      * [`DatasetDocument.annotation_runs`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.annotation_runs)
      * [`DatasetDocument.brain_methods`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.brain_methods)
      * [`DatasetDocument.evaluations`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.evaluations)
      * [`DatasetDocument.runs`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.runs)
      * [`DatasetDocument.active_label_schemas`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.active_label_schemas)
      * [`DatasetDocument.label_schemas`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.label_schemas)
      * [`DatasetDocument.get_saved_views()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_saved_views)
      * [`DatasetDocument.get_workspaces()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_workspaces)
      * [`DatasetDocument.get_annotation_runs()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_annotation_runs)
      * [`DatasetDocument.get_brain_methods()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_brain_methods)
      * [`DatasetDocument.get_evaluations()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_evaluations)
      * [`DatasetDocument.get_runs()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_runs)
      * [`DatasetDocument.DoesNotExist`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.DoesNotExist)
        * [`DatasetDocument.DoesNotExist.add_note()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.DoesNotExist.add_note)
        * [`DatasetDocument.DoesNotExist.args`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.DoesNotExist.args)
        * [`DatasetDocument.DoesNotExist.with_traceback()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.DoesNotExist.with_traceback)
      * [`DatasetDocument.MultipleObjectsReturned`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.MultipleObjectsReturned)
        * [`DatasetDocument.MultipleObjectsReturned.add_note()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.MultipleObjectsReturned.add_note)
        * [`DatasetDocument.MultipleObjectsReturned.args`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.MultipleObjectsReturned.args)
        * [`DatasetDocument.MultipleObjectsReturned.with_traceback()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.MultipleObjectsReturned.with_traceback)
      * [`DatasetDocument.STRICT`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.STRICT)
      * [`DatasetDocument.cascade_save()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.cascade_save)
      * [`DatasetDocument.clean()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.clean)
      * [`DatasetDocument.clear_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.clear_field)
      * [`DatasetDocument.compare_indexes()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.compare_indexes)
      * [`DatasetDocument.copy()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.copy)
      * [`DatasetDocument.copy_with_new_id()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.copy_with_new_id)
      * [`DatasetDocument.create_index()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.create_index)
      * [`DatasetDocument.delete()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.delete)
      * [`DatasetDocument.drop_collection()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.drop_collection)
      * [`DatasetDocument.ensure_indexes()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.ensure_indexes)
      * [`DatasetDocument.fancy_repr()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.fancy_repr)
      * [`DatasetDocument.field_names`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.field_names)
      * [`DatasetDocument.field_to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.field_to_mongo)
      * [`DatasetDocument.field_to_python()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.field_to_python)
      * [`DatasetDocument.from_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.from_dict)
      * [`DatasetDocument.from_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.from_json)
      * [`DatasetDocument.get_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_field)
      * [`DatasetDocument.get_text_score()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.get_text_score)
      * [`DatasetDocument.has_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.has_field)
      * [`DatasetDocument.id`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.id)
      * [`DatasetDocument.in_db`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.in_db)
      * [`DatasetDocument.iter_fields()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.iter_fields)
      * [`DatasetDocument.list_indexes()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.list_indexes)
      * [`DatasetDocument.merge()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.merge)
      * [`DatasetDocument.modify()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.modify)
      * [`DatasetDocument.my_metaclass`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.my_metaclass)
      * [`DatasetDocument.pk`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.pk)
      * [`DatasetDocument.register_delete_rule()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.register_delete_rule)
      * [`DatasetDocument.reload()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.reload)
      * [`DatasetDocument.save()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.save)
      * [`DatasetDocument.select_related()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.select_related)
      * [`DatasetDocument.set_field()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.set_field)
      * [`DatasetDocument.switch_collection()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.switch_collection)
      * [`DatasetDocument.switch_db()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.switch_db)
      * [`DatasetDocument.to_dbref()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.to_dbref)
      * [`DatasetDocument.to_dict()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.to_dict)
      * [`DatasetDocument.to_json()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.to_json)
      * [`DatasetDocument.to_mongo()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.to_mongo)
      * [`DatasetDocument.update()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.update)
      * [`DatasetDocument.validate()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetDocument.validate)
  * [fiftyone.core.odm.document](api__fiftyone.core.odm.document.md)
    * [`SerializableDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument)
      * [`SerializableDocument.field_names`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.field_names)
      * [`SerializableDocument.fancy_repr()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.fancy_repr)
      * [`SerializableDocument.has_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.has_field)
      * [`SerializableDocument.get_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.get_field)
      * [`SerializableDocument.set_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.set_field)
      * [`SerializableDocument.clear_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.clear_field)
      * [`SerializableDocument.iter_fields()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.iter_fields)
      * [`SerializableDocument.copy()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.copy)
      * [`SerializableDocument.merge()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.merge)
      * [`SerializableDocument.to_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.to_dict)
      * [`SerializableDocument.from_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.from_dict)
      * [`SerializableDocument.to_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.to_json)
      * [`SerializableDocument.from_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument.from_json)
    * [`MongoEngineBaseDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument)
      * [`MongoEngineBaseDocument.field_names`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.field_names)
      * [`MongoEngineBaseDocument.has_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.has_field)
      * [`MongoEngineBaseDocument.get_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.get_field)
      * [`MongoEngineBaseDocument.set_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.set_field)
      * [`MongoEngineBaseDocument.clear_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.clear_field)
      * [`MongoEngineBaseDocument.field_to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.field_to_mongo)
      * [`MongoEngineBaseDocument.field_to_python()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.field_to_python)
      * [`MongoEngineBaseDocument.to_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.to_dict)
      * [`MongoEngineBaseDocument.from_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.from_dict)
      * [`MongoEngineBaseDocument.copy()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.copy)
      * [`MongoEngineBaseDocument.fancy_repr()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.fancy_repr)
      * [`MongoEngineBaseDocument.from_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.from_json)
      * [`MongoEngineBaseDocument.iter_fields()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.iter_fields)
      * [`MongoEngineBaseDocument.merge()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.merge)
      * [`MongoEngineBaseDocument.to_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument.to_json)
    * [`DynamicMixin`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicMixin)
      * [`DynamicMixin.to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicMixin.to_mongo)
    * [`BaseDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument)
      * [`BaseDocument.id`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.id)
      * [`BaseDocument.in_db`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.in_db)
      * [`BaseDocument.clear_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.clear_field)
      * [`BaseDocument.copy()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.copy)
      * [`BaseDocument.fancy_repr()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.fancy_repr)
      * [`BaseDocument.field_names`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.field_names)
      * [`BaseDocument.field_to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.field_to_mongo)
      * [`BaseDocument.field_to_python()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.field_to_python)
      * [`BaseDocument.from_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.from_dict)
      * [`BaseDocument.from_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.from_json)
      * [`BaseDocument.get_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.get_field)
      * [`BaseDocument.has_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.has_field)
      * [`BaseDocument.iter_fields()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.iter_fields)
      * [`BaseDocument.merge()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.merge)
      * [`BaseDocument.set_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.set_field)
      * [`BaseDocument.to_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.to_dict)
      * [`BaseDocument.to_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument.to_json)
    * [`DynamicDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument)
      * [`DynamicDocument.id`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.id)
      * [`DynamicDocument.STRICT`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.STRICT)
      * [`DynamicDocument.cascade_save()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.cascade_save)
      * [`DynamicDocument.clean()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.clean)
      * [`DynamicDocument.clear_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.clear_field)
      * [`DynamicDocument.compare_indexes()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.compare_indexes)
      * [`DynamicDocument.copy()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.copy)
      * [`DynamicDocument.create_index()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.create_index)
      * [`DynamicDocument.delete()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.delete)
      * [`DynamicDocument.drop_collection()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.drop_collection)
      * [`DynamicDocument.ensure_indexes()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.ensure_indexes)
      * [`DynamicDocument.fancy_repr()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.fancy_repr)
      * [`DynamicDocument.field_names`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.field_names)
      * [`DynamicDocument.field_to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.field_to_mongo)
      * [`DynamicDocument.field_to_python()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.field_to_python)
      * [`DynamicDocument.from_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.from_dict)
      * [`DynamicDocument.from_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.from_json)
      * [`DynamicDocument.get_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.get_field)
      * [`DynamicDocument.get_text_score()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.get_text_score)
      * [`DynamicDocument.has_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.has_field)
      * [`DynamicDocument.in_db`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.in_db)
      * [`DynamicDocument.iter_fields()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.iter_fields)
      * [`DynamicDocument.list_indexes()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.list_indexes)
      * [`DynamicDocument.merge()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.merge)
      * [`DynamicDocument.modify()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.modify)
      * [`DynamicDocument.my_metaclass`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.my_metaclass)
      * [`DynamicDocument.pk`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.pk)
      * [`DynamicDocument.register_delete_rule()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.register_delete_rule)
      * [`DynamicDocument.reload()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.reload)
      * [`DynamicDocument.save()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.save)
      * [`DynamicDocument.select_related()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.select_related)
      * [`DynamicDocument.set_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.set_field)
      * [`DynamicDocument.switch_collection()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.switch_collection)
      * [`DynamicDocument.switch_db()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.switch_db)
      * [`DynamicDocument.to_dbref()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.to_dbref)
      * [`DynamicDocument.to_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.to_dict)
      * [`DynamicDocument.to_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.to_json)
      * [`DynamicDocument.to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.to_mongo)
      * [`DynamicDocument.update()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.update)
      * [`DynamicDocument.validate()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicDocument.validate)
    * [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document)
      * [`Document.id`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.id)
      * [`Document.copy()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.copy)
      * [`Document.reload()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.reload)
      * [`Document.save()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.save)
      * [`Document.copy_with_new_id()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.copy_with_new_id)
      * [`Document.STRICT`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.STRICT)
      * [`Document.cascade_save()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.cascade_save)
      * [`Document.clean()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.clean)
      * [`Document.clear_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.clear_field)
      * [`Document.compare_indexes()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.compare_indexes)
      * [`Document.create_index()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.create_index)
      * [`Document.delete()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.delete)
      * [`Document.drop_collection()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.drop_collection)
      * [`Document.ensure_indexes()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.ensure_indexes)
      * [`Document.fancy_repr()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.fancy_repr)
      * [`Document.field_names`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.field_names)
      * [`Document.field_to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.field_to_mongo)
      * [`Document.field_to_python()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.field_to_python)
      * [`Document.from_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.from_dict)
      * [`Document.from_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.from_json)
      * [`Document.get_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.get_field)
      * [`Document.get_text_score()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.get_text_score)
      * [`Document.has_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.has_field)
      * [`Document.in_db`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.in_db)
      * [`Document.iter_fields()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.iter_fields)
      * [`Document.list_indexes()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.list_indexes)
      * [`Document.merge()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.merge)
      * [`Document.modify()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.modify)
      * [`Document.my_metaclass`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.my_metaclass)
      * [`Document.pk`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.pk)
      * [`Document.register_delete_rule()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.register_delete_rule)
      * [`Document.select_related()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.select_related)
      * [`Document.set_field()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.set_field)
      * [`Document.switch_collection()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.switch_collection)
      * [`Document.switch_db()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.switch_db)
      * [`Document.to_dbref()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.to_dbref)
      * [`Document.to_dict()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.to_dict)
      * [`Document.to_json()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.to_json)
      * [`Document.to_mongo()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.to_mongo)
      * [`Document.update()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.update)
      * [`Document.validate()`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document.validate)
  * [fiftyone.core.odm.embedded_document](api__fiftyone.core.odm.embedded_document.md)
    * [`BaseEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument)
      * [`BaseEmbeddedDocument.clear_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.clear_field)
      * [`BaseEmbeddedDocument.copy()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.copy)
      * [`BaseEmbeddedDocument.fancy_repr()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.fancy_repr)
      * [`BaseEmbeddedDocument.field_names`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.field_names)
      * [`BaseEmbeddedDocument.field_to_mongo()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.field_to_mongo)
      * [`BaseEmbeddedDocument.field_to_python()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.field_to_python)
      * [`BaseEmbeddedDocument.from_dict()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.from_dict)
      * [`BaseEmbeddedDocument.from_json()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.from_json)
      * [`BaseEmbeddedDocument.get_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.get_field)
      * [`BaseEmbeddedDocument.has_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.has_field)
      * [`BaseEmbeddedDocument.iter_fields()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.iter_fields)
      * [`BaseEmbeddedDocument.merge()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.merge)
      * [`BaseEmbeddedDocument.set_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.set_field)
      * [`BaseEmbeddedDocument.to_dict()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.to_dict)
      * [`BaseEmbeddedDocument.to_json()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument.to_json)
    * [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument)
      * [`EmbeddedDocument.STRICT`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.STRICT)
      * [`EmbeddedDocument.clean()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.clean)
      * [`EmbeddedDocument.clear_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.clear_field)
      * [`EmbeddedDocument.copy()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.copy)
      * [`EmbeddedDocument.fancy_repr()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.fancy_repr)
      * [`EmbeddedDocument.field_names`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.field_names)
      * [`EmbeddedDocument.field_to_mongo()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.field_to_mongo)
      * [`EmbeddedDocument.field_to_python()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.field_to_python)
      * [`EmbeddedDocument.from_dict()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.from_dict)
      * [`EmbeddedDocument.from_json()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.from_json)
      * [`EmbeddedDocument.get_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.get_field)
      * [`EmbeddedDocument.get_text_score()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.get_text_score)
      * [`EmbeddedDocument.has_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.has_field)
      * [`EmbeddedDocument.iter_fields()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.iter_fields)
      * [`EmbeddedDocument.merge()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.merge)
      * [`EmbeddedDocument.my_metaclass`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.my_metaclass)
      * [`EmbeddedDocument.set_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.set_field)
      * [`EmbeddedDocument.to_dict()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.to_dict)
      * [`EmbeddedDocument.to_json()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.to_json)
      * [`EmbeddedDocument.to_mongo()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.to_mongo)
      * [`EmbeddedDocument.validate()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument.validate)
    * [`DynamicEmbeddedDocumentException`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocumentException)
      * [`DynamicEmbeddedDocumentException.add_note()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocumentException.add_note)
      * [`DynamicEmbeddedDocumentException.args`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocumentException.args)
      * [`DynamicEmbeddedDocumentException.with_traceback()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocumentException.with_traceback)
    * [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument)
      * [`DynamicEmbeddedDocument.STRICT`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.STRICT)
      * [`DynamicEmbeddedDocument.clean()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.clean)
      * [`DynamicEmbeddedDocument.clear_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.clear_field)
      * [`DynamicEmbeddedDocument.copy()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.copy)
      * [`DynamicEmbeddedDocument.fancy_repr()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.fancy_repr)
      * [`DynamicEmbeddedDocument.field_names`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.field_names)
      * [`DynamicEmbeddedDocument.field_to_mongo()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.field_to_mongo)
      * [`DynamicEmbeddedDocument.field_to_python()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.field_to_python)
      * [`DynamicEmbeddedDocument.from_dict()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.from_dict)
      * [`DynamicEmbeddedDocument.from_json()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.from_json)
      * [`DynamicEmbeddedDocument.get_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.get_field)
      * [`DynamicEmbeddedDocument.get_text_score()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.get_text_score)
      * [`DynamicEmbeddedDocument.has_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.has_field)
      * [`DynamicEmbeddedDocument.iter_fields()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.iter_fields)
      * [`DynamicEmbeddedDocument.merge()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.merge)
      * [`DynamicEmbeddedDocument.my_metaclass`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.my_metaclass)
      * [`DynamicEmbeddedDocument.set_field()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.set_field)
      * [`DynamicEmbeddedDocument.to_dict()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.to_dict)
      * [`DynamicEmbeddedDocument.to_json()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.to_json)
      * [`DynamicEmbeddedDocument.to_mongo()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.to_mongo)
      * [`DynamicEmbeddedDocument.validate()`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument.validate)
  * [fiftyone.core.odm.frame](api__fiftyone.core.odm.frame.md)
    * [`DatasetFrameDocument`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument)
      * [`DatasetFrameDocument.id`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.id)
      * [`DatasetFrameDocument.frame_number`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.frame_number)
      * [`DatasetFrameDocument.created_at`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.created_at)
      * [`DatasetFrameDocument.last_modified_at`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.last_modified_at)
      * [`DatasetFrameDocument.STRICT`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.STRICT)
      * [`DatasetFrameDocument.add_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.add_field)
      * [`DatasetFrameDocument.add_implied_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.add_implied_field)
      * [`DatasetFrameDocument.cascade_save()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.cascade_save)
      * [`DatasetFrameDocument.clean()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.clean)
      * [`DatasetFrameDocument.clear_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.clear_field)
      * [`DatasetFrameDocument.collection_name`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.collection_name)
      * [`DatasetFrameDocument.compare_indexes()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.compare_indexes)
      * [`DatasetFrameDocument.copy()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.copy)
      * [`DatasetFrameDocument.copy_with_new_id()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.copy_with_new_id)
      * [`DatasetFrameDocument.create_index()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.create_index)
      * [`DatasetFrameDocument.delete()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.delete)
      * [`DatasetFrameDocument.drop_collection()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.drop_collection)
      * [`DatasetFrameDocument.ensure_indexes()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.ensure_indexes)
      * [`DatasetFrameDocument.fancy_repr()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.fancy_repr)
      * [`DatasetFrameDocument.field_names`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.field_names)
      * [`DatasetFrameDocument.field_to_mongo()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.field_to_mongo)
      * [`DatasetFrameDocument.field_to_python()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.field_to_python)
      * [`DatasetFrameDocument.from_dict()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.from_dict)
      * [`DatasetFrameDocument.from_json()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.from_json)
      * [`DatasetFrameDocument.get_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.get_field)
      * [`DatasetFrameDocument.get_field_schema()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.get_field_schema)
      * [`DatasetFrameDocument.get_text_score()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.get_text_score)
      * [`DatasetFrameDocument.has_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.has_field)
      * [`DatasetFrameDocument.in_db`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.in_db)
      * [`DatasetFrameDocument.iter_fields()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.iter_fields)
      * [`DatasetFrameDocument.list_indexes()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.list_indexes)
      * [`DatasetFrameDocument.merge()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.merge)
      * [`DatasetFrameDocument.merge_field_schema()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.merge_field_schema)
      * [`DatasetFrameDocument.modify()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.modify)
      * [`DatasetFrameDocument.my_metaclass`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.my_metaclass)
      * [`DatasetFrameDocument.pk`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.pk)
      * [`DatasetFrameDocument.register_delete_rule()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.register_delete_rule)
      * [`DatasetFrameDocument.reload()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.reload)
      * [`DatasetFrameDocument.save()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.save)
      * [`DatasetFrameDocument.select_related()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.select_related)
      * [`DatasetFrameDocument.set_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.set_field)
      * [`DatasetFrameDocument.switch_collection()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.switch_collection)
      * [`DatasetFrameDocument.switch_db()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.switch_db)
      * [`DatasetFrameDocument.to_dbref()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.to_dbref)
      * [`DatasetFrameDocument.to_dict()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.to_dict)
      * [`DatasetFrameDocument.to_json()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.to_json)
      * [`DatasetFrameDocument.to_mongo()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.to_mongo)
      * [`DatasetFrameDocument.update()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.update)
      * [`DatasetFrameDocument.validate()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument.validate)
    * [`NoDatasetFrameDocument`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument)
      * [`NoDatasetFrameDocument.default_fields`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.default_fields)
      * [`NoDatasetFrameDocument.default_fields_ordered`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.default_fields_ordered)
      * [`NoDatasetFrameDocument.clear_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.clear_field)
      * [`NoDatasetFrameDocument.copy()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.copy)
      * [`NoDatasetFrameDocument.delete()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.delete)
      * [`NoDatasetFrameDocument.fancy_repr()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.fancy_repr)
      * [`NoDatasetFrameDocument.field_names`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.field_names)
      * [`NoDatasetFrameDocument.from_dict()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.from_dict)
      * [`NoDatasetFrameDocument.from_json()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.from_json)
      * [`NoDatasetFrameDocument.get_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.get_field)
      * [`NoDatasetFrameDocument.has_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.has_field)
      * [`NoDatasetFrameDocument.in_db`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.in_db)
      * [`NoDatasetFrameDocument.iter_fields()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.iter_fields)
      * [`NoDatasetFrameDocument.merge()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.merge)
      * [`NoDatasetFrameDocument.reload()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.reload)
      * [`NoDatasetFrameDocument.save()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.save)
      * [`NoDatasetFrameDocument.set_field()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.set_field)
      * [`NoDatasetFrameDocument.to_dict()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.to_dict)
      * [`NoDatasetFrameDocument.to_json()`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.NoDatasetFrameDocument.to_json)
  * [fiftyone.core.odm.mixins](api__fiftyone.core.odm.mixins.md)
    * [`get_default_fields()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.get_default_fields)
    * [`DatasetMixin`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin)
      * [`DatasetMixin.collection_name`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.collection_name)
      * [`DatasetMixin.field_names`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.field_names)
      * [`DatasetMixin.get_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.get_field)
      * [`DatasetMixin.set_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.set_field)
      * [`DatasetMixin.clear_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.clear_field)
      * [`DatasetMixin.get_field_schema()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.get_field_schema)
      * [`DatasetMixin.merge_field_schema()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.merge_field_schema)
      * [`DatasetMixin.add_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.add_field)
      * [`DatasetMixin.add_implied_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin.add_implied_field)
    * [`NoDatasetMixin`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin)
      * [`NoDatasetMixin.field_names`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.field_names)
      * [`NoDatasetMixin.in_db`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.in_db)
      * [`NoDatasetMixin.has_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.has_field)
      * [`NoDatasetMixin.get_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.get_field)
      * [`NoDatasetMixin.set_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.set_field)
      * [`NoDatasetMixin.clear_field()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.clear_field)
      * [`NoDatasetMixin.to_dict()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.to_dict)
      * [`NoDatasetMixin.from_dict()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.from_dict)
      * [`NoDatasetMixin.save()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.save)
      * [`NoDatasetMixin.reload()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.reload)
      * [`NoDatasetMixin.delete()`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin.delete)
  * [fiftyone.core.odm.ontology](api__fiftyone.core.odm.ontology.md)
    * [`OntologyType`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType)
      * [`OntologyType.TAXONOMY`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.TAXONOMY)
      * [`OntologyType.ANNOTATION_ONTOLOGY`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.ANNOTATION_ONTOLOGY)
      * [`OntologyType.encode()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.encode)
      * [`OntologyType.replace()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.replace)
      * [`OntologyType.split()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.split)
      * [`OntologyType.rsplit()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.rsplit)
      * [`OntologyType.join()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.join)
      * [`OntologyType.capitalize()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.capitalize)
      * [`OntologyType.casefold()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.casefold)
      * [`OntologyType.title()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.title)
      * [`OntologyType.center()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.center)
      * [`OntologyType.count()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.count)
      * [`OntologyType.expandtabs()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.expandtabs)
      * [`OntologyType.find()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.find)
      * [`OntologyType.partition()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.partition)
      * [`OntologyType.index()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.index)
      * [`OntologyType.ljust()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.ljust)
      * [`OntologyType.lower()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.lower)
      * [`OntologyType.lstrip()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.lstrip)
      * [`OntologyType.rfind()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.rfind)
      * [`OntologyType.rindex()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.rindex)
      * [`OntologyType.rjust()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.rjust)
      * [`OntologyType.rstrip()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.rstrip)
      * [`OntologyType.rpartition()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.rpartition)
      * [`OntologyType.splitlines()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.splitlines)
      * [`OntologyType.strip()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.strip)
      * [`OntologyType.swapcase()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.swapcase)
      * [`OntologyType.translate()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.translate)
      * [`OntologyType.upper()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.upper)
      * [`OntologyType.startswith()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.startswith)
      * [`OntologyType.endswith()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.endswith)
      * [`OntologyType.removeprefix()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.removeprefix)
      * [`OntologyType.removesuffix()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.removesuffix)
      * [`OntologyType.isascii()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isascii)
      * [`OntologyType.islower()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.islower)
      * [`OntologyType.isupper()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isupper)
      * [`OntologyType.istitle()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.istitle)
      * [`OntologyType.isspace()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isspace)
      * [`OntologyType.isdecimal()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isdecimal)
      * [`OntologyType.isdigit()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isdigit)
      * [`OntologyType.isnumeric()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isnumeric)
      * [`OntologyType.isalpha()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isalpha)
      * [`OntologyType.isalnum()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isalnum)
      * [`OntologyType.isidentifier()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isidentifier)
      * [`OntologyType.isprintable()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.isprintable)
      * [`OntologyType.zfill()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.zfill)
      * [`OntologyType.format()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.format)
      * [`OntologyType.format_map()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.format_map)
      * [`OntologyType.maketrans()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyType.maketrans)
    * [`OntologyDocument`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument)
      * [`OntologyDocument.name`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.name)
      * [`OntologyDocument.slug`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.slug)
      * [`OntologyDocument.version`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.version)
      * [`OntologyDocument.schema_version`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.schema_version)
      * [`OntologyDocument.type`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.type)
      * [`OntologyDocument.description`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.description)
      * [`OntologyDocument.root`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.root)
      * [`OntologyDocument.created_at`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.created_at)
      * [`OntologyDocument.last_modified_at`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.last_modified_at)
      * [`OntologyDocument.save()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.save)
      * [`OntologyDocument.DoesNotExist`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.DoesNotExist)
        * [`OntologyDocument.DoesNotExist.add_note()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.DoesNotExist.add_note)
        * [`OntologyDocument.DoesNotExist.args`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.DoesNotExist.args)
        * [`OntologyDocument.DoesNotExist.with_traceback()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.DoesNotExist.with_traceback)
      * [`OntologyDocument.MultipleObjectsReturned`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.MultipleObjectsReturned)
        * [`OntologyDocument.MultipleObjectsReturned.add_note()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.MultipleObjectsReturned.add_note)
        * [`OntologyDocument.MultipleObjectsReturned.args`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.MultipleObjectsReturned.args)
        * [`OntologyDocument.MultipleObjectsReturned.with_traceback()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.MultipleObjectsReturned.with_traceback)
      * [`OntologyDocument.STRICT`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.STRICT)
      * [`OntologyDocument.cascade_save()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.cascade_save)
      * [`OntologyDocument.clean()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.clean)
      * [`OntologyDocument.clear_field()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.clear_field)
      * [`OntologyDocument.compare_indexes()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.compare_indexes)
      * [`OntologyDocument.copy()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.copy)
      * [`OntologyDocument.copy_with_new_id()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.copy_with_new_id)
      * [`OntologyDocument.create_index()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.create_index)
      * [`OntologyDocument.delete()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.delete)
      * [`OntologyDocument.drop_collection()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.drop_collection)
      * [`OntologyDocument.ensure_indexes()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.ensure_indexes)
      * [`OntologyDocument.fancy_repr()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.fancy_repr)
      * [`OntologyDocument.field_names`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.field_names)
      * [`OntologyDocument.field_to_mongo()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.field_to_mongo)
      * [`OntologyDocument.field_to_python()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.field_to_python)
      * [`OntologyDocument.from_dict()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.from_dict)
      * [`OntologyDocument.from_json()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.from_json)
      * [`OntologyDocument.get_field()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.get_field)
      * [`OntologyDocument.get_text_score()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.get_text_score)
      * [`OntologyDocument.has_field()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.has_field)
      * [`OntologyDocument.id`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.id)
      * [`OntologyDocument.in_db`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.in_db)
      * [`OntologyDocument.iter_fields()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.iter_fields)
      * [`OntologyDocument.list_indexes()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.list_indexes)
      * [`OntologyDocument.merge()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.merge)
      * [`OntologyDocument.modify()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.modify)
      * [`OntologyDocument.my_metaclass`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.my_metaclass)
      * [`OntologyDocument.pk`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.pk)
      * [`OntologyDocument.register_delete_rule()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.register_delete_rule)
      * [`OntologyDocument.reload()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.reload)
      * [`OntologyDocument.select_related()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.select_related)
      * [`OntologyDocument.set_field()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.set_field)
      * [`OntologyDocument.switch_collection()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.switch_collection)
      * [`OntologyDocument.switch_db()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.switch_db)
      * [`OntologyDocument.to_dbref()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.to_dbref)
      * [`OntologyDocument.to_dict()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.to_dict)
      * [`OntologyDocument.to_json()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.to_json)
      * [`OntologyDocument.to_mongo()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.to_mongo)
      * [`OntologyDocument.update()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.update)
      * [`OntologyDocument.validate()`](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument.validate)
  * [fiftyone.core.odm.runs](api__fiftyone.core.odm.runs.md)
    * [`RunDocument`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument)
      * [`RunDocument.dataset_id`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.dataset_id)
      * [`RunDocument.key`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.key)
      * [`RunDocument.version`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.version)
      * [`RunDocument.timestamp`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.timestamp)
      * [`RunDocument.config`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.config)
      * [`RunDocument.view_stages`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.view_stages)
      * [`RunDocument.results`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.results)
      * [`RunDocument.DoesNotExist`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.DoesNotExist)
        * [`RunDocument.DoesNotExist.add_note()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.DoesNotExist.add_note)
        * [`RunDocument.DoesNotExist.args`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.DoesNotExist.args)
        * [`RunDocument.DoesNotExist.with_traceback()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.DoesNotExist.with_traceback)
      * [`RunDocument.MultipleObjectsReturned`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.MultipleObjectsReturned)
        * [`RunDocument.MultipleObjectsReturned.add_note()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.MultipleObjectsReturned.add_note)
        * [`RunDocument.MultipleObjectsReturned.args`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.MultipleObjectsReturned.args)
        * [`RunDocument.MultipleObjectsReturned.with_traceback()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.MultipleObjectsReturned.with_traceback)
      * [`RunDocument.STRICT`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.STRICT)
      * [`RunDocument.cascade_save()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.cascade_save)
      * [`RunDocument.clean()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.clean)
      * [`RunDocument.clear_field()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.clear_field)
      * [`RunDocument.compare_indexes()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.compare_indexes)
      * [`RunDocument.copy()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.copy)
      * [`RunDocument.copy_with_new_id()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.copy_with_new_id)
      * [`RunDocument.create_index()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.create_index)
      * [`RunDocument.delete()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.delete)
      * [`RunDocument.drop_collection()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.drop_collection)
      * [`RunDocument.ensure_indexes()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.ensure_indexes)
      * [`RunDocument.fancy_repr()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.fancy_repr)
      * [`RunDocument.field_names`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.field_names)
      * [`RunDocument.field_to_mongo()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.field_to_mongo)
      * [`RunDocument.field_to_python()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.field_to_python)
      * [`RunDocument.from_dict()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.from_dict)
      * [`RunDocument.from_json()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.from_json)
      * [`RunDocument.get_field()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.get_field)
      * [`RunDocument.get_text_score()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.get_text_score)
      * [`RunDocument.has_field()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.has_field)
      * [`RunDocument.id`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.id)
      * [`RunDocument.in_db`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.in_db)
      * [`RunDocument.iter_fields()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.iter_fields)
      * [`RunDocument.list_indexes()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.list_indexes)
      * [`RunDocument.merge()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.merge)
      * [`RunDocument.modify()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.modify)
      * [`RunDocument.my_metaclass`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.my_metaclass)
      * [`RunDocument.pk`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.pk)
      * [`RunDocument.register_delete_rule()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.register_delete_rule)
      * [`RunDocument.reload()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.reload)
      * [`RunDocument.save()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.save)
      * [`RunDocument.select_related()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.select_related)
      * [`RunDocument.set_field()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.set_field)
      * [`RunDocument.switch_collection()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.switch_collection)
      * [`RunDocument.switch_db()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.switch_db)
      * [`RunDocument.to_dbref()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.to_dbref)
      * [`RunDocument.to_dict()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.to_dict)
      * [`RunDocument.to_json()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.to_json)
      * [`RunDocument.to_mongo()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.to_mongo)
      * [`RunDocument.update()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.update)
      * [`RunDocument.validate()`](api__fiftyone.core.odm.runs.md#fiftyone.core.odm.runs.RunDocument.validate)
  * [fiftyone.core.odm.sample](api__fiftyone.core.odm.sample.md)
    * [`DatasetSampleDocument`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument)
      * [`DatasetSampleDocument.id`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.id)
      * [`DatasetSampleDocument.filepath`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.filepath)
      * [`DatasetSampleDocument.tags`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.tags)
      * [`DatasetSampleDocument.metadata`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.metadata)
      * [`DatasetSampleDocument.created_at`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.created_at)
      * [`DatasetSampleDocument.last_modified_at`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.last_modified_at)
      * [`DatasetSampleDocument.media_type`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.media_type)
      * [`DatasetSampleDocument.STRICT`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.STRICT)
      * [`DatasetSampleDocument.add_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.add_field)
      * [`DatasetSampleDocument.add_implied_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.add_implied_field)
      * [`DatasetSampleDocument.cascade_save()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.cascade_save)
      * [`DatasetSampleDocument.clean()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.clean)
      * [`DatasetSampleDocument.clear_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.clear_field)
      * [`DatasetSampleDocument.collection_name`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.collection_name)
      * [`DatasetSampleDocument.compare_indexes()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.compare_indexes)
      * [`DatasetSampleDocument.copy()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.copy)
      * [`DatasetSampleDocument.copy_with_new_id()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.copy_with_new_id)
      * [`DatasetSampleDocument.create_index()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.create_index)
      * [`DatasetSampleDocument.delete()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.delete)
      * [`DatasetSampleDocument.drop_collection()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.drop_collection)
      * [`DatasetSampleDocument.ensure_indexes()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.ensure_indexes)
      * [`DatasetSampleDocument.fancy_repr()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.fancy_repr)
      * [`DatasetSampleDocument.field_names`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.field_names)
      * [`DatasetSampleDocument.field_to_mongo()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.field_to_mongo)
      * [`DatasetSampleDocument.field_to_python()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.field_to_python)
      * [`DatasetSampleDocument.from_dict()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.from_dict)
      * [`DatasetSampleDocument.from_json()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.from_json)
      * [`DatasetSampleDocument.get_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.get_field)
      * [`DatasetSampleDocument.get_field_schema()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.get_field_schema)
      * [`DatasetSampleDocument.get_text_score()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.get_text_score)
      * [`DatasetSampleDocument.has_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.has_field)
      * [`DatasetSampleDocument.in_db`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.in_db)
      * [`DatasetSampleDocument.iter_fields()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.iter_fields)
      * [`DatasetSampleDocument.list_indexes()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.list_indexes)
      * [`DatasetSampleDocument.merge()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.merge)
      * [`DatasetSampleDocument.merge_field_schema()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.merge_field_schema)
      * [`DatasetSampleDocument.modify()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.modify)
      * [`DatasetSampleDocument.my_metaclass`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.my_metaclass)
      * [`DatasetSampleDocument.pk`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.pk)
      * [`DatasetSampleDocument.register_delete_rule()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.register_delete_rule)
      * [`DatasetSampleDocument.reload()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.reload)
      * [`DatasetSampleDocument.save()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.save)
      * [`DatasetSampleDocument.select_related()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.select_related)
      * [`DatasetSampleDocument.set_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.set_field)
      * [`DatasetSampleDocument.switch_collection()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.switch_collection)
      * [`DatasetSampleDocument.switch_db()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.switch_db)
      * [`DatasetSampleDocument.to_dbref()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.to_dbref)
      * [`DatasetSampleDocument.to_dict()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.to_dict)
      * [`DatasetSampleDocument.to_json()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.to_json)
      * [`DatasetSampleDocument.to_mongo()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.to_mongo)
      * [`DatasetSampleDocument.update()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.update)
      * [`DatasetSampleDocument.validate()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument.validate)
    * [`NoDatasetSampleDocument`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument)
      * [`NoDatasetSampleDocument.default_fields`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.default_fields)
      * [`NoDatasetSampleDocument.default_fields_ordered`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.default_fields_ordered)
      * [`NoDatasetSampleDocument.media_type`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.media_type)
      * [`NoDatasetSampleDocument.clear_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.clear_field)
      * [`NoDatasetSampleDocument.copy()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.copy)
      * [`NoDatasetSampleDocument.delete()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.delete)
      * [`NoDatasetSampleDocument.fancy_repr()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.fancy_repr)
      * [`NoDatasetSampleDocument.field_names`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.field_names)
      * [`NoDatasetSampleDocument.from_dict()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.from_dict)
      * [`NoDatasetSampleDocument.from_json()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.from_json)
      * [`NoDatasetSampleDocument.get_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.get_field)
      * [`NoDatasetSampleDocument.has_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.has_field)
      * [`NoDatasetSampleDocument.in_db`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.in_db)
      * [`NoDatasetSampleDocument.iter_fields()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.iter_fields)
      * [`NoDatasetSampleDocument.merge()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.merge)
      * [`NoDatasetSampleDocument.reload()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.reload)
      * [`NoDatasetSampleDocument.save()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.save)
      * [`NoDatasetSampleDocument.set_field()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.set_field)
      * [`NoDatasetSampleDocument.to_dict()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.to_dict)
      * [`NoDatasetSampleDocument.to_json()`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument.to_json)
  * [fiftyone.core.odm.utils](api__fiftyone.core.odm.utils.md)
    * [`serialize_value()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.serialize_value)
    * [`deserialize_value()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.deserialize_value)
    * [`validate_field_name()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.validate_field_name)
    * [`create_field()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.create_field)
    * [`create_implied_field()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.create_implied_field)
    * [`get_field_kwargs()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.get_field_kwargs)
    * [`get_implied_field_kwargs()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.get_implied_field_kwargs)
    * [`validate_fields_match()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.validate_fields_match)
    * [`DocumentRegistry`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.DocumentRegistry)
    * [`DocumentRegistryError`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.DocumentRegistryError)
      * [`DocumentRegistryError.add_note()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.DocumentRegistryError.add_note)
      * [`DocumentRegistryError.args`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.DocumentRegistryError.args)
      * [`DocumentRegistryError.with_traceback()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.DocumentRegistryError.with_traceback)
    * [`load_dataset()`](api__fiftyone.core.odm.utils.md#fiftyone.core.odm.utils.load_dataset)
  * [fiftyone.core.odm.views](api__fiftyone.core.odm.views.md)
    * [`SavedViewDocument`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument)
      * [`SavedViewDocument.dataset_id`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.dataset_id)
      * [`SavedViewDocument.name`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.name)
      * [`SavedViewDocument.description`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.description)
      * [`SavedViewDocument.slug`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.slug)
      * [`SavedViewDocument.color`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.color)
      * [`SavedViewDocument.view_stages`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.view_stages)
      * [`SavedViewDocument.created_at`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.created_at)
      * [`SavedViewDocument.last_modified_at`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.last_modified_at)
      * [`SavedViewDocument.last_loaded_at`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.last_loaded_at)
      * [`SavedViewDocument.DoesNotExist`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.DoesNotExist)
        * [`SavedViewDocument.DoesNotExist.add_note()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.DoesNotExist.add_note)
        * [`SavedViewDocument.DoesNotExist.args`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.DoesNotExist.args)
        * [`SavedViewDocument.DoesNotExist.with_traceback()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.DoesNotExist.with_traceback)
      * [`SavedViewDocument.MultipleObjectsReturned`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.MultipleObjectsReturned)
        * [`SavedViewDocument.MultipleObjectsReturned.add_note()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.MultipleObjectsReturned.add_note)
        * [`SavedViewDocument.MultipleObjectsReturned.args`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.MultipleObjectsReturned.args)
        * [`SavedViewDocument.MultipleObjectsReturned.with_traceback()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.MultipleObjectsReturned.with_traceback)
      * [`SavedViewDocument.STRICT`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.STRICT)
      * [`SavedViewDocument.cascade_save()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.cascade_save)
      * [`SavedViewDocument.clean()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.clean)
      * [`SavedViewDocument.clear_field()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.clear_field)
      * [`SavedViewDocument.compare_indexes()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.compare_indexes)
      * [`SavedViewDocument.copy()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.copy)
      * [`SavedViewDocument.copy_with_new_id()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.copy_with_new_id)
      * [`SavedViewDocument.create_index()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.create_index)
      * [`SavedViewDocument.delete()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.delete)
      * [`SavedViewDocument.drop_collection()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.drop_collection)
      * [`SavedViewDocument.ensure_indexes()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.ensure_indexes)
      * [`SavedViewDocument.fancy_repr()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.fancy_repr)
      * [`SavedViewDocument.field_names`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.field_names)
      * [`SavedViewDocument.field_to_mongo()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.field_to_mongo)
      * [`SavedViewDocument.field_to_python()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.field_to_python)
      * [`SavedViewDocument.from_dict()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.from_dict)
      * [`SavedViewDocument.from_json()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.from_json)
      * [`SavedViewDocument.get_field()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.get_field)
      * [`SavedViewDocument.get_text_score()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.get_text_score)
      * [`SavedViewDocument.has_field()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.has_field)
      * [`SavedViewDocument.id`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.id)
      * [`SavedViewDocument.in_db`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.in_db)
      * [`SavedViewDocument.iter_fields()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.iter_fields)
      * [`SavedViewDocument.list_indexes()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.list_indexes)
      * [`SavedViewDocument.merge()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.merge)
      * [`SavedViewDocument.modify()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.modify)
      * [`SavedViewDocument.my_metaclass`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.my_metaclass)
      * [`SavedViewDocument.pk`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.pk)
      * [`SavedViewDocument.register_delete_rule()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.register_delete_rule)
      * [`SavedViewDocument.reload()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.reload)
      * [`SavedViewDocument.save()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.save)
      * [`SavedViewDocument.select_related()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.select_related)
      * [`SavedViewDocument.set_field()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.set_field)
      * [`SavedViewDocument.switch_collection()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.switch_collection)
      * [`SavedViewDocument.switch_db()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.switch_db)
      * [`SavedViewDocument.to_dbref()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.to_dbref)
      * [`SavedViewDocument.to_dict()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.to_dict)
      * [`SavedViewDocument.to_json()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.to_json)
      * [`SavedViewDocument.to_mongo()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.to_mongo)
      * [`SavedViewDocument.update()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.update)
      * [`SavedViewDocument.validate()`](api__fiftyone.core.odm.views.md#fiftyone.core.odm.views.SavedViewDocument.validate)
  * [fiftyone.core.odm.workspace](api__fiftyone.core.odm.workspace.md)
    * [`AppComponent`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent)
      * [`AppComponent.component_id`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.component_id)
      * [`AppComponent.STRICT`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.STRICT)
      * [`AppComponent.clean()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.clean)
      * [`AppComponent.clear_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.clear_field)
      * [`AppComponent.copy()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.copy)
      * [`AppComponent.fancy_repr()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.fancy_repr)
      * [`AppComponent.field_names`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.field_names)
      * [`AppComponent.field_to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.field_to_mongo)
      * [`AppComponent.field_to_python()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.field_to_python)
      * [`AppComponent.from_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.from_dict)
      * [`AppComponent.from_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.from_json)
      * [`AppComponent.get_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.get_field)
      * [`AppComponent.get_text_score()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.get_text_score)
      * [`AppComponent.has_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.has_field)
      * [`AppComponent.iter_fields()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.iter_fields)
      * [`AppComponent.merge()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.merge)
      * [`AppComponent.my_metaclass`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.my_metaclass)
      * [`AppComponent.set_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.set_field)
      * [`AppComponent.to_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.to_dict)
      * [`AppComponent.to_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.to_json)
      * [`AppComponent.to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.to_mongo)
      * [`AppComponent.validate()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent.validate)
    * [`Panel`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel)
      * [`Panel.type`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.type)
      * [`Panel.pinned`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.pinned)
      * [`Panel.state`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.state)
      * [`Panel.STRICT`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.STRICT)
      * [`Panel.clean()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.clean)
      * [`Panel.clear_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.clear_field)
      * [`Panel.component_id`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.component_id)
      * [`Panel.copy()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.copy)
      * [`Panel.fancy_repr()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.fancy_repr)
      * [`Panel.field_names`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.field_names)
      * [`Panel.field_to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.field_to_mongo)
      * [`Panel.field_to_python()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.field_to_python)
      * [`Panel.from_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.from_dict)
      * [`Panel.from_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.from_json)
      * [`Panel.get_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.get_field)
      * [`Panel.get_text_score()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.get_text_score)
      * [`Panel.has_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.has_field)
      * [`Panel.iter_fields()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.iter_fields)
      * [`Panel.merge()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.merge)
      * [`Panel.my_metaclass`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.my_metaclass)
      * [`Panel.set_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.set_field)
      * [`Panel.to_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.to_dict)
      * [`Panel.to_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.to_json)
      * [`Panel.to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.to_mongo)
      * [`Panel.validate()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Panel.validate)
    * [`Space`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space)
      * [`Space.children`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.children)
      * [`Space.orientation`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.orientation)
      * [`Space.active_child`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.active_child)
      * [`Space.sizes`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.sizes)
      * [`Space.name`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.name)
      * [`Space.STRICT`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.STRICT)
      * [`Space.clean()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.clean)
      * [`Space.clear_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.clear_field)
      * [`Space.component_id`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.component_id)
      * [`Space.copy()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.copy)
      * [`Space.fancy_repr()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.fancy_repr)
      * [`Space.field_names`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.field_names)
      * [`Space.field_to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.field_to_mongo)
      * [`Space.field_to_python()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.field_to_python)
      * [`Space.from_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.from_dict)
      * [`Space.from_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.from_json)
      * [`Space.get_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.get_field)
      * [`Space.get_text_score()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.get_text_score)
      * [`Space.has_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.has_field)
      * [`Space.iter_fields()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.iter_fields)
      * [`Space.merge()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.merge)
      * [`Space.my_metaclass`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.my_metaclass)
      * [`Space.set_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.set_field)
      * [`Space.to_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.to_dict)
      * [`Space.to_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.to_json)
      * [`Space.to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.to_mongo)
      * [`Space.validate()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space.validate)
    * [`WorkspaceDocument`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument)
      * [`WorkspaceDocument.child`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.child)
      * [`WorkspaceDocument.color`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.color)
      * [`WorkspaceDocument.created_at`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.created_at)
      * [`WorkspaceDocument.dataset_id`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.dataset_id)
      * [`WorkspaceDocument.description`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.description)
      * [`WorkspaceDocument.last_loaded_at`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.last_loaded_at)
      * [`WorkspaceDocument.last_modified_at`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.last_modified_at)
      * [`WorkspaceDocument.slug`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.slug)
      * [`WorkspaceDocument.DoesNotExist`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.DoesNotExist)
        * [`WorkspaceDocument.DoesNotExist.add_note()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.DoesNotExist.add_note)
        * [`WorkspaceDocument.DoesNotExist.args`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.DoesNotExist.args)
        * [`WorkspaceDocument.DoesNotExist.with_traceback()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.DoesNotExist.with_traceback)
      * [`WorkspaceDocument.MultipleObjectsReturned`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.MultipleObjectsReturned)
        * [`WorkspaceDocument.MultipleObjectsReturned.add_note()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.MultipleObjectsReturned.add_note)
        * [`WorkspaceDocument.MultipleObjectsReturned.args`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.MultipleObjectsReturned.args)
        * [`WorkspaceDocument.MultipleObjectsReturned.with_traceback()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.MultipleObjectsReturned.with_traceback)
      * [`WorkspaceDocument.STRICT`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.STRICT)
      * [`WorkspaceDocument.cascade_save()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.cascade_save)
      * [`WorkspaceDocument.clean()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.clean)
      * [`WorkspaceDocument.clear_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.clear_field)
      * [`WorkspaceDocument.compare_indexes()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.compare_indexes)
      * [`WorkspaceDocument.copy()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.copy)
      * [`WorkspaceDocument.copy_with_new_id()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.copy_with_new_id)
      * [`WorkspaceDocument.create_index()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.create_index)
      * [`WorkspaceDocument.delete()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.delete)
      * [`WorkspaceDocument.drop_collection()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.drop_collection)
      * [`WorkspaceDocument.ensure_indexes()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.ensure_indexes)
      * [`WorkspaceDocument.fancy_repr()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.fancy_repr)
      * [`WorkspaceDocument.field_names`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.field_names)
      * [`WorkspaceDocument.field_to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.field_to_mongo)
      * [`WorkspaceDocument.field_to_python()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.field_to_python)
      * [`WorkspaceDocument.from_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.from_dict)
      * [`WorkspaceDocument.from_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.from_json)
      * [`WorkspaceDocument.get_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.get_field)
      * [`WorkspaceDocument.get_text_score()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.get_text_score)
      * [`WorkspaceDocument.has_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.has_field)
      * [`WorkspaceDocument.id`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.id)
      * [`WorkspaceDocument.in_db`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.in_db)
      * [`WorkspaceDocument.iter_fields()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.iter_fields)
      * [`WorkspaceDocument.list_indexes()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.list_indexes)
      * [`WorkspaceDocument.merge()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.merge)
      * [`WorkspaceDocument.modify()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.modify)
      * [`WorkspaceDocument.my_metaclass`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.my_metaclass)
      * [`WorkspaceDocument.name`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.name)
      * [`WorkspaceDocument.pk`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.pk)
      * [`WorkspaceDocument.register_delete_rule()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.register_delete_rule)
      * [`WorkspaceDocument.reload()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.reload)
      * [`WorkspaceDocument.save()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.save)
      * [`WorkspaceDocument.select_related()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.select_related)
      * [`WorkspaceDocument.set_field()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.set_field)
      * [`WorkspaceDocument.switch_collection()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.switch_collection)
      * [`WorkspaceDocument.switch_db()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.switch_db)
      * [`WorkspaceDocument.to_dbref()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.to_dbref)
      * [`WorkspaceDocument.to_dict()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.to_dict)
      * [`WorkspaceDocument.to_json()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.to_json)
      * [`WorkspaceDocument.to_mongo()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.to_mongo)
      * [`WorkspaceDocument.update()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.update)
      * [`WorkspaceDocument.validate()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.WorkspaceDocument.validate)
    * [`default_workspace_factory()`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.default_workspace_factory)



## Module contents#

ODM package declaration.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`aggregate`(collection,Â pipelines[,Â hints,Â ...]) | Executes one or more aggregations on a collection.  
---|---  
`get_db_config`() | Retrieves the database config.  
`establish_db_conn`(config) | Establishes the database connection.  
`get_db_client`() | Returns a database client.  
`get_db_conn`() | Returns a connection to the database.  
`get_db_version`() | Returns the database version.  
`get_async_db_client`([use_global]) | Returns an async database client.  
`get_async_db_conn`([use_global]) | Returns an async connection to the database.  
`drop_database`() | Drops the database.  
`sync_database`() | Syncs all pending database writes to disk.  
`list_datasets`() | Returns the list of available FiftyOne datasets.  
`load_dataset`([id,Â name,Â reload]) | Loads the FiftyOne dataset with the given ID or name.  
`patch_saved_views`(dataset_name[,Â dry_run]) | Ensures that the saved view documents in the `views` collection for the given dataset exactly match the IDs in its dataset document.  
`patch_workspaces`(dataset_name[,Â dry_run]) | Ensures that the workspace documents in the `workspaces` collection for the given dataset exactly match the IDs in its dataset document.  
`patch_annotation_runs`(dataset_name[,Â dry_run]) | Ensures that the annotation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`patch_brain_runs`(dataset_name[,Â dry_run]) | Ensures that the brain method runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`patch_evaluations`(dataset_name[,Â dry_run]) | Ensures that the evaluation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`patch_runs`(dataset_name[,Â dry_run]) | Ensures that the runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`delete_dataset`(name[,Â dry_run]) | Deletes the dataset with the given name.  
`delete_saved_view`(dataset_name,Â view_name[,Â ...]) | Deletes the saved view with the given name from the dataset with the given name.  
`delete_saved_views`(dataset_name[,Â dry_run]) | Deletes all saved views from the dataset with the given name.  
`delete_workspace`(dataset_name,Â workspace_name) | Deletes the workspace with the given name from the dataset with the given name.  
`delete_workspaces`(dataset_name[,Â dry_run]) | Deletes all workspaces from the dataset with the given name.  
`delete_evaluation`(name,Â eval_key[,Â dry_run]) | Deletes the evaluation run with the given key from the dataset with the given name.  
`delete_evaluations`(name[,Â dry_run]) | Deletes all evaluations from the dataset with the given name.  
`delete_brain_run`(name,Â brain_key[,Â dry_run]) | Deletes the brain method run with the given key from the dataset with the given name.  
`delete_brain_runs`(name[,Â dry_run]) | Deletes all brain method runs from the dataset with the given name.  
`delete_run`(name,Â run_key[,Â dry_run]) | Deletes the run with the given key from the dataset with the given name.  
`delete_runs`(name[,Â dry_run]) | Deletes all runs from the dataset with the given name.  
`drop_collection`(collection_name) | Drops specified collection from the database.  
`drop_orphan_collections`([dry_run]) | Drops all orphan collections from the database.  
`drop_orphan_saved_views`([dry_run]) | Drops all orphan saved views from the database.  
`drop_orphan_generated_datasets`([dry_run]) | Marks all orphan generated datasets as non-persistent so that they will  
`drop_orphan_workspaces`([dry_run]) | Drops all orphan workspaces from the database.  
`drop_orphan_runs`([dry_run]) | Drops all orphan runs from the database.  
`drop_orphan_delegated_ops`([dry_run]) | Drops all orphan delegated operations from the database.  
`drop_orphan_stores`([dry_run]) | Drops all orphan execution stores from the database.  
`list_collections`() | Returns a list of all collection names in the database.  
`get_collection_stats`(collection_name) | Sets stats about the collection.  
`get_indexed_values`(collection,Â ...[,Â ...]) | Returns the values of the field(s) for all samples in the given collection that are covered by the index.  
`stream_collection`(collection_name) | Streams the contents of the collection to stdout.  
`count_documents`(coll,Â pipeline) |   
`export_document`(doc,Â json_path) | Exports the document to disk in JSON format.  
`export_collection`(docs,Â json_dir_or_path[,Â ...]) | Exports the collection to disk in JSON format.  
`import_document`(json_path) | Imports a document from JSON on disk.  
`import_collection`(json_dir_or_path[,Â key]) | Imports the collection from JSON on disk.  
`insert_documents`(docs,Â coll[,Â ordered,Â ...]) | Inserts documents into a collection.  
`bulk_write`(ops,Â coll[,Â ordered,Â batcher,Â ...]) | Performs a batch of write operations on a collection.  
`get_default_fields`(cls[,Â include_private,Â ...]) | Gets the default fields present on all instances of the given `DatasetMixin` class.  
`serialize_value`(value[,Â extended]) | Serializes the given value.  
`deserialize_value`(value) | Deserializes the given value.  
`validate_field_name`(field_name[,Â ...]) | Verifies that the given field name is valid.  
`create_field`(name,Â ftype[,Â ...]) | Creates the field defined by the given specification.  
`create_implied_field`(path,Â value[,Â dynamic]) | Creates the field for the given value.  
`get_field_kwargs`(field) | Constructs the field keyword arguments dictionary for the given field.  
`get_implied_field_kwargs`(value[,Â dynamic]) | Infers the field keyword arguments dictionary for a field that can hold the given value.  
`validate_fields_match`(name,Â field,Â ...) | Validates that the types of the given fields match.  
`default_workspace_factory`() | Creates a default top-level instance of `Space`  
  
**Classes:**

`ActiveFields`(*args,Â **kwargs) | Description of active fields in the App as defined by the sidebar's checkboxes  
---|---  
`SampleFieldDocument`(*args,Â **kwargs) | Description of a sample field.  
`ColorScheme`(*args,Â **kwargs) | Description of a color scheme in the App.  
`KeypointSkeleton`(*args,Â **kwargs) | Description of a keypoint skeleton.  
`DatasetAppConfig`(*args,Â **kwargs) | Dataset-specific settings that customize how a dataset is visualized in the App.  
`DatasetDocument`(**kwargs) | Backing document for datasets.  
`SidebarGroupDocument`(*args,Â **kwargs) | Description of a sidebar group in the App.  
`Document`(**kwargs) | Base class for documents that are stored in a MongoDB collection.  
`SerializableDocument`() | Mixin for documents that can be serialized in BSON or JSON format.  
`BaseEmbeddedDocument`() | Base class for documents that are embedded within other documents and therefore are not stored in their own collection in the database.  
`DynamicEmbeddedDocument`(*args,Â **kwargs) | Base class for dynamic documents that are embedded within other documents and therefore aren't stored in their own collection in the database.  
`EmbeddedDocument`(*args,Â **kwargs) | Base class for documents that are embedded within other documents and therefore are not stored in their own collection in the database.  
`DatasetFrameDocument`(**kwargs) |   
`NoDatasetFrameDocument`(**kwargs) |   
`OntologyDocument`(**kwargs) | Backing document for ontologies.  
`OntologyType`(value) | Allowed values for `OntologyDocument.type` in storage and APIs.  
`RunDocument`(**kwargs) | Backing document for dataset runs.  
`DatasetSampleDocument`(**kwargs) | Base class for sample documents backing samples in datasets.  
`NoDatasetSampleDocument`(**kwargs) | Backing document for samples that have not been added to a dataset.  
`SavedViewDocument`(**kwargs) | Backing document for saved views.  
`Panel`(*args,Â **kwargs) | Document for a panel (tab) within a Workspace in the App.  
`Space`(*args,Â **kwargs) | Document for configuration of a Space in the App.  
`WorkspaceDocument`(*args,Â **kwargs) | Document for configuration of a saved workspace in the App.  
  
**Exceptions:**

`DynamicEmbeddedDocumentException` | Exception raised when an error occurs in a dynamic document operation.  
---|---  
  
fiftyone.core.odm.aggregate(_collection_ , _pipelines_ , _hints =None_, _maxTimeMS =None_, __stream =False_)#
    

Executes one or more aggregations on a collection.

> Multiple aggregations are executed using multiple threads, and their results are returned as lists rather than cursors.

Parameters:
    

  * **collection** â a `pymongo.collection.Collection` or `motor.motor_asyncio.AsyncIOMotorCollection`

  * **pipelines** â a MongoDB aggregation pipeline or a list of pipelines

  * **hints** (_None_) â a corresponding index hint or list of index hints for each pipeline

  * **maxTimeMS** (_None_) â max timeout for the request(s)



Returns:
    

  * If a single pipeline is provided, a `pymongo.command_cursor.CommandCursor` or `motor.motor_asyncio.AsyncIOMotorCommandCursor` is returned

  * If multiple pipelines are provided, each cursor is extracted into a list and the list of lists is returned




fiftyone.core.odm.get_db_config()#
    

Retrieves the database config.

Returns:
    

a `DatabaseConfigDocument`

fiftyone.core.odm.establish_db_conn(_config_)#
    

Establishes the database connection.

If `fiftyone.config.database_uri` is defined, then we connect to that URI. Otherwise, a [`fiftyone.core.service.DatabaseService`](api__fiftyone.core.service.md#fiftyone.core.service.DatabaseService "fiftyone.core.service.DatabaseService") is created.

Parameters:
    

**config** â a [`fiftyone.core.config.FiftyOneConfig`](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfig "fiftyone.core.config.FiftyOneConfig")

Raises:
    

  * **ConnectionError** â if a connection to `mongod` could not be established

  * [**FiftyOneConfigError**](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfigError "fiftyone.core.config.FiftyOneConfigError") â if `fiftyone.config.database_uri` is not defined and `mongod` could not be found

  * [**ServiceExecutableNotFound**](api__fiftyone.core.service.md#fiftyone.core.service.ServiceExecutableNotFound "fiftyone.core.service.ServiceExecutableNotFound") â if [`fiftyone.core.service.DatabaseService`](api__fiftyone.core.service.md#fiftyone.core.service.DatabaseService "fiftyone.core.service.DatabaseService") startup was attempted, but `mongod` was not found in `fiftyone.db.bin`

  * **RuntimeError** â if the `mongod` found does not meet FiftyOneâs requirements, or validation could not occur




fiftyone.core.odm.get_db_client()#
    

Returns a database client.

Returns:
    

a `pymongo.mongo_client.MongoClient`

fiftyone.core.odm.get_db_conn()#
    

Returns a connection to the database.

Returns:
    

a `pymongo.database.Database`

fiftyone.core.odm.get_db_version()#
    

Returns the database version.

Returns:
    

a `packaging.version.Version`

fiftyone.core.odm.get_async_db_client(_use_global =False_)#
    

Returns an async database client.

Parameters:
    

**use_global** â whether to use the global client singleton

Returns:
    

a `motor.motor_asyncio.AsyncIOMotorClient`

fiftyone.core.odm.get_async_db_conn(_use_global =False_)#
    

Returns an async connection to the database.

Returns:
    

a `motor.motor_asyncio.AsyncIOMotorDatabase`

fiftyone.core.odm.drop_database()#
    

Drops the database.

fiftyone.core.odm.sync_database()#
    

Syncs all pending database writes to disk.

fiftyone.core.odm.list_datasets()#
    

Returns the list of available FiftyOne datasets.

This is a low-level implementation of dataset listing that does not call [`fiftyone.core.dataset.list_datasets()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.list_datasets "fiftyone.core.dataset.list_datasets"), which is helpful if a database may be corrupted.

Returns:
    

a list of `Dataset` names

fiftyone.core.odm.load_dataset(_id =None_, _name =None_, _reload =False_)#
    

Loads the FiftyOne dataset with the given ID or name.

Parameters:
    

  * **id** (_None_) â the ID of the dataset

  * **name** (_None_) â the name of the dataset

  * **reload** (_False_) â whether to reload the dataset if necessary



Returns:
    

a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

fiftyone.core.odm.patch_saved_views(_dataset_name_ , _dry_run =False_)#
    

Ensures that the saved view documents in the `views` collection for the given dataset exactly match the IDs in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.patch_workspaces(_dataset_name_ , _dry_run =False_)#
    

Ensures that the workspace documents in the `workspaces` collection for the given dataset exactly match the IDs in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.patch_annotation_runs(_dataset_name_ , _dry_run =False_)#
    

Ensures that the annotation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.patch_brain_runs(_dataset_name_ , _dry_run =False_)#
    

Ensures that the brain method runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.patch_evaluations(_dataset_name_ , _dry_run =False_)#
    

Ensures that the evaluation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.patch_runs(_dataset_name_ , _dry_run =False_)#
    

Ensures that the runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_dataset(_name_ , _dry_run =False_)#
    

Deletes the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_saved_view(_dataset_name_ , _view_name_ , _dry_run =False_)#
    

Deletes the saved view with the given name from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_saved_view()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **view_name** â the name of the saved view

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_saved_views(_dataset_name_ , _dry_run =False_)#
    

Deletes all saved views from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_saved_view()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_workspace(_dataset_name_ , _workspace_name_ , _dry_run =False_)#
    

Deletes the workspace with the given name from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_workspace()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **workspace_name** â the name of the workspace

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_workspaces(_dataset_name_ , _dry_run =False_)#
    

Deletes all workspaces from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_workspace()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_evaluation(_name_ , _eval_key_ , _dry_run =False_)#
    

Deletes the evaluation run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_evaluation()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_evaluation "fiftyone.core.collections.SampleCollection.delete_evaluation"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **eval_key** â the evaluation key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_evaluations(_name_ , _dry_run =False_)#
    

Deletes all evaluations from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_evaluations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_evaluations "fiftyone.core.collections.SampleCollection.delete_evaluations"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_brain_run(_name_ , _brain_key_ , _dry_run =False_)#
    

Deletes the brain method run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **brain_key** â the brain key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_brain_runs(_name_ , _dry_run =False_)#
    

Deletes all brain method runs from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_brain_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_runs "fiftyone.core.collections.SampleCollection.delete_brain_runs"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_run(_name_ , _run_key_ , _dry_run =False_)#
    

Deletes the run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_run "fiftyone.core.collections.SampleCollection.delete_run"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **run_key** â the run key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.delete_runs(_name_ , _dry_run =False_)#
    

Deletes all runs from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_runs "fiftyone.core.collections.SampleCollection.delete_runs"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.drop_collection(_collection_name_)#
    

Drops specified collection from the database.

Parameters:
    

**collection_name** â the collection name

fiftyone.core.odm.drop_orphan_collections(_dry_run =False_)#
    

Drops all orphan collections from the database.

Orphan collections are collections that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.drop_orphan_saved_views(_dry_run =False_)#
    

Drops all orphan saved views from the database.

Orphan saved views are saved view documents that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.drop_orphan_generated_datasets(_dry_run =False_)#
    

Marks all orphan generated datasets as non-persistent so that they will
    

be deleted the next time non-persistent dataset cleanup runs.

Orphan generated datasets are datasets that were originally associated with a saved generated view that no longer exists.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.drop_orphan_workspaces(_dry_run =False_)#
    

Drops all orphan workspaces from the database.

Orphan workspaces are workspace documents that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.drop_orphan_runs(_dry_run =False_)#
    

Drops all orphan runs from the database.

Orphan runs are runs that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.drop_orphan_delegated_ops(_dry_run =False_)#
    

Drops all orphan delegated operations from the database.

Orphan delegated operations are those that are associated with a dataset that no longer exists in the database.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.drop_orphan_stores(_dry_run =False_)#
    

Drops all orphan execution stores from the database.

Orphan stores are those that are associated with a dataset that no longer exists in the database.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.list_collections()#
    

Returns a list of all collection names in the database.

Returns:
    

a list of all collection names

fiftyone.core.odm.get_collection_stats(_collection_name_)#
    

Sets stats about the collection.

Parameters:
    

**collection_name** â the name of the collection

Returns:
    

a stats dict

fiftyone.core.odm.get_indexed_values(_collection_ , _field_or_fields_ , _*_ , _index_key =None_, _query =None_, _values_only =False_, __stream =False_)#
    

Returns the values of the field(s) for all samples in the given collection that are covered by the index. Raises an error if the field is not indexed.

Parameters:
    

  * **collection** â a `pymongo.collection.Collection` or `motor.motor_asyncio.AsyncIOMotorCollection`

  * **field_or_fields** â the field name or list of field names to retrieve.

  * **index_key** (_None_) â the name of the index to use. If None, the default index name will be constructed from the field name(s).

  * **query** (_None_) â a dict selection filter to apply when querying. For performance, this should only include fields that are in the specified index.

  * **values_only** (_False_) â whether to remove field names from the resulting list. If True, the field names are removed and only the values will be returned as a list for each sample. If False, the field names are preserved and the values will be returned as a dict for each sample.



Returns:
    

a list of values for the specified field or index keys for each sample sorted in the same order as the index

Raises:
    

**ValueError** â if the field is not indexed

fiftyone.core.odm.stream_collection(_collection_name_)#
    

Streams the contents of the collection to stdout.

Parameters:
    

**collection_name** â the name of the collection

fiftyone.core.odm.count_documents(_coll_ , _pipeline_)#
    

fiftyone.core.odm.export_document(_doc_ , _json_path_)#
    

Exports the document to disk in JSON format.

Parameters:
    

  * **doc** â a BSON document dict

  * **json_path** â the path to write the JSON file




fiftyone.core.odm.export_collection(_docs_ , _json_dir_or_path_ , _key ='documents'_, _patt ='{idx:06d}-{id}.json'_, _num_docs =None_, _progress =None_)#
    

Exports the collection to disk in JSON format.

Parameters:
    

  * **docs** â an iterable containing the documents to export

  * **json_dir_or_path** â the path to write a single JSON file containing the entire collection, or a directory in which to write per-document JSON files

  * **key** (_"documents"_) â the field name under which to store the documents when `json_path` is a single JSON file

  * **(****"{idx** (_patt_) â 06d}-{id}.jsonâ): a filename pattern to use when `json_path` is a directory. The pattern may contain `idx` to refer to the index of the document in `docs` or `id` to refer to the documentâs ID

  * **num_docs** (_None_) â the total number of documents. If omitted, this must be computable via `len(docs)`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.odm.import_document(_json_path_)#
    

Imports a document from JSON on disk.

Parameters:
    

**json_path** â the path to the document

Returns:
    

a BSON document dict

fiftyone.core.odm.import_collection(_json_dir_or_path_ , _key ='documents'_)#
    

Imports the collection from JSON on disk.

Parameters:
    

  * **json_dir_or_path** â the path to a JSON file on disk, or a directory containing per-document JSON files

  * **key** (_"documents"_) â the field name under which the documents are stored when `json_path` is a single JSON file



Returns:
    

a tuple of

  * an iterable of BSON documents

  * the number of documents




fiftyone.core.odm.insert_documents(_docs_ , _coll_ , _ordered =False_, _batcher =None_, _progress =None_, _num_docs =None_)#
    

Inserts documents into a collection.

The `_id` field of the input documents will be populated if it is not already set.

Parameters:
    

  * **docs** â an iterable of BSON document dicts

  * **coll** â a pymongo collection

  * **ordered** (_False_) â whether the documents must be inserted in order

  * **batcher** (_None_) â an optional [`fiftyone.core.utils.Batcher`](api__fiftyone.core.utils.md#fiftyone.core.utils.Batcher "fiftyone.core.utils.Batcher") class to use to batch the documents, or `False` to strictly insert the documents in a single batch. By default, `fiftyone.config.default_batcher` is used

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **num_docs** (_None_) â the total number of documents. Only used when `progress=True`. If omitted, this will be computed via `len(docs)`, if possible



Returns:
    

a list of IDs of the inserted documents

fiftyone.core.odm.bulk_write(_ops_ , _coll_ , _ordered =False_, _batcher =None_, _progress =False_)#
    

Performs a batch of write operations on a collection.

Parameters:
    

  * **ops** â a list of pymongo operations

  * **coll** â a pymongo collection

  * **ordered** (_False_) â whether the operations must be performed in order

  * **batcher** (_None_) â an optional [`fiftyone.core.utils.Batcher`](api__fiftyone.core.utils.md#fiftyone.core.utils.Batcher "fiftyone.core.utils.Batcher") class to use to batch the operations, or `False` to strictly perform the operations in a single batch. By default, `fiftyone.config.default_batcher` is used

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

A list of [`pymongo.results.BulkWriteResult`](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.BulkWriteResult "\(in PyMongo v4.17.0\)") objects

class fiftyone.core.odm.ActiveFields(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Description of active fields in the App as defined by the sidebarâs checkboxes

Parameters:
    

  * **exclude** (_None_) â whether the paths are exclusionary

  * **paths** (_[__]_) â the list of `field` or `embedded.field.name` paths




**Attributes:**

`exclude` | A boolean field.  
---|---  
`paths` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
exclude#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




paths#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.SampleFieldDocument(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Description of a sample field.

**Attributes:**

`name` | A unicode string field.  
---|---  
`ftype` | A unicode string field.  
`embedded_doc_type` | A unicode string field.  
`subfield` | A unicode string field.  
`fields` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`db_field` | A unicode string field.  
`description` | A unicode string field.  
`info` | A dictionary field that wraps a standard Python dictionary.  
`read_only` | A boolean field.  
`created_at` | A datetime field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`to_field`() | Creates the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") specified by this document.  
---|---  
`from_field`(field) | Creates a `SampleFieldDocument` for a field.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




ftype#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




embedded_doc_type#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




subfield#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




fields#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




db_field#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




description#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




info#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




read_only#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_field()#
    

Creates the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") specified by this document.

Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

classmethod from_field(_field_)#
    

Creates a `SampleFieldDocument` for a field.

Parameters:
    

**field** â a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instance

Returns:
    

a `SampleFieldDocument`

STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.ColorScheme(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Description of a color scheme in the App.

Example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Store a custom color scheme for a dataset
    dataset.app_config.color_scheme = fo.ColorScheme(
        color_by="value",
        color_pool=[
            "#ff0000",
            "#00ff00",
            "#0000ff",
            "pink",
            "yellowgreen",
        ],
        fields=[
            {
                "path": "ground_truth",
                "fieldColor": "#ff00ff",
                "colorByAttribute": "label",
                "valueColors": [{"value": "dog", "color": "yellow"}],
                "maskTargetsColors": [
                    {"intTarget": 2, "color": "#ff0000"},
                    {"intTarget": 12, "color": "#99ff00"},
                ],
            }
        ],
        label_tags={
            "fieldColor": "#00ffff",
            "valueColors": [
                {"value": "correct", "color": "#ff00ff"},
                {"value": "mistake", "color": "#00ff00"},
            ],
        },
        colorscales=[
            {
                "path": "heatmap1",
                "list": [
                    {"value": 0, "color": "rgb(0, 0, 255)"},
                    {"value": 1, "color": "rgb(0, 255, 255)"},
                ],
            },
            {
                "path": "heatmap2",
                "name": "hsv",
            },
        ],
        multicolor_keypoints=False,
        opacity=0.5,
        show_skeletons=True,
        default_mask_targets_colors=[
            {"intTarget": 1, "color": "#FEC0AA"},
            {"intTarget": 2, "color": "#EC4E20"},
        ],
        default_colorscale={"name": "sunset", "list": None},
    )
    
    session = fo.launch_app(dataset)
    

Parameters:
    

  * **color_by** (_None_) â whether annotations should be colored by `"field"`, `"value"`, or `"instance"`

  * **color_pool** (_None_) â an optional list of colors to use as a color pool for this dataset

  * **multicolor_keypoints** (_None_) â whether to use multiple colors for keypoints

  * **opacity** (_None_) â transparency of the annotation, between 0 and 1

  * **show_skeletons** (_None_) â whether to show skeletons of keypoints

  * **fields** (_None_) â 

an optional list of dicts of per-field custom colors with the following keys:

    * `path` (required): the fully-qualified path to the field youâre customizing

    * `fieldColor` (optional): a color to assign to the field in the App sidebar

    * `colorByAttribute` (optional): the attribute to use to assign per-value colors. Only applicable when the field is an embedded document

    * `valueColors` (optional): a list of dicts specifying colors to use for individual values of this field

    * `maskTargetsColors` (optional): a list of dicts specifying index and color for 2D masks in the same format as described below for default mask targets

  * **default_mask_targets_colors** (_None_) â 

a list of dicts with the following keys specifying index and color for 2D masks of the dataset. If a field does not have field specific mask targets colors, this list will be used:

    * `intTarget`: an integer target value

    * `color`: a color string

Note that the pixel value `0` is a reserved âbackgroundâ class that is always rendered as invisible in the App

  * **default_colorscale** (_None_) â 

dataset default colorscale dict with the following keys:

    * `name` (optional): a named plotly colorscale, e.g. `"hsv"`. See <https://plotly.com/python/builtin-colorscales>

    * `list` (optional): a list of dicts of colorscale values

      * `value`: a float number between 0 and 1. A valid list must have colors defined for 0 and 1

      * `color`: an RGB color string

  * **colorscales** (_None_) â 

an optional list of dicts of per-field custom colorscales with the following keys:

    * `path` (required): the fully-qualified path to the field youâre customizing. use âdatasetâ if you are setting the default colorscale for dataset

    * `name` (optional): a named colorscale plotly recognizes

    * `list` (optional): a list of dicts of colorscale values with the following keys:

      * `value`: a float number between 0 and 1. A valid list must have colors defined for 0 and 1

      * `color`: an RGB color string

  * **label_tags** (_None_) â 

an optional dict specifying custom colors for label tags with the following keys:

    * `fieldColor` (optional): a color to assign to all label tags

    * `valueColors` (optional): a list of dicts




**Attributes:**

`id` | An Object ID field.  
---|---  
`color_pool` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`color_by` | A unicode string field.  
`fields` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`label_tags` | A dictionary field that wraps a standard Python dictionary.  
`multicolor_keypoints` | A boolean field.  
`opacity` | A floating point number field.  
`show_skeletons` | A boolean field.  
`default_mask_targets_colors` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`colorscales` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`default_colorscale` | A dictionary field that wraps a standard Python dictionary.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




color_pool#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




color_by#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




fields#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




label_tags#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




multicolor_keypoints#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




opacity#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




show_skeletons#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




default_mask_targets_colors#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




colorscales#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




default_colorscale#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.KeypointSkeleton(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Description of a keypoint skeleton.

Keypoint skeletons can be associated with [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") fields whose [`points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points") attributes all contain a fixed number of semantically ordered points.

The `edges` argument contains lists of integer indexes that define the connectivity of the points in the skeleton, and the optional `labels` argument defines the label strings for each node in the skeleton.

For example, the skeleton below is defined by edges between the following nodes:
    
    
    left hand <-> left shoulder <-> right shoulder <-> right hand
    left eye <-> right eye <-> mouth
    

Example:
    
    
    import fiftyone as fo
    
    # A skeleton for an object made of 7 points
    skeleton = fo.KeypointSkeleton(
        labels=[
            "left hand" "left shoulder", "right shoulder", "right hand",
            "left eye", "right eye", "mouth",
        ],
        edges=[[0, 1, 2, 3], [4, 5, 6]],
    )
    

Parameters:
    

  * **labels** (_None_) â an optional list of label strings for each node

  * **edges** â a list of lists of integer indexes defining the connectivity between nodes




**Attributes:**

`labels` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`edges` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
labels#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




edges#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.DatasetAppConfig(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Dataset-specific settings that customize how a dataset is visualized in the App.

Parameters:
    

  * **active_fields** (_None_) â an optional `ActiveFields` dataset default

  * **color_scheme** (_None_) â an optional `ColorScheme` dataset default

  * **disable_frame_filtering** (_False_) â whether to disable frame filtering for video datasets in the Appâs grid view

  * **dynamic_groups_target_frame_rate** (_30_) â the target frame rate when rendering ordered dynamic groups of images as videos

  * **grid_media_field** (_"filepath"_) â the default sample field from which to serve media in the Appâs grid view

  * **media_fallback** (_False_) â whether to fall back to the default media field (`"filepath"`) when the alternate media field value for a sample is not defined

  * **media_fields** (_[__"filepath"__]_) â the list of sample fields that contain media and should be available to choose from the Appâs settings menus

  * **modal_media_field** (_"filepath"_) â the default sample field from which to serve media in the Appâs modal view

  * **plugins** (_{}_) â 

an optional dict mapping plugin names to plugin configuration dicts. Builtin plugins include:

    * `"map"`: See the [map plugin docs](user_guide__app.md#app-map-panel) for supported options

    * `"point-cloud"`: See the [3D visualizer docs](user_guide__app.md#app-3d-visualizer-config) for supported options

  * **sidebar_groups** (_None_) â an optional list of `SidebarGroupDocument` describing sidebar groups to use in the App




**Attributes:**

`active_fields` | A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.  
---|---  
`color_scheme` | A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.  
`disable_frame_filtering` | A boolean field.  
`dynamic_groups_target_frame_rate` | A 32 bit integer field.  
`grid_media_field` | A unicode string field.  
`media_fallback` | A boolean field.  
`media_fields` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`modal_media_field` | A unicode string field.  
`plugins` | A dictionary field that wraps a standard Python dictionary.  
`sidebar_groups` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`default_active_fields`(sample_collection) | Generates the default `active_fields` for the given collection.  
---|---  
`default_sidebar_groups`(sample_collection) | Generates the default `sidebar_groups` for the given collection.  
`is_custom`() | Determines whether this app config differs from the default one.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
active_fields#
    

A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




color_scheme#
    

A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




disable_frame_filtering#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




dynamic_groups_target_frame_rate#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




grid_media_field#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




media_fallback#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




media_fields#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




modal_media_field#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




plugins#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




sidebar_groups#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




static default_active_fields(_sample_collection_)#
    

Generates the default `active_fields` for the given collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    active_fields = fo.DatasetAppConfig.default_active_fields(dataset)
    dataset.app_config.active_fields = active_fields
    print(dataset.app_config)
    

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Returns:
    

an `ActiveFields` instance

static default_sidebar_groups(_sample_collection_)#
    

Generates the default `sidebar_groups` for the given collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    sidebar_groups = fo.DatasetAppConfig.default_sidebar_groups(dataset)
    dataset.app_config.sidebar_groups = sidebar_groups
    print(dataset.app_config)
    

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Returns:
    

a list of `SidebarGroupDocument` instances

is_custom()#
    

Determines whether this app config differs from the default one.

Returns:
    

True/False

STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.DatasetDocument(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Backing document for datasets.

**Attributes:**

`name` | A unicode string field.  
---|---  
`slug` | A unicode string field.  
`version` | A unicode string field.  
`created_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`last_deletion_at` | A datetime field.  
`last_loaded_at` | A datetime field.  
`sample_collection_name` | A unicode string field.  
`frame_collection_name` | A unicode string field.  
`persistent` | A boolean field.  
`media_type` | A unicode string field.  
`group_field` | A unicode string field.  
`group_media_types` | A dictionary field that wraps a standard Python dictionary.  
`default_group_slice` | A unicode string field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`description` | A unicode string field.  
`info` | A dictionary field that wraps a standard Python dictionary.  
`app_config` | A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.  
`classes` | A dictionary field that wraps a standard Python dictionary.  
`default_classes` | A `ListField` that stores class label strings.  
`mask_targets` | A dictionary field that wraps a standard Python dictionary.  
`default_mask_targets` | A `DictField` that stores mapping between integer keys or RGB string hex keys and string targets.  
`skeletons` | A dictionary field that wraps a standard Python dictionary.  
`default_skeleton` | A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.  
`camera_intrinsics` | A dictionary field that wraps a standard Python dictionary.  
`static_transforms` | A dictionary field that wraps a standard Python dictionary.  
`sample_fields` | A field that stores a list of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` objects.  
`frame_fields` | A field that stores a list of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` objects.  
`saved_views` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`workspaces` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`annotation_runs` | A dictionary field that wraps a standard Python dictionary.  
`brain_methods` | A dictionary field that wraps a standard Python dictionary.  
`evaluations` | A dictionary field that wraps a standard Python dictionary.  
`runs` | A dictionary field that wraps a standard Python dictionary.  
`active_label_schemas` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`label_schemas` | A dictionary field that wraps a standard Python dictionary.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Methods:**

`get_saved_views`() |   
---|---  
`get_workspaces`() |   
`get_annotation_runs`() |   
`get_brain_methods`() |   
`get_evaluations`() |   
`get_runs`() |   
`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`(*args[,Â no_dereference]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Classes:**

`my_metaclass` |   
---|---  
  
name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




slug#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




version#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_deletion_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_loaded_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




sample_collection_name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




frame_collection_name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




persistent#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




media_type#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




group_field#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




group_media_types#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




default_group_slice#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




description#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




info#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




app_config#
    

A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




classes#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




default_classes#
    

A `ListField` that stores class label strings.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




mask_targets#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




default_mask_targets#
    

A `DictField` that stores mapping between integer keys or RGB string hex keys and string targets.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




skeletons#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




default_skeleton#
    

A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




camera_intrinsics#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




static_transforms#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




sample_fields#
    

A field that stores a list of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` objects.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




frame_fields#
    

A field that stores a list of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` objects.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




saved_views#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




workspaces#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




annotation_runs#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




brain_methods#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




evaluations#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




runs#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




active_label_schemas#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




label_schemas#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




get_saved_views()#
    

get_workspaces()#
    

get_annotation_runs()#
    

get_brain_methods()#
    

get_evaluations()#
    

get_runs()#
    

exception DoesNotExist#
    

Bases: `DoesNotExist`

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

exception MultipleObjectsReturned#
    

Bases: `MultipleObjectsReturned`

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

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

A field wrapper around MongoDBâs ObjectIds.

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_* args_, _no_dereference =False_, _** kwargs_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.SidebarGroupDocument(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Description of a sidebar group in the App.

Parameters:
    

  * **name** â the name of the sidebar group

  * **paths** (_[__]_) â the list of `field` or `embedded.field.name` paths in the group

  * **expanded** (_None_) â whether this group should be expanded by default




**Attributes:**

`name` | A unicode string field.  
---|---  
`paths` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`expanded` | A boolean field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




paths#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




expanded#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.Document(_** kwargs_)#
    

Bases: [`BaseDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.BaseDocument "fiftyone.core.odm.document.BaseDocument"), `Document`

Base class for documents that are stored in a MongoDB collection.

The ID of a document is automatically populated when it is added to the database, and the ID of a document is `None` if it has not been added to the database.

id#
    

the ID of the document, or `None` if it has not been added to the database

**Methods:**

`copy`([new_id]) | Returns a deep copy of the document.  
---|---  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`copy_with_new_id`() |   
`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Attributes:**

`STRICT` |   
---|---  
`field_names` | An ordered tuple of the public fields of this document.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

copy_with_new_id()#
    

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.SerializableDocument#
    

Bases: `object`

Mixin for documents that can be serialized in BSON or JSON format.

**Attributes:**

`field_names` | An ordered tuple of the public fields of this document.  
---|---  
  
**Methods:**

`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
---|---  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`get_field`(field_name) | Gets the field of the document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`clear_field`(field_name) | Clears the field from the document.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`copy`() | Returns a deep copy of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`from_json`(s) | Loads the document from a JSON string.  
  
property field_names#
    

An ordered tuple of the public fields of this document.

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

class fiftyone.core.odm.BaseEmbeddedDocument#
    

Bases: [`MongoEngineBaseDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument "fiftyone.core.odm.document.MongoEngineBaseDocument")

Base class for documents that are embedded within other documents and therefore are not stored in their own collection in the database.

**Methods:**

`clear_field`(field_name) | Clears the field from the document.  
---|---  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
  
**Attributes:**

`field_names` | An ordered tuple of the public fields of this document.  
---|---  
  
clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

class fiftyone.core.odm.DynamicEmbeddedDocument(_* args_, _** kwargs_)#
    

Bases: [`DynamicMixin`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.DynamicMixin "fiftyone.core.odm.document.DynamicMixin"), [`BaseEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument "fiftyone.core.odm.embedded_document.BaseEmbeddedDocument"), `DynamicEmbeddedDocument`

Base class for dynamic documents that are embedded within other documents and therefore arenât stored in their own collection in the database.

Dynamic documents can have arbitrary fields added to them.

**Attributes:**

`STRICT` |   
---|---  
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

exception fiftyone.core.odm.DynamicEmbeddedDocumentException#
    

Bases: `Exception`

Exception raised when an error occurs in a dynamic document operation.

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

class fiftyone.core.odm.EmbeddedDocument(_* args_, _** kwargs_)#
    

Bases: [`BaseEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.BaseEmbeddedDocument "fiftyone.core.odm.embedded_document.BaseEmbeddedDocument"), `EmbeddedDocument`

Base class for documents that are embedded within other documents and therefore are not stored in their own collection in the database.

**Attributes:**

`STRICT` |   
---|---  
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.DatasetFrameDocument(_** kwargs_)#
    

Bases: [`DatasetMixin`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin "fiftyone.core.odm.mixins.DatasetMixin"), [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

**Attributes:**

`id` | An Object ID field.  
---|---  
`frame_number` | A video frame number field.  
`created_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`STRICT` |   
`collection_name` |   
`field_names` | An ordered tuple of the public fields of this document.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Methods:**

`add_field`(path,Â ftype[,Â embedded_doc_type,Â ...]) | Adds a new field or embedded field to the document, if necessary.  
---|---  
`add_implied_field`(path,Â value[,Â ...]) | Adds the field or embedded field to the document, if necessary, inferring the field type from the provided value.  
`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_field_schema`([ftype,Â embedded_doc_type,Â ...]) | Returns a schema dictionary describing the fields of this document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`merge_field_schema`(schema[,Â expand_schema,Â ...]) | Merges the field schema into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




frame_number#
    

A video frame number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

classmethod add_field(_path_ , _ftype_ , _embedded_doc_type =None_, _subfield =None_, _fields =None_, _description =None_, _info =None_, _read_only =False_, _expand_schema =True_, _recursive =True_, _validate =True_, _** kwargs_)#
    

Adds a new field or embedded field to the document, if necessary.

Parameters:
    

  * **path** â the field name or `embedded.field.name`

  * **ftype** â the field type to create. Must be a subclass of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â the `fiftyone.core.odm.BaseEmbeddedDocument` type of the field. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **subfield** (_None_) â the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") type of the contained field. Only applicable when `ftype` is [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") or [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")

  * **fields** (_None_) â a list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances defining embedded document attributes. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field should be read-only

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that the field already exists with a consistent type (False)

  * **recursive** (_True_) â whether to recursively add embedded document fields

  * **validate** (_True_) â whether to validate the field against an existing field at the same path



Returns:
    

True/False whether one or more fields or embedded fields were added to the document or its children

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name

classmethod add_implied_field(_path_ , _value_ , _expand_schema =True_, _dynamic =False_, _recursive =True_, _validate =True_)#
    

Adds the field or embedded field to the document, if necessary, inferring the field type from the provided value.

Parameters:
    

  * **path** â the field name or `embedded.field.name`

  * **value** â the field value

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that the field already exists with a consistent type (False)

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields

  * **recursive** (_True_) â whether to recursively add embedded document fields

  * **validate** (_True_) â whether to validate the field against an existing field at the same path



Returns:
    

True/False whether one or more fields or embedded fields were added to the document or its children

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

property collection_name#
    

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

classmethod get_field_schema(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Returns a schema dictionary describing the fields of this document.

If the document belongs to a dataset, the schema will apply to all documents in the collection.

Parameters:
    

  * **ftype** (_None_) â an optional field type or iterable of field types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of `fiftyone.core.odm.BaseEmbeddedDocument`

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

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




classmethod merge_field_schema(_schema_ , _expand_schema =True_, _recursive =True_, _validate =True_, _overwrite =False_)#
    

Merges the field schema into this document.

Parameters:
    

  * **schema** â a dict mapping field names or `embedded.field.names` to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that fields already exist with consistent types (False)

  * **recursive** (_True_) â whether to recursively merge embedded document fields

  * **validate** (_True_) â whether to validate fields against existing fields at the same path

  * **overwrite** (_False_) â whether to overwrite the editable metadata of existing fields



Returns:
    

True/False whether any new fields were added

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name or a new field is found but `expand_schema == False`

modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_, __enforce_read_only =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.NoDatasetFrameDocument(_** kwargs_)#
    

Bases: [`NoDatasetMixin`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin "fiftyone.core.odm.mixins.NoDatasetMixin"), [`SerializableDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument "fiftyone.core.odm.document.SerializableDocument")

**Attributes:**

`default_fields` |   
---|---  
`default_fields_ordered` |   
`field_names` | An ordered tuple of the public fields of this document.  
`in_db` |   
  
**Methods:**

`clear_field`(field_name) | Clears the field from the document.  
---|---  
`copy`() | Returns a deep copy of the document.  
`delete`() |   
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`reload`() |   
`save`() |   
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
  
default_fields = {'_dataset_id': <fiftyone.core.fields.ObjectIdField object>, '_sample_id': <fiftyone.core.fields.ObjectIdField object>, 'created_at': <fiftyone.core.fields.DateTimeField object>, 'frame_number': <fiftyone.core.fields.FrameNumberField object>, 'id': <fiftyone.core.fields.ObjectIdField object>, 'last_modified_at': <fiftyone.core.fields.DateTimeField object>}#
    

default_fields_ordered = ('id', 'frame_number', 'created_at', 'last_modified_at', '_sample_id', '_dataset_id')#
    

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

delete()#
    

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_db#
    

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




reload()#
    

save()#
    

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

fiftyone.core.odm.get_default_fields(_cls_ , _include_private =False_, _use_db_fields =False_)#
    

Gets the default fields present on all instances of the given `DatasetMixin` class.

Parameters:
    

  * **cls** â the `DatasetMixin` class

  * **include_private** (_False_) â whether to include fields starting with `_`

  * **use_db_fields** (_False_) â whether to return database fields rather than user-facing fields, when applicable



Returns:
    

a tuple of field names

class fiftyone.core.odm.OntologyDocument(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Backing document for ontologies.

Ontologies are global resources not scoped to any single dataset. Multiple datasets can reference the same ontology by name. Each save creates a new versioned document; `(slug, version)` is unique, so names differing only in case or punctuation collide on save.

`schema_version` records the internal layout version of the row at write time. Bump `CURRENT_SCHEMA_VERSION` and add a migration when changing the persisted structure (especially `root`).

**Attributes:**

`name` | A unicode string field.  
---|---  
`slug` | A unicode string field.  
`version` | A 32 bit integer field.  
`schema_version` | A 32 bit integer field.  
`type` | A unicode string field.  
`description` | A unicode string field.  
`root` | A dictionary field that wraps a standard Python dictionary.  
`created_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Methods:**

`save`(*args,Â **kwargs) | Saves the document to the database.  
---|---  
`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Classes:**

`my_metaclass` |   
---|---  
  
name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




slug#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




version#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




schema_version#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




type#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




description#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




root#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




save(_* args: Any_, _** kwargs: Any_) → [OntologyDocument](api__fiftyone.core.odm.ontology.md#fiftyone.core.odm.ontology.OntologyDocument "fiftyone.core.odm.ontology.OntologyDocument")#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

exception DoesNotExist#
    

Bases: `DoesNotExist`

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

exception MultipleObjectsReturned#
    

Bases: `MultipleObjectsReturned`

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

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

A field wrapper around MongoDBâs ObjectIds.

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.OntologyType(_value_)#
    

Bases: `str`, `Enum`

Allowed values for `OntologyDocument.type` in storage and APIs.

`TAXONOMY` â a reusable hierarchical class tree. Multiple annotation ontologies can reference the same taxonomy by name.

`ANNOTATION_ONTOLOGY` â a container that defines classes, attributes (with optional conditional display logic), and references to taxonomies. This is the document that gets connected to a label schema on a field.

**Attributes:**

`TAXONOMY` |   
---|---  
`ANNOTATION_ONTOLOGY` |   
  
**Methods:**

`encode`([encoding,Â errors]) | Encode the string using the codec registered for encoding.  
---|---  
`replace`(old,Â new[,Â count]) | Return a copy with all occurrences of substring old replaced by new.  
`split`([sep,Â maxsplit]) | Return a list of the substrings in the string, using sep as the separator string.  
`rsplit`([sep,Â maxsplit]) | Return a list of the substrings in the string, using sep as the separator string.  
`join`(iterable,Â /) | Concatenate any number of strings.  
`capitalize`() | Return a capitalized version of the string.  
`casefold`() | Return a version of the string suitable for caseless comparisons.  
`title`() | Return a version of the string where each word is titlecased.  
`center`(width[,Â fillchar]) | Return a centered string of length width.  
`count`(sub[,Â start[,Â end]]) | Return the number of non-overlapping occurrences of substring sub in string S[start:end].  
`expandtabs`([tabsize]) | Return a copy where all tab characters are expanded using spaces.  
`find`(sub[,Â start[,Â end]]) | Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
`partition`(sep,Â /) | Partition the string into three parts using the given separator.  
`index`(sub[,Â start[,Â end]]) | Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
`ljust`(width[,Â fillchar]) | Return a left-justified string of length width.  
`lower`() | Return a copy of the string converted to lowercase.  
`lstrip`([chars]) | Return a copy of the string with leading whitespace removed.  
`rfind`(sub[,Â start[,Â end]]) | Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  
`rindex`(sub[,Â start[,Â end]]) | Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  
`rjust`(width[,Â fillchar]) | Return a right-justified string of length width.  
`rstrip`([chars]) | Return a copy of the string with trailing whitespace removed.  
`rpartition`(sep,Â /) | Partition the string into three parts using the given separator.  
`splitlines`([keepends]) | Return a list of the lines in the string, breaking at line boundaries.  
`strip`([chars]) | Return a copy of the string with leading and trailing whitespace removed.  
`swapcase`() | Convert uppercase characters to lowercase and lowercase characters to uppercase.  
`translate`(table,Â /) | Replace each character in the string using the given translation table.  
`upper`() | Return a copy of the string converted to uppercase.  
`startswith`(prefix[,Â start[,Â end]]) | Return True if S starts with the specified prefix, False otherwise.  
`endswith`(suffix[,Â start[,Â end]]) | Return True if S ends with the specified suffix, False otherwise.  
`removeprefix`(prefix,Â /) | Return a str with the given prefix string removed if present.  
`removesuffix`(suffix,Â /) | Return a str with the given suffix string removed if present.  
`isascii`() | Return True if all characters in the string are ASCII, False otherwise.  
`islower`() | Return True if the string is a lowercase string, False otherwise.  
`isupper`() | Return True if the string is an uppercase string, False otherwise.  
`istitle`() | Return True if the string is a title-cased string, False otherwise.  
`isspace`() | Return True if the string is a whitespace string, False otherwise.  
`isdecimal`() | Return True if the string is a decimal string, False otherwise.  
`isdigit`() | Return True if the string is a digit string, False otherwise.  
`isnumeric`() | Return True if the string is a numeric string, False otherwise.  
`isalpha`() | Return True if the string is an alphabetic string, False otherwise.  
`isalnum`() | Return True if the string is an alpha-numeric string, False otherwise.  
`isidentifier`() | Return True if the string is a valid Python identifier, False otherwise.  
`isprintable`() | Return True if the string is printable, False otherwise.  
`zfill`(width,Â /) | Pad a numeric string with zeros on the left, to fill a field of the given width.  
`format`(*args,Â **kwargs) | Return a formatted version of S, using substitutions from args and kwargs.  
`format_map`(mapping) | Return a formatted version of S, using substitutions from mapping.  
`maketrans` | Return a translation table usable for str.translate().  
  
TAXONOMY = 'taxonomy'#
    

ANNOTATION_ONTOLOGY = 'annotation_ontology'#
    

encode(_encoding ='utf-8'_, _errors ='strict'_)#
    

Encode the string using the codec registered for encoding.

encoding
    

The encoding in which to encode the string.

errors
    

The error handling scheme to use for encoding errors. The default is âstrictâ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are âignoreâ, âreplaceâ and âxmlcharrefreplaceâ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

replace(_old_ , _new_ , _count =-1_, _/_)#
    

Return a copy with all occurrences of substring old replaced by new.

> count
>     
> 
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

split(_sep =None_, _maxsplit =-1_)#
    

Return a list of the substrings in the string, using sep as the separator string.

> sep
>     
> 
> The separator used to split the string.
> 
> When set to None (the default value), will split on any whitespace character (including n r t f and spaces) and will discard empty strings from the result.
> 
> maxsplit
>     
> 
> Maximum number of splits. -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

rsplit(_sep =None_, _maxsplit =-1_)#
    

Return a list of the substrings in the string, using sep as the separator string.

> sep
>     
> 
> The separator used to split the string.
> 
> When set to None (the default value), will split on any whitespace character (including n r t f and spaces) and will discard empty strings from the result.
> 
> maxsplit
>     
> 
> Maximum number of splits. -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

join(_iterable_ , _/_)#
    

Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: â.â.join([âabâ, âpqâ, ârsâ]) -> âab.pq.rsâ

capitalize()#
    

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()#
    

Return a version of the string suitable for caseless comparisons.

title()#
    

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

center(_width_ , _fillchar =' '_, _/_)#
    

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(_sub_[, _start_[, _end_]]) → int#
    

Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

expandtabs(_tabsize =8_)#
    

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(_sub_[, _start_[, _end_]]) → int#
    

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

partition(_sep_ , _/_)#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

index(_sub_[, _start_[, _end_]]) → int#
    

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

ljust(_width_ , _fillchar =' '_, _/_)#
    

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#
    

Return a copy of the string converted to lowercase.

lstrip(_chars =None_, _/_)#
    

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

rfind(_sub_[, _start_[, _end_]]) → int#
    

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(_sub_[, _start_[, _end_]]) → int#
    

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(_width_ , _fillchar =' '_, _/_)#
    

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rstrip(_chars =None_, _/_)#
    

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

rpartition(_sep_ , _/_)#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

splitlines(_keepends =False_)#
    

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

strip(_chars =None_, _/_)#
    

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#
    

Convert uppercase characters to lowercase and lowercase characters to uppercase.

translate(_table_ , _/_)#
    

Replace each character in the string using the given translation table.

> table
>     
> 
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()#
    

Return a copy of the string converted to uppercase.

startswith(_prefix_[, _start_[, _end_]]) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

endswith(_suffix_[, _start_[, _end_]]) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

removeprefix(_prefix_ , _/_)#
    

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

removesuffix(_suffix_ , _/_)#
    

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

isascii()#
    

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

islower()#
    

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isupper()#
    

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

istitle()#
    

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isspace()#
    

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

isdecimal()#
    

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()#
    

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isnumeric()#
    

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isalpha()#
    

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isalnum()#
    

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isidentifier()#
    

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as âdefâ or âclassâ.

isprintable()#
    

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

zfill(_width_ , _/_)#
    

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

format(_* args_, _** kwargs_) → str#
    

Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (â{â and â}â).

format_map(_mapping_) → str#
    

Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (â{â and â}â).

static maketrans()#
    

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

class fiftyone.core.odm.RunDocument(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Backing document for dataset runs.

**Attributes:**

`dataset_id` | An Object ID field.  
---|---  
`key` | A unicode string field.  
`version` | A unicode string field.  
`timestamp` | A datetime field.  
`config` | A dictionary field that wraps a standard Python dictionary.  
`view_stages` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`results` | A GridFS storage field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Methods:**

`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
---|---  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
dataset_id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




key#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




version#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




timestamp#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




config#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




view_stages#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




results#
    

A GridFS storage field.

exception DoesNotExist#
    

Bases: `DoesNotExist`

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

exception MultipleObjectsReturned#
    

Bases: `MultipleObjectsReturned`

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

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

A field wrapper around MongoDBâs ObjectIds.

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.DatasetSampleDocument(_** kwargs_)#
    

Bases: [`DatasetMixin`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.DatasetMixin "fiftyone.core.odm.mixins.DatasetMixin"), [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Base class for sample documents backing samples in datasets.

All `fiftyone.core.dataset.Dataset._sample_doc_cls` classes inherit from this class.

**Attributes:**

`id` | An Object ID field.  
---|---  
`filepath` | A unicode string field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`metadata` | A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.  
`created_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`media_type` |   
`STRICT` |   
`collection_name` |   
`field_names` | An ordered tuple of the public fields of this document.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Methods:**

`add_field`(path,Â ftype[,Â embedded_doc_type,Â ...]) | Adds a new field or embedded field to the document, if necessary.  
---|---  
`add_implied_field`(path,Â value[,Â ...]) | Adds the field or embedded field to the document, if necessary, inferring the field type from the provided value.  
`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_field_schema`([ftype,Â embedded_doc_type,Â ...]) | Returns a schema dictionary describing the fields of this document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`merge_field_schema`(schema[,Â expand_schema,Â ...]) | Merges the field schema into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




filepath#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




metadata#
    

A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property media_type#
    

STRICT = False#
    

classmethod add_field(_path_ , _ftype_ , _embedded_doc_type =None_, _subfield =None_, _fields =None_, _description =None_, _info =None_, _read_only =False_, _expand_schema =True_, _recursive =True_, _validate =True_, _** kwargs_)#
    

Adds a new field or embedded field to the document, if necessary.

Parameters:
    

  * **path** â the field name or `embedded.field.name`

  * **ftype** â the field type to create. Must be a subclass of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â the `fiftyone.core.odm.BaseEmbeddedDocument` type of the field. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **subfield** (_None_) â the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") type of the contained field. Only applicable when `ftype` is [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") or [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")

  * **fields** (_None_) â a list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances defining embedded document attributes. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field should be read-only

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that the field already exists with a consistent type (False)

  * **recursive** (_True_) â whether to recursively add embedded document fields

  * **validate** (_True_) â whether to validate the field against an existing field at the same path



Returns:
    

True/False whether one or more fields or embedded fields were added to the document or its children

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name

classmethod add_implied_field(_path_ , _value_ , _expand_schema =True_, _dynamic =False_, _recursive =True_, _validate =True_)#
    

Adds the field or embedded field to the document, if necessary, inferring the field type from the provided value.

Parameters:
    

  * **path** â the field name or `embedded.field.name`

  * **value** â the field value

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that the field already exists with a consistent type (False)

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields

  * **recursive** (_True_) â whether to recursively add embedded document fields

  * **validate** (_True_) â whether to validate the field against an existing field at the same path



Returns:
    

True/False whether one or more fields or embedded fields were added to the document or its children

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

property collection_name#
    

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

classmethod get_field_schema(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Returns a schema dictionary describing the fields of this document.

If the document belongs to a dataset, the schema will apply to all documents in the collection.

Parameters:
    

  * **ftype** (_None_) â an optional field type or iterable of field types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of `fiftyone.core.odm.BaseEmbeddedDocument`

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

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




classmethod merge_field_schema(_schema_ , _expand_schema =True_, _recursive =True_, _validate =True_, _overwrite =False_)#
    

Merges the field schema into this document.

Parameters:
    

  * **schema** â a dict mapping field names or `embedded.field.names` to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that fields already exist with consistent types (False)

  * **recursive** (_True_) â whether to recursively merge embedded document fields

  * **validate** (_True_) â whether to validate fields against existing fields at the same path

  * **overwrite** (_False_) â whether to overwrite the editable metadata of existing fields



Returns:
    

True/False whether any new fields were added

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name or a new field is found but `expand_schema == False`

modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_, __enforce_read_only =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.NoDatasetSampleDocument(_** kwargs_)#
    

Bases: [`NoDatasetMixin`](api__fiftyone.core.odm.mixins.md#fiftyone.core.odm.mixins.NoDatasetMixin "fiftyone.core.odm.mixins.NoDatasetMixin"), [`SerializableDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument "fiftyone.core.odm.document.SerializableDocument")

Backing document for samples that have not been added to a dataset.

**Attributes:**

`default_fields` |   
---|---  
`default_fields_ordered` |   
`media_type` |   
`field_names` | An ordered tuple of the public fields of this document.  
`in_db` |   
  
**Methods:**

`clear_field`(field_name) | Clears the field from the document.  
---|---  
`copy`() | Returns a deep copy of the document.  
`delete`() |   
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`reload`() |   
`save`() |   
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
  
default_fields = {'_dataset_id': <fiftyone.core.fields.ObjectIdField object>, '_media_type': <fiftyone.core.fields.StringField object>, '_rand': <fiftyone.core.fields.FloatField object>, 'created_at': <fiftyone.core.fields.DateTimeField object>, 'filepath': <fiftyone.core.fields.StringField object>, 'id': <fiftyone.core.fields.ObjectIdField object>, 'last_modified_at': <fiftyone.core.fields.DateTimeField object>, 'metadata': <fiftyone.core.fields.EmbeddedDocumentField object>, 'tags': <fiftyone.core.fields.ListField object>}#
    

default_fields_ordered = ('id', 'filepath', 'tags', 'metadata', 'created_at', 'last_modified_at', '_media_type', '_rand', '_dataset_id')#
    

property media_type#
    

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

delete()#
    

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_db#
    

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




reload()#
    

save()#
    

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

fiftyone.core.odm.serialize_value(_value_ , _extended =False_)#
    

Serializes the given value.

Parameters:
    

  * **value** â the value

  * **extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format



Returns:
    

the serialized value

fiftyone.core.odm.deserialize_value(_value_)#
    

Deserializes the given value.

Parameters:
    

**value** â the serialized value

Returns:
    

the value

fiftyone.core.odm.validate_field_name(_field_name_ , _media_type =None_, _is_frame_field =False_)#
    

Verifies that the given field name is valid.

Parameters:
    

  * **field_name** â the field name

  * **media_type** (_None_) â the media type of the sample, if known

  * **is_frame_field** (_False_) â whether this is a frame-level field



Raises:
    

**ValueError** â if the field name is invalid

fiftyone.core.odm.create_field(_name_ , _ftype_ , _embedded_doc_type =None_, _subfield =None_, _fields =None_, _db_field =None_, _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Creates the field defined by the given specification.

Note

This method is used exclusively to create user-defined (non-default) fields. Any parameters accepted here must be stored on [`fiftyone.core.odm.dataset.SampleFieldDocument`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument "fiftyone.core.odm.dataset.SampleFieldDocument") or else datasets will âloseâ any additional decorations when they are loaded from the database.

Parameters:
    

  * **name** â the field name

  * **ftype** â the field type to create. Must be a subclass of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â the `fiftyone.core.odm.BaseEmbeddedDocument` type of the field. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **subfield** (_None_) â the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") type of the contained field. Only applicable when `ftype` is [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") or [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")

  * **fields** (_None_) â a list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances defining embedded document attributes. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **db_field** (_None_) â the database field to store this field in. By default, `name` is used

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field should be read-only

  * **created_at** (_None_) â the datetime the field was created



Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

fiftyone.core.odm.create_implied_field(_path_ , _value_ , _dynamic =False_)#
    

Creates the field for the given value.

Parameters:
    

  * **path** â the field name or path

  * **value** â a value

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

fiftyone.core.odm.get_field_kwargs(_field_)#
    

Constructs the field keyword arguments dictionary for the given field.

Parameters:
    

**field** â a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") or `str(field)` representation of one

Returns:
    

a field specification dict

fiftyone.core.odm.get_implied_field_kwargs(_value_ , _dynamic =False_)#
    

Infers the field keyword arguments dictionary for a field that can hold the given value.

Parameters:
    

  * **value** â a value

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Returns:
    

a field specification dict

fiftyone.core.odm.validate_fields_match(_name_ , _field_ , _existing_field_)#
    

Validates that the types of the given fields match.

Embedded document fields are not validated, if applicable.

Parameters:
    

  * **name** â the field name or `embedded.field.name`

  * **field** â a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **existing_field** â the reference [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")



Raises:
    

**ValueError** â if the fields do not match

class fiftyone.core.odm.SavedViewDocument(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Backing document for saved views.

**Attributes:**

`dataset_id` | An Object ID field.  
---|---  
`name` | A unicode string field.  
`description` | A unicode string field.  
`slug` | A unicode string field.  
`color` | A string field that holds a hex color string like '#FF6D04'.  
`view_stages` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`created_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`last_loaded_at` | A datetime field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Methods:**

`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
---|---  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
dataset_id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




description#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




slug#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




color#
    

A string field that holds a hex color string like â#FF6D04â.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




view_stages#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_loaded_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




exception DoesNotExist#
    

Bases: `DoesNotExist`

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

exception MultipleObjectsReturned#
    

Bases: `MultipleObjectsReturned`

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

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

A field wrapper around MongoDBâs ObjectIds.

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

fiftyone.core.odm.default_workspace_factory()#
    

Creates a default top-level instance of `Space`

Returns:
    

a default `Space` instance

class fiftyone.core.odm.Panel(_* args_, _** kwargs_)#
    

Bases: [`AppComponent`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent "fiftyone.core.odm.workspace.AppComponent")

Document for a panel (tab) within a Workspace in the App.

Parameters:
    

  * **component_id** â the component ID

  * **type** â the Panel type

  * **pinned** â whether the Panel is currently pinned

  * **state** â an optional Panel state dict




**Attributes:**

`type` | A unicode string field.  
---|---  
`pinned` | A boolean field.  
`state` | A dictionary field that wraps a standard Python dictionary.  
`STRICT` |   
`component_id` | A unicode string field.  
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
type#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




pinned#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




state#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

component_id#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.Space(_* args_, _** kwargs_)#
    

Bases: [`AppComponent`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.AppComponent "fiftyone.core.odm.workspace.AppComponent")

Document for configuration of a Space in the App.

Parameters:
    

  * **component_id** â the componentâs ID

  * **children** â the list of `Component` children of this space, if any

  * **orientation** (_[__"horizontal"__,__"vertical"__]_) â the orientation of this spaceâs children

  * **active_child** â the `component_id` of this spaceâs currently active child

  * **sizes** â the ordered list of relative sizes for children of a space in `[0, 1]`




**Attributes:**

`children` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`orientation` | A unicode string field.  
`active_child` | A unicode string field.  
`sizes` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`name` |   
`STRICT` |   
`component_id` | A unicode string field.  
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
children#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




orientation#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




active_child#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




sizes#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property name#
    

STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

component_id#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.odm.WorkspaceDocument(_* args_, _** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Document for configuration of a saved workspace in the App.

Contains a single `Space` as a child, which can in turn contain multiple children.

**Attributes:**

`child` | A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.  
---|---  
`color` | A string field that holds a hex color string like '#FF6D04'.  
`created_at` | A datetime field.  
`dataset_id` | An Object ID field.  
`description` | A unicode string field.  
`last_loaded_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`slug` | A unicode string field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`name` |   
`pk` | Get the primary key.  
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Methods:**

`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
---|---  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
child#
    

A field that stores instances of a given type of `fiftyone.core.odm.BaseEmbeddedDocument` object.

Parameters:
    

  * **document_type** â the `fiftyone.core.odm.BaseEmbeddedDocument` type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




color#
    

A string field that holds a hex color string like â#FF6D04â.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




dataset_id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




description#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_loaded_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




slug#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




exception DoesNotExist#
    

Bases: `DoesNotExist`

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

exception MultipleObjectsReturned#
    

Bases: `MultipleObjectsReturned`

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

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

A field wrapper around MongoDBâs ObjectIds.

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property name#
    

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
