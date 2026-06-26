---
source_url: https://docs.voxel51.com/api/fiftyone.utils.eval.html
---

# fiftyone.utils.eval#

  * [fiftyone.utils.eval.activitynet](api__fiftyone.utils.eval.activitynet.md)
    * [`ActivityNetEvaluationConfig`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig)
      * [`ActivityNetEvaluationConfig.method`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.method)
      * [`ActivityNetEvaluationConfig.attributes()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.attributes)
      * [`ActivityNetEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.base_config_cls)
      * [`ActivityNetEvaluationConfig.build()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.build)
      * [`ActivityNetEvaluationConfig.builder()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.builder)
      * [`ActivityNetEvaluationConfig.cls`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.cls)
      * [`ActivityNetEvaluationConfig.copy()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.copy)
      * [`ActivityNetEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.custom_attributes)
      * [`ActivityNetEvaluationConfig.default()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.default)
      * [`ActivityNetEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.from_dict)
      * [`ActivityNetEvaluationConfig.from_json()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.from_json)
      * [`ActivityNetEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.from_kwargs)
      * [`ActivityNetEvaluationConfig.from_str()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.from_str)
      * [`ActivityNetEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.get_class_name)
      * [`ActivityNetEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.load_credentials)
      * [`ActivityNetEvaluationConfig.load_default()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.load_default)
      * [`ActivityNetEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_array)
      * [`ActivityNetEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_bool)
      * [`ActivityNetEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_categorical)
      * [`ActivityNetEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_dict)
      * [`ActivityNetEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_int)
      * [`ActivityNetEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_mutually_exclusive_fields)
      * [`ActivityNetEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_number)
      * [`ActivityNetEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_object)
      * [`ActivityNetEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_object_array)
      * [`ActivityNetEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_object_dict)
      * [`ActivityNetEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_path)
      * [`ActivityNetEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_raw)
      * [`ActivityNetEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.parse_string)
      * [`ActivityNetEvaluationConfig.requires_additional_fields`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.requires_additional_fields)
      * [`ActivityNetEvaluationConfig.run_cls`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.run_cls)
      * [`ActivityNetEvaluationConfig.serialize()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.serialize)
      * [`ActivityNetEvaluationConfig.to_str()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.to_str)
      * [`ActivityNetEvaluationConfig.type`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.type)
      * [`ActivityNetEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.validate_all_or_nothing_fields)
      * [`ActivityNetEvaluationConfig.write_json()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig.write_json)
    * [`ActivityNetEvaluation`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation)
      * [`ActivityNetEvaluation.evaluate()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.evaluate)
      * [`ActivityNetEvaluation.generate_results()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.generate_results)
      * [`ActivityNetEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.add_fields_to_sidebar_group)
      * [`ActivityNetEvaluation.cleanup()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.cleanup)
      * [`ActivityNetEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.cleanup_custom_metrics)
      * [`ActivityNetEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.compute_custom_metrics)
      * [`ActivityNetEvaluation.delete_run()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.delete_run)
      * [`ActivityNetEvaluation.delete_runs()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.delete_runs)
      * [`ActivityNetEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.ensure_requirements)
      * [`ActivityNetEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.ensure_usage_requirements)
      * [`ActivityNetEvaluation.from_config()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.from_config)
      * [`ActivityNetEvaluation.from_dict()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.from_dict)
      * [`ActivityNetEvaluation.from_json()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.from_json)
      * [`ActivityNetEvaluation.from_kwargs()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.from_kwargs)
      * [`ActivityNetEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.get_custom_metric_fields)
      * [`ActivityNetEvaluation.get_fields()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.get_fields)
      * [`ActivityNetEvaluation.get_run_info()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.get_run_info)
      * [`ActivityNetEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.has_cached_run_results)
      * [`ActivityNetEvaluation.list_runs()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.list_runs)
      * [`ActivityNetEvaluation.load_run_results()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.load_run_results)
      * [`ActivityNetEvaluation.load_run_view()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.load_run_view)
      * [`ActivityNetEvaluation.parse()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.parse)
      * [`ActivityNetEvaluation.register_run()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.register_run)
      * [`ActivityNetEvaluation.register_samples()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.register_samples)
      * [`ActivityNetEvaluation.rename()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.rename)
      * [`ActivityNetEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.rename_custom_metrics)
      * [`ActivityNetEvaluation.run_info_cls()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.run_info_cls)
      * [`ActivityNetEvaluation.save_run_info()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.save_run_info)
      * [`ActivityNetEvaluation.save_run_results()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.save_run_results)
      * [`ActivityNetEvaluation.update_run_config()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.update_run_config)
      * [`ActivityNetEvaluation.update_run_key()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.update_run_key)
      * [`ActivityNetEvaluation.validate()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.validate)
      * [`ActivityNetEvaluation.validate_run()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetEvaluation.validate_run)
    * [`ActivityNetDetectionResults`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults)
      * [`ActivityNetDetectionResults.plot_pr_curves()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.plot_pr_curves)
      * [`ActivityNetDetectionResults.mAP()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.mAP)
      * [`ActivityNetDetectionResults.add_custom_metrics()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.add_custom_metrics)
      * [`ActivityNetDetectionResults.attributes()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.attributes)
      * [`ActivityNetDetectionResults.backend`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.backend)
      * [`ActivityNetDetectionResults.base_results_cls()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.base_results_cls)
      * [`ActivityNetDetectionResults.clear_subset()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.clear_subset)
      * [`ActivityNetDetectionResults.cls`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.cls)
      * [`ActivityNetDetectionResults.config`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.config)
      * [`ActivityNetDetectionResults.confusion_matrix()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.confusion_matrix)
      * [`ActivityNetDetectionResults.copy()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.copy)
      * [`ActivityNetDetectionResults.custom_attributes()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.custom_attributes)
      * [`ActivityNetDetectionResults.from_dict()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.from_dict)
      * [`ActivityNetDetectionResults.from_json()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.from_json)
      * [`ActivityNetDetectionResults.from_str()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.from_str)
      * [`ActivityNetDetectionResults.get_class_name()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.get_class_name)
      * [`ActivityNetDetectionResults.has_subset`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.has_subset)
      * [`ActivityNetDetectionResults.key`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.key)
      * [`ActivityNetDetectionResults.metrics()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.metrics)
      * [`ActivityNetDetectionResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.plot_confusion_matrix)
      * [`ActivityNetDetectionResults.print_metrics()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.print_metrics)
      * [`ActivityNetDetectionResults.print_report()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.print_report)
      * [`ActivityNetDetectionResults.report()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.report)
      * [`ActivityNetDetectionResults.samples`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.samples)
      * [`ActivityNetDetectionResults.save()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.save)
      * [`ActivityNetDetectionResults.save_config()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.save_config)
      * [`ActivityNetDetectionResults.serialize()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.serialize)
      * [`ActivityNetDetectionResults.to_str()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.to_str)
      * [`ActivityNetDetectionResults.use_subset()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.use_subset)
      * [`ActivityNetDetectionResults.write_json()`](api__fiftyone.utils.eval.activitynet.md#fiftyone.utils.eval.activitynet.ActivityNetDetectionResults.write_json)
  * [fiftyone.utils.eval.base](api__fiftyone.utils.eval.base.md)
    * [`get_subset_view()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.get_subset_view)
    * [`BaseEvaluationMethodConfig`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig)
      * [`BaseEvaluationMethodConfig.attributes()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.attributes)
      * [`BaseEvaluationMethodConfig.base_config_cls()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.base_config_cls)
      * [`BaseEvaluationMethodConfig.build()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.build)
      * [`BaseEvaluationMethodConfig.builder()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.builder)
      * [`BaseEvaluationMethodConfig.cls`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.cls)
      * [`BaseEvaluationMethodConfig.copy()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.copy)
      * [`BaseEvaluationMethodConfig.custom_attributes()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.custom_attributes)
      * [`BaseEvaluationMethodConfig.default()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.default)
      * [`BaseEvaluationMethodConfig.from_dict()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.from_dict)
      * [`BaseEvaluationMethodConfig.from_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.from_json)
      * [`BaseEvaluationMethodConfig.from_kwargs()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.from_kwargs)
      * [`BaseEvaluationMethodConfig.from_str()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.from_str)
      * [`BaseEvaluationMethodConfig.get_class_name()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.get_class_name)
      * [`BaseEvaluationMethodConfig.load_credentials()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.load_credentials)
      * [`BaseEvaluationMethodConfig.load_default()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.load_default)
      * [`BaseEvaluationMethodConfig.method`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.method)
      * [`BaseEvaluationMethodConfig.parse_array()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_array)
      * [`BaseEvaluationMethodConfig.parse_bool()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_bool)
      * [`BaseEvaluationMethodConfig.parse_categorical()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_categorical)
      * [`BaseEvaluationMethodConfig.parse_dict()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_dict)
      * [`BaseEvaluationMethodConfig.parse_int()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_int)
      * [`BaseEvaluationMethodConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_mutually_exclusive_fields)
      * [`BaseEvaluationMethodConfig.parse_number()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_number)
      * [`BaseEvaluationMethodConfig.parse_object()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_object)
      * [`BaseEvaluationMethodConfig.parse_object_array()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_object_array)
      * [`BaseEvaluationMethodConfig.parse_object_dict()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_object_dict)
      * [`BaseEvaluationMethodConfig.parse_path()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_path)
      * [`BaseEvaluationMethodConfig.parse_raw()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_raw)
      * [`BaseEvaluationMethodConfig.parse_string()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.parse_string)
      * [`BaseEvaluationMethodConfig.run_cls`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.run_cls)
      * [`BaseEvaluationMethodConfig.serialize()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.serialize)
      * [`BaseEvaluationMethodConfig.to_str()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.to_str)
      * [`BaseEvaluationMethodConfig.type`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.type)
      * [`BaseEvaluationMethodConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.validate_all_or_nothing_fields)
      * [`BaseEvaluationMethodConfig.write_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig.write_json)
    * [`BaseEvaluationMethod`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod)
      * [`BaseEvaluationMethod.compute_custom_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.compute_custom_metrics)
      * [`BaseEvaluationMethod.get_custom_metric_fields()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.get_custom_metric_fields)
      * [`BaseEvaluationMethod.rename_custom_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.rename_custom_metrics)
      * [`BaseEvaluationMethod.cleanup_custom_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.cleanup_custom_metrics)
      * [`BaseEvaluationMethod.get_fields()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.get_fields)
      * [`BaseEvaluationMethod.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.add_fields_to_sidebar_group)
      * [`BaseEvaluationMethod.cleanup()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.cleanup)
      * [`BaseEvaluationMethod.delete_run()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.delete_run)
      * [`BaseEvaluationMethod.delete_runs()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.delete_runs)
      * [`BaseEvaluationMethod.ensure_requirements()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.ensure_requirements)
      * [`BaseEvaluationMethod.ensure_usage_requirements()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.ensure_usage_requirements)
      * [`BaseEvaluationMethod.from_config()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.from_config)
      * [`BaseEvaluationMethod.from_dict()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.from_dict)
      * [`BaseEvaluationMethod.from_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.from_json)
      * [`BaseEvaluationMethod.from_kwargs()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.from_kwargs)
      * [`BaseEvaluationMethod.get_run_info()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.get_run_info)
      * [`BaseEvaluationMethod.has_cached_run_results()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.has_cached_run_results)
      * [`BaseEvaluationMethod.list_runs()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.list_runs)
      * [`BaseEvaluationMethod.load_run_results()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.load_run_results)
      * [`BaseEvaluationMethod.load_run_view()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.load_run_view)
      * [`BaseEvaluationMethod.parse()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.parse)
      * [`BaseEvaluationMethod.register_run()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.register_run)
      * [`BaseEvaluationMethod.rename()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.rename)
      * [`BaseEvaluationMethod.run_info_cls()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.run_info_cls)
      * [`BaseEvaluationMethod.save_run_info()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.save_run_info)
      * [`BaseEvaluationMethod.save_run_results()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.save_run_results)
      * [`BaseEvaluationMethod.update_run_config()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.update_run_config)
      * [`BaseEvaluationMethod.update_run_key()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.update_run_key)
      * [`BaseEvaluationMethod.validate()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.validate)
      * [`BaseEvaluationMethod.validate_run()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethod.validate_run)
    * [`BaseEvaluationResults`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults)
      * [`BaseEvaluationResults.add_custom_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.add_custom_metrics)
      * [`BaseEvaluationResults.metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.metrics)
      * [`BaseEvaluationResults.print_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.print_metrics)
      * [`BaseEvaluationResults.attributes()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.attributes)
      * [`BaseEvaluationResults.backend`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.backend)
      * [`BaseEvaluationResults.base_results_cls()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.base_results_cls)
      * [`BaseEvaluationResults.cls`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.cls)
      * [`BaseEvaluationResults.config`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.config)
      * [`BaseEvaluationResults.copy()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.copy)
      * [`BaseEvaluationResults.custom_attributes()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.custom_attributes)
      * [`BaseEvaluationResults.from_dict()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.from_dict)
      * [`BaseEvaluationResults.from_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.from_json)
      * [`BaseEvaluationResults.from_str()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.from_str)
      * [`BaseEvaluationResults.get_class_name()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.get_class_name)
      * [`BaseEvaluationResults.key`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.key)
      * [`BaseEvaluationResults.samples`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.samples)
      * [`BaseEvaluationResults.save()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.save)
      * [`BaseEvaluationResults.save_config()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.save_config)
      * [`BaseEvaluationResults.serialize()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.serialize)
      * [`BaseEvaluationResults.to_str()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.to_str)
      * [`BaseEvaluationResults.write_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.write_json)
    * [`BaseClassificationResults`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults)
      * [`BaseClassificationResults.has_subset`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.has_subset)
      * [`BaseClassificationResults.use_subset()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.use_subset)
      * [`BaseClassificationResults.clear_subset()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.clear_subset)
      * [`BaseClassificationResults.report()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.report)
      * [`BaseClassificationResults.print_report()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.print_report)
      * [`BaseClassificationResults.metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.metrics)
      * [`BaseClassificationResults.print_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.print_metrics)
      * [`BaseClassificationResults.confusion_matrix()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.confusion_matrix)
      * [`BaseClassificationResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.plot_confusion_matrix)
      * [`BaseClassificationResults.add_custom_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.add_custom_metrics)
      * [`BaseClassificationResults.attributes()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.attributes)
      * [`BaseClassificationResults.backend`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.backend)
      * [`BaseClassificationResults.base_results_cls()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.base_results_cls)
      * [`BaseClassificationResults.cls`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.cls)
      * [`BaseClassificationResults.config`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.config)
      * [`BaseClassificationResults.copy()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.copy)
      * [`BaseClassificationResults.custom_attributes()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.custom_attributes)
      * [`BaseClassificationResults.from_dict()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.from_dict)
      * [`BaseClassificationResults.from_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.from_json)
      * [`BaseClassificationResults.from_str()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.from_str)
      * [`BaseClassificationResults.get_class_name()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.get_class_name)
      * [`BaseClassificationResults.key`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.key)
      * [`BaseClassificationResults.samples`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.samples)
      * [`BaseClassificationResults.save()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.save)
      * [`BaseClassificationResults.save_config()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.save_config)
      * [`BaseClassificationResults.serialize()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.serialize)
      * [`BaseClassificationResults.to_str()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.to_str)
      * [`BaseClassificationResults.write_json()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.write_json)
  * [fiftyone.utils.eval.classification](api__fiftyone.utils.eval.classification.md)
    * [`evaluate_classifications()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.evaluate_classifications)
    * [`ClassificationEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig)
      * [`ClassificationEvaluationConfig.type`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.type)
      * [`ClassificationEvaluationConfig.attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.attributes)
      * [`ClassificationEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.base_config_cls)
      * [`ClassificationEvaluationConfig.build()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.build)
      * [`ClassificationEvaluationConfig.builder()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.builder)
      * [`ClassificationEvaluationConfig.cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.cls)
      * [`ClassificationEvaluationConfig.copy()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.copy)
      * [`ClassificationEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.custom_attributes)
      * [`ClassificationEvaluationConfig.default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.default)
      * [`ClassificationEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.from_dict)
      * [`ClassificationEvaluationConfig.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.from_json)
      * [`ClassificationEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.from_kwargs)
      * [`ClassificationEvaluationConfig.from_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.from_str)
      * [`ClassificationEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.get_class_name)
      * [`ClassificationEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.load_credentials)
      * [`ClassificationEvaluationConfig.load_default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.load_default)
      * [`ClassificationEvaluationConfig.method`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.method)
      * [`ClassificationEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_array)
      * [`ClassificationEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_bool)
      * [`ClassificationEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_categorical)
      * [`ClassificationEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_dict)
      * [`ClassificationEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_int)
      * [`ClassificationEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_mutually_exclusive_fields)
      * [`ClassificationEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_number)
      * [`ClassificationEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_object)
      * [`ClassificationEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_object_array)
      * [`ClassificationEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_object_dict)
      * [`ClassificationEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_path)
      * [`ClassificationEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_raw)
      * [`ClassificationEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.parse_string)
      * [`ClassificationEvaluationConfig.run_cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.run_cls)
      * [`ClassificationEvaluationConfig.serialize()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.serialize)
      * [`ClassificationEvaluationConfig.to_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.to_str)
      * [`ClassificationEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.validate_all_or_nothing_fields)
      * [`ClassificationEvaluationConfig.write_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluationConfig.write_json)
    * [`ClassificationEvaluation`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation)
      * [`ClassificationEvaluation.register_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.register_samples)
      * [`ClassificationEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.evaluate_samples)
      * [`ClassificationEvaluation.get_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.get_fields)
      * [`ClassificationEvaluation.rename()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.rename)
      * [`ClassificationEvaluation.cleanup()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.cleanup)
      * [`ClassificationEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.add_fields_to_sidebar_group)
      * [`ClassificationEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.cleanup_custom_metrics)
      * [`ClassificationEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.compute_custom_metrics)
      * [`ClassificationEvaluation.delete_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.delete_run)
      * [`ClassificationEvaluation.delete_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.delete_runs)
      * [`ClassificationEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.ensure_requirements)
      * [`ClassificationEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.ensure_usage_requirements)
      * [`ClassificationEvaluation.from_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.from_config)
      * [`ClassificationEvaluation.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.from_dict)
      * [`ClassificationEvaluation.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.from_json)
      * [`ClassificationEvaluation.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.from_kwargs)
      * [`ClassificationEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.get_custom_metric_fields)
      * [`ClassificationEvaluation.get_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.get_run_info)
      * [`ClassificationEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.has_cached_run_results)
      * [`ClassificationEvaluation.list_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.list_runs)
      * [`ClassificationEvaluation.load_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.load_run_results)
      * [`ClassificationEvaluation.load_run_view()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.load_run_view)
      * [`ClassificationEvaluation.parse()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.parse)
      * [`ClassificationEvaluation.register_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.register_run)
      * [`ClassificationEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.rename_custom_metrics)
      * [`ClassificationEvaluation.run_info_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.run_info_cls)
      * [`ClassificationEvaluation.save_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.save_run_info)
      * [`ClassificationEvaluation.save_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.save_run_results)
      * [`ClassificationEvaluation.update_run_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.update_run_config)
      * [`ClassificationEvaluation.update_run_key()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.update_run_key)
      * [`ClassificationEvaluation.validate()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.validate)
      * [`ClassificationEvaluation.validate_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationEvaluation.validate_run)
    * [`SimpleEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig)
      * [`SimpleEvaluationConfig.method`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.method)
      * [`SimpleEvaluationConfig.attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.attributes)
      * [`SimpleEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.base_config_cls)
      * [`SimpleEvaluationConfig.build()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.build)
      * [`SimpleEvaluationConfig.builder()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.builder)
      * [`SimpleEvaluationConfig.cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.cls)
      * [`SimpleEvaluationConfig.copy()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.copy)
      * [`SimpleEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.custom_attributes)
      * [`SimpleEvaluationConfig.default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.default)
      * [`SimpleEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.from_dict)
      * [`SimpleEvaluationConfig.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.from_json)
      * [`SimpleEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.from_kwargs)
      * [`SimpleEvaluationConfig.from_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.from_str)
      * [`SimpleEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.get_class_name)
      * [`SimpleEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.load_credentials)
      * [`SimpleEvaluationConfig.load_default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.load_default)
      * [`SimpleEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_array)
      * [`SimpleEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_bool)
      * [`SimpleEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_categorical)
      * [`SimpleEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_dict)
      * [`SimpleEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_int)
      * [`SimpleEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_mutually_exclusive_fields)
      * [`SimpleEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_number)
      * [`SimpleEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_object)
      * [`SimpleEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_object_array)
      * [`SimpleEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_object_dict)
      * [`SimpleEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_path)
      * [`SimpleEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_raw)
      * [`SimpleEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.parse_string)
      * [`SimpleEvaluationConfig.run_cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.run_cls)
      * [`SimpleEvaluationConfig.serialize()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.serialize)
      * [`SimpleEvaluationConfig.to_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.to_str)
      * [`SimpleEvaluationConfig.type`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.type)
      * [`SimpleEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.validate_all_or_nothing_fields)
      * [`SimpleEvaluationConfig.write_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluationConfig.write_json)
    * [`SimpleEvaluation`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation)
      * [`SimpleEvaluation.register_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.register_samples)
      * [`SimpleEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.evaluate_samples)
      * [`SimpleEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.add_fields_to_sidebar_group)
      * [`SimpleEvaluation.cleanup()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.cleanup)
      * [`SimpleEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.cleanup_custom_metrics)
      * [`SimpleEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.compute_custom_metrics)
      * [`SimpleEvaluation.delete_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.delete_run)
      * [`SimpleEvaluation.delete_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.delete_runs)
      * [`SimpleEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.ensure_requirements)
      * [`SimpleEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.ensure_usage_requirements)
      * [`SimpleEvaluation.from_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.from_config)
      * [`SimpleEvaluation.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.from_dict)
      * [`SimpleEvaluation.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.from_json)
      * [`SimpleEvaluation.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.from_kwargs)
      * [`SimpleEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.get_custom_metric_fields)
      * [`SimpleEvaluation.get_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.get_fields)
      * [`SimpleEvaluation.get_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.get_run_info)
      * [`SimpleEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.has_cached_run_results)
      * [`SimpleEvaluation.list_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.list_runs)
      * [`SimpleEvaluation.load_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.load_run_results)
      * [`SimpleEvaluation.load_run_view()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.load_run_view)
      * [`SimpleEvaluation.parse()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.parse)
      * [`SimpleEvaluation.register_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.register_run)
      * [`SimpleEvaluation.rename()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.rename)
      * [`SimpleEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.rename_custom_metrics)
      * [`SimpleEvaluation.run_info_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.run_info_cls)
      * [`SimpleEvaluation.save_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.save_run_info)
      * [`SimpleEvaluation.save_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.save_run_results)
      * [`SimpleEvaluation.update_run_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.update_run_config)
      * [`SimpleEvaluation.update_run_key()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.update_run_key)
      * [`SimpleEvaluation.validate()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.validate)
      * [`SimpleEvaluation.validate_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.SimpleEvaluation.validate_run)
    * [`TopKEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig)
      * [`TopKEvaluationConfig.method`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.method)
      * [`TopKEvaluationConfig.attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.attributes)
      * [`TopKEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.base_config_cls)
      * [`TopKEvaluationConfig.build()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.build)
      * [`TopKEvaluationConfig.builder()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.builder)
      * [`TopKEvaluationConfig.cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.cls)
      * [`TopKEvaluationConfig.copy()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.copy)
      * [`TopKEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.custom_attributes)
      * [`TopKEvaluationConfig.default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.default)
      * [`TopKEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.from_dict)
      * [`TopKEvaluationConfig.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.from_json)
      * [`TopKEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.from_kwargs)
      * [`TopKEvaluationConfig.from_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.from_str)
      * [`TopKEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.get_class_name)
      * [`TopKEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.load_credentials)
      * [`TopKEvaluationConfig.load_default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.load_default)
      * [`TopKEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_array)
      * [`TopKEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_bool)
      * [`TopKEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_categorical)
      * [`TopKEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_dict)
      * [`TopKEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_int)
      * [`TopKEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_mutually_exclusive_fields)
      * [`TopKEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_number)
      * [`TopKEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_object)
      * [`TopKEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_object_array)
      * [`TopKEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_object_dict)
      * [`TopKEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_path)
      * [`TopKEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_raw)
      * [`TopKEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.parse_string)
      * [`TopKEvaluationConfig.run_cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.run_cls)
      * [`TopKEvaluationConfig.serialize()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.serialize)
      * [`TopKEvaluationConfig.to_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.to_str)
      * [`TopKEvaluationConfig.type`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.type)
      * [`TopKEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.validate_all_or_nothing_fields)
      * [`TopKEvaluationConfig.write_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluationConfig.write_json)
    * [`TopKEvaluation`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation)
      * [`TopKEvaluation.register_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.register_samples)
      * [`TopKEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.evaluate_samples)
      * [`TopKEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.add_fields_to_sidebar_group)
      * [`TopKEvaluation.cleanup()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.cleanup)
      * [`TopKEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.cleanup_custom_metrics)
      * [`TopKEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.compute_custom_metrics)
      * [`TopKEvaluation.delete_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.delete_run)
      * [`TopKEvaluation.delete_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.delete_runs)
      * [`TopKEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.ensure_requirements)
      * [`TopKEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.ensure_usage_requirements)
      * [`TopKEvaluation.from_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.from_config)
      * [`TopKEvaluation.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.from_dict)
      * [`TopKEvaluation.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.from_json)
      * [`TopKEvaluation.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.from_kwargs)
      * [`TopKEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.get_custom_metric_fields)
      * [`TopKEvaluation.get_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.get_fields)
      * [`TopKEvaluation.get_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.get_run_info)
      * [`TopKEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.has_cached_run_results)
      * [`TopKEvaluation.list_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.list_runs)
      * [`TopKEvaluation.load_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.load_run_results)
      * [`TopKEvaluation.load_run_view()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.load_run_view)
      * [`TopKEvaluation.parse()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.parse)
      * [`TopKEvaluation.register_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.register_run)
      * [`TopKEvaluation.rename()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.rename)
      * [`TopKEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.rename_custom_metrics)
      * [`TopKEvaluation.run_info_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.run_info_cls)
      * [`TopKEvaluation.save_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.save_run_info)
      * [`TopKEvaluation.save_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.save_run_results)
      * [`TopKEvaluation.update_run_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.update_run_config)
      * [`TopKEvaluation.update_run_key()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.update_run_key)
      * [`TopKEvaluation.validate()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.validate)
      * [`TopKEvaluation.validate_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.TopKEvaluation.validate_run)
    * [`BinaryEvaluationConfig`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig)
      * [`BinaryEvaluationConfig.method`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.method)
      * [`BinaryEvaluationConfig.attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.attributes)
      * [`BinaryEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.base_config_cls)
      * [`BinaryEvaluationConfig.build()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.build)
      * [`BinaryEvaluationConfig.builder()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.builder)
      * [`BinaryEvaluationConfig.cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.cls)
      * [`BinaryEvaluationConfig.copy()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.copy)
      * [`BinaryEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.custom_attributes)
      * [`BinaryEvaluationConfig.default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.default)
      * [`BinaryEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.from_dict)
      * [`BinaryEvaluationConfig.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.from_json)
      * [`BinaryEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.from_kwargs)
      * [`BinaryEvaluationConfig.from_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.from_str)
      * [`BinaryEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.get_class_name)
      * [`BinaryEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.load_credentials)
      * [`BinaryEvaluationConfig.load_default()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.load_default)
      * [`BinaryEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_array)
      * [`BinaryEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_bool)
      * [`BinaryEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_categorical)
      * [`BinaryEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_dict)
      * [`BinaryEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_int)
      * [`BinaryEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_mutually_exclusive_fields)
      * [`BinaryEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_number)
      * [`BinaryEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_object)
      * [`BinaryEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_object_array)
      * [`BinaryEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_object_dict)
      * [`BinaryEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_path)
      * [`BinaryEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_raw)
      * [`BinaryEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.parse_string)
      * [`BinaryEvaluationConfig.run_cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.run_cls)
      * [`BinaryEvaluationConfig.serialize()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.serialize)
      * [`BinaryEvaluationConfig.to_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.to_str)
      * [`BinaryEvaluationConfig.type`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.type)
      * [`BinaryEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.validate_all_or_nothing_fields)
      * [`BinaryEvaluationConfig.write_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluationConfig.write_json)
    * [`BinaryEvaluation`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation)
      * [`BinaryEvaluation.register_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.register_samples)
      * [`BinaryEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.evaluate_samples)
      * [`BinaryEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.add_fields_to_sidebar_group)
      * [`BinaryEvaluation.cleanup()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.cleanup)
      * [`BinaryEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.cleanup_custom_metrics)
      * [`BinaryEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.compute_custom_metrics)
      * [`BinaryEvaluation.delete_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.delete_run)
      * [`BinaryEvaluation.delete_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.delete_runs)
      * [`BinaryEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.ensure_requirements)
      * [`BinaryEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.ensure_usage_requirements)
      * [`BinaryEvaluation.from_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.from_config)
      * [`BinaryEvaluation.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.from_dict)
      * [`BinaryEvaluation.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.from_json)
      * [`BinaryEvaluation.from_kwargs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.from_kwargs)
      * [`BinaryEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.get_custom_metric_fields)
      * [`BinaryEvaluation.get_fields()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.get_fields)
      * [`BinaryEvaluation.get_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.get_run_info)
      * [`BinaryEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.has_cached_run_results)
      * [`BinaryEvaluation.list_runs()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.list_runs)
      * [`BinaryEvaluation.load_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.load_run_results)
      * [`BinaryEvaluation.load_run_view()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.load_run_view)
      * [`BinaryEvaluation.parse()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.parse)
      * [`BinaryEvaluation.register_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.register_run)
      * [`BinaryEvaluation.rename()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.rename)
      * [`BinaryEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.rename_custom_metrics)
      * [`BinaryEvaluation.run_info_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.run_info_cls)
      * [`BinaryEvaluation.save_run_info()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.save_run_info)
      * [`BinaryEvaluation.save_run_results()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.save_run_results)
      * [`BinaryEvaluation.update_run_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.update_run_config)
      * [`BinaryEvaluation.update_run_key()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.update_run_key)
      * [`BinaryEvaluation.validate()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.validate)
      * [`BinaryEvaluation.validate_run()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryEvaluation.validate_run)
    * [`ClassificationResults`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults)
      * [`ClassificationResults.add_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.add_custom_metrics)
      * [`ClassificationResults.attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.attributes)
      * [`ClassificationResults.backend`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.backend)
      * [`ClassificationResults.base_results_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.base_results_cls)
      * [`ClassificationResults.clear_subset()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.clear_subset)
      * [`ClassificationResults.cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.cls)
      * [`ClassificationResults.config`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.config)
      * [`ClassificationResults.confusion_matrix()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.confusion_matrix)
      * [`ClassificationResults.copy()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.copy)
      * [`ClassificationResults.custom_attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.custom_attributes)
      * [`ClassificationResults.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.from_dict)
      * [`ClassificationResults.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.from_json)
      * [`ClassificationResults.from_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.from_str)
      * [`ClassificationResults.get_class_name()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.get_class_name)
      * [`ClassificationResults.has_subset`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.has_subset)
      * [`ClassificationResults.key`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.key)
      * [`ClassificationResults.metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.metrics)
      * [`ClassificationResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.plot_confusion_matrix)
      * [`ClassificationResults.print_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.print_metrics)
      * [`ClassificationResults.print_report()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.print_report)
      * [`ClassificationResults.report()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.report)
      * [`ClassificationResults.samples`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.samples)
      * [`ClassificationResults.save()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.save)
      * [`ClassificationResults.save_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.save_config)
      * [`ClassificationResults.serialize()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.serialize)
      * [`ClassificationResults.to_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.to_str)
      * [`ClassificationResults.use_subset()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.use_subset)
      * [`ClassificationResults.write_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.write_json)
    * [`BinaryClassificationResults`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults)
      * [`BinaryClassificationResults.average_precision()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.average_precision)
      * [`BinaryClassificationResults.plot_pr_curve()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.plot_pr_curve)
      * [`BinaryClassificationResults.plot_roc_curve()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.plot_roc_curve)
      * [`BinaryClassificationResults.metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.metrics)
      * [`BinaryClassificationResults.add_custom_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.add_custom_metrics)
      * [`BinaryClassificationResults.attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.attributes)
      * [`BinaryClassificationResults.backend`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.backend)
      * [`BinaryClassificationResults.base_results_cls()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.base_results_cls)
      * [`BinaryClassificationResults.clear_subset()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.clear_subset)
      * [`BinaryClassificationResults.cls`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.cls)
      * [`BinaryClassificationResults.config`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.config)
      * [`BinaryClassificationResults.confusion_matrix()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.confusion_matrix)
      * [`BinaryClassificationResults.copy()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.copy)
      * [`BinaryClassificationResults.custom_attributes()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.custom_attributes)
      * [`BinaryClassificationResults.from_dict()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.from_dict)
      * [`BinaryClassificationResults.from_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.from_json)
      * [`BinaryClassificationResults.from_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.from_str)
      * [`BinaryClassificationResults.get_class_name()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.get_class_name)
      * [`BinaryClassificationResults.has_subset`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.has_subset)
      * [`BinaryClassificationResults.key`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.key)
      * [`BinaryClassificationResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.plot_confusion_matrix)
      * [`BinaryClassificationResults.print_metrics()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.print_metrics)
      * [`BinaryClassificationResults.print_report()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.print_report)
      * [`BinaryClassificationResults.report()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.report)
      * [`BinaryClassificationResults.samples`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.samples)
      * [`BinaryClassificationResults.save()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.save)
      * [`BinaryClassificationResults.save_config()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.save_config)
      * [`BinaryClassificationResults.serialize()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.serialize)
      * [`BinaryClassificationResults.to_str()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.to_str)
      * [`BinaryClassificationResults.use_subset()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.use_subset)
      * [`BinaryClassificationResults.write_json()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.write_json)
  * [fiftyone.utils.eval.coco](api__fiftyone.utils.eval.coco.md)
    * [`COCOEvaluationConfig`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig)
      * [`COCOEvaluationConfig.method`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.method)
      * [`COCOEvaluationConfig.attributes()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.attributes)
      * [`COCOEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.base_config_cls)
      * [`COCOEvaluationConfig.build()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.build)
      * [`COCOEvaluationConfig.builder()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.builder)
      * [`COCOEvaluationConfig.cls`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.cls)
      * [`COCOEvaluationConfig.copy()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.copy)
      * [`COCOEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.custom_attributes)
      * [`COCOEvaluationConfig.default()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.default)
      * [`COCOEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.from_dict)
      * [`COCOEvaluationConfig.from_json()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.from_json)
      * [`COCOEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.from_kwargs)
      * [`COCOEvaluationConfig.from_str()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.from_str)
      * [`COCOEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.get_class_name)
      * [`COCOEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.load_credentials)
      * [`COCOEvaluationConfig.load_default()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.load_default)
      * [`COCOEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_array)
      * [`COCOEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_bool)
      * [`COCOEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_categorical)
      * [`COCOEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_dict)
      * [`COCOEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_int)
      * [`COCOEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_mutually_exclusive_fields)
      * [`COCOEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_number)
      * [`COCOEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_object)
      * [`COCOEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_object_array)
      * [`COCOEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_object_dict)
      * [`COCOEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_path)
      * [`COCOEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_raw)
      * [`COCOEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.parse_string)
      * [`COCOEvaluationConfig.requires_additional_fields`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.requires_additional_fields)
      * [`COCOEvaluationConfig.run_cls`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.run_cls)
      * [`COCOEvaluationConfig.serialize()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.serialize)
      * [`COCOEvaluationConfig.to_str()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.to_str)
      * [`COCOEvaluationConfig.type`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.type)
      * [`COCOEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.validate_all_or_nothing_fields)
      * [`COCOEvaluationConfig.write_json()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluationConfig.write_json)
    * [`COCOEvaluation`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation)
      * [`COCOEvaluation.evaluate()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.evaluate)
      * [`COCOEvaluation.generate_results()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.generate_results)
      * [`COCOEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.add_fields_to_sidebar_group)
      * [`COCOEvaluation.cleanup()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.cleanup)
      * [`COCOEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.cleanup_custom_metrics)
      * [`COCOEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.compute_custom_metrics)
      * [`COCOEvaluation.delete_run()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.delete_run)
      * [`COCOEvaluation.delete_runs()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.delete_runs)
      * [`COCOEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.ensure_requirements)
      * [`COCOEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.ensure_usage_requirements)
      * [`COCOEvaluation.from_config()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.from_config)
      * [`COCOEvaluation.from_dict()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.from_dict)
      * [`COCOEvaluation.from_json()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.from_json)
      * [`COCOEvaluation.from_kwargs()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.from_kwargs)
      * [`COCOEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.get_custom_metric_fields)
      * [`COCOEvaluation.get_fields()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.get_fields)
      * [`COCOEvaluation.get_run_info()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.get_run_info)
      * [`COCOEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.has_cached_run_results)
      * [`COCOEvaluation.list_runs()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.list_runs)
      * [`COCOEvaluation.load_run_results()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.load_run_results)
      * [`COCOEvaluation.load_run_view()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.load_run_view)
      * [`COCOEvaluation.parse()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.parse)
      * [`COCOEvaluation.register_run()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.register_run)
      * [`COCOEvaluation.register_samples()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.register_samples)
      * [`COCOEvaluation.rename()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.rename)
      * [`COCOEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.rename_custom_metrics)
      * [`COCOEvaluation.run_info_cls()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.run_info_cls)
      * [`COCOEvaluation.save_run_info()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.save_run_info)
      * [`COCOEvaluation.save_run_results()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.save_run_results)
      * [`COCOEvaluation.update_run_config()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.update_run_config)
      * [`COCOEvaluation.update_run_key()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.update_run_key)
      * [`COCOEvaluation.validate()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.validate)
      * [`COCOEvaluation.validate_run()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCOEvaluation.validate_run)
    * [`COCODetectionResults`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults)
      * [`COCODetectionResults.plot_pr_curves()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.plot_pr_curves)
      * [`COCODetectionResults.mAP()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.mAP)
      * [`COCODetectionResults.mAR()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.mAR)
      * [`COCODetectionResults.add_custom_metrics()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.add_custom_metrics)
      * [`COCODetectionResults.attributes()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.attributes)
      * [`COCODetectionResults.backend`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.backend)
      * [`COCODetectionResults.base_results_cls()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.base_results_cls)
      * [`COCODetectionResults.clear_subset()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.clear_subset)
      * [`COCODetectionResults.cls`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.cls)
      * [`COCODetectionResults.config`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.config)
      * [`COCODetectionResults.confusion_matrix()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.confusion_matrix)
      * [`COCODetectionResults.copy()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.copy)
      * [`COCODetectionResults.custom_attributes()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.custom_attributes)
      * [`COCODetectionResults.from_dict()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.from_dict)
      * [`COCODetectionResults.from_json()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.from_json)
      * [`COCODetectionResults.from_str()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.from_str)
      * [`COCODetectionResults.get_class_name()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.get_class_name)
      * [`COCODetectionResults.has_subset`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.has_subset)
      * [`COCODetectionResults.key`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.key)
      * [`COCODetectionResults.metrics()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.metrics)
      * [`COCODetectionResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.plot_confusion_matrix)
      * [`COCODetectionResults.print_metrics()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.print_metrics)
      * [`COCODetectionResults.print_report()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.print_report)
      * [`COCODetectionResults.report()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.report)
      * [`COCODetectionResults.samples`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.samples)
      * [`COCODetectionResults.save()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.save)
      * [`COCODetectionResults.save_config()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.save_config)
      * [`COCODetectionResults.serialize()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.serialize)
      * [`COCODetectionResults.to_str()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.to_str)
      * [`COCODetectionResults.use_subset()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.use_subset)
      * [`COCODetectionResults.write_json()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.write_json)
  * [fiftyone.utils.eval.detection](api__fiftyone.utils.eval.detection.md)
    * [`evaluate_detections()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.evaluate_detections)
    * [`DetectionEvaluationConfig`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig)
      * [`DetectionEvaluationConfig.type`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.type)
      * [`DetectionEvaluationConfig.requires_additional_fields`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.requires_additional_fields)
      * [`DetectionEvaluationConfig.attributes()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.attributes)
      * [`DetectionEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.base_config_cls)
      * [`DetectionEvaluationConfig.build()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.build)
      * [`DetectionEvaluationConfig.builder()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.builder)
      * [`DetectionEvaluationConfig.cls`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.cls)
      * [`DetectionEvaluationConfig.copy()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.copy)
      * [`DetectionEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.custom_attributes)
      * [`DetectionEvaluationConfig.default()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.default)
      * [`DetectionEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.from_dict)
      * [`DetectionEvaluationConfig.from_json()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.from_json)
      * [`DetectionEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.from_kwargs)
      * [`DetectionEvaluationConfig.from_str()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.from_str)
      * [`DetectionEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.get_class_name)
      * [`DetectionEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.load_credentials)
      * [`DetectionEvaluationConfig.load_default()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.load_default)
      * [`DetectionEvaluationConfig.method`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.method)
      * [`DetectionEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_array)
      * [`DetectionEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_bool)
      * [`DetectionEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_categorical)
      * [`DetectionEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_dict)
      * [`DetectionEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_int)
      * [`DetectionEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_mutually_exclusive_fields)
      * [`DetectionEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_number)
      * [`DetectionEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_object)
      * [`DetectionEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_object_array)
      * [`DetectionEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_object_dict)
      * [`DetectionEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_path)
      * [`DetectionEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_raw)
      * [`DetectionEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.parse_string)
      * [`DetectionEvaluationConfig.run_cls`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.run_cls)
      * [`DetectionEvaluationConfig.serialize()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.serialize)
      * [`DetectionEvaluationConfig.to_str()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.to_str)
      * [`DetectionEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.validate_all_or_nothing_fields)
      * [`DetectionEvaluationConfig.write_json()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig.write_json)
    * [`DetectionEvaluation`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation)
      * [`DetectionEvaluation.register_samples()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.register_samples)
      * [`DetectionEvaluation.evaluate()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.evaluate)
      * [`DetectionEvaluation.generate_results()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.generate_results)
      * [`DetectionEvaluation.get_fields()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.get_fields)
      * [`DetectionEvaluation.rename()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.rename)
      * [`DetectionEvaluation.cleanup()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.cleanup)
      * [`DetectionEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.add_fields_to_sidebar_group)
      * [`DetectionEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.cleanup_custom_metrics)
      * [`DetectionEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.compute_custom_metrics)
      * [`DetectionEvaluation.delete_run()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.delete_run)
      * [`DetectionEvaluation.delete_runs()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.delete_runs)
      * [`DetectionEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.ensure_requirements)
      * [`DetectionEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.ensure_usage_requirements)
      * [`DetectionEvaluation.from_config()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.from_config)
      * [`DetectionEvaluation.from_dict()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.from_dict)
      * [`DetectionEvaluation.from_json()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.from_json)
      * [`DetectionEvaluation.from_kwargs()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.from_kwargs)
      * [`DetectionEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.get_custom_metric_fields)
      * [`DetectionEvaluation.get_run_info()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.get_run_info)
      * [`DetectionEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.has_cached_run_results)
      * [`DetectionEvaluation.list_runs()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.list_runs)
      * [`DetectionEvaluation.load_run_results()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.load_run_results)
      * [`DetectionEvaluation.load_run_view()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.load_run_view)
      * [`DetectionEvaluation.parse()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.parse)
      * [`DetectionEvaluation.register_run()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.register_run)
      * [`DetectionEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.rename_custom_metrics)
      * [`DetectionEvaluation.run_info_cls()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.run_info_cls)
      * [`DetectionEvaluation.save_run_info()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.save_run_info)
      * [`DetectionEvaluation.save_run_results()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.save_run_results)
      * [`DetectionEvaluation.update_run_config()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.update_run_config)
      * [`DetectionEvaluation.update_run_key()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.update_run_key)
      * [`DetectionEvaluation.validate()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.validate)
      * [`DetectionEvaluation.validate_run()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation.validate_run)
    * [`DetectionResults`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults)
      * [`DetectionResults.add_custom_metrics()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.add_custom_metrics)
      * [`DetectionResults.attributes()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.attributes)
      * [`DetectionResults.backend`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.backend)
      * [`DetectionResults.base_results_cls()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.base_results_cls)
      * [`DetectionResults.clear_subset()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.clear_subset)
      * [`DetectionResults.cls`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.cls)
      * [`DetectionResults.config`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.config)
      * [`DetectionResults.confusion_matrix()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.confusion_matrix)
      * [`DetectionResults.copy()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.copy)
      * [`DetectionResults.custom_attributes()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.custom_attributes)
      * [`DetectionResults.from_dict()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.from_dict)
      * [`DetectionResults.from_json()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.from_json)
      * [`DetectionResults.from_str()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.from_str)
      * [`DetectionResults.get_class_name()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.get_class_name)
      * [`DetectionResults.has_subset`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.has_subset)
      * [`DetectionResults.key`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.key)
      * [`DetectionResults.metrics()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.metrics)
      * [`DetectionResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.plot_confusion_matrix)
      * [`DetectionResults.print_metrics()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.print_metrics)
      * [`DetectionResults.print_report()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.print_report)
      * [`DetectionResults.report()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.report)
      * [`DetectionResults.samples`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.samples)
      * [`DetectionResults.save()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.save)
      * [`DetectionResults.save_config()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.save_config)
      * [`DetectionResults.serialize()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.serialize)
      * [`DetectionResults.to_str()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.to_str)
      * [`DetectionResults.use_subset()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.use_subset)
      * [`DetectionResults.write_json()`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults.write_json)
  * [fiftyone.utils.eval.openimages](api__fiftyone.utils.eval.openimages.md)
    * [`OpenImagesEvaluationConfig`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig)
      * [`OpenImagesEvaluationConfig.method`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.method)
      * [`OpenImagesEvaluationConfig.requires_additional_fields`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.requires_additional_fields)
      * [`OpenImagesEvaluationConfig.attributes()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.attributes)
      * [`OpenImagesEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.base_config_cls)
      * [`OpenImagesEvaluationConfig.build()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.build)
      * [`OpenImagesEvaluationConfig.builder()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.builder)
      * [`OpenImagesEvaluationConfig.cls`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.cls)
      * [`OpenImagesEvaluationConfig.copy()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.copy)
      * [`OpenImagesEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.custom_attributes)
      * [`OpenImagesEvaluationConfig.default()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.default)
      * [`OpenImagesEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.from_dict)
      * [`OpenImagesEvaluationConfig.from_json()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.from_json)
      * [`OpenImagesEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.from_kwargs)
      * [`OpenImagesEvaluationConfig.from_str()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.from_str)
      * [`OpenImagesEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.get_class_name)
      * [`OpenImagesEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.load_credentials)
      * [`OpenImagesEvaluationConfig.load_default()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.load_default)
      * [`OpenImagesEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_array)
      * [`OpenImagesEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_bool)
      * [`OpenImagesEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_categorical)
      * [`OpenImagesEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_dict)
      * [`OpenImagesEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_int)
      * [`OpenImagesEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_mutually_exclusive_fields)
      * [`OpenImagesEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_number)
      * [`OpenImagesEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_object)
      * [`OpenImagesEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_object_array)
      * [`OpenImagesEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_object_dict)
      * [`OpenImagesEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_path)
      * [`OpenImagesEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_raw)
      * [`OpenImagesEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.parse_string)
      * [`OpenImagesEvaluationConfig.run_cls`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.run_cls)
      * [`OpenImagesEvaluationConfig.serialize()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.serialize)
      * [`OpenImagesEvaluationConfig.to_str()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.to_str)
      * [`OpenImagesEvaluationConfig.type`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.type)
      * [`OpenImagesEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.validate_all_or_nothing_fields)
      * [`OpenImagesEvaluationConfig.write_json()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig.write_json)
    * [`OpenImagesEvaluation`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation)
      * [`OpenImagesEvaluation.evaluate()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.evaluate)
      * [`OpenImagesEvaluation.generate_results()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.generate_results)
      * [`OpenImagesEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.add_fields_to_sidebar_group)
      * [`OpenImagesEvaluation.cleanup()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.cleanup)
      * [`OpenImagesEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.cleanup_custom_metrics)
      * [`OpenImagesEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.compute_custom_metrics)
      * [`OpenImagesEvaluation.delete_run()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.delete_run)
      * [`OpenImagesEvaluation.delete_runs()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.delete_runs)
      * [`OpenImagesEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.ensure_requirements)
      * [`OpenImagesEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.ensure_usage_requirements)
      * [`OpenImagesEvaluation.from_config()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.from_config)
      * [`OpenImagesEvaluation.from_dict()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.from_dict)
      * [`OpenImagesEvaluation.from_json()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.from_json)
      * [`OpenImagesEvaluation.from_kwargs()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.from_kwargs)
      * [`OpenImagesEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.get_custom_metric_fields)
      * [`OpenImagesEvaluation.get_fields()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.get_fields)
      * [`OpenImagesEvaluation.get_run_info()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.get_run_info)
      * [`OpenImagesEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.has_cached_run_results)
      * [`OpenImagesEvaluation.list_runs()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.list_runs)
      * [`OpenImagesEvaluation.load_run_results()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.load_run_results)
      * [`OpenImagesEvaluation.load_run_view()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.load_run_view)
      * [`OpenImagesEvaluation.parse()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.parse)
      * [`OpenImagesEvaluation.register_run()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.register_run)
      * [`OpenImagesEvaluation.register_samples()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.register_samples)
      * [`OpenImagesEvaluation.rename()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.rename)
      * [`OpenImagesEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.rename_custom_metrics)
      * [`OpenImagesEvaluation.run_info_cls()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.run_info_cls)
      * [`OpenImagesEvaluation.save_run_info()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.save_run_info)
      * [`OpenImagesEvaluation.save_run_results()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.save_run_results)
      * [`OpenImagesEvaluation.update_run_config()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.update_run_config)
      * [`OpenImagesEvaluation.update_run_key()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.update_run_key)
      * [`OpenImagesEvaluation.validate()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.validate)
      * [`OpenImagesEvaluation.validate_run()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluation.validate_run)
    * [`OpenImagesDetectionResults`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults)
      * [`OpenImagesDetectionResults.plot_pr_curves()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.plot_pr_curves)
      * [`OpenImagesDetectionResults.mAP()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.mAP)
      * [`OpenImagesDetectionResults.add_custom_metrics()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.add_custom_metrics)
      * [`OpenImagesDetectionResults.attributes()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.attributes)
      * [`OpenImagesDetectionResults.backend`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.backend)
      * [`OpenImagesDetectionResults.base_results_cls()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.base_results_cls)
      * [`OpenImagesDetectionResults.clear_subset()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.clear_subset)
      * [`OpenImagesDetectionResults.cls`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.cls)
      * [`OpenImagesDetectionResults.config`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.config)
      * [`OpenImagesDetectionResults.confusion_matrix()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.confusion_matrix)
      * [`OpenImagesDetectionResults.copy()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.copy)
      * [`OpenImagesDetectionResults.custom_attributes()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.custom_attributes)
      * [`OpenImagesDetectionResults.from_dict()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.from_dict)
      * [`OpenImagesDetectionResults.from_json()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.from_json)
      * [`OpenImagesDetectionResults.from_str()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.from_str)
      * [`OpenImagesDetectionResults.get_class_name()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.get_class_name)
      * [`OpenImagesDetectionResults.has_subset`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.has_subset)
      * [`OpenImagesDetectionResults.key`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.key)
      * [`OpenImagesDetectionResults.metrics()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.metrics)
      * [`OpenImagesDetectionResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.plot_confusion_matrix)
      * [`OpenImagesDetectionResults.print_metrics()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.print_metrics)
      * [`OpenImagesDetectionResults.print_report()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.print_report)
      * [`OpenImagesDetectionResults.report()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.report)
      * [`OpenImagesDetectionResults.samples`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.samples)
      * [`OpenImagesDetectionResults.save()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.save)
      * [`OpenImagesDetectionResults.save_config()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.save_config)
      * [`OpenImagesDetectionResults.serialize()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.serialize)
      * [`OpenImagesDetectionResults.to_str()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.to_str)
      * [`OpenImagesDetectionResults.use_subset()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.use_subset)
      * [`OpenImagesDetectionResults.write_json()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.write_json)
  * [fiftyone.utils.eval.regression](api__fiftyone.utils.eval.regression.md)
    * [`evaluate_regressions()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.evaluate_regressions)
    * [`RegressionEvaluationConfig`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig)
      * [`RegressionEvaluationConfig.type`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.type)
      * [`RegressionEvaluationConfig.attributes()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.attributes)
      * [`RegressionEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.base_config_cls)
      * [`RegressionEvaluationConfig.build()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.build)
      * [`RegressionEvaluationConfig.builder()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.builder)
      * [`RegressionEvaluationConfig.cls`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.cls)
      * [`RegressionEvaluationConfig.copy()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.copy)
      * [`RegressionEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.custom_attributes)
      * [`RegressionEvaluationConfig.default()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.default)
      * [`RegressionEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.from_dict)
      * [`RegressionEvaluationConfig.from_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.from_json)
      * [`RegressionEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.from_kwargs)
      * [`RegressionEvaluationConfig.from_str()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.from_str)
      * [`RegressionEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.get_class_name)
      * [`RegressionEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.load_credentials)
      * [`RegressionEvaluationConfig.load_default()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.load_default)
      * [`RegressionEvaluationConfig.method`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.method)
      * [`RegressionEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_array)
      * [`RegressionEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_bool)
      * [`RegressionEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_categorical)
      * [`RegressionEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_dict)
      * [`RegressionEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_int)
      * [`RegressionEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_mutually_exclusive_fields)
      * [`RegressionEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_number)
      * [`RegressionEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_object)
      * [`RegressionEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_object_array)
      * [`RegressionEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_object_dict)
      * [`RegressionEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_path)
      * [`RegressionEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_raw)
      * [`RegressionEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.parse_string)
      * [`RegressionEvaluationConfig.run_cls`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.run_cls)
      * [`RegressionEvaluationConfig.serialize()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.serialize)
      * [`RegressionEvaluationConfig.to_str()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.to_str)
      * [`RegressionEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.validate_all_or_nothing_fields)
      * [`RegressionEvaluationConfig.write_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluationConfig.write_json)
    * [`RegressionEvaluation`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation)
      * [`RegressionEvaluation.register_samples()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.register_samples)
      * [`RegressionEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.evaluate_samples)
      * [`RegressionEvaluation.get_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.get_fields)
      * [`RegressionEvaluation.rename()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.rename)
      * [`RegressionEvaluation.cleanup()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.cleanup)
      * [`RegressionEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.add_fields_to_sidebar_group)
      * [`RegressionEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.cleanup_custom_metrics)
      * [`RegressionEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.compute_custom_metrics)
      * [`RegressionEvaluation.delete_run()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.delete_run)
      * [`RegressionEvaluation.delete_runs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.delete_runs)
      * [`RegressionEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.ensure_requirements)
      * [`RegressionEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.ensure_usage_requirements)
      * [`RegressionEvaluation.from_config()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.from_config)
      * [`RegressionEvaluation.from_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.from_dict)
      * [`RegressionEvaluation.from_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.from_json)
      * [`RegressionEvaluation.from_kwargs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.from_kwargs)
      * [`RegressionEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.get_custom_metric_fields)
      * [`RegressionEvaluation.get_run_info()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.get_run_info)
      * [`RegressionEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.has_cached_run_results)
      * [`RegressionEvaluation.list_runs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.list_runs)
      * [`RegressionEvaluation.load_run_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.load_run_results)
      * [`RegressionEvaluation.load_run_view()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.load_run_view)
      * [`RegressionEvaluation.parse()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.parse)
      * [`RegressionEvaluation.register_run()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.register_run)
      * [`RegressionEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.rename_custom_metrics)
      * [`RegressionEvaluation.run_info_cls()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.run_info_cls)
      * [`RegressionEvaluation.save_run_info()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.save_run_info)
      * [`RegressionEvaluation.save_run_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.save_run_results)
      * [`RegressionEvaluation.update_run_config()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.update_run_config)
      * [`RegressionEvaluation.update_run_key()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.update_run_key)
      * [`RegressionEvaluation.validate()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.validate)
      * [`RegressionEvaluation.validate_run()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionEvaluation.validate_run)
    * [`SimpleEvaluationConfig`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig)
      * [`SimpleEvaluationConfig.method`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.method)
      * [`SimpleEvaluationConfig.metric`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.metric)
      * [`SimpleEvaluationConfig.attributes()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.attributes)
      * [`SimpleEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.base_config_cls)
      * [`SimpleEvaluationConfig.build()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.build)
      * [`SimpleEvaluationConfig.builder()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.builder)
      * [`SimpleEvaluationConfig.cls`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.cls)
      * [`SimpleEvaluationConfig.copy()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.copy)
      * [`SimpleEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.custom_attributes)
      * [`SimpleEvaluationConfig.default()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.default)
      * [`SimpleEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.from_dict)
      * [`SimpleEvaluationConfig.from_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.from_json)
      * [`SimpleEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.from_kwargs)
      * [`SimpleEvaluationConfig.from_str()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.from_str)
      * [`SimpleEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.get_class_name)
      * [`SimpleEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.load_credentials)
      * [`SimpleEvaluationConfig.load_default()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.load_default)
      * [`SimpleEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_array)
      * [`SimpleEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_bool)
      * [`SimpleEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_categorical)
      * [`SimpleEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_dict)
      * [`SimpleEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_int)
      * [`SimpleEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_mutually_exclusive_fields)
      * [`SimpleEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_number)
      * [`SimpleEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_object)
      * [`SimpleEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_object_array)
      * [`SimpleEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_object_dict)
      * [`SimpleEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_path)
      * [`SimpleEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_raw)
      * [`SimpleEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.parse_string)
      * [`SimpleEvaluationConfig.run_cls`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.run_cls)
      * [`SimpleEvaluationConfig.serialize()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.serialize)
      * [`SimpleEvaluationConfig.to_str()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.to_str)
      * [`SimpleEvaluationConfig.type`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.type)
      * [`SimpleEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.validate_all_or_nothing_fields)
      * [`SimpleEvaluationConfig.write_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluationConfig.write_json)
    * [`SimpleEvaluation`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation)
      * [`SimpleEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.evaluate_samples)
      * [`SimpleEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.add_fields_to_sidebar_group)
      * [`SimpleEvaluation.cleanup()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.cleanup)
      * [`SimpleEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.cleanup_custom_metrics)
      * [`SimpleEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.compute_custom_metrics)
      * [`SimpleEvaluation.delete_run()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.delete_run)
      * [`SimpleEvaluation.delete_runs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.delete_runs)
      * [`SimpleEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.ensure_requirements)
      * [`SimpleEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.ensure_usage_requirements)
      * [`SimpleEvaluation.from_config()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.from_config)
      * [`SimpleEvaluation.from_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.from_dict)
      * [`SimpleEvaluation.from_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.from_json)
      * [`SimpleEvaluation.from_kwargs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.from_kwargs)
      * [`SimpleEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.get_custom_metric_fields)
      * [`SimpleEvaluation.get_fields()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.get_fields)
      * [`SimpleEvaluation.get_run_info()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.get_run_info)
      * [`SimpleEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.has_cached_run_results)
      * [`SimpleEvaluation.list_runs()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.list_runs)
      * [`SimpleEvaluation.load_run_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.load_run_results)
      * [`SimpleEvaluation.load_run_view()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.load_run_view)
      * [`SimpleEvaluation.parse()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.parse)
      * [`SimpleEvaluation.register_run()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.register_run)
      * [`SimpleEvaluation.register_samples()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.register_samples)
      * [`SimpleEvaluation.rename()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.rename)
      * [`SimpleEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.rename_custom_metrics)
      * [`SimpleEvaluation.run_info_cls()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.run_info_cls)
      * [`SimpleEvaluation.save_run_info()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.save_run_info)
      * [`SimpleEvaluation.save_run_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.save_run_results)
      * [`SimpleEvaluation.update_run_config()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.update_run_config)
      * [`SimpleEvaluation.update_run_key()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.update_run_key)
      * [`SimpleEvaluation.validate()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.validate)
      * [`SimpleEvaluation.validate_run()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.SimpleEvaluation.validate_run)
    * [`RegressionResults`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults)
      * [`RegressionResults.metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.metrics)
      * [`RegressionResults.print_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.print_metrics)
      * [`RegressionResults.plot_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.plot_results)
      * [`RegressionResults.add_custom_metrics()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.add_custom_metrics)
      * [`RegressionResults.attributes()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.attributes)
      * [`RegressionResults.backend`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.backend)
      * [`RegressionResults.base_results_cls()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.base_results_cls)
      * [`RegressionResults.cls`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.cls)
      * [`RegressionResults.config`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.config)
      * [`RegressionResults.copy()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.copy)
      * [`RegressionResults.custom_attributes()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.custom_attributes)
      * [`RegressionResults.from_dict()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.from_dict)
      * [`RegressionResults.from_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.from_json)
      * [`RegressionResults.from_str()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.from_str)
      * [`RegressionResults.get_class_name()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.get_class_name)
      * [`RegressionResults.key`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.key)
      * [`RegressionResults.samples`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.samples)
      * [`RegressionResults.save()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.save)
      * [`RegressionResults.save_config()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.save_config)
      * [`RegressionResults.serialize()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.serialize)
      * [`RegressionResults.to_str()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.to_str)
      * [`RegressionResults.write_json()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.write_json)
  * [fiftyone.utils.eval.segmentation](api__fiftyone.utils.eval.segmentation.md)
    * [`evaluate_segmentations()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.evaluate_segmentations)
    * [`SegmentationEvaluationConfig`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig)
      * [`SegmentationEvaluationConfig.type`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.type)
      * [`SegmentationEvaluationConfig.attributes()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.attributes)
      * [`SegmentationEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.base_config_cls)
      * [`SegmentationEvaluationConfig.build()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.build)
      * [`SegmentationEvaluationConfig.builder()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.builder)
      * [`SegmentationEvaluationConfig.cls`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.cls)
      * [`SegmentationEvaluationConfig.copy()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.copy)
      * [`SegmentationEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.custom_attributes)
      * [`SegmentationEvaluationConfig.default()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.default)
      * [`SegmentationEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.from_dict)
      * [`SegmentationEvaluationConfig.from_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.from_json)
      * [`SegmentationEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.from_kwargs)
      * [`SegmentationEvaluationConfig.from_str()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.from_str)
      * [`SegmentationEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.get_class_name)
      * [`SegmentationEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.load_credentials)
      * [`SegmentationEvaluationConfig.load_default()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.load_default)
      * [`SegmentationEvaluationConfig.method`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.method)
      * [`SegmentationEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_array)
      * [`SegmentationEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_bool)
      * [`SegmentationEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_categorical)
      * [`SegmentationEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_dict)
      * [`SegmentationEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_int)
      * [`SegmentationEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_mutually_exclusive_fields)
      * [`SegmentationEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_number)
      * [`SegmentationEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_object)
      * [`SegmentationEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_object_array)
      * [`SegmentationEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_object_dict)
      * [`SegmentationEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_path)
      * [`SegmentationEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_raw)
      * [`SegmentationEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.parse_string)
      * [`SegmentationEvaluationConfig.run_cls`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.run_cls)
      * [`SegmentationEvaluationConfig.serialize()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.serialize)
      * [`SegmentationEvaluationConfig.to_str()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.to_str)
      * [`SegmentationEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.validate_all_or_nothing_fields)
      * [`SegmentationEvaluationConfig.write_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluationConfig.write_json)
    * [`SegmentationEvaluation`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation)
      * [`SegmentationEvaluation.register_samples()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.register_samples)
      * [`SegmentationEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.evaluate_samples)
      * [`SegmentationEvaluation.get_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.get_fields)
      * [`SegmentationEvaluation.rename()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.rename)
      * [`SegmentationEvaluation.cleanup()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.cleanup)
      * [`SegmentationEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.add_fields_to_sidebar_group)
      * [`SegmentationEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.cleanup_custom_metrics)
      * [`SegmentationEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.compute_custom_metrics)
      * [`SegmentationEvaluation.delete_run()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.delete_run)
      * [`SegmentationEvaluation.delete_runs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.delete_runs)
      * [`SegmentationEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.ensure_requirements)
      * [`SegmentationEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.ensure_usage_requirements)
      * [`SegmentationEvaluation.from_config()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.from_config)
      * [`SegmentationEvaluation.from_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.from_dict)
      * [`SegmentationEvaluation.from_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.from_json)
      * [`SegmentationEvaluation.from_kwargs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.from_kwargs)
      * [`SegmentationEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.get_custom_metric_fields)
      * [`SegmentationEvaluation.get_run_info()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.get_run_info)
      * [`SegmentationEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.has_cached_run_results)
      * [`SegmentationEvaluation.list_runs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.list_runs)
      * [`SegmentationEvaluation.load_run_results()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.load_run_results)
      * [`SegmentationEvaluation.load_run_view()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.load_run_view)
      * [`SegmentationEvaluation.parse()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.parse)
      * [`SegmentationEvaluation.register_run()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.register_run)
      * [`SegmentationEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.rename_custom_metrics)
      * [`SegmentationEvaluation.run_info_cls()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.run_info_cls)
      * [`SegmentationEvaluation.save_run_info()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.save_run_info)
      * [`SegmentationEvaluation.save_run_results()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.save_run_results)
      * [`SegmentationEvaluation.update_run_config()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.update_run_config)
      * [`SegmentationEvaluation.update_run_key()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.update_run_key)
      * [`SegmentationEvaluation.validate()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.validate)
      * [`SegmentationEvaluation.validate_run()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationEvaluation.validate_run)
    * [`SimpleEvaluationConfig`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig)
      * [`SimpleEvaluationConfig.method`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.method)
      * [`SimpleEvaluationConfig.attributes()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.attributes)
      * [`SimpleEvaluationConfig.base_config_cls()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.base_config_cls)
      * [`SimpleEvaluationConfig.build()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.build)
      * [`SimpleEvaluationConfig.builder()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.builder)
      * [`SimpleEvaluationConfig.cls`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.cls)
      * [`SimpleEvaluationConfig.copy()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.copy)
      * [`SimpleEvaluationConfig.custom_attributes()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.custom_attributes)
      * [`SimpleEvaluationConfig.default()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.default)
      * [`SimpleEvaluationConfig.from_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.from_dict)
      * [`SimpleEvaluationConfig.from_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.from_json)
      * [`SimpleEvaluationConfig.from_kwargs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.from_kwargs)
      * [`SimpleEvaluationConfig.from_str()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.from_str)
      * [`SimpleEvaluationConfig.get_class_name()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.get_class_name)
      * [`SimpleEvaluationConfig.load_credentials()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.load_credentials)
      * [`SimpleEvaluationConfig.load_default()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.load_default)
      * [`SimpleEvaluationConfig.parse_array()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_array)
      * [`SimpleEvaluationConfig.parse_bool()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_bool)
      * [`SimpleEvaluationConfig.parse_categorical()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_categorical)
      * [`SimpleEvaluationConfig.parse_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_dict)
      * [`SimpleEvaluationConfig.parse_int()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_int)
      * [`SimpleEvaluationConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_mutually_exclusive_fields)
      * [`SimpleEvaluationConfig.parse_number()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_number)
      * [`SimpleEvaluationConfig.parse_object()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_object)
      * [`SimpleEvaluationConfig.parse_object_array()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_object_array)
      * [`SimpleEvaluationConfig.parse_object_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_object_dict)
      * [`SimpleEvaluationConfig.parse_path()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_path)
      * [`SimpleEvaluationConfig.parse_raw()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_raw)
      * [`SimpleEvaluationConfig.parse_string()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.parse_string)
      * [`SimpleEvaluationConfig.run_cls`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.run_cls)
      * [`SimpleEvaluationConfig.serialize()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.serialize)
      * [`SimpleEvaluationConfig.to_str()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.to_str)
      * [`SimpleEvaluationConfig.type`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.type)
      * [`SimpleEvaluationConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.validate_all_or_nothing_fields)
      * [`SimpleEvaluationConfig.write_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluationConfig.write_json)
    * [`SimpleEvaluation`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation)
      * [`SimpleEvaluation.evaluate_samples()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.evaluate_samples)
      * [`SimpleEvaluation.add_fields_to_sidebar_group()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.add_fields_to_sidebar_group)
      * [`SimpleEvaluation.cleanup()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.cleanup)
      * [`SimpleEvaluation.cleanup_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.cleanup_custom_metrics)
      * [`SimpleEvaluation.compute_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.compute_custom_metrics)
      * [`SimpleEvaluation.delete_run()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.delete_run)
      * [`SimpleEvaluation.delete_runs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.delete_runs)
      * [`SimpleEvaluation.ensure_requirements()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.ensure_requirements)
      * [`SimpleEvaluation.ensure_usage_requirements()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.ensure_usage_requirements)
      * [`SimpleEvaluation.from_config()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.from_config)
      * [`SimpleEvaluation.from_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.from_dict)
      * [`SimpleEvaluation.from_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.from_json)
      * [`SimpleEvaluation.from_kwargs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.from_kwargs)
      * [`SimpleEvaluation.get_custom_metric_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.get_custom_metric_fields)
      * [`SimpleEvaluation.get_fields()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.get_fields)
      * [`SimpleEvaluation.get_run_info()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.get_run_info)
      * [`SimpleEvaluation.has_cached_run_results()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.has_cached_run_results)
      * [`SimpleEvaluation.list_runs()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.list_runs)
      * [`SimpleEvaluation.load_run_results()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.load_run_results)
      * [`SimpleEvaluation.load_run_view()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.load_run_view)
      * [`SimpleEvaluation.parse()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.parse)
      * [`SimpleEvaluation.register_run()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.register_run)
      * [`SimpleEvaluation.register_samples()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.register_samples)
      * [`SimpleEvaluation.rename()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.rename)
      * [`SimpleEvaluation.rename_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.rename_custom_metrics)
      * [`SimpleEvaluation.run_info_cls()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.run_info_cls)
      * [`SimpleEvaluation.save_run_info()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.save_run_info)
      * [`SimpleEvaluation.save_run_results()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.save_run_results)
      * [`SimpleEvaluation.update_run_config()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.update_run_config)
      * [`SimpleEvaluation.update_run_key()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.update_run_key)
      * [`SimpleEvaluation.validate()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.validate)
      * [`SimpleEvaluation.validate_run()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SimpleEvaluation.validate_run)
    * [`SegmentationResults`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults)
      * [`SegmentationResults.dice_score()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.dice_score)
      * [`SegmentationResults.add_custom_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.add_custom_metrics)
      * [`SegmentationResults.attributes()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.attributes)
      * [`SegmentationResults.backend`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.backend)
      * [`SegmentationResults.base_results_cls()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.base_results_cls)
      * [`SegmentationResults.clear_subset()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.clear_subset)
      * [`SegmentationResults.cls`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.cls)
      * [`SegmentationResults.config`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.config)
      * [`SegmentationResults.confusion_matrix()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.confusion_matrix)
      * [`SegmentationResults.copy()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.copy)
      * [`SegmentationResults.custom_attributes()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.custom_attributes)
      * [`SegmentationResults.from_dict()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.from_dict)
      * [`SegmentationResults.from_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.from_json)
      * [`SegmentationResults.from_str()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.from_str)
      * [`SegmentationResults.get_class_name()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.get_class_name)
      * [`SegmentationResults.has_subset`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.has_subset)
      * [`SegmentationResults.key`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.key)
      * [`SegmentationResults.metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.metrics)
      * [`SegmentationResults.plot_confusion_matrix()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.plot_confusion_matrix)
      * [`SegmentationResults.print_metrics()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.print_metrics)
      * [`SegmentationResults.print_report()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.print_report)
      * [`SegmentationResults.report()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.report)
      * [`SegmentationResults.samples`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.samples)
      * [`SegmentationResults.save()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.save)
      * [`SegmentationResults.save_config()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.save_config)
      * [`SegmentationResults.serialize()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.serialize)
      * [`SegmentationResults.to_str()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.to_str)
      * [`SegmentationResults.use_subset()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.use_subset)
      * [`SegmentationResults.write_json()`](api__fiftyone.utils.eval.segmentation.md#fiftyone.utils.eval.segmentation.SegmentationResults.write_json)



## Module contents#

Evaluation utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_subset_view`(sample_collection,Â gt_field,Â ...) | Returns the view into the given collection specified by the subset definition.  
---|---  
`evaluate_classifications`(samples,Â pred_field) | Evaluates the classification predictions in the given collection with respect to the specified ground truth labels.  
`evaluate_detections`(samples,Â pred_field[,Â ...]) | Evaluates the predicted detections in the given samples with respect to the specified ground truth detections.  
`evaluate_regressions`(samples,Â pred_field[,Â ...]) | Evaluates the regression predictions in the given collection with respect to the specified ground truth values.  
`evaluate_segmentations`(samples,Â pred_field) | Evaluates the specified semantic segmentation masks in the given collection with respect to the specified ground truth masks.  
  
**Classes:**

`ClassificationEvaluationConfig`(pred_field,Â ...) | Base class for configuring `ClassificationEvaluation` instances.  
---|---  
`ClassificationResults`(samples,Â config,Â ...) | Class that stores the results of a classification evaluation.  
`DetectionEvaluationConfig`(pred_field,Â gt_field) | Base class for configuring `DetectionEvaluation` instances.  
`DetectionResults`(samples,Â config,Â eval_key,Â ...) | Class that stores the results of a detection evaluation.  
`RegressionEvaluationConfig`(pred_field,Â gt_field) | Base class for configuring `RegressionEvaluation` instances.  
`RegressionResults`(samples,Â config,Â eval_key,Â ...) | Class that stores the results of a regression evaluation.  
`SegmentationEvaluationConfig`(pred_field,Â ...) | Base class for configuring `SegmentationEvaluation` instances.  
`SegmentationResults`(samples,Â config,Â ...[,Â ...]) | Class that stores the results of a segmentation evaluation.  
  
fiftyone.utils.eval.get_subset_view(_sample_collection_ , _gt_field_ , _subset_def_)#
    

Returns the view into the given collection specified by the subset definition.

Example subset definitions:
    
    
    # Subset defined by a saved view
    subset_def = {
        "type": "view",
        "view": "night_view",
    }
    
    # Subset defined by a sample field value
    subset_def = {
        "type": "sample",
        "field": "timeofday",
        "value": "night",
    }
    
    # Subset defined by a sample field expression
    subset_def = {
        "type": "field",
        "expr": F("uniqueness") > 0.75,
    }
    
    # Subset defined by a label attribute value
    subset_def = {
        "type": "attribute",
        "field": "type",
        "value": "sedan",
    }
    
    # Subset defined by a label expression
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    subset_def = {
        "type": "attribute",
        "expr": (0.05 <= bbox_area) & (bbox_area <= 0.5),
    }
    
    # Compound subset defined by a sample field value + sample expression
    subset_def = [
        {
            "type": "field",
            "field": "timeofday",
            "value": "night",
        },
        {
            "type": "field",
            "expr": F("uniqueness") > 0.75,
        },
    ]
    
    # Compound subset defined by a sample field value + label expression
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    subset_def = [
        {
            "type": "field",
            "field": "timeofday",
            "value": "night",
        },
        {
            "type": "attribute",
            "expr": (0.05 <= bbox_area) & (bbox_area <= 0.5),
        },
    ]
    
    # Compound subset defined by a saved view + label attribute value
    subset_def = [
        {
            "type": "view",
            "view": "night_view",
        },
        {
            "type": "attribute",
            "field": "type",
            "value": "sedan",
        }
    ]
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **gt_field** â the ground truth field

  * **subset_def** â a dict or list of dicts defining the subset. See above for syntax and examples



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

fiftyone.utils.eval.evaluate_classifications(_samples_ , _pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _classes =None_, _missing =None_, _method =None_, _custom_metrics =None_, _progress =None_, _** kwargs_)#
    

Evaluates the classification predictions in the given collection with respect to the specified ground truth labels.

By default, this method simply compares the ground truth and prediction for each sample, but other strategies such as binary evaluation and top-k matching can be configured via the `method` parameter.

You can customize the evaluation method by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"simple"`: `SimpleEvaluationConfig`

  * `"top-k"`: `TopKEvaluationConfig`

  * `"binary"`: `BinaryEvaluationConfig`




If an `eval_key` is specified, then this method will record some statistics on each sample:

  * When evaluating sample-level fields, an `eval_key` field will be populated on each sample recording whether that sampleâs prediction is correct.

  * When evaluating frame-level fields, an `eval_key` field will be populated on each frame recording whether that frameâs prediction is correct. In addition, an `eval_key` field will be populated on each sample that records the average accuracy of the frame predictions of the sample.




Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances

  * **eval_key** (_None_) â an evaluation key to use to refer to this evaluation

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used

  * **missing** (_None_) â a missing label string. Any None-valued labels are given this label for results purposes

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.classification_backends.keys()` and the default is `fo.evaluation_config.default_classification_backend`

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the `ClassificationEvaluationConfig` being used



Returns:
    

a `ClassificationResults`

class fiftyone.utils.eval.ClassificationEvaluationConfig(_pred_field_ , _gt_field_ , _custom_metrics =None_, _** kwargs_)#
    

Bases: [`BaseEvaluationMethodConfig`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig "fiftyone.utils.eval.base.BaseEvaluationMethodConfig")

Base class for configuring `ClassificationEvaluation` instances.

Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances

  * **gt_field** â the name of the field containing the ground truth [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts




**Attributes:**

`type` | The type of run.  
---|---  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`method` | The name of the method.  
`run_cls` | The `BaseRun` class associated with this config.  
  
**Methods:**

`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
---|---  
`base_config_cls`(type) | Returns the config class for the given run type.  
`build`() | Builds the `BaseRun` instance associated with this config.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_credentials`(**kwargs) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property type#
    

The type of run.

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

static base_config_cls(_type_)#
    

Returns the config class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunConfig` subclass

build()#
    

Builds the `BaseRun` instance associated with this config.

Returns:
    

a `BaseRun` instance

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property cls#
    

The fully-qualified name of this `BaseRunConfig` class.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

classmethod from_dict(_d_)#
    

Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `BaseRunConfig`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

load_credentials(_** kwargs_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

property method#
    

The name of the method.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

property run_cls#
    

The `BaseRun` class associated with this config.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.eval.ClassificationResults(_samples_ , _config_ , _eval_key_ , _ytrue_ , _ypred_ , _confs =None_, _weights =None_, _ytrue_ids =None_, _ypred_ids =None_, _classes =None_, _missing =None_, _custom_metrics =None_, _backend =None_)#
    

Bases: [`BaseClassificationResults`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults "fiftyone.utils.eval.base.BaseClassificationResults")

Class that stores the results of a classification evaluation.

Parameters:
    

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") used

  * **config** â the `ClassificationEvaluationConfig` used

  * **eval_key** â the evaluation key

  * **ytrue** â a list of ground truth labels

  * **ypred** â a list of predicted labels

  * **confs** (_None_) â an optional list of confidences for the predictions

  * **weights** (_None_) â an optional list of sample weights

  * **ytrue_ids** (_None_) â a list of IDs for the ground truth labels

  * **ypred_ids** (_None_) â a list of IDs for the predicted labels

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used

  * **missing** (_None_) â a missing label string. Any None-valued labels are given this label for evaluation purposes

  * **custom_metrics** (_None_) â an optional dict of custom metrics

  * **backend** (_None_) â a `ClassificationEvaluation` backend




**Methods:**

`add_custom_metrics`(custom_metrics[,Â overwrite]) | Computes the given custom metrics and adds them to these results.  
---|---  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`clear_subset`() | Clears the subset set by `use_subset()`, if any.  
`confusion_matrix`([classes,Â include_other,Â ...]) | Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`metrics`([classes,Â average,Â beta]) | Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.  
`plot_confusion_matrix`([classes,Â ...]) | Plots a confusion matrix for the evaluation results.  
`print_metrics`([classes,Â average,Â beta,Â digits]) | Prints the metrics computed via `metrics()`.  
`print_report`([classes,Â digits]) | Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`report`([classes]) | Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`use_subset`(subset_def) | Restricts the evaluation results to the specified subset.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`has_subset` | Whether these results are currently restricted to a subset via `use_subset()`.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
add_custom_metrics(_custom_metrics_ , _overwrite =True_)#
    

Computes the given custom metrics and adds them to these results.

Parameters:
    

  * **custom_metrics** â a list of custom metrics to compute or a dict mapping metric names to kwargs dicts

  * **overwrite** (_True_) â whether to recompute any custom metrics that have already been applied




attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

property backend#
    

The `BaseRun` for these results.

static base_results_cls(_type_)#
    

Returns the results class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunResults` subclass

clear_subset()#
    

Clears the subset set by `use_subset()`, if any.

Subsequent operations will be performed on the full results.

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

confusion_matrix(_classes =None_, _include_other =False_, _include_missing =False_)#
    

Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").

The rows of the confusion matrix represent ground truth and the columns represent predictions.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_False_) â whether to include an extra row/column at the end of the matrix for labels that do not appear in `classes`. Only applicable if `classes` are provided

  * **include_missing** (_False_) â whether to include a row/column at the end of the matrix for unmatched labels. Only applicable if `self.missing` does not already appear in `classes`. If both âotherâ and âmissingâ rows/columns are requested, this one is last



Returns:
    

a `num_classes x num_classes` confusion matrix

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_dict(_d_ , _samples_ , _config_ , _key_)#
    

Builds a `BaseRunResults` from a JSON dict representation of it.

Parameters:
    

  * **d** â a JSON dict

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for the run

  * **config** â the `BaseRunConfig` for the run

  * **key** â the run key



Returns:
    

a `BaseRunResults`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

property has_subset#
    

Whether these results are currently restricted to a subset via `use_subset()`.

property key#
    

The run key for these results.

metrics(_classes =None_, _average ='micro'_, _beta =1.0_)#
    

Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.

See [`sklearn.metrics.precision_recall_fscore_support()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "\(in scikit-learn v1.9\)") for details.

Also includes any custom metrics from `custom_metrics`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use



Returns:
    

a dict

plot_confusion_matrix(_classes =None_, _include_other =None_, _include_missing =None_, _other_label ='(other)'_, _backend ='plotly'_, _** kwargs_)#
    

Plots a confusion matrix for the evaluation results.

If you are working in a notebook environment with the default plotly backend, this method returns an interactive [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap") that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected cells in the confusion matrix.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_None_) â 

whether to include a row/column for examples whose label is in `classes` but are matched to labels that do not appear in `classes`. Only applicable if `classes` are provided. The supported values are:

    * None (default): only include a row/column for other labels if there are any

    * True: do include a row/column for other labels

    * False: do not include a row/column for other labels

  * **include_missing** (_None_) â 

whether to include a row/column for missing ground truth/predictions in the confusion matrix. The supported values are:

    * None (default): only include a row/column for missing labels if there are any

    * True: do include a row/column for missing labels

    * False: do not include a row/column for missing labels

  * **other_label** (_"__(__other_ _)__"_) â the label to use for âotherâ predictions

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix "fiftyone.core.plots.plotly.plot_confusion_matrix")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix "fiftyone.core.plots.matplotlib.plot_confusion_matrix")



Returns:
    

  * a [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap"), if the plotly backend is used

  * a matplotlib figure, otherwise




Return type:
    

one of the following

print_metrics(_classes =None_, _average ='micro'_, _beta =1.0_, _digits =2_)#
    

Prints the metrics computed via `metrics()`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use

  * **digits** (_2_) â the number of digits of precision to print




print_report(_classes =None_, _digits =2_)#
    

Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the report

  * **digits** (_2_) â the number of digits of precision to print




report(_classes =None_)#
    

Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

**classes** (_None_) â an optional list of classes to include in the report

Returns:
    

a dict

property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.

save()#
    

Saves the results to the database.

save_config()#
    

Saves these results config to the database.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

use_subset(_subset_def_)#
    

Restricts the evaluation results to the specified subset.

Subsequent calls to supported methods on this instance will only contain results from the specified subset rather than the full results.

Use `clear_subset()` to reset to the full results. Or, equivalently, use the context manager interface as demonstrated below to automatically reset the results when the context exits.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.random as four
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    four.random_split(dataset, {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.1})
    
    results = dataset.evaluate_detections(
        "predictions",
        gt_field="ground_truth",
        eval_key="eval",
    )
    
    counts = dataset.count_values("ground_truth.detections.label")
    classes = sorted(counts, key=counts.get, reverse=True)[:5]
    
    # Full results
    results.print_report(classes=classes)
    
    # Sunny samples
    subset_def = dict(type="field", field="tags", value="sunny")
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    
    # Small objects
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    small_objects = bbox_area <= 0.05
    subset_def = dict(type="attribute", expr=small_objects)
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    

Parameters:
    

**subset_def** â 

the subset definition, which can be:

  * a dict or list of dicts defining the subset. See above for examples and see `get_subset_view()` for full syntax

  * a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") defining the subset




Returns:
    

self

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




fiftyone.utils.eval.evaluate_detections(_samples_ , _pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _classes =None_, _missing =None_, _method =None_, _iou =0.5_, _use_masks =False_, _use_boxes =False_, _classwise =True_, _dynamic =True_, _custom_metrics =None_, _progress =None_, _** kwargs_)#
    

Evaluates the predicted detections in the given samples with respect to the specified ground truth detections.

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

  * True positive (TP), false positive (FP), and false negative (FN) counts for each sample are saved in top-level fields of each sample:
        
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
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections")

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections")

  * **eval_key** (_None_) â an evaluation key to use to refer to this evaluation

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used

  * **missing** (_None_) â a missing label string. Any unmatched objects are given this label for results purposes

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.detection_backends.keys()` and the default is `fo.evaluation_config.default_detection_backend`

  * **iou** (_0.50_) â the IoU threshold to use to determine matches

  * **use_masks** (_False_) â whether to compute IoUs using the instances masks in the `mask` attribute of the provided objects, which must be [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") instances

  * **use_boxes** (_False_) â whether to compute IoUs using the bounding boxes of the provided [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") instances rather than using their actual geometries

  * **classwise** (_True_) â whether to only match objects with the same class label (True) or allow matches between classes (False)

  * **dynamic** (_True_) â whether to declare the dynamic object-level attributes that are populated on the datasetâs schema

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the `DetectionEvaluationConfig` being used



Returns:
    

a `DetectionResults`

class fiftyone.utils.eval.DetectionEvaluationConfig(_pred_field_ , _gt_field_ , _iou =None_, _classwise =None_, _custom_metrics =None_, _** kwargs_)#
    

Bases: [`BaseEvaluationMethodConfig`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig "fiftyone.utils.eval.base.BaseEvaluationMethodConfig")

Base class for configuring `DetectionEvaluation` instances.

Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **gt_field** â the name of the field containing the ground truth [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **iou** (_None_) â the IoU threshold to use to determine matches

  * **classwise** (_None_) â whether to only match objects with the same class label (True) or allow matches between classes (False)

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts




**Attributes:**

`type` | The type of run.  
---|---  
`requires_additional_fields` | Whether fields besides `pred_field` and `gt_field` are required in order to perform evaluation.  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`method` | The name of the method.  
`run_cls` | The `BaseRun` class associated with this config.  
  
**Methods:**

`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
---|---  
`base_config_cls`(type) | Returns the config class for the given run type.  
`build`() | Builds the `BaseRun` instance associated with this config.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_credentials`(**kwargs) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property type#
    

The type of run.

property requires_additional_fields#
    

Whether fields besides `pred_field` and `gt_field` are required in order to perform evaluation.

If True then the entire samples will be loaded rather than using [`select_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_fields "fiftyone.core.collections.SampleCollection.select_fields") to optimize.

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

static base_config_cls(_type_)#
    

Returns the config class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunConfig` subclass

build()#
    

Builds the `BaseRun` instance associated with this config.

Returns:
    

a `BaseRun` instance

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property cls#
    

The fully-qualified name of this `BaseRunConfig` class.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

classmethod from_dict(_d_)#
    

Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `BaseRunConfig`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

load_credentials(_** kwargs_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

property method#
    

The name of the method.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

property run_cls#
    

The `BaseRun` class associated with this config.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.eval.DetectionResults(_samples_ , _config_ , _eval_key_ , _matches_ , _classes =None_, _missing =None_, _custom_metrics =None_, _backend =None_)#
    

Bases: [`BaseClassificationResults`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults "fiftyone.utils.eval.base.BaseClassificationResults")

Class that stores the results of a detection evaluation.

Parameters:
    

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") used

  * **config** â the `DetectionEvaluationConfig` used

  * **eval_key** â the evaluation key

  * **matches** â a list of `(gt_label, pred_label, iou, pred_confidence, gt_id, pred_id)` matches. Either label can be `None` to indicate an unmatched object

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used

  * **missing** (_None_) â a missing label string. Any unmatched objects are given this label for evaluation purposes

  * **custom_metrics** (_None_) â an optional dict of custom metrics

  * **backend** (_None_) â a `DetectionEvaluation` backend




**Methods:**

`add_custom_metrics`(custom_metrics[,Â overwrite]) | Computes the given custom metrics and adds them to these results.  
---|---  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`clear_subset`() | Clears the subset set by `use_subset()`, if any.  
`confusion_matrix`([classes,Â include_other,Â ...]) | Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`metrics`([classes,Â average,Â beta]) | Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.  
`plot_confusion_matrix`([classes,Â ...]) | Plots a confusion matrix for the evaluation results.  
`print_metrics`([classes,Â average,Â beta,Â digits]) | Prints the metrics computed via `metrics()`.  
`print_report`([classes,Â digits]) | Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`report`([classes]) | Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`use_subset`(subset_def) | Restricts the evaluation results to the specified subset.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`has_subset` | Whether these results are currently restricted to a subset via `use_subset()`.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
add_custom_metrics(_custom_metrics_ , _overwrite =True_)#
    

Computes the given custom metrics and adds them to these results.

Parameters:
    

  * **custom_metrics** â a list of custom metrics to compute or a dict mapping metric names to kwargs dicts

  * **overwrite** (_True_) â whether to recompute any custom metrics that have already been applied




attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

property backend#
    

The `BaseRun` for these results.

static base_results_cls(_type_)#
    

Returns the results class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunResults` subclass

clear_subset()#
    

Clears the subset set by `use_subset()`, if any.

Subsequent operations will be performed on the full results.

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

confusion_matrix(_classes =None_, _include_other =False_, _include_missing =False_)#
    

Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").

The rows of the confusion matrix represent ground truth and the columns represent predictions.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_False_) â whether to include an extra row/column at the end of the matrix for labels that do not appear in `classes`. Only applicable if `classes` are provided

  * **include_missing** (_False_) â whether to include a row/column at the end of the matrix for unmatched labels. Only applicable if `self.missing` does not already appear in `classes`. If both âotherâ and âmissingâ rows/columns are requested, this one is last



Returns:
    

a `num_classes x num_classes` confusion matrix

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_dict(_d_ , _samples_ , _config_ , _key_)#
    

Builds a `BaseRunResults` from a JSON dict representation of it.

Parameters:
    

  * **d** â a JSON dict

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for the run

  * **config** â the `BaseRunConfig` for the run

  * **key** â the run key



Returns:
    

a `BaseRunResults`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

property has_subset#
    

Whether these results are currently restricted to a subset via `use_subset()`.

property key#
    

The run key for these results.

metrics(_classes =None_, _average ='micro'_, _beta =1.0_)#
    

Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.

See [`sklearn.metrics.precision_recall_fscore_support()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "\(in scikit-learn v1.9\)") for details.

Also includes any custom metrics from `custom_metrics`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use



Returns:
    

a dict

plot_confusion_matrix(_classes =None_, _include_other =None_, _include_missing =None_, _other_label ='(other)'_, _backend ='plotly'_, _** kwargs_)#
    

Plots a confusion matrix for the evaluation results.

If you are working in a notebook environment with the default plotly backend, this method returns an interactive [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap") that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected cells in the confusion matrix.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_None_) â 

whether to include a row/column for examples whose label is in `classes` but are matched to labels that do not appear in `classes`. Only applicable if `classes` are provided. The supported values are:

    * None (default): only include a row/column for other labels if there are any

    * True: do include a row/column for other labels

    * False: do not include a row/column for other labels

  * **include_missing** (_None_) â 

whether to include a row/column for missing ground truth/predictions in the confusion matrix. The supported values are:

    * None (default): only include a row/column for missing labels if there are any

    * True: do include a row/column for missing labels

    * False: do not include a row/column for missing labels

  * **other_label** (_"__(__other_ _)__"_) â the label to use for âotherâ predictions

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix "fiftyone.core.plots.plotly.plot_confusion_matrix")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix "fiftyone.core.plots.matplotlib.plot_confusion_matrix")



Returns:
    

  * a [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap"), if the plotly backend is used

  * a matplotlib figure, otherwise




Return type:
    

one of the following

print_metrics(_classes =None_, _average ='micro'_, _beta =1.0_, _digits =2_)#
    

Prints the metrics computed via `metrics()`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use

  * **digits** (_2_) â the number of digits of precision to print




print_report(_classes =None_, _digits =2_)#
    

Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the report

  * **digits** (_2_) â the number of digits of precision to print




report(_classes =None_)#
    

Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

**classes** (_None_) â an optional list of classes to include in the report

Returns:
    

a dict

property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.

save()#
    

Saves the results to the database.

save_config()#
    

Saves these results config to the database.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

use_subset(_subset_def_)#
    

Restricts the evaluation results to the specified subset.

Subsequent calls to supported methods on this instance will only contain results from the specified subset rather than the full results.

Use `clear_subset()` to reset to the full results. Or, equivalently, use the context manager interface as demonstrated below to automatically reset the results when the context exits.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.random as four
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    four.random_split(dataset, {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.1})
    
    results = dataset.evaluate_detections(
        "predictions",
        gt_field="ground_truth",
        eval_key="eval",
    )
    
    counts = dataset.count_values("ground_truth.detections.label")
    classes = sorted(counts, key=counts.get, reverse=True)[:5]
    
    # Full results
    results.print_report(classes=classes)
    
    # Sunny samples
    subset_def = dict(type="field", field="tags", value="sunny")
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    
    # Small objects
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    small_objects = bbox_area <= 0.05
    subset_def = dict(type="attribute", expr=small_objects)
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    

Parameters:
    

**subset_def** â 

the subset definition, which can be:

  * a dict or list of dicts defining the subset. See above for examples and see `get_subset_view()` for full syntax

  * a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") defining the subset




Returns:
    

self

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




fiftyone.utils.eval.evaluate_regressions(_samples_ , _pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _missing =None_, _method =None_, _custom_metrics =None_, _progress =None_, _** kwargs_)#
    

Evaluates the regression predictions in the given collection with respect to the specified ground truth values.

You can customize the evaluation method by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"simple"`: `SimpleEvaluationConfig`




If an `eval_key` is specified, then this method will record some statistics on each sample:

  * When evaluating sample-level fields, an `eval_key` field will be populated on each sample recording the error of that sampleâs prediction.

  * When evaluating frame-level fields, an `eval_key` field will be populated on each frame recording the error of that frameâs prediction. In addition, an `eval_key` field will be populated on each sample that records the average error of the frame predictions of the sample.




Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") instances

  * **eval_key** (_None_) â a string key to use to refer to this evaluation

  * **missing** (_None_) â a missing value. Any None-valued regressions are given this value for results purposes

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.regression_backends.keys()` and the default is `fo.evaluation_config.default_regression_backend`

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the `RegressionEvaluationConfig` being used



Returns:
    

a `RegressionResults`

class fiftyone.utils.eval.RegressionEvaluationConfig(_pred_field_ , _gt_field_ , _custom_metrics =None_, _** kwargs_)#
    

Bases: [`BaseEvaluationMethodConfig`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig "fiftyone.utils.eval.base.BaseEvaluationMethodConfig")

Base class for configuring `RegressionEvaluation` instances.

Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") instances

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts




**Attributes:**

`type` | The type of run.  
---|---  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`method` | The name of the method.  
`run_cls` | The `BaseRun` class associated with this config.  
  
**Methods:**

`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
---|---  
`base_config_cls`(type) | Returns the config class for the given run type.  
`build`() | Builds the `BaseRun` instance associated with this config.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_credentials`(**kwargs) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property type#
    

The type of run.

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

static base_config_cls(_type_)#
    

Returns the config class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunConfig` subclass

build()#
    

Builds the `BaseRun` instance associated with this config.

Returns:
    

a `BaseRun` instance

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property cls#
    

The fully-qualified name of this `BaseRunConfig` class.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

classmethod from_dict(_d_)#
    

Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `BaseRunConfig`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

load_credentials(_** kwargs_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

property method#
    

The name of the method.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

property run_cls#
    

The `BaseRun` class associated with this config.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.eval.RegressionResults(_samples_ , _config_ , _eval_key_ , _ytrue_ , _ypred_ , _confs =None_, _ids =None_, _missing =None_, _custom_metrics =None_, _backend =None_)#
    

Bases: [`BaseEvaluationResults`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults "fiftyone.utils.eval.base.BaseEvaluationResults")

Class that stores the results of a regression evaluation.

Parameters:
    

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") used

  * **config** â the `RegressionEvaluationConfig` used

  * **eval_key** (_None_) â the evaluation key

  * **ytrue** â a list of ground truth values

  * **ypred** â a list of predicted values

  * **confs** (_None_) â an optional list of confidences for the predictions

  * **eval_key** â the evaluation key of the evaluation

  * **gt_field** (_None_) â the name of the ground truth field

  * **pred_field** (_None_) â the name of the predictions field

  * **ids** (_None_) â a list of sample or frame IDs corresponding to the regressions

  * **missing** (_None_) â a missing value. Any None-valued regressions are given this value for results purposes

  * **custom_metrics** (_None_) â an optional dict of custom metrics

  * **backend** (_None_) â a `RegressionEvaluation` backend




**Methods:**

`metrics`([weights]) | Computes various popular regression metrics for the results.  
---|---  
`print_metrics`([weights,Â digits]) | Prints the metrics computed via `metrics()`.  
`plot_results`([labels,Â sizes,Â backend]) | Plots the regression results.  
`add_custom_metrics`(custom_metrics[,Â overwrite]) | Computes the given custom metrics and adds them to these results.  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
metrics(_weights =None_)#
    

Computes various popular regression metrics for the results.

The computed metrics are:

  * Mean squared error: [`sklearn.metrics.mean_squared_error()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "\(in scikit-learn v1.9\)")

  * Root mean squared error: [`sklearn.metrics.mean_squared_error()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "\(in scikit-learn v1.9\)")

  * Mean absolute error: [`sklearn.metrics.mean_absolute_error()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "\(in scikit-learn v1.9\)")

  * Median absolute error: [`sklearn.metrics.median_absolute_error()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "\(in scikit-learn v1.9\)")

  * R^2 score: [`sklearn.metrics.r2_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "\(in scikit-learn v1.9\)")

  * Explained variance score: [`sklearn.metrics.explained_variance_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "\(in scikit-learn v1.9\)")

  * Max error: [`sklearn.metrics.max_error()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "\(in scikit-learn v1.9\)")

  * Support: the number of examples




Also includes any custom metrics from `custom_metrics`.

Parameters:
    

**weights** (_None_) â an optional list of weights for each example

Returns:
    

a dict

print_metrics(_weights =None_, _digits =2_)#
    

Prints the metrics computed via `metrics()`.

Parameters:
    

  * **weights** (_None_) â an optional list of weights for each example

  * **digits** (_2_) â the number of digits of precision to print




plot_results(_labels =None_, _sizes =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots the regression results.

You can use the `labels` parameters to define a coloring for the points, and you can use the `sizes` parameter to scale the sizes of the points.

You can attach plots generated by this method to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot.

Parameters:
    

  * **labels** (_None_) â 

data to use to color the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of from which to extract numeric or string values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to extract via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * a list or array-like of numeric or string values (or lists of lists for frame-level regressions)

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric values to extract via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * a list or array-like of numeric values (or lists of lists for frame-level regressions)

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_regressions()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_regressions "fiftyone.core.plots.plotly.plot_regressions")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_regressions()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_regressions "fiftyone.core.plots.matplotlib.plot_regressions")



Returns:
    

an [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot")

add_custom_metrics(_custom_metrics_ , _overwrite =True_)#
    

Computes the given custom metrics and adds them to these results.

Parameters:
    

  * **custom_metrics** â a list of custom metrics to compute or a dict mapping metric names to kwargs dicts

  * **overwrite** (_True_) â whether to recompute any custom metrics that have already been applied




attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

property backend#
    

The `BaseRun` for these results.

static base_results_cls(_type_)#
    

Returns the results class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunResults` subclass

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_dict(_d_ , _samples_ , _config_ , _key_)#
    

Builds a `BaseRunResults` from a JSON dict representation of it.

Parameters:
    

  * **d** â a JSON dict

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for the run

  * **config** â the `BaseRunConfig` for the run

  * **key** â the run key



Returns:
    

a `BaseRunResults`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

property key#
    

The run key for these results.

property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.

save()#
    

Saves the results to the database.

save_config()#
    

Saves these results config to the database.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




fiftyone.utils.eval.evaluate_segmentations(_samples_ , _pred_field_ , _gt_field ='ground_truth'_, _eval_key =None_, _mask_targets =None_, _method =None_, _custom_metrics =None_, _progress =None_, _** kwargs_)#
    

Evaluates the specified semantic segmentation masks in the given collection with respect to the specified ground truth masks.

If the size of a predicted mask does not match the ground truth mask, it is resized to match the ground truth.

By default, this method simply performs pixelwise evaluation of the full masks, but other strategies such as boundary-only evaluation can be configured by passing additional parameters for the methodâs config class as `kwargs`.

The natively provided `method` values and their associated configs are:

  * `"simple"`: `SimpleEvaluationConfig`




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
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") instances

  * **gt_field** (_"ground_truth"_) â the name of the field containing the ground truth [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") instances

  * **eval_key** (_None_) â an evaluation key to use to refer to this evaluation

  * **mask_targets** (_None_) â a dict mapping pixel values or RGB hex strings to labels. If not provided, the observed values are used as labels

  * **method** (_None_) â a string specifying the evaluation method to use. The supported values are `fo.evaluation_config.segmentation_backends.keys()` and the default is `fo.evaluation_config.default_segmentation_backend`

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for the constructor of the `SegmentationEvaluationConfig` being used



Returns:
    

a `SegmentationResults`

class fiftyone.utils.eval.SegmentationEvaluationConfig(_pred_field_ , _gt_field_ , _compute_dice =False_, _custom_metrics =None_, _** kwargs_)#
    

Bases: [`BaseEvaluationMethodConfig`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationMethodConfig "fiftyone.utils.eval.base.BaseEvaluationMethodConfig")

Base class for configuring `SegmentationEvaluation` instances.

Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") instances

  * **gt_field** â the name of the field containing the ground truth [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") instances

  * **compute_dice** (_False_) â whether to compute the Dice coefficient for each sample

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts




**Attributes:**

`type` | The type of run.  
---|---  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`method` | The name of the method.  
`run_cls` | The `BaseRun` class associated with this config.  
  
**Methods:**

`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
---|---  
`base_config_cls`(type) | Returns the config class for the given run type.  
`build`() | Builds the `BaseRun` instance associated with this config.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_credentials`(**kwargs) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property type#
    

The type of run.

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

static base_config_cls(_type_)#
    

Returns the config class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunConfig` subclass

build()#
    

Builds the `BaseRun` instance associated with this config.

Returns:
    

a `BaseRun` instance

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property cls#
    

The fully-qualified name of this `BaseRunConfig` class.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

classmethod from_dict(_d_)#
    

Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `BaseRunConfig`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

load_credentials(_** kwargs_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

property method#
    

The name of the method.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

property run_cls#
    

The `BaseRun` class associated with this config.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.eval.SegmentationResults(_samples_ , _config_ , _eval_key_ , _pixel_confusion_matrix_ , _classes_ , _matches =None_, _missing =None_, _custom_metrics =None_, _backend =None_)#
    

Bases: [`BaseClassificationResults`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults "fiftyone.utils.eval.base.BaseClassificationResults")

Class that stores the results of a segmentation evaluation.

Parameters:
    

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") used

  * **config** â the `SegmentationEvaluationConfig` used

  * **eval_key** â the evaluation key

  * **pixel_confusion_matrix** â a pixel value confusion matrix

  * **classes** â a list of class labels corresponding to the confusion matrix

  * **matches** (_None_) â a list of `(gt_label, pred_label, pixel_count, gt_id, pred_id)` matches

  * **missing** (_None_) â a missing (background) class

  * **custom_metrics** (_None_) â an optional dict of custom metrics

  * **backend** (_None_) â a `SegmentationEvaluation` backend




**Methods:**

`dice_score`() | Computes the Dice score across all samples in the evaluation.  
---|---  
`add_custom_metrics`(custom_metrics[,Â overwrite]) | Computes the given custom metrics and adds them to these results.  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`clear_subset`() | Clears the subset set by `use_subset()`, if any.  
`confusion_matrix`([classes,Â include_other,Â ...]) | Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`metrics`([classes,Â average,Â beta]) | Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.  
`plot_confusion_matrix`([classes,Â ...]) | Plots a confusion matrix for the evaluation results.  
`print_metrics`([classes,Â average,Â beta,Â digits]) | Prints the metrics computed via `metrics()`.  
`print_report`([classes,Â digits]) | Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`report`([classes]) | Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`use_subset`(subset_def) | Restricts the evaluation results to the specified subset.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`has_subset` | Whether these results are currently restricted to a subset via `use_subset()`.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
dice_score()#
    

Computes the Dice score across all samples in the evaluation.

Returns:
    

the Dice score in `[0, 1]`

add_custom_metrics(_custom_metrics_ , _overwrite =True_)#
    

Computes the given custom metrics and adds them to these results.

Parameters:
    

  * **custom_metrics** â a list of custom metrics to compute or a dict mapping metric names to kwargs dicts

  * **overwrite** (_True_) â whether to recompute any custom metrics that have already been applied




attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

property backend#
    

The `BaseRun` for these results.

static base_results_cls(_type_)#
    

Returns the results class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunResults` subclass

clear_subset()#
    

Clears the subset set by `use_subset()`, if any.

Subsequent operations will be performed on the full results.

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

confusion_matrix(_classes =None_, _include_other =False_, _include_missing =False_)#
    

Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").

The rows of the confusion matrix represent ground truth and the columns represent predictions.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_False_) â whether to include an extra row/column at the end of the matrix for labels that do not appear in `classes`. Only applicable if `classes` are provided

  * **include_missing** (_False_) â whether to include a row/column at the end of the matrix for unmatched labels. Only applicable if `self.missing` does not already appear in `classes`. If both âotherâ and âmissingâ rows/columns are requested, this one is last



Returns:
    

a `num_classes x num_classes` confusion matrix

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_dict(_d_ , _samples_ , _config_ , _key_)#
    

Builds a `BaseRunResults` from a JSON dict representation of it.

Parameters:
    

  * **d** â a JSON dict

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for the run

  * **config** â the `BaseRunConfig` for the run

  * **key** â the run key



Returns:
    

a `BaseRunResults`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

property has_subset#
    

Whether these results are currently restricted to a subset via `use_subset()`.

property key#
    

The run key for these results.

metrics(_classes =None_, _average ='micro'_, _beta =1.0_)#
    

Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.

See [`sklearn.metrics.precision_recall_fscore_support()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "\(in scikit-learn v1.9\)") for details.

Also includes any custom metrics from `custom_metrics`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use



Returns:
    

a dict

plot_confusion_matrix(_classes =None_, _include_other =None_, _include_missing =None_, _other_label ='(other)'_, _backend ='plotly'_, _** kwargs_)#
    

Plots a confusion matrix for the evaluation results.

If you are working in a notebook environment with the default plotly backend, this method returns an interactive [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap") that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected cells in the confusion matrix.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_None_) â 

whether to include a row/column for examples whose label is in `classes` but are matched to labels that do not appear in `classes`. Only applicable if `classes` are provided. The supported values are:

    * None (default): only include a row/column for other labels if there are any

    * True: do include a row/column for other labels

    * False: do not include a row/column for other labels

  * **include_missing** (_None_) â 

whether to include a row/column for missing ground truth/predictions in the confusion matrix. The supported values are:

    * None (default): only include a row/column for missing labels if there are any

    * True: do include a row/column for missing labels

    * False: do not include a row/column for missing labels

  * **other_label** (_"__(__other_ _)__"_) â the label to use for âotherâ predictions

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix "fiftyone.core.plots.plotly.plot_confusion_matrix")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix "fiftyone.core.plots.matplotlib.plot_confusion_matrix")



Returns:
    

  * a [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap"), if the plotly backend is used

  * a matplotlib figure, otherwise




Return type:
    

one of the following

print_metrics(_classes =None_, _average ='micro'_, _beta =1.0_, _digits =2_)#
    

Prints the metrics computed via `metrics()`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use

  * **digits** (_2_) â the number of digits of precision to print




print_report(_classes =None_, _digits =2_)#
    

Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the report

  * **digits** (_2_) â the number of digits of precision to print




report(_classes =None_)#
    

Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

**classes** (_None_) â an optional list of classes to include in the report

Returns:
    

a dict

property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.

save()#
    

Saves the results to the database.

save_config()#
    

Saves these results config to the database.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

use_subset(_subset_def_)#
    

Restricts the evaluation results to the specified subset.

Subsequent calls to supported methods on this instance will only contain results from the specified subset rather than the full results.

Use `clear_subset()` to reset to the full results. Or, equivalently, use the context manager interface as demonstrated below to automatically reset the results when the context exits.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.random as four
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    four.random_split(dataset, {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.1})
    
    results = dataset.evaluate_detections(
        "predictions",
        gt_field="ground_truth",
        eval_key="eval",
    )
    
    counts = dataset.count_values("ground_truth.detections.label")
    classes = sorted(counts, key=counts.get, reverse=True)[:5]
    
    # Full results
    results.print_report(classes=classes)
    
    # Sunny samples
    subset_def = dict(type="field", field="tags", value="sunny")
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    
    # Small objects
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    small_objects = bbox_area <= 0.05
    subset_def = dict(type="attribute", expr=small_objects)
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    

Parameters:
    

**subset_def** â 

the subset definition, which can be:

  * a dict or list of dicts defining the subset. See above for examples and see `get_subset_view()` for full syntax

  * a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") defining the subset




Returns:
    

self

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
