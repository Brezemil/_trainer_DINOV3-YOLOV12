---
source_url: https://docs.voxel51.com/enterprise/app.html
---

# FiftyOne Enterprise App#

The FiftyOne Enterprise App allows you to visualize, browse, and interact with your individual datasets like you can with the [FiftyOne App](user_guide__app.md#fiftyone-app), but with expanded features for organizing, permissioning, versioning, and sharing your teamâs datasets, all from a centralized web portal.

This page provides a brief overview of some features available only in the FiftyOne Enterprise App.

## The homepage#

When you login to the FiftyOne Enterprise App, youâll land on the homepage pictured below.

In the top bar of this page, on the left side, the gray number next to âAll datasetsâ indicates the total number of datasets that you have access to. If there are more than 20 datasets, you can use the âPreviousâ and âNextâ buttons at the bottom of the page to see different batches of datasets.

Note

You can return to the homepage from any page of the Enterprise App by clicking on the Voxel51 logo in the upper left corner.

![app-homepage](../_images/homepage.png)

### Pinned datasets#

You can pin datasets for easy access by hovering over the datasetâs name in the main table and clicking the pin icon.

The âYour pinned datasetsâ widget on the right-hand side of the hompage shows your pinned datasets at a glance and allows you to quickly open one by clicking on its name. Pinned datasets are listed in reverse chronological order (most recently pinned on top).

To unpin a dataset, click the pin icon next to the dataset name in the âYour pinned datasetsâ widget or the pin next to the datasetâs name in the main table.

[![pin-datasets](https://docs.voxel51.com/_images/pinned_datasets.png) ](../_images/pinned_datasets.png)

### Sorting datasets#

You can use the drop-down menu in the upper left of the main table to sort your datasets by various criteria, including size, creation date, recently used, and alphabetically by name:

[![order-datasets](https://docs.voxel51.com/_images/ordering_datasets.png) ](../_images/ordering_datasets.png)

### Filtering datasets#

You can use the search bar (with the magnifying glass icon) in the upper right corner of the dataset table to filter datasets by name, tags, and media type:

[![dataset-search-bar](https://docs.voxel51.com/_images/dataset_search_bar.png) ](../_images/dataset_search_bar.png)

By default, datasets that match across any supported field are returned, but you can narrow the search to specific fields by selecting the relevant option in the search dropdown:

[![dataset-search-fields](https://docs.voxel51.com/_images/dataset_search_fields.png) ](../_images/dataset_search_fields.png)

## Creating datasets#

To create a new dataset, click on the âNew datasetâ button in the upper right corner of the homepage. A pop-up will appear allowing you to choose a name, description, and tags for the dataset:

  * **Name** : as youâre typing a name for your dataset, a URL will appear below denoting the address at which the dataset will be accessible. If the name or URL is not available, you will be prompted to try another name.

  * **Description** : an optional free text description that you can use to store relevant information about your dataset.

  * **Tags** : an optional list of tag(s) for your dataset. For example, you may want to record the media type, task type, project name, or other pertinent information. To add a tag, type it in the text bar. If you have previously used a tag, it will automatically appear in a dropdown and you can select it. To add a new tag, type tab or comma.




Note

A datasetâs name, description, and tags can be edited later from the datasetâs Manage tab.

![create-dataset](../_images/create_dataset.png)

Note

What next? Use the [FiftyOne Enterprise Python SDK](enterprise__installation.md#enterprise-python-sdk) to upload new samples, labels, and metadata to your dataset. A common approach is to automate this process via [cloud functions](enterprise__cloud_media.md#enterprise-cloud-functions).

## Using a dataset#

Click on a dataset from the homepage to open the datasetâs âSamplesâ tab.

From the Samples tab you can visualize, tag, filter, and explore your dataset just as you would via the [FiftyOne App](user_guide__app.md#fiftyone-app).

![samples-page](../_images/samples_page.png)

Note

Did you know? You can also navigate directly to a dataset of interest by pasting its URL into your browserâs URL bar.

## Managing a dataset#

The FiftyOne Enterprise App provides a number of options for managing existing datasets, as described below.

You can access these options from the Samples tab by clicking on the âManageâ tab in the upper left corner of the page.

You can also directly navigate to this page from the homepage by clicking the three dots on the right hand side of a row of the dataset listing table and selecting âEdit datasetâ.

Note

Did you know? You can also use the [Enterprise SDK](enterprise__installation.md#enterprise-python-sdk) to programmatically, create, edit, and delete datasets.

### Basic info#

The âBasic infoâ tab is accessible to all users with [Can view](enterprise__roles_and_permissions.md#enterprise-can-view) access to the dataset.

Users with [Can manage](enterprise__roles_and_permissions.md#enterprise-can-manage) permissions on the dataset can edit the name, description, and tags of a dataset from this page.

Additionally, members can create a copy of the dataset by clicking on the âClone this datasetâ button.

![dataset-basic-info](../_images/dataset_basic_info.png)

### Access#

The âAccessâ tab is only accessible to users with [Can manage](enterprise__roles_and_permissions.md#enterprise-can-manage) permissions on the dataset.

From this tab, users can add, remove, edit, or invite users to the dataset. Refer to [this page](enterprise__roles_and_permissions.md#enterprise-permissions) for more information about the available dataset-level permissions that you can grant.

![dataset-access](../_images/dataset_access.png)

### Danger zone#

The âDanger zoneâ tab is only accessible to users with [Can manage](enterprise__roles_and_permissions.md#enterprise-can-manage) permissions on the dataset.

From this tab, you can select âDelete entire datasetâ to permanently delete a dataset from your Enterprise deployment. You must type the datasetâs full name in the modal to confirm this action.

![danger-zone](../_images/dataset_danger_zone.png)

Warning

Deleting a dataset is permanent!

Note

The FiftyOne Enterprise App ships with AI-assisted mask segmentation for annotation workflows. The feature works out of the box with no configuration. Deployments that prefer to serve the model weights from their own infrastructure can do so via the [AI model weights](enterprise__installation.md#enterprise-ai-model-weights) setting.

IN THIS ARTICLE 
