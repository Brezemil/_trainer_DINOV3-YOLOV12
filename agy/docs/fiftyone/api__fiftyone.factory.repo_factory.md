---
source_url: https://docs.voxel51.com/api/fiftyone.factory.repo_factory.html
---

# fiftyone.factory.repo_factory#

FiftyOne repository factory.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`RepositoryFactory`() |   
---|---  
  
class fiftyone.factory.repo_factory.RepositoryFactory#
    

Bases: `object`

**Attributes:**

`repos` |   
---|---  
  
**Methods:**

`delegated_operation_repo`() |   
---|---  
`execution_store_repo`([dataset_id,Â ...]) |   
  
repos = {}#
    

static delegated_operation_repo() → [DelegatedOperationRepo](api__fiftyone.factory.repos.delegated_operation.md#fiftyone.factory.repos.delegated_operation.DelegatedOperationRepo "fiftyone.factory.repos.delegated_operation.DelegatedOperationRepo")#
    

static execution_store_repo(_dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _collection_name : str | None = None_, _notification_service : [ChangeStreamNotificationService](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService "fiftyone.operators.store.notification_service.ChangeStreamNotificationService") | None = None_) → [ExecutionStoreRepo](api__fiftyone.factory.repos.execution_store.md#fiftyone.factory.repos.execution_store.ExecutionStoreRepo "fiftyone.factory.repos.execution_store.ExecutionStoreRepo")#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
