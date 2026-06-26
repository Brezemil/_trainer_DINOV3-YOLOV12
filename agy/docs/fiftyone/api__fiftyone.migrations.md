---
source_url: https://docs.voxel51.com/api/fiftyone.migrations.html
---

# fiftyone.migrations#

  * [fiftyone.migrations.runner](api__fiftyone.migrations.runner.md)
    * [`Version()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.Version)
    * [`get_database_revision()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.get_database_revision)
    * [`get_dataset_revision()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.get_dataset_revision)
    * [`get_datasets_revisions()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.get_datasets_revisions)
    * [`migrate_all()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.migrate_all)
    * [`migrate_database_if_necessary()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.migrate_database_if_necessary)
    * [`needs_migration()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.needs_migration)
    * [`migrate_dataset_if_necessary()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.migrate_dataset_if_necessary)
    * [`MigrationRunner`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner)
      * [`MigrationRunner.head`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.head)
      * [`MigrationRunner.destination`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.destination)
      * [`MigrationRunner.direction`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.direction)
      * [`MigrationRunner.has_revisions`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.has_revisions)
      * [`MigrationRunner.has_admin_revisions`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.has_admin_revisions)
      * [`MigrationRunner.revisions`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.revisions)
      * [`MigrationRunner.admin_revisions`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.admin_revisions)
      * [`MigrationRunner.run()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.run)
      * [`MigrationRunner.run_admin()`](api__fiftyone.migrations.runner.md#fiftyone.migrations.runner.MigrationRunner.run_admin)



## Module contents#

FiftyOneâs migration interface.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_database_revision`() | Gets the current revision of the database.  
---|---  
`get_dataset_revision`(name) | Gets the current revision of the given dataset.  
`get_datasets_revisions`() | Gets the current revision of all datasets.  
`migrate_all`([destination,Â error_level,Â verbose]) | Migrates the database and all datasets to the specified destination revision.  
`migrate_database_if_necessary`([destination,Â ...]) | Migrates the database to the specified revision, if necessary.  
`migrate_dataset_if_necessary`(name[,Â ...]) | Migrates the dataset from its current revision to the specified destination revision.  
`needs_migration`([name,Â head,Â destination]) | Determines whether a dataset requires a migration in order to be used in the specified destination revision.  
  
fiftyone.migrations.get_database_revision()#
    

Gets the current revision of the database.

Returns:
    

the database revision string

fiftyone.migrations.get_dataset_revision(_name_)#
    

Gets the current revision of the given dataset.

Parameters:
    

**name** â the name of the dataset

Returns:
    

the dataset revision string

fiftyone.migrations.get_datasets_revisions()#
    

Gets the current revision of all datasets.

Returns:
    

a dictionary mapping dataset names to their revision strings

fiftyone.migrations.migrate_all(_destination =None_, _error_level =0_, _verbose =False_)#
    

Migrates the database and all datasets to the specified destination revision.

If `fiftyone.config.database_admin` is `False` and no `destination` is provided, the database and each dataset will only be migrated if their current versions are not compatible with the clientâs version.

Parameters:
    

  * **destination** (_None_) â the destination revision. By default, the `fiftyone` client version is used

  * **error_level** (_0_) â 

the error level to use if an individual dataset cannot be migrated. Valid values are:

    * 0: raise error if a dataset cannot be migrated

    * 1: log warning if a dataset cannot be migrated

    * 2: ignore datasets that cannot be migrated

  * **verbose** (_False_) â whether to log incremental migrations that are run




fiftyone.migrations.migrate_database_if_necessary(_destination =None_, _verbose =False_, _config =None_)#
    

Migrates the database to the specified revision, if necessary.

If `fiftyone.config.database_admin` is `False` and no `destination` is provided, the database will only be migrated if its current version is not compatible with the clientâs version.

Parameters:
    

  * **destination** (_None_) â the destination revision. By default, the `fiftyone` client version is used

  * **verbose** (_False_) â whether to log incremental migrations that are run

  * **config** (_None_) â an optional `DatabaseConfigDocument`. By default, DB config is pulled from the database.




fiftyone.migrations.migrate_dataset_if_necessary(_name_ , _destination =None_, _error_level =0_, _verbose =False_)#
    

Migrates the dataset from its current revision to the specified destination revision.

If `fiftyone.config.database_admin` is `False` and no `destination` is provided, the dataset will only be migrated if its current version is not compatible with the clientâs version.

Parameters:
    

  * **name** â the name of the dataset

  * **destination** (_None_) â the destination revision. By default, the current database version is used

  * **error_level** (_0_) â 

the error level to use. Valid values are:

    * 0: raise error if the dataset cannot be migrated

    * 1: log warning if the dataset cannot be migrated

    * 2: ignore datasets that cannot be migrated

  * **verbose** (_False_) â whether to log incremental migrations that are run




fiftyone.migrations.needs_migration(_name =None_, _head =None_, _destination =None_)#
    

Determines whether a dataset requires a migration in order to be used in the specified destination revision.

To use this method, specify either the `name` of an existing dataset or provide the `head` revision of the dataset.

If `fiftyone.config.database_admin` is `False` and no `destination` is provided, a dataset will be deemed to require no migration if its current version if compatible with the clientâs version.

Parameters:
    

  * **name** (_None_) â the name of the dataset

  * **head** (_None_) â the current revision of the dataset

  * **destination** (_None_) â the destination revision. By default, the current database version is used



Returns:
    

True/False

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
