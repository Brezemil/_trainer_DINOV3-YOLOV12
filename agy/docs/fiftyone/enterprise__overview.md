---
source_url: https://docs.voxel51.com/enterprise/overview.html
---

# FiftyOne Enterprise Overview#

FiftyOne Enterprise is purpose-built to integrate into your existing ML workflows, including annotation, evaluation, model training, and deployment. Note [Learn more](https://voxel51.com/fiftyone/why-upgrade) about FiftyOne Enterprise and [contact us](https://voxel51.com/talk-to-sales) to try it!

## Open Source vs Enterprise#

Hereâs a high-level overview of the capabilities that FiftyOne Enterprise brings: |  | FiftyOne Enterprise | FiftyOne Open Source  
---|---|---  
Curate Datasets | ![check](/_static/images/icons/checkmark.svg) | ![check](/_static/images/icons/checkmark.svg)  
Evaluate Models | ![check](/_static/images/icons/checkmark.svg) | ![check](/_static/images/icons/checkmark.svg)  
Find Mistakes | ![check](/_static/images/icons/checkmark.svg) | ![check](/_static/images/icons/checkmark.svg)  
Visualize Embeddings | ![check](/_static/images/icons/checkmark.svg) | ![check](/_static/images/icons/checkmark.svg)  
Deployment | Multi-user, on-premise,  
private/public cloud | Local, Single user  
Dataset Management | ![check](/_static/images/icons/checkmark.svg) |   
User Permissions | ![check](/_static/images/icons/checkmark.svg) |   
Dataset Permissions | ![check](/_static/images/icons/checkmark.svg) |   
Dataset Versioning | ![check](/_static/images/icons/checkmark.svg) |   
SSO | ![check](/_static/images/icons/checkmark.svg) |   
Enterprise Support | ![check](/_static/images/icons/checkmark.svg) | Discord Community  
Licensing | Unlimited data, flexible  
user-based licensing  
  
Apache 2.0

## Backwards compatibility#

FiftyOne Enterprise is fully backwards compatible with FiftyOne Open Source. This means that all of your pre-existing FiftyOne Open Source workflows should be usable without modification. For example, you can continue running all of the workflows listed below as you would with FiftyOne Open Source: | Application | Workflows  
---|---  
Data ingestion | [Importing data into FiftyOne](user_guide__import_datasets.md#importing-datasets)  
Data curation |  [Using the FiftyOne App](user_guide__app.md#fiftyone-app) [Creating views into datasets](https://docs.voxel51.com/user_guide/using_views.html#using-views) [Embedding-based dataset analysis](https://voxel51.com/docs/fiftyone/tutorials/image_embeddings.html) [Visual similarity](brain.md#brain-similarity) and [dataset uniqueness](brain.md#brain-image-uniqueness)  
Annotation | [Using the annotation API](integrations__annotation.md#fiftyone-annotation)  
Model training and evaluation |  [Exporting data for model training](user_guide__export_datasets.md#exporting-datasets) [Adding model predictions to FiftyOne](https://voxel51.com/docs/fiftyone/tutorials/evaluate_detections.html#Add-predictions-to-dataset) [Evaluating models in FiftyOne](user_guide__evaluation.md#evaluating-models) [Using interactive plots to explore results](user_guide__plots.md#interactive-plots)  
  
## System architecture#

FiftyOne Enterprise is implemented as a set of interoperable services, as described in the figure below.

![enterprise-architecture](../_images/enterprise_architecture.png)

FiftyOne Enterprise is strictly a software offering. All relevant hardware is owned and managed by your organization, whether on-premises or in your virtual private cloud.

**Enterprise database services**

The primary storage location for all of the FiftyOne Enterprise datasets and related metadata (excluding media files) for your organization.

**Enterprise web service**

An always-on front-end from which you can visually access the datasets in your FiftyOne Enterprise deployment. Web-based access is the standard entrypoint for non-technical users who need point-and-click access to dataset curation and related features, as well as basic workflows for technical users. Most dataset curation and model analysis work by engineers happens via client installations.

**Enterprise API authentication**

Technical users connecting to FiftyOne Enterprise via Python or Jupyter notebooks use token-based authentication to make authorized connections to the centralized database storing your Teamâs dataset metadata.

**Python/notebook users (your organization)**

Similar to FiftyOne Open Source, technical users can install the FiftyOne Enterprise client in their working environment(s). These clients are configured to use the centralized database service and will additionally serve their own App instances (like FiftyOne Open Source) so that engineers can work locally, remotely, and in Jupyter notebooks.

**Web users (your organization)**

FiftyOne Enterprise provides an always-on login portal at `https://<your-org>.fiftyone.ai` that users can login to from any browser for web-only workflows.

**Data lake (your organization)**

FiftyOne Enterprise does not require duplication or control over how your source media files are stored. Instead, FiftyOne Enterprise stores references (e.g., cloud object URLs or network storage paths) to the media in your datasets, thereby minimizing storage costs and providing you the flexibility to provision your object storage as you see fit. FiftyOne Enterprise has full support for cloud, network, and local media storage.

**User authentication (your organization)**

FiftyOne Enterprise can be configured to work with your organizationâs authentication and authorization systems, enabling you to manage access to FiftyOne Enterprise using your existing OAuth stack. FiftyOne Enterprise supports SAML 2.0 and OAuth 2.0.

## Security considerations#

FiftyOne Enterprise relies on your organizationâs existing security infrastructure. No user accounts are created specifically for FiftyOne Enterprise; we integrate directly with your OAuth system.

Usage of the FiftyOne Enterprise client by technical users of your organization is also secure. All database access is managed by the central authentication service, and self-hosted App instances can be configured to only accept connections from known servers (e.g., only localhost connections). In remote client workflows, users are instructed how to configure ssh tunneling to securely access self-hosted App instances.

No outside network access is required to operate FiftyOne Enterprise. Voxel51 only requests the ability to (a) access the system logs for usage tracking and auditing purposes, and (b) access the system at the customerâs request to provide technical support. We are flexible in the mechanisms used to accomplish these goals.

IN THIS ARTICLE 
