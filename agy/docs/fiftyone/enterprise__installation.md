---
source_url: https://docs.voxel51.com/enterprise/installation.html
---

# FiftyOne Enterprise Installation#

FiftyOne Enterprise deployments come with a centralized FiftyOne Enterprise App and database that allows your entire team to collaborate securely on the same datasets. FiftyOne Enterprise is deployed entirely into your environment, either on-premises or in a private cloud. Your data never leaves your environment.

FiftyOne Enterprise can be deployed on a wide variety of infrastructure solutions, including Kubernetes and Docker.

Note

Detailed instructions for the initial FiftyOne Enterprise deployment, along with all necessary components, are made available by your Voxel51 support team during the onboarding process.

## Python SDK#

While the [FiftyOne Enterprise App](enterprise__app.md#enterprise-app) allows for countless new App-centric workflows, any existing Python-based workflows that youâve fallen in love with in the open-source version of FiftyOne are still directly applicable!

FiftyOne Enterprise requires an updated Python SDK, which is a wrapper around the open-source FiftyOne package that adds new functionality like support for cloud-backed media.

You can find the installation instructions under the âInstall FiftyOneâ section of the Enterprise App by clicking on your user icon in the upper right corner:

[![install-enterprise](https://docs.voxel51.com/_images/install_fiftyone.png) ](../_images/install_fiftyone.png)

There youâll see instructions for installing a `fiftyone` package from the private PyPI server as shown below:
    
    
    pip install --index-url https://${TOKEN}@pypi.fiftyone.ai fiftyone
    

Note

See Installation with Poetry if you use `poetry` instead of `pip`.

Note

The Enterprise Python package is named `fiftyone` and has the same module structure as [fiftyone](api__fiftyone.md), so any existing scripts you built using open source will continue to run after you upgrade!

### Next Steps#

After installing the Enterprise Python SDK in your virtual environment, youâll need to configure two things:

  * Your teamâs [API connection](enterprise__api_connection.md#enterprise-api-connection) or [MongoDB connection](user_guide__config.md#configuring-mongodb-connection)

  * The cloud credentials to access your cloud-backed media




Thatâs it! Any operations you perform will be stored in a centralized location and will be available to all users with access to the same datasets in the Enterprise App or their Python workflows.

### Installation with Poetry#

If you are using [poetry](https://python-poetry.org/) to install your dependencies rather than `pip`, you will need to follow instructions in [the docs for installing from a private repository.](https://python-poetry.org/docs/repositories/#installing-from-private-package-sources) The two key points are specifying the additional private source and declaring that the `fiftyone` module should be found there and not the default PyPI location.

#### Add source#

In poetry v1.5, it is recommended to use an [explicit package source.](https://python-poetry.org/docs/repositories/#explicit-package-sources)
    
    
    poetry source add --priority=explicit fiftyone-enterprise https://pypi.fiftyone.ai/simple/
    

Prior to v1.5, you should use the deprecated [secondary package source.](https://python-poetry.org/docs/1.4/repositories/#secondary-package-sources)
    
    
    poetry source add --secondary fiftyone-enterprise https://pypi.fiftyone.ai/simple/
    

#### Configure credentials#
    
    
    poetry config http-basic.fiftyone-enterprise ${TOKEN} ""
    

Alternatively, you can specify the credentials in environment variables.
    
    
    export POETRY_HTTP_BASIC_FIFTYONE_ENTERPRISE_USERNAME="${TOKEN}"
    export POETRY_HTTP_BASIC_FIFTYONE_ENTERPRISE_PASSWORD=""
    

If you have trouble configuring the credentials, see [more in the poetry docs here.](https://python-poetry.org/docs/repositories/#configuring-credentials)

#### Add fiftyone dependency#

Replace `X.Y.Z` with the proper version
    
    
    poetry add --source fiftyone-enterprise fiftyone==X.Y.Z
    

You should then see snippets in the `pyproject.toml` file like the following (the `priority` line will be different for `poetry<v1.5`):
    
    
    [[tool.poetry.source]]
    name = "fiftyone-enterprise"
    url = "https://pypi.fiftyone.ai"
    priority = "explicit"
    
    
    
    [tool.poetry.dependencies]
    fiftyone = {version = "X.Y.Z", source = "fiftyone-enterprise"}
    

## Cloud credentials#

In order to utilize cloud-backed media functionality of FiftyOne Enterprise, at least one cloud source must be configured with proper credentials. Below are instructions for configuring each supported cloud provider for local SDK use or directly to the Enterprise containers. An admin can also configure credentials for use by all app users.

### Cross-origin resource sharing (CORS)#

If your datasets include cloud-backed [point clouds](https://docs.voxel51.com/user_guide/using_datasets.html#point-cloud-datasets) or [segmentation maps](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation), you may need to configure cross-origin resource sharing (CORS) for your cloud buckets. Details are provided below for each cloud platform.

### Browser caching#

If your datasets include cloud-backed media, we strongly recommend configuring your data sources to allow for built in browser caching. This will cache signed URL responses so you donât need to reload assets from your cloud storage between sessions. Details are provided below for each cloud platform.

### Amazon S3#

To work with FiftyOne datasets whose media are stored in Amazon S3, you simply need to provide [AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-a-configuration-file) to your Enterprise client with read access to the relevant objects and buckets.

You can do this in any of the following ways:

1\. Configure/provide AWS credentials in any format supported by the [boto3 library](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials). For example, here are two of the supported methods:
    
    
    # Access key
    export AWS_ACCESS_KEY_ID=...
    export AWS_SECRET_ACCESS_KEY=...
    export AWS_SESSION_TOKEN=... # if applicable
    export AWS_DEFAULT_REGION=...
    
    
    
    # Web identity provider
    export AWS_ROLE_ARN=...
    export AWS_WEB_IDENTITY_TOKEN_FILE=...
    export AWS_ROLE_SESSION_NAME... #if applicable
    export AWS_DEFAULT_REGION=...
    

2\. Provide AWS credentials on a per-session basis by setting one of the following sets of environment variables to point to your AWS credentials on disk:
    
    
    # AWS config file
    export AWS_CONFIG_FILE="/path/to/aws-config.ini"
    export AWS_PROFILE=default  # optional
    
    
    
    # Shared credentials file
    export AWS_SHARED_CREDENTIALS_FILE="/path/to/aws-credentials.ini"
    export AWS_PROFILE=default  # optional
    

In the above, the config file should use [this syntax](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-a-configuration-file) and the shared credentials file should use [this syntax](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

Note

FiftyOne Enterprise requires either the `s3:ListBucket` or `s3:GetBucketLocation` permission in order to access objects in S3 buckets.

If you wish to use multi-account credentials, your credentials must have the `s3:ListBucket` permission, as `s3:GetBucketLocation` does not support this.

3\. Permanently register AWS credentials on a particular machine by adding the following keys to your [media cache config](enterprise__cloud_media.md#enterprise-media-cache-config):
    
    
    {
        "aws_config_file": "/path/to/aws-config.ini",
        "aws_profile": "default"  # optional
    }
    

If you need to [configure CORS on your AWS buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html), here is an example configuration:
    
    
    [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "HEAD"],
            "AllowedOrigins": ["https://fiftyone-enterprise-deployment.yourcompany.com"],
            "ExposeHeaders": [],
            "MaxAgeSeconds": 86400
        }
    ]
    

If you would like to take advantage of browser caching you can [specify cache-control headers on S3 objects](https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/controlling-how-long-amazon-s3-content-is-cached-by-amazon-cloudfront.html#specify-cache-control-headers). By default S3 does not provide cache-control headers so it will be up to your browserâs heuristics engine to determine how long to cache the object.

### Google Cloud Storage#

To work with FiftyOne datasets whose media are stored in Google Cloud Storage, you simply need to provide [credentials](https://cloud.google.com/docs/authentication) to your Enterprise client with read access to the relevant objects and buckets.

You can do this in any of the following ways:

1\. Configure [application default credentials](https://cloud.google.com/docs/authentication/application-default-credentials) in a manner supported by Google Cloud, such as:

  * [Using the gcloud CLI](https://cloud.google.com/docs/authentication/application-default-credentials#personal)

  * [Attaching a service account to your Google Cloud resource](https://cloud.google.com/docs/authentication/application-default-credentials#attached-sa)




2\. Provide GCS credentials on a per-session basis by setting the following environment variables to point to your GCS credentials on disk:
    
    
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/gcp-credentials.json"
    

3\. Permanently register GCS credentials on a particular machine by adding the following keys to your [media cache config](enterprise__cloud_media.md#enterprise-media-cache-config):
    
    
    {
        "google_application_credentials": "/path/to/gcp-credentials.json"
    }
    

In the above, the credentials file can contain any format supported by [google.auth.load_credentials_from_file()](https://google-auth.readthedocs.io/en/master/reference/google.auth.html#google.auth.load_credentials_from_file), which includes a service account key, stored authorized user credentials, or external account credentials.

If you need to [configure CORS on your GCP buckets](https://cloud.google.com/storage/docs/using-cors), here is an example configuration:
    
    
    [
        {
            "origin": ["https://fiftyone-enterprise-deployment.yourcompany.com"],
            "method": ["GET", "HEAD"],
            "responseHeader": ["*"],
            "maxAgeSeconds": 3600
        }
    ]
    

If you would like to take advantage of browser caching you can [specify cache-control headers on GCP content](https://cloud.google.com/storage/docs/metadata#cache-control). By default GCP sets the max-age=0 seconds meaning no caching will occur.

### Microsoft Azure#

To work with FiftyOne datasets whose media are stored in Azure Storage, you simply need to provide [Azure credentials](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-data-operations-cli) to your Enterprise client with read access to the relevant objects and containers.

You can do this in any of the following ways:

1\. Provide your Azure credentials in any manner recognized by [azure.identity.DefaultAzureCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python)

2\. Provide your Azure credentials on a per-session basis by setting any group of environment variables shown below:
    
    
    # Option 1
    export AZURE_STORAGE_CONNECTION_STRING=...
    export AZURE_ALIAS=...  # optional
    
    
    
    # Option 2
    export AZURE_STORAGE_ACCOUNT=...
    export AZURE_STORAGE_KEY=...
    export AZURE_ALIAS=...  # optional
    
    
    
    # Option 3
    export AZURE_STORAGE_ACCOUNT=...
    export AZURE_CLIENT_ID=...
    export AZURE_CLIENT_SECRET=...
    export AZURE_TENANT_ID=...
    export AZURE_ALIAS=...  # optional
    

3\. Provide Azure credentials on a per-session basis by setting the following environment variables to point to your Azure credentials on disk:
    
    
    export AZURE_CREDENTIALS_FILE=/path/to/azure-credentials.ini
    export AZURE_PROFILE=default  # optional
    

4\. Permanently register Azure credentials on a particular machine by adding the following keys to your [media cache config](enterprise__cloud_media.md#enterprise-media-cache-config):
    
    
    {
        "azure_credentials_file": "/path/to/azure-credentials.ini",
        "azure_profile": "default"  # optional
    }
    

In the options above, the `.ini` file should have syntax similar to one of the following:
    
    
    [default]
    conn_str = ...
    alias = ...  # optional
    
    
    
    [default]
    account_name = ...
    account_key = ...
    alias = ...  # optional
    
    
    
    [default]
    account_name = ...
    sas_token = ...
    alias = ...  # optional
    
    
    
    [default]
    account_name = ...
    client_id = ...
    secret = ...
    tenant = ...
    alias = ...  # optional
    

Note

File based cloud credentials support interpolation so make sure to escape any special characters if you want their literal version to be used. For example, sas_tokens often contain `%` characters that should be escaped as `%%` in the .ini file.

When populating samples with Azure Storage filepaths, you can either specify paths by their full URL:
    
    
    filepath = "https://${account_name}.blob.core.windows.net/container/path/to/object.ext"
    
    # For example
    filepath = "https://voxel51.blob.core.windows.net/test-container/image.jpg"
    

or, if you have defined an alias in your config, you may instead prefix the alias:
    
    
    filepath = "${alias}://container/path/to/object.ext"
    
    # For example
    filepath = "az://test-container/image.jpg"
    

Note

If you use a [custom Azure domain](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal), you can provide it by setting the `AZURE_STORAGE_ACCOUNT_URL` environment variable or by including the `account_url` key in your credentials `.ini` file.

If you would like to take advantage of browser caching you can [specify cache-control headers on Azure blobs](https://learn.microsoft.com/en-us/azure/cdn/cdn-manage-expiration-of-blob-content#setting-cache-control-headers-by-using-azure-powershell). By default Azure does not provide cache-control headers so it will be up to your browserâs heuristics engine to determine how long to cache the object.

### MinIO#

To work with FiftyOne datasets whose media are stored in [MinIO](https://min.io/), you simply need to provide the credentials to your Enterprise client with read access to the relevant objects and buckets.

You can do this in any of the following ways:

1\. Provide your MinIO credentials on a per-session basis by setting the individual environment variables shown below:
    
    
    export MINIO_ACCESS_KEY=...
    export MINIO_SECRET_ACCESS_KEY=...
    export MINIO_ENDPOINT_URL=...
    export MINIO_ALIAS=...  # optional
    export MINIO_REGION=...  # if applicable
    

2\. Provide MinIO credentials on a per-session basis by setting the following environment variables to point to your MinIO credentials on disk:
    
    
    export MINIO_CONFIG_FILE=/path/to/minio-config.ini
    export MINIO_PROFILE=default  # optional
    

3\. Permanently register MinIO credentials on a particular machine by adding the following keys to your [media cache config](enterprise__cloud_media.md#enterprise-media-cache-config):
    
    
    {
        "minio_config_file": "/path/to/minio-config.ini",
        "minio_profile": "default"  # optional
    }
    

In the options above, the `.ini` file should have syntax similar the following:
    
    
    [default]
    access_key = ...
    secret_access_key = ...
    endpoint_url = ...
    alias = ...  # optional
    region = ...  # if applicable
    

When populating samples with MinIO filepaths, you can either specify paths by prefixing your MinIO endpoint URL:
    
    
    filepath = "${endpoint_url}/bucket/path/to/object.ext"
    
    # For example
    filepath = "https://voxel51.min.io/test-bucket/image.jpg"
    

or, if you have defined an alias in your config, you may instead prefix the alias:
    
    
    filepath = "${alias}://bucket/path/to/object.ext"
    
    # For example
    filepath = "minio://test-bucket/image.jpg"
    

If you would like to take advantage of browser caching you can [specify cache-control headers on MinIO content using the metadata field of the put_object API](https://min.io/docs/minio/linux/developers/python/API.html). By default Minio does not provide cache-control headers so it will be up to your browserâs heuristics engine to determine how long to cache the object.

### Extra client arguments#

Configuring credentials following the instructions above is almost always sufficient for FiftyOne Enterprise to properly utilize them. In rare cases where the cloud provider client needs non-default configuration, you can add extra client kwargs via the [media cache config](enterprise__cloud_media.md#enterprise-media-cache-config):
    
    
    {
        "extra_client_kwargs": {
            "azure": {"extra_kwarg": "value"},
            "gcs": {"extra_kwarg": "value"},
            "minio": {"extra_kwarg": "value"},
            "s3": {"extra_kwarg": "value"}
        }
    }
    

Provider names and the class that extra kwargs are passed to:

  * **azure** : `azure.identity.DefaultAzureCredential`
  * **gcs** : `google.cloud.storage.Client`
  * **minio** : `botocore.config.Config`
  * **s3** : `botocore.config.Config`



## Managed Cloud Credentials#

Cloud provider credentials can be managed directly on the Enterprise server. Managed credentials are automatically loaded for all matching media requests (App, local SDK, Delegated Operators, etc.) and stored encrypted in the Enterprise database, eliminating the need for environment variable configuration in your deployment.

Managed credentials can be scoped to be a specific user or user group, or be available globally to all users. Any user can configure credentials for their own use, while only admins can configure group specific or global credentials.

A managed credential can optionally be restricted to a specific list of bucket(s):

  * If one or more buckets are provided, the credentials are **bucket-specific credentials** that will only be used to read/write media within the specified bucket(s)

  * If no buckets are provided, the credentials are **default credentials** that will be used whenever trying to read/write any media for the provider that does not belong to a bucket with bucket-specific credentials




Note

Bucket-specific credentials are useful in situations where you cannot or do not wish to provide a single set of credentials to cover all buckets that your team plans to use within a given cloud storage provider.

When providing bucket-specific credentials, you may either provide bucket names like `my-bucket`, or you can provide fully-qualified buckets like `s3://my-bucket` and `https://voxel51.blob.core.windows.net/my-container`.

Managed credentials are considered unique based on the scope (user, group, or global), cloud provider, and the optional bucket(s) they are associated with. The system will look for credentials in the following default order, stopping once the first credential is found:

  1. If the current user has any bucket-specific credentials that match the bucket of the media being accessed, those credentials will be used

  2. If the current user belongs to any groups that have bucket-specific credentials that match the bucket of the media being accessed, those credentials will be used

  3. If any global bucket-specific credentials match the bucket of the media being accessed, those credentials will be used

  4. If the current user has any default credentials for the provider of the media being accessed, those credentials will be used

  5. If the current user belongs to any groups that have default credentials for the provider of the media being accessed, those credentials will be used

  6. If any global default credentials for the provider of the media being accessed exist, those credentials will be used




### Setting Managed Credentials#

Admins can configure cloud credentials via the Settings > Cloud storage page.

To upload a new credential, click the `Add credential` button:

![cloud-creds-add-credentials-button](../_images/cloud_creds_add_btn.png)

This will open a modal that you can use to add a credential for any of the available providers:

![blank-cloud-creds-modal](../_images/cloud_creds_modal_blank.png)

Note

Any credentials configured via environment variables in your deployment will not be displayed in this page.

After the appropriate files or fields are populated, click `Save credential` to store the (encrypted) credential.

Alternatively, credentials can be updated programmatically with the [`add_cloud_credentials()`](enterprise__management_sdk.md#fiftyone.management.cloud_credentials.add_cloud_credentials "fiftyone.management.cloud_credentials.add_cloud_credentials") method in the Management SDK.

Any cloud credentials uploaded via this method will automatically be used by the Enterprise UI when any user attempts to load media associated with the appropriate provider or specific bucket.

Note

By default, Enterprise servers refresh their credentials every 120 seconds, so you may need to wait up to two minutes after modifying your credentials via this page in order for the changes to take effect.

Note

Users cannot access stored credentials directly, either via the Enterprise UI or by using the Enterprise SDK locally. The credentials are only decrypted and used internally by the Enterprise servers.

### Cloud Credentials Origin Preference#

If credentials are configured both on the local machine and remotely via the Enterprise server, the behavior is for the Enterprise SDK to use the first matching set of credentials found.

  * When running the Enterprise SDK locally, the default is to use local credentials, if any exist, and otherwise to use managed credentials returned by the Enterprise server.

  * However, if the Enterprise SDK is being used in an Internal Service (App server, delegated operator, etc.) the default is to prefer managed credentials returned by the Enterprise server.




This can be manually controlled by setting the `FIFTYONE_CLOUD_CREDS_ORIGIN_PREFERENCE` environment variable on the machine to either `local` or `remote`. Regardless of the preference, credentials from both sources will be considered if the default location has none that match. So if credentials from the preferred source have no matches for a given request, credentials from the other source will be attempted before giving up.

### Cloud Credentials Local Download#

By default, users must set up local credentials when using the Enterprise SDK with an API connection. This is to prevent downloading credentials from the Enterprise server to that userâs local machine. However, you can change this default, so that local SDK usage will download credentials from the Enterprise server, and there is no need to configure credentials locally. To enable downloading of credentials to machines, set the environment variable `FEATURE_FLAG_ENABLE_CREDS_LOCAL_USE` to `True` in the `teams-api` container.

### AI Model Weights#

The FiftyOne Enterprise App ships with AI-assisted mask segmentation for annotation workflows. By default, the required model weights are served from Voxel51âs CDN and no configuration is required.

Deployments that prefer to serve the weights from their own infrastructure can set the optional `FIFTYONE_MODEL_WEIGHTS_BASE_SAM2` environment variable on the `fiftyone-app` container. The value is a base URL or cloud path that hosts the weights. The App appends the specific weight file to it at request time.

The base location must host the two files that the App fetches:

  * `encoder.with_runtime_opt.ort`

  * `decoder.onnx`




The SAM2 tiny variant is recommended for optimal user experience. The simplest way to populate your own location is to mirror the files Voxel51 serves from its CDN, which are the canonical artifacts that the App is built against:
    
    
    curl -sSL -o encoder.with_runtime_opt.ort \
        https://models-cdn.voxel51.com/sam2/encoder.with_runtime_opt.ort
    curl -sSL -o decoder.onnx \
        https://models-cdn.voxel51.com/sam2/decoder.onnx
    

Then upload both files to the location referenced by `FIFTYONE_MODEL_WEIGHTS_BASE_SAM2`.
    
    
    # Private GCS bucket
    FIFTYONE_MODEL_WEIGHTS_BASE_SAM2=gs://my-bucket/sam2
    
    # Private S3 bucket
    FIFTYONE_MODEL_WEIGHTS_BASE_SAM2=s3://my-bucket/sam2
    
    # Private HTTPS endpoint
    FIFTYONE_MODEL_WEIGHTS_BASE_SAM2=https://cdn.internal.example.com/sam2
    

When a cloud path is used, URLs are signed automatically using the deploymentâs cloud credentials, so the `fiftyone-app` container must have read access to the bucket.

IN THIS ARTICLE 
