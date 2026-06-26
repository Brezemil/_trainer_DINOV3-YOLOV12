---
source_url: https://docs.voxel51.com/enterprise/query_performance.html
---

# Query Performance#

Query Performance is a builtin feature of the [FiftyOne Enterprise App](enterprise__app.md#enterprise-app) that leverages database indexes to optimize your queries on large-scale datasets.

## Optimizing Query Performance#

The Appâs sidebar is optimized to leverage database indexes whenever possible.

Fields that are indexed are indicated by lightning bolt icons next to their field/attribute names:

![app-query-performance](../_images/app-query-performance.gif)

The above GIF shows Query Performance in action on the train split of the [BDD100K dataset](dataset_zoo__datasets__bdd100k.md#dataset-zoo-bdd100k) with an index on the `detections.detections.label` field.

Note

When filtering by multiple fields, queries will be more efficient when your **first** filter is on an indexed field.

If you perform a filter that could benefit from an index and the query takes longer than a few seconds, youâll see a toast notification that nudges you to take the appropriate action to optimize the query:

![query-performance-toast](../_images/qp_toast.png)

Clicking âCreate Indexâ will open the Query Performance panel with a preconfigured recommendation of an index or summary field to create.

Note

Clicking âDismissâ will prevent this notification from appearing for the remainder of your current App session.

## Query Performance panel#

You can open the Query Performance panel manually either by clicking the â+â icon next to the Samples tab or by clicking the yellow lightning bolt in the top-right of the sidbar:

![query-performance-tooltip](../_images/qp_tooltip.png)

The first time you open the Query Performance panel, youâll see a welcome page:

![query-performance-home-tab](../_images/qp_home.png)

After youâve created at least one custom index or summary field for a dataset, youâll instead see a list of the indexes and summary fields that exist on the dataset:

![query-performance-tableview](../_images/qp_tableview.png)

### Creating indexes#

You can create a new index at any time by clicking the `Create Index` button in the top-right of the panel:

![query-performance-create-index](../_images/qp_create_index.png)

When you click âExecuteâ, the index will be initiated and youâll see âIn progressâ in the panelâs summary table.

After the index creation has finished, the field that you indexed will have a lightning bolt icon in the sidebar, and you should notice that expanding the fieldâs filter widget and performing queries on it will be noticeably faster.

Warning

For large datasets, index creation can have a significant impact on the performance of the database while the index is under construction.

We recommend indexing _only_ the specific fields that you wish to perform initial filters on, and we recommend consulting with your deployment admin before creating multiple indexes simultaneously.

You can also create and manage custom indexes [via the SDK](user_guide__app.md#app-optimizing-query-performance).

### Creating summary fields#

The Query Performance panel also allows you to create [summary fields](https://docs.voxel51.com/user_guide/using_datasets.html#summary-fields), which are sample-level fields that allow you to efficiently perform queries on large datasets where directly querying the underlying field is prohibitively slow due to the number of objects/frames in the field.

For example, summary fields can help you query video datasets to find samples that contain specific classes of interest, eg `person`, in at least one frame.

You can create a new summary field at any time by clicking the `Create Index` button in the top-right of the panel and selecting the âSummary fieldâ type in the model:

![query-performance-create-summary-field](../_images/qp_create_summary_field.png)

Warning

For large datasets, creating summary fields can take a few minutes.

You can also create and manage summary fields [via the SDK](https://docs.voxel51.com/user_guide/using_datasets.html#summary-fields).

### Updating summary fields#

Since a [summary field](https://docs.voxel51.com/user_guide/using_datasets.html#summary-fields) is derived from the contents of another field, it must be updated whenever there have been modifications to its source field.

Click the update icon in the actions column of any summary field to open a modal that will provide guidance on whether to update the summary field to reflect recent dataset changes.

### Deleting indexes/summaries#

You can delete a custom index or summary field by clicking its trash can icon in the actions column of the panel.

## Disabling Query Performance#

Query Performance is enabled by default for all datasets. This is generally the recommended setting for all large datasets to ensure that queries are performant.

However, in certain circumstances you may prefer to disable Query Performance, which enables the Appâs sidebar to show additional information such as label/value counts that are useful but more expensive to compute.

You can enable/disable Query Performance for a particular dataset for its lifetime (in your current browser) via the gear icon in the Samples panelâs actions row:

![app-query-performance-disabled](../_images/app-query-performance-disabled.gif)

You can also enable/disable Query Performance via the status button in the upper right corner of the Query Performance panel:

![query-performance-config](../_images/qp_config.png)

Deployment admins can also configure the global behavior of Query Performance via the following environment variables:
    
    
    # Disable Query Performance by default for all new datasets
    FIFTYONE_APP_DEFAULT_QUERY_PERFORMANCE=false
    
    
    
    # Completely disable Query Performance for all users
    FIFTYONE_APP_ENABLE_QUERY_PERFORMANCE=false
    

IN THIS ARTICLE 
