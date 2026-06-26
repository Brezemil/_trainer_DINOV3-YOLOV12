---
source_url: https://docs.voxel51.com/enterprise/migrations.html
---

# Migrations#

This page describes how to migrate between FiftyOne Enterprise versions, both for admins migrating the core FiftyOne Enterprise infrastructure and individual users who need to install a new version of the FiftyOne Enterprise Python SDK.

Refer to this section to see how to migrate existing datasets from FiftyOne Open Source to FiftyOne Enterprise.

## Upgrading your Python SDK#

Users can upgrade their FiftyOne Enterprise Python client to the latest version as follows:
    
    
    pip install --index-url https://${TOKEN}@pypi.fiftyone.ai --upgrade fiftyone
    

A specific FiftyOne Enterprise client version can be installed like so:
    
    
    pip install --index-url https://${TOKEN}@pypi.fiftyone.ai fiftyone==${VERSION}
    

Note

You can find your `TOKEN` by logging into the FiftyOne Enterprise App and clicking on the [account icon](enterprise__installation.md#enterprise-python-sdk) in the upper right.

## Upgrading your deployment#

The basic **admin workflow** for upgrading a FiftyOne Enterprise deployment is:

  * Upgrade all automated services and individual user workflows that use the FiftyOne Enterprise Python SDK to an appropriate SDK version

  * Upgrade your core FiftyOne Enterprise infrastructure (via Kubernetes, Docker, etc)

  * Upgrade your databaseâs version, as described below




Note

Contact your Voxel51 CS Engineer for all relevant upgrade information, including compatible SDK versions, deployment assets, and upgrade assistance.

New FiftyOne Enterprise versions occasionally introduce data model changes that require database migrations when upgrading your deployment.

Admins can check a deploymentâs current version via the Python SDK as shown below:
    
    
    $ fiftyone migrate --info
    FiftyOne Enterprise version: 0.7.1
    FiftyOne compatibility version: 0.15.1
    Database version: 0.15.1
    
    ...
    

Note

Individual datasets have versions as well. They are lazily upgraded the first time they are loaded under a new database version. Often there is no migration required, but there could be.

[Unlike FiftyOne Open Source](https://voxel51.com/docs/fiftyone/user_guide/config.html#database-migrations), a FiftyOne Enterprise database is not automatically upgraded when a user connects to the database with a newer Python client version. Instead, an admin must manually upgrade your database by installing the newest version of the FiftyOne Enterprise SDK locally, assuming admin privileges, and running the following command:

Beginning with FiftyOne Enterprise `v2.14.0`, there is a new migration tool which is designed specifically for Enterprise deployments. It is similar in use to the existing `fiftyone migrate` command, but does not come packaged with the FiftyOne distribution by default.

## Installing the Enterprise Migration Tool#

Install the `fiftyone-migrator` package:
    
    
    pip install fiftyone-migrator \
      --extra-index-url=https://${TOKEN}@pypi.fiftyone.ai
    

## Configuring the Enterprise Migration Tool#

The Enterprise Migration Tool requires the following environment variables to be defined where it is run:

  * `CAS_DATABASE_URI` \- The database URI used by CAS

  * `CAS_DATABASE_NAME` \- The database name used by CAS

  * `FIFTYONE_DATABASE_URI` \- The database URI used by FiftyOne

  * `FIFTYONE_DATABASE_NAME` \- The database name used by FiftyOne




## Using the Enterprise Migration Tool#

**IMPORTANT** : As with any database migration, Voxel51 **strongly** recommends backing up your database prior to migrating. While many precautions are taken to mitigate the risk of data corruption, data migration always carries a risk of introducing unintended modifications.

The enterprise migration tool allows migrating each of the enterprise services:

  * `datasets` \- Migrate core datasets; this is equivalent to the existing `fiftyone migrate` command

  * `enterprise` \- Migrate enterprise-specific dataset features

  * `cas` \- Migrate the Centralized Authentication Service (CAS)

  * `hub` \- Migrate the enterprise API




Each of these services can be selectively included or excluded from migration.
    
    
    export FIFTYONE_DATABASE_ADMIN=true
    
    # Migrate all enterprise services to the most current state
    fiftyone-migrator migrate
    
    # Migrate all enterprise services to a specific version
    fiftyone-migrator migrate 2.15.0
    
    # Migrate specific services
    fiftyone-migrator migrate --include enterprise
    
    # Migrate all-but specific services
    fiftyone-migrator migrate --exclude cas hub
    

Note

Once the database is upgraded, all users must upgrade their Python SDK to a compatible version. Any connections from incompatible Python clients will be refused and an informative error message will be displayed.

## Reverting a Migration with the Enterprise Migration Tool#

Migrations done with the Enterprise Migration Tool are designed to be bidirectional. In the event that you need to revert a migration, simply provide the version which you want to restore.
    
    
    # Migrate from v2.14.0 to v2.15.0
    fiftyone-migrator migrate 2.15.0
    
    # Oops, need to revert this migration!
    # Migrate from v2.15.0 to v2.14.0
    fiftyone-migrator migrate 2.14.0
    

## Downgrading your deployment without the Enterprise Migration Tool#

**For migrations done prior to FiftyOne Enterprise v2.14.0 and the Enterprise Migration Tool**

Admins can also downgrade their FiftyOne Enterprise deployment to an older version if necessary.

The steps are the same as when upgrading, except that youâll need to know the appropriate database version to migrate down to. Each version of FiftyOne Enterprise corresponds to a version of FiftyOne Open Source called its âopen source compatibility versionâ, and this versioning system is used to set the database version.

For example, you can downgrade to FiftyOne Enterprise v0.10 like so:
    
    
    OS_COMPAT_VERSION=0.18.0  # OS compatibility version for Enterprise v0.10.0
    
    export FIFTYONE_DATABASE_ADMIN=true
    fiftyone migrate --all -v ${OS_COMPAT_VERSION}
    

Note

The above command must be run with the **newer SDK version** installed.

Note

Contact your Voxel51 support team if you need to know the open source compatibility version for a particular FiftyOne Enterprise version that you wish to downgrade to.

## Migrating datasets to Enterprise#

Any datasets that you have created via FiftyOne Open Source can be migrated to your FiftyOne Enterprise deployment by exporting them in [FiftyOneDataset](user_guide__export_datasets.md#fiftyonedataset-export) format:
    
    
     1# Open source SDK
     2import fiftyone as fo
     3
     4dataset = fo.load_dataset(...)
     5
     6dataset.export(
     7    export_dir="/tmp/dataset",
     8    dataset_type=fo.types.FiftyOneDataset,
     9    export_media=False,
    10)
    

and then re-importing them with the FiftyOne Enterprise SDK connected to your Enterprise deployment:
    
    
    1# Enterprise SDK
    2import fiftyone as fo
    3
    4dataset = fo.Dataset.from_dir(
    5    dataset_dir="/tmp/dataset",
    6    dataset_type=fo.types.FiftyOneDataset,
    7    persistent=True,
    8)
    

Note that youâll need to update any local filepaths to cloud paths in order to use the dataset in FiftyOne Enterprise.

If you need to upload the local media to the cloud, the FiftyOne Enterprise SDK provides a builtin utility for this:
    
    
    1import fiftyone.core.storage as fos
    2
    3fos.upload_media(
    4    dataset,
    5    "s3://path/for/media",
    6    update_filepaths=True,
    7    progress=True,
    8)
    

Note

By default, the above method only uploads the media in the `filepath` field of your samples. If your dataset contains other media fields (e.g. [thumbnails](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-media-fields), [segmentations](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation), or [heatmaps](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps)) simply run the above command multiple times, using the `media_field` argument to specify the appropriate fields to upload.

If any media fields use the same filenames as other fields, be sure to provide different `remote_dir` paths each time you call the above method to avoid overwriting existing media.

If the files already exist in cloud buckets, you can manually update the filepaths on the dataset:
    
    
    1cloud_paths = []
    2for filepath in dataset.values("filepath"):
    3    cloud_path = get_cloud_path(filepath)  # your function
    4    cloud_paths.append(cloud_path)
    5
    6dataset.set_values("filepath", cloud_paths)
    

When youâre finished, delete the local export of the dataset:
    
    
    1shutil.rmtree("/tmp/dataset")
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
