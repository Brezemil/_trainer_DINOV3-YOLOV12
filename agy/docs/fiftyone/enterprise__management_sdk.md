---
source_url: https://docs.voxel51.com/enterprise/management_sdk.html
---

# Enterprise Management SDK#

One of FiftyOneâs core design principles is that you should be able to do everything _programmatically_ if you want.

To this end, the `fiftyone.management` module provides Enterprise-specific methods for managing users, invitations, dataset permissions, plugins, API keys, and more.

Note

You must use an [API connection](enterprise__api_connection.md#enterprise-api-connection) (not a direct MongoDB connection) in order to use Management SDK methods.

## API reference#

## Connections#

API connection.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.connection.APIClientConnection#
    

instance = None#
    

reload()#
    

property has_principal_endpoints: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

True if the connected API supports principal (user + SA) endpoints.

property client#
    

fiftyone.management.connection.reload_api_connection() → None#
    

Reloads the API connection.

This is necessary if the API URI or API key are changed after the first usage of this module.

Note

This should rarely be needed unless a script is working across deployments.

Examples:
    
    
    import fiftyone.management as fom
    import fiftyone as fo
    
    # https://api.dev.mycompany.org
    print(fo.config.api_uri)
    fom.whoami()
    
    # Change API URI, need to reload cached connection
    fo.config.api_uri = "https://api.test.mycompany.org"
    fom.reload_api_connection()
    fom.whoami()
    

fiftyone.management.connection.test_api_connection()#
    

Tests the API connection.

If the connection succeeds, a message will be printed. If the connection failes, an exception will be raised.

Examples:
    
    
    import fiftyone.management as fom
    fom.test_api_connection() # API connection succeeded
    

## API keys#

API key management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.api_key.ServiceAccount#
    

Service account information dataclass.

id: str#
    

name: str#
    

role: fiftyone.management.users.UserRole#
    

description: str | None = None#
    

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

fiftyone.management.api_key.resolve_service_account_id(_service_account_or_id : str | ServiceAccount | Dict[str, Any] | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → str | None#
    

Resolves a service account ID from an ID string, ServiceAccount instance, or a dict containing an `"id"` key.

class fiftyone.management.api_key.APIKey#
    

API key dataclass.

id: str#
    

name: str#
    

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

fiftyone.management.api_key.delete_api_key(_key : str_, _user : str | fiftyone.management.users.User | fiftyone.management.service_account.ServiceAccount | None = None_) → None#
    

Deletes the API key for the given user or service account (default: current user).

Note

Only admins can delete keys for other users.

Examples:
    
    
    import fiftyone.management as fom
    
    # Delete all keys from a user
    email = "user@company.com"
    for key in fom.list_api_keys(email):
        fom.delete_api_key(key.id, email)
    
    # Delete all keys from a service account
    sa = fom.get_service_account("some-id")
    for key in fom.list_api_keys(sa):
        fom.delete_api_key(key.id, sa)
    

Parameters:
    

  * **key** â the ID of the key to delete

  * **user** (_None_) â an optional user ID, email string, `User` instance, or `ServiceAccount` instance. Defaults to the current user.




fiftyone.management.api_key.generate_api_key(_key_name : str_, _user : str | fiftyone.management.users.User | fiftyone.management.service_account.ServiceAccount | None = None_) → str#
    

Generates an API key for the given user or service account (default: current user).

Note

Only admins can generate keys for other users.

Warning

Once generated, this key cannot be recovered! If itâs lost, you must generate a new key.

Examples:
    
    
    import fiftyone.management as fom
    
    # 1. Generate key for myself
    fom.generate_api_key("my-key")
    
    # 2.a Generate key for user@example.com
    fom.generate_api_key("your-key", "user@example.com")
    
    # 2.b Generate key for a service account
    sa = fom.get_service_account("some-id")
    fom.generate_api_key("sa-key", sa)
    

Parameters:
    

  * **key_name** â a descriptive name for the key

  * **user** (_None_) â an optional user ID, email string, `User` instance, or `ServiceAccount` instance. Defaults to the current user.



Returns:
    

the API key string

fiftyone.management.api_key.list_api_keys(_user : str | fiftyone.management.users.User | fiftyone.management.service_account.ServiceAccount | None = None_)#
    

Lists all API keys for the given user or service account (default: current user).

The returned key objects only have their name and IDs populated; the raw key is only available at time of generation.

Note

Only admins can request keys for other users.

Examples:
    
    
    import fiftyone.management as fom
    
    # 1. List my keys
    fom.list_api_keys()
    
    # 2.a List keys for user@example.com
    fom.list_api_keys("user@example.com")
    
    # 2.b List keys for a service account
    sa = fom.get_service_account("some-id")
    fom.list_api_keys(sa)
    

Parameters:
    

**user** (_None_) â an optional user ID, email string, `User` instance, or `ServiceAccount` instance. Defaults to the current user.

Returns:
    

a list of `APIKey` instances

## Cloud credentials#

Cloud credentials management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.cloud_credentials.CloudCredential#
    

Cloud Credentials Info

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

prefixes: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

provider: str#
    

description: str | None = None#
    

scope: str | None = None#
    

sid: str | None = None#
    

fiftyone.management.cloud_credentials.add_cloud_credentials(_provider : Literal['GCP', 'AWS', 'AZURE', 'MINIO']_, _credential_type : Literal['ini', 'json', 'factory']_, _credentials : str | Dict_, _description : str | None = None_, _prefixes : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str] | None = None_, _overwrite : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = True_, _user_id : str | None = None_, _user_group_id : str | None = None_) → None#
    

Adds cloud credentials to the system.

Credentials are stored in an encrypted format in the database.

Note

Admins can add cloud credentials for any user or group. Non-admin users may add credentials for their own user ID only.

Warning

This will overwrite any previously existing credentials with the same provider/prefixes combination.

Warning

Cloud credentials are made available for use for all app users (no access to the credentials themselves). This is for media only and doesnât affect FiftyOne dataset permissions.

Warning

Raw credentials are sent to the server in plaintext. Ensure that your connection to the server is secure (e.g., via HTTPS) to avoid credentials being intercepted in transit.

Examples:
    
    
    import os
    import fiftyone.management as fom
    
    # Add default GCP credentials from service account json file
    fom.add_cloud_credentials(
        "GCP",
        "json",
        "/path/to/gcp-svc-acct.json",
        description="Default GCP credentials"
    )
    
    # Add bucket-specific AWS credentials from .ini file
    fom.add_cloud_credentials(
        "AWS",
        "ini",
        "/path/to/aws-creds.ini",
        description="Readonly credentials for bucket1,bucket2",
        prefixes=["bucket1", "bucket2"]
    )
    
    # Add default AWS credentials from access keys
    formatted_credentials = fom.AwsCredentialsFactory.from_access_keys(
        access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        default_region="us-west-2"
    )
    
    fom.add_cloud_credentials(
        "AWS",
        "factory",
        formatted_credentials,
        description="Default AWS credentials from access keys"
    )
    

Parameters:
    

  * **provider** â the shorthand cloud provider string. One of [âGCPâ, âAWSâ, âAZUREâ, âMINIOâ]

  * **credential_type** â 

Type of credentials passed into `credentials` param. One of `["ini", "json", "factory"]`. `ini`: Path to an .ini file containing the credentials, such as

> `/Users/voxel51/.aws/credentials`

`json`: Path to a JSON file containing credentials, such as
    

`/Users/voxel51/.config/gcloud/service-account-creds.json`

`factory`: A `dict` returned by a class method in one of the
    

provider-specific credentials factories: `AwsCredentialsFactory`, `AzureCredentialsFactory`, `MinIoCredentialsFactory`

  * **credentials** â Dict of factory-built credentials or string path to credentials file, based on `credential_type` parameter.

  * **description** (`None`) â Optional description for this credential set.

  * **prefixes** (`None`) â The list of bucket names the credentials apply to, if applicable. Defaults to `None` meaning the default credentials for the provider.

  * **overwrite** (`True`) â Whether to overwrite existing credentials for the same provider/prefixes combination.

  * **user_id** (`None`) â The user ID that these credentials should be associated with, if any. Mutually exclusive with user_group_id.

  * **user_group_id** (`None`) â The user group ID that these credentials should be associated with, if any. Mutually exclusive with user_id.



Raises:
    

**ValueError** â if invalid provider is supplied

fiftyone.management.cloud_credentials.delete_cloud_credentials(_provider : Literal['GCP', 'AWS', 'AZURE', 'MINIO']_, _prefixes : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str] | None = None_, _user_id : str | None = None_, _user_group_id : str | None = None_) → None#
    

Deletes the installed cloud credentials.

Note

Admins can delete any cloud credentials. Non-admin users can only delete their own.

Warning

This will delete credentials for all app users in the system. Ensure there is another cloud media storage access method in place to avoid system outage.

Examples:
    
    
    import fiftyone.management as fom
    
    # Delete all credentials for a provider
    provider = "AWS"
    for credentials in fom.list_cloud_credentials():
        if credentials.provider == provider:
            fom.delete_cloud_credentials(provider, credentials.prefixes)
    

Parameters:
    

  * **provider** â the shorthand cloud provider string. One of [âGCPâ, âAWSâ, âAZUREâ, âMINIOâ]

  * **prefixes** (_None_) â The list of bucket names the credentials apply to, if applicable. Defaults to `None` meaning the default credentials for the provider.

  * **user_id** (`None`) â The user ID that these credentials are associated with, if any. Mutually exclusive with user_group_id.

  * **user_group_id** (`None`) â The user group ID that these credentials are associated with, if any. Mutually exclusive with user_id.



Raises:
    

**ValueError** â if invalid provider is supplied

fiftyone.management.cloud_credentials.list_cloud_credentials() → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[CloudCredential]#
    

Lists all cloud credentials installed in the system.

The returned credentials objects only have their provider, prefixes, description, and creation time set. You cannot view the plaintext or encrypted credentials.

Note

Only admins can list cloud credentials

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_cloud_credentials()
    

Returns:
    

a list of `CloudCredential` instances

class fiftyone.management.cloud_credentials.AwsCredentialsFactory#
    

Credential factory methods for Amazon AWS provider

classmethod from_access_keys(_access_key_id : str_, _secret_access_key : str_, _default_region : str | None = None_, _session_token : str | None = None_) → Dict[str, str]#
    

Get formatted AWS credentials from access keys.

For use in `fom.add_cloud_credentials()` only.

Parameters:
    

  * **access_key_id** â AWS access key ID

  * **secret_access_key** â AWS secret access key

  * **default_region** (`None`) â default AWS region to set

  * **session_token** (`None`) â AWS session token



Returns:
    

Formatted credentials

class fiftyone.management.cloud_credentials.AzureCredentialsFactory#
    

Credential factory methods for Microsoft Azure provider

classmethod from_sas_token(_account_name_ , _sas_token_ , _alias : str | None = None_) → Dict[str, str]#
    

Get formatted AZURE credentials from SAS token

For use in `fom.add_cloud_credentials()` only. Note: SAS tokens often times have `%` characters that need to be escaped to avoid interpolation. Make sure to escape them by replacing `%` with `%%` in the token string.

Parameters:
    

  * **account_name** â Azure account name

  * **sas_token** â Azure SAS token

  * **alias** (`None`) â alias to use for storage blobs



Returns:
    

Formatted credentials

classmethod from_account_key(_account_name_ , _account_key_ , _alias : str | None = None_) → Dict[str, str]#
    

Get formatted AZURE credentials from access keys

For use in `fom.add_cloud_credentials()` only.

Parameters:
    

  * **account_name** â Azure account name

  * **account_key** â Azure account key

  * **alias** (`None`) â alias to use for storage blobs



Returns:
    

Formatted credentials

classmethod from_connection_string(_connection_string_ , _alias : str | None = None_) → Dict[str, str]#
    

Get formatted AZURE credentials from connection string

For use in `fom.add_cloud_credentials()` only.

Parameters:
    

  * **connection_string** â Azure connection string

  * **alias** (`None`) â alias to use for storage blobs



Returns:
    

Formatted credentials

classmethod from_client_secret(_account_name_ , _client_id_ , _client_secret_ , _tenant_id_ , _alias : str | None = None_) → Dict[str, str]#
    

Get formatted AZURE credentials from client secret

For use in `fom.add_cloud_credentials()` only.

Parameters:
    

  * **account_name** â Azure account name

  * **client_id** â Azure client ID

  * **client_secret** â Azure client secret

  * **tenant_id** â Azure tenant ID

  * **alias** (`None`) â alias to use for storage blobs



Returns:
    

Formatted credentials

class fiftyone.management.cloud_credentials.MinIoCredentialsFactory#
    

Credential factory methods for MINIO provider

classmethod from_access_keys(_access_key_id : str_, _secret_access_key : str_, _endpoint_url : str_, _alias : str | None = None_, _default_region : str | None = None_) → Dict[str, str]#
    

Get formatted MINIO credentials from access keys

For use in `fom.add_cloud_credentials()` only.

Parameters:
    

  * **access_key_id** â MinIO access key ID

  * **secret_access_key** â MinIO secret access key

  * **endpoint_url** â MinIO endpoint URL

  * **alias** (`None`) â alias to use for storage blobs

  * **default_region** (`None`) â default MinIO region to set



Returns:
    

Formatted credentials

## Dataset permissions#

Dataset management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.dataset.UserGroup#
    

User Group information dataclass.

id: str#
    

name: str#
    

description: str | None#
    

principals: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[Any] | None = None#
    

cloud_credentials: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.management.cloud_credentials.CloudCredential] | None = None#
    

users: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.management.users.User] | None = None#
    

fiftyone.management.dataset.resolve_user_group_id(_group_or_id_or_name : str | UserGroup | None | dict_) → str#
    

Resolves group ID - by looking up group by name if it has to

exception fiftyone.management.dataset.FiftyOneManagementError(_message_)#
    

Exception raised for errors in the SDK.

message \-- explanation of the error
    

message#
    

add_note()#
    

Exception.add_note(note) â add a note to the exception

class args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.management.dataset.DatasetPermission(_* args_, _** kwds_)#
    

Dataset permission enum.

NO_ACCESS = 'NO_ACCESS'#
    

VIEW = 'VIEW'#
    

TAG = 'TAG'#
    

EDIT = 'EDIT'#
    

MANAGE = 'MANAGE'#
    

name()#
    

The name of the Enum member.

value()#
    

The value of the Enum member.

fiftyone.management.dataset.delete_dataset_user_permission(_dataset_name : str_, _user : str | fiftyone.management.users.User_) → None#
    

Removes the given userâs specific access to the given dataset.

Note

The caller must have `Can Manage` permissions on the dataset.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    user = "guest@company.com"
    
    fom.set_dataset_user_permission(dataset_name, user, fom.VIEW)
    
    fom.delete_dataset_user_permission(dataset_name, user)
    
    assert fom.get_permissions(dataset_name=dataset_name, user=user) == fom.NO_ACCESS
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **user** â a user ID, email string, or `User` instance.




fiftyone.management.dataset.get_dataset_creator(_dataset_name : str_) → fiftyone.management.users.User | None#
    

Gets creator of a dataset, if known.

Examples:
    
    
    import fiftyone.management as fom
    
    user = fom.get_dataset_creator("dataset")
    

Parameters:
    

**dataset_name** â the dataset name

Raises:
    

**ValueError** â if `dataset_name` does not exist or calling user does not have access to it.

Returns:
    

`User` instance, or `None` if dataset has no recorded creator.

fiftyone.management.dataset.get_permissions(_*_ , _dataset_name : str = None_, _user : str | fiftyone.management.users.User = None_, _user_group : str | fiftyone.management.user_groups.UserGroup = None_)#
    

Gets the specified dataset or user permissions.

This method is a convenience wrapper around the methods below based on which arguments you provide:

  * `dataset_name`: `get_permissions_for_dataset()`

  * `user`: `get_permissions_for_user()`

  * `user_group`: `get_permissions_for_dataset_user_group()`

  * `dataset_name` and `user`: `get_permissions_for_dataset_user()`

  * `dataset_name` and `user_group`:
    

`get_permissions_for_dataset_user_group()`




Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    user = "guest@company.com"
    
    # Get permissions for user
    assert (
        fom.get_permissions(user=user) ==
        fom.get_permissions_for_user(user)
    )
    
    # Get permissions for dataset
    assert (
        fom.get_permissions(dataset_name=dataset_name) ==
        fom.get_permissions_for_dataset(dataset_name)
    )
    
    # Get permissions for user-dataset combination
    assert (
        fom.get_permissions(dataset_name=dataset_name, user=user) ==
        fom.get_permissions_for_dataset_user(dataset_name, user)
    )
    
    # Get permissions for user group-dataset
    assert (
        fom.get_permissions(dataset_name=dataset_name,
            user_group="some-id") ==
        fom.get_permissions_for_dataset_user_group(dataset_name, "some-id")
    )
    

Parameters:
    

  * **dataset_name** (_None_) â a dataset name

  * **user** (_None_) â a user ID, email string, or `User` instance

  * **user_group** (_None_) â a user group ID or name string, or a `UserGroup` instance



Returns:
    

the requested user/dataset permissions

fiftyone.management.dataset.get_permissions_for_dataset(_dataset_name : str_, _include_groups =True_) → Dict#
    

Gets the list of users that have access to the given dataset.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    
    fom.get_permissions_for_dataset(dataset_name)
    

Example output:
    
    
    [
        {'name': 'A. User', 'email': 'a@company.com', 'id': '12345', 'permission': 'MANAGE'},
        {'name': 'B. User', 'email': 'b@company.com', 'id': '67890', 'permission': 'EDIT'},
    ]
    

Parameters:
    

**dataset_name** â the dataset name

Returns:
    

If include_groups is True, return a dictionary contains a list of user
    

info and group info. Otherwise, return a list of user info.

fiftyone.management.dataset.get_permissions_for_dataset_user(_dataset_name : str_, _user : str_) → DatasetPermission#
    

Gets the access permission (if any) that a given user has to a given dataset.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    user = "guest@company.com"
    
    fom.get_permissions_for_dataset_user(dataset_name, user)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **user** â a user ID, email string, or `User` instance



Returns:
    

`DatasetPermission`

fiftyone.management.dataset.get_permissions_for_dataset_user_group(_dataset_name : str_, _user_group : str | fiftyone.management.user_groups.UserGroup_) → DatasetPermission#
    

Gets the access permission (if any) that a given user group has to a given dataset.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    user_group = "interns"
    
    fom.get_permissions_for_dataset_user_group(dataset_name, user_group)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **user_group** â a user group ID or name string or `UserGroup`



Returns:
    

`DatasetPermission`

fiftyone.management.dataset.get_permissions_for_user(_user : str_)#
    

Gets a list of datasets a given user has access to.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    user = "guest@company.com"
    
    fom.get_permissions_for_user(user)
    

Example output:
    
    
    [
        {'name': 'datasetA', 'permission': 'EDIT'},
        {'name': 'datasetB', 'permission': 'VIEW'},
    ]
    

Parameters:
    

**user** â a user ID, email string, or `User` instance

Returns:
    

a list of permission dicts

fiftyone.management.dataset.get_permissions_for_user_group(_user_group : str | fiftyone.management.user_groups.UserGroup_)#
    

Gets a list of datasets a given user group has access to.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    user_group = "some-group-id"
    
    fom.get_permissions_for_user_group(user_group)
    

Example output:
    
    
    [
        {'name': 'datasetA', 'permission': 'EDIT'},
        {'name': 'datasetB', 'permission': 'VIEW'},
    ]
    

Parameters:
    

**user_group** â a user group ID or name or `UserGroup`

Returns:
    

a list of permission dicts

fiftyone.management.dataset.set_dataset_default_permission(_dataset_name : str_, _permission : DatasetPermission_) → None#
    

Sets the default member access level for the given dataset.

Note

The caller must have `Can Manage` permissions on the dataset.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    
    # Give every Member Edit access by default
    fom.set_dataset_default_permission(dataset_name, fom.EDIT)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **permission** â the `DatasetPermission` to set




fiftyone.management.dataset.set_dataset_user_permission(_dataset_name : str_, _user : str | fiftyone.management.users.User_, _permission : DatasetPermission_, _invite : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Grants the given user specific access to the given dataset at the specified permission level.

Note

The caller must have `Can Manage` permissions on the dataset.

Warning

If an unknown email is passed to this function and `invite` is `True`, an invitation to join the organization will be sent to the email. The user will be created and have access to the dataset on invitation acceptance. Please double-check the email correctness before running.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    guest = "guest@company.com"
    new_guest = "new-guest@company.com"
    
    # Existing user
    fom.set_dataset_user_permission(dataset_name, guest, fom.VIEW)
    
    assert fom.get_permissions(dataset_name=dataset_name, user=guest) == fom.VIEW
    
    # Nonexisting user
    fom.set_dataset_user_permission(dataset_name, new_guest, fom.VIEW, invite=True)
    assert guest in [i.invitee_email for i in fom.list_pending_invitations()]
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **user** â a user ID, email string, or `User` instance

  * **permission** â the `DatasetPermission` to grant

  * **invite** (_False_) â if `True` and `user` is an email, an invitation will be sent to join the organization.




fiftyone.management.dataset.set_dataset_user_group_permission(_dataset_name : str_, _user_group : str | fiftyone.management.user_groups.UserGroup_, _permission : str | DatasetPermission_) → None#
    

Grants the given user group specific access to the given dataset at the specified permission level.

Note

The caller must have `Can Manage` permissions on the dataset.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    group_id = "some-group-id"
    
    fom.set_dataset_user_permission(dataset_name, group_id, fom.VIEW)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **user_group** â a user group ID or name string or a `UserGroup` instance

  * **permission** â the `DatasetPermission`




fiftyone.management.dataset.remove_dataset_user_group_permission(_dataset_name : str_, _user_group : str | fiftyone.management.user_groups.UserGroup_) → None#
    

Remove the user groupâs explicit access to the given dataset

Note

The caller must have `Can Manage` permissions on the dataset.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset_name = "special-dataset"
    group_id = "some-group-id"
    
    fom.remove_dataset_user_group_permission(dataset_name, group_id)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **user_group** â a user group id or name string or a `UserGroup` instance




## Organization settings#

Organization settings management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.organization.OrganizationSettings#
    

default_user_role: fiftyone.management.users.UserRole#
    

default_dataset_permission: fiftyone.management.dataset.DatasetPermission#
    

default_operator_minimum_role: fiftyone.management.users.UserRole#
    

default_operator_minimum_dataset_permission: fiftyone.management.dataset.DatasetPermission#
    

fiftyone.management.organization.get_organization_settings() → OrganizationSettings#
    

Gets organization-wide settings for the FiftyOne Enterprise deployment.

Note

Only admins can retrieve this information

Examples:
    
    
    import fiftyone.management as fom
    
    fom.get_organization_settings()
    

Returns:
    

`OrganizationSettings`

fiftyone.management.organization.set_organization_settings(_*_ , _default_user_role : fiftyone.management.users.UserRole | None = None_, _default_dataset_permission : fiftyone.management.dataset.DatasetPermission | None = None_, _default_operator_minimum_role : fiftyone.management.users.UserRole | None = None_, _default_operator_minimum_dataset_permission : fiftyone.management.dataset.DatasetPermission | None = None_) → OrganizationSettings#
    

Sets organization-wide settings for the FiftyOne Enterprise deployment.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    user_role = fom.MEMBER
    dataset_perm = fom.EDIT
    
    # Set only default user role
    fom.set_organization_settings(default_user_role=user_role)
    
    # Set only default dataset permission
    fom.set_organization_settings(default_dataset_permission=dataset_perm)
    
    # Set multiple settings at once
    fom.set_organization_settings(
        default_user_role=user_role,
        default_dataset_permission=dataset_perm,
        default_operator_minimum_role=user_role,
        default_operator_minimum_dataset_permission=dataset_perm,
    )
    

Parameters:
    

  * **default_user_role** (_None_) â an optional `UserRole` to set.

  * **default_dataset_permission** (_None_) â an optional `DatasetPermission` to set,

  * **default_operator_minimum_role** (_None_) â an optional `UserRole` to set

  * **default_operator_minimum_dataset_permission** (_None_) â an optional `DatasetPermission` to set



Returns:
    

`OrganizationSettings`

## Plugin management#

Plugin management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.plugin.OperatorPermission#
    

Operator permission dataclass.

minimum_role: fiftyone.management.users.UserRole#
    

minimum_dataset_permission: fiftyone.management.dataset.DatasetPermission#
    

class fiftyone.management.plugin.PluginOperator#
    

Plugin operator dataclass.

name: str#
    

enabled: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

permission: OperatorPermission#
    

class fiftyone.management.plugin.Plugin#
    

Plugin dataclass.

name: str#
    

description: str#
    

version: str#
    

fiftyone_version: str#
    

enabled: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

operators: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[PluginOperator]#
    

fiftyone.management.plugin.list_plugins(_include_builtin : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[Plugin]#
    

Returns a list of all installed plugins in the FiftyOne Enterprise deployment.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_plugins()
    

Parameters:
    

**include_builtin** (_False_) â whether to include builtin plugins

Returns:
    

a list of `Plugin` instances

fiftyone.management.plugin.get_plugin_info(_plugin_name : str_) → Plugin#
    

Gets information about the specified plugin in the FiftyOne Enterprise deployment.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.get_plugin_info("my-plugin")
    

Parameters:
    

**plugin_name** â a plugin name

Returns:
    

`Plugin`, or `None` if no such plugin is found

fiftyone.management.plugin.upload_plugin(_plugin_path : str_, _overwrite : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _optimize =False_) → Plugin#
    

Uploads a plugin to the FiftyOne Enterprise deployment.

The local plugin must be a zip file that contains a single directory with a `fiftyone.yml` or `fiftyone.yaml` file. For example:
    
    
    my_plugin/
        fiftyone.yml
        __init__.py
        data.txt
    

Note

Only admins can upload plugins.

Examples:
    
    
    import fiftyone.management as fom
    
    # Upload a raw plugin directory
    fom.upload_plugin("/path/to/plugin_dir", overwrite=True)
    
    # Upload a plugin, optimizing the directory before the upload
    fom.upload_plugin("/path/to/plugin_dir", overwrite=True, optimize=True)
    
    # Upload a plugin as ZIP file
    fom.upload_plugin("/path/to/plugin.zip", overwrite=True)
    

Parameters:
    

  * **plugin_path** â the path to a plugin zip or directory

  * **overwrite** (_False_) â whether to overwrite an existing plugin with same name

  * **optimize** (_False_) â whether to optimize the created zip file before uploading. If a `.gitignore` file exists, an attempt will first be made to use `git archive` to create the zip. If not or this doesnât work, a zip will be created by pruning various known system-generated files and directories such as `.git/` and `__pycache__/`. This argument has no effect if `plugin_path` does not point to a directory




fiftyone.management.plugin.delete_plugin(_plugin_name : str_) → None#
    

Deletes the given plugin from the FiftyOne Enterprise deployment.

Examples:
    
    
    import fiftyone.management as fom
    
    plugin_name = "special-plugin"
    fom.delete_plugin(plugin_name)
    
    plugins = fom.list_plugins()
    assert not any(plugin.name == plugin_name for plugin in plugins)
    

Note

Only admins can perform this action.

Parameters:
    

**plugin_name** â a plugin name

fiftyone.management.plugin.download_plugin(_plugin_name : str_, _download_dir : str_) → str#
    

Downloads a plugin from the FiftyOne Enterprise deployment.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.download_plugin("special-plugin", "/path/to/local/plugins/")
    

Parameters:
    

  * **plugin_name** â a plugin name

  * **download_dir** â a directory into which to download the plugin



Returns:
    

the path to the downloaded plugin

fiftyone.management.plugin.set_plugin_enabled(_plugin_name : str_, _enabled : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")_) → None#
    

Sets the enabled status of the given plugin in the FiftyOne Enterprise deployment.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    # Disable whole plugin
    fom.set_plugin_enabled("special-plugin", False)
    

Parameters:
    

  * **plugin_name** â a plugin name

  * **enabled** â a bool specifying what to set enabled status to




fiftyone.management.plugin.set_plugin_operator_enabled(_plugin_name : str_, _operator_name : str_, _enabled : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")_) → None#
    

Sets the enabled status of the given plugin operator in the FiftyOne Enterprise deployment.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    # Disable a particular operator
    fom.set_plugin_operator_enabled("special-plugin", "special-operator", False)
    

Parameters:
    

  * **plugin_name** â a plugin name

  * **operator_name** â an operator name within the given plugin

  * **enabled** â a bool specifying what to set operator enabled status to




fiftyone.management.plugin.set_plugin_operator_permissions(_plugin_name : str_, _operator_name : str_, _minimum_role : fiftyone.management.users.UserRole | None = None_, _minimum_dataset_permission : fiftyone.management.dataset.DatasetPermission | None = None_)#
    

Sets permission levels of the given plugin operator in the FiftyOne Enterprise deployment.

At least one of `minimum_role` and `minimum_dataset_permission` must be set.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    plugin_name = "special-plugin"
    operator_name = "special-operator"
    
    # Set minimum role permission only
    fom.set_plugin_operator_permissions(
        plugin_name,
        operator_name,
        minimum_role=fom.MEMBER
        )
    
    # Set minimum dataset permission only
    fom.set_plugin_operator_permissions(
        plugin_name,
        operator_name,
        minimum_dataset_permission=fom.EDIT
    )
    
    # Set both minimum role and minimum dataset permissions
    fom.set_plugin_operator_permissions(
        plugin_name,
        operator_name,
        minimum_role=fom.EDIT,
        minimum_dataset_permission=fom.EDIT
    )
    

Parameters:
    

  * **plugin_name** â a plugin name

  * **operator_name** â an operator name within the given plugin

  * **minimum_role** (_None_) â an optional `UserRole` to set

  * **minimum_dataset_permission** (_None_) â an optional `DatasetPermission` to set




## Orchestrator management#

Orchestrator management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.orchestrator.OrchestratorEnvironment#
    

Orchestrator environment types.

DATABRICKS = 'databricks'#
    

ANYSCALE = 'anyscale'#
    

KUBERNETES = 'kubernetes'#
    

SELF_REGISTERED = 'self_registered'#
    

map_to_graphql_value() → str#
    

Maps the enum value to its GraphQL value

classmethod map_from_graphql_value(_value : str_) → OrchestratorEnvironment#
    

Maps a GraphQL value to the enum value

capitalize()#
    

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()#
    

Return a version of the string suitable for caseless comparisons.

center()#
    

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count()#
    

S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

encode()#
    

Encode the string using the codec registered for encoding.

encoding
    

The encoding in which to encode the string.

errors
    

The error handling scheme to use for encoding errors. The default is âstrictâ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are âignoreâ, âreplaceâ and âxmlcharrefreplaceâ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

endswith()#
    

S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

expandtabs()#
    

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find()#
    

S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format()#
    

S.format(*args, **kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (â{â and â}â).

format_map()#
    

S.format_map(mapping) -> str

Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (â{â and â}â).

index()#
    

S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()#
    

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isalpha()#
    

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isascii()#
    

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

isdecimal()#
    

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()#
    

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isidentifier()#
    

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as âdefâ or âclassâ.

islower()#
    

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isnumeric()#
    

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isprintable()#
    

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

isspace()#
    

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

istitle()#
    

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isupper()#
    

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

join()#
    

Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: â.â.join([âabâ, âpqâ, ârsâ]) -> âab.pq.rsâ

ljust()#
    

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#
    

Return a copy of the string converted to lowercase.

lstrip()#
    

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

partition()#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

removeprefix()#
    

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

removesuffix()#
    

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

replace()#
    

Return a copy with all occurrences of substring old replaced by new.

> count
>     
> 
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

rfind()#
    

S.rfind(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex()#
    

S.rindex(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust()#
    

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition()#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

rsplit()#
    

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

rstrip()#
    

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split()#
    

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

splitlines()#
    

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

startswith()#
    

S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

strip()#
    

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#
    

Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()#
    

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

translate()#
    

Replace each character in the string using the given translation table.

> table
>     
> 
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()#
    

Return a copy of the string converted to uppercase.

zfill()#
    

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

name()#
    

The name of the Enum member.

value()#
    

The value of the Enum member.

class fiftyone.management.orchestrator.OrchestratorDocument#
    

Orchestrator document representation.

instance_identifier: str#
    

description: str = None#
    

environment: str#
    

available_operators: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str] = None#
    

config: Dict | None = None#
    

secrets: Dict | None = None#
    

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

updated_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

fiftyone.management.orchestrator.get_orchestrator(_instance_id : str_, _user : str | fiftyone.management.users.User = None_) → OrchestratorDocument#
    

Retrieves an orchestrator by its instance identifier.

Parameters:
    

  * **instance_id** â the instance identifier / unique name of the orchestrator

  * **user** â the user requesting the orchestrator (optional)



Returns:
    

the orchestrator document

Raises:
    

**ValueError** â if the orchestrator doesnât exist

fiftyone.management.orchestrator.list_orchestrators(_include_deactivated : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

Lists orchestrators with pagination, filtering, and sorting.

Parameters:
    

  * **page** â the page number (1-indexed)

  * **filters** â filter criteria (e.g., {âinclude_deactivatedâ: True})



Returns:
    

a list of orchestrator instance_identifiers

fiftyone.management.orchestrator.register_orchestrator(_instance_id : str_, _description : str_, _environment : str | OrchestratorEnvironment_, _config : Dict | None_, _secrets : Dict | None_) → OrchestratorDocument#
    

Registers a new orchestrator to run delegated operations.

Any secrets provided will be stored in the FiftyOne [secrets store](https://docs.voxel51.com/enterprise/secrets.html), encrypted.

Parameters:
    

  * **instance_id** â the instance identifier of the orchestrator

  * **description** â the description of the orchestrator

  * **environment** â the orchestrator environment (e.g., âdatabricksâ, âanyscaleâ, âkubernetesâ)

  * **config** â environment-specific configuration

  * **secrets** â environment-specific secrets




Note

The `config` and `secrets` fields must include a top-level key that corresponds to the environment

Warning

Raw secret values are sent to the server in plaintext. Ensure that your connection to the server is secure (e.g., via HTTPS) to avoid secrets being intercepted in transit.

Examples:
    
    
    # databricks config example
    {
        "databricks": {
            "jobId": "1234567890abcdef",
            "executionTaskId": "0987654321fedcba",
            "registrationTaskId": "a12b3c4d"
        }
    }
    
    # anyscale config example
    {
        "anyscale": {
            "jobQueueName": "JobQueueName",
            "imageUri": "an-image-uri",
            "executionComputeConfig": "exec-config"
        }
    }
    
    # kubernetes config example
    {
        "kubernetes": {
            "executionTmplUri": "/uri/to/template", # URI OR base64-encoded
            "registrationTmplUri": "/optional/uri", # CPU or lower resources
            "context": "kube context to use",       # Optional
            "namespace": "namespace to deploy to"   # Optional
        }
    }
    
    # databricks secrets example
    {
        "databricks": {
            "host": "host_name",
            "accountId": "account_id",
            "clientId": "your_client_id",
            "clientSecret": "your_client_secret",
        }
    }
    
    # anyscale secrets example
    {
        "anyscale": {
            "authToken": "your_auth_token",
        }
    }
    
    # kubernetes secrets example
    {
        "kubernetes": {
            "kubeConfig": "kubeConfig or empty for in_cluster creds",
        }
    }
    

Returns:
    

the registered orchestrator document

Raises:
    

**ValueError** â if environment is invalid or config is missing required fields

fiftyone.management.orchestrator.delete_orchestrator(_instance_id : str_) → None#
    

Deletes an orchestrator by its instance identifier.

Parameters:
    

**instance_id** â the instance identifier of the orchestrator to delete

Raises:
    

**ValueError** â if the orchestrator doesnât exist

## Secrets#

Secrets management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.secret.FiftyOneSecret#
    

Secret Info

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

key: str#
    

description: str | None = None#
    

fiftyone.management.secret.add_secret(_key : str_, _value : str_, _description : str | None = None_) → None#
    

Adds a secret for use by FiftyOne plugins.

Secrets are stored in an encrypted format in the database.

Note

Only admins can add secrets.

Warning

Raw secret values are sent to the server in plaintext. Ensure that your connection to the server is secure (e.g., via HTTPS) to avoid secrets being intercepted in transit.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.add_secret(
        "MY_SECRET",
        "PASSWORD12345",
        description="very secure secret"
    )
    

Parameters:
    

  * **key** â String key of the secret.

  * **value** â Value to give the secret. Itâs encrypted upon upload.

  * **description** (`None`) â Optional description for this secret.




fiftyone.management.secret.delete_secret(_key : str_) → None#
    

Deletes the uploaded secret.

Note

Only admins can delete secrets.

Warning

This will delete the secret for all users. A new value will need to be uploaded if a plugin requires this secret.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.delete_secret("MY_SECRET")
    

Parameters:
    

**key** â string key of secret to delete

fiftyone.management.secret.get_secret_info(_key : str_) → FiftyOneSecret | None#
    

Get information about a FiftyOne secret.

The returned secret object only has certain fields set. You cannot view the plaintext or encrypted value of the secret.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.get_secret_info("MY_SECRET")
    

Parameters:
    

**key** â string key of secret to get info on

Returns:
    

A `FiftyOneSecret` instance, or None if the secret doesnât exist.

fiftyone.management.secret.list_secrets() → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

Lists the keys for all secrets installed in the system.

The returned secret object only have their provider, prefixes, description, and creation time set. You cannot view the plaintext or encrypted value.

Note

Only admins can list secrets

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_secrets()
    

Returns:
    

a list of `FiftyOneSecret` instances

fiftyone.management.secret.update_secret(_key : str_, _value : str | None = None_, _description : str | None = None_) → None#
    

Updates an existing secret for use by FiftyOne plugins.

Secrets are stored in an encrypted format in the database.

Note

Only admins can update secrets.

Warning

Raw secret values are sent to the server in plaintext. Ensure that your connection to the server is secure (e.g., via HTTPS) to avoid secrets being intercepted in transit.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.update_secret(
        "MY_SECRET",
        "PASSWORD12345",
        description="very secure secret"
    )
    

Parameters:
    

  * **key** â String key of the existing secret.

  * **value** (`None`) â Optional Value to update on the secret.

  * **description** (`None`) â Optional description to update on the secret.




## Snapshots#

Dataset snapshot management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.snapshot.DatasetSnapshotStatus(_* args_, _** kwds_)#
    

User role enum.

UNLOADED = 'UNLOADED'#
    

LOADING = 'LOADING'#
    

LOADED = 'LOADED'#
    

name()#
    

The name of the Enum member.

value()#
    

The value of the Enum member.

class fiftyone.management.snapshot.SampleChangeSummary#
    

total_samples: int#
    

num_samples_added: int#
    

num_samples_deleted: int#
    

num_samples_changed: int#
    

updated_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

class fiftyone.management.snapshot.DatasetSnapshot#
    

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

description: str | None#
    

id: str#
    

linear_change_summary: SampleChangeSummary | None#
    

load_status: DatasetSnapshotStatus#
    

name: str#
    

slug: str#
    

created_by: str | None = None#
    

created_by_principal: dict | None = None#
    

fiftyone.management.snapshot.MATERIALIZE_SNAPSHOT_TIMEOUT = 3600#
    

fiftyone.management.snapshot.DELETE_SNAPSHOT_TIMEOUT = 600#
    

fiftyone.management.snapshot.CALCULATE_CHANGES_TIMEOUT = 3600#
    

fiftyone.management.snapshot.archive_snapshot(_dataset_name : str_, _snapshot_name : str_) → None#
    

Archive snapshot to the configured cold storage location.

Note

Only users with `MANAGE` access can create a snapshot

Warning

Archiving a snapshot will make it unavailable for browsing to any user, even if they are currently using/browsing.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.management as fom
    
    snapshot_name = "v0.1"
    # We don't use this regularly, archive it!
    fom.archive_snapshot(dataset.name, snapshot_name)
    
    fo.load_dataset(dataset.name, snapshot_name) # throws error, can't load!
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **snapshot_name** â the snapshot name




fiftyone.management.snapshot.calculate_dataset_latest_changes_summary(_dataset_name : str_) → SampleChangeSummary#
    

Calculate change summary between recent snapshot and HEAD of dataset.

Examples:
    
    
    import fiftyone.management as fom
    
    old = fom.calculate_dataset_latest_changes_summary(dataset.name)
    assert old == fom.get_dataset_latest_changes_summary(dataset.name)
    
    dataset.delete_samples(dataset.take(5))
    
    # Cached summary hasn't been updated
    assert old == fom.get_dataset_latest_changes_summary(dataset.name)
    
    new = fom.calculate_dataset_latest_changes_summary(dataset.name)
    assert new.updated_at > changes.updated_at
    

Parameters:
    

**dataset_name** â the dataset name

Returns:
    

Change summary between most recent snapshot and HEAD of this dataset.

fiftyone.management.snapshot.create_snapshot(_dataset_name : str_, _snapshot_name : str_, _description : str | None = None_) → DatasetSnapshot#
    

Create and store a snapshot of the current state of `dataset_name`.

Snapshot name must be unique for the given dataset.

Note

Only users with `MANAGE` access can create a snapshot

Examples:
    
    
    import fiftyone.management as fom
    
    snapshot_name = "v0.1"
    description = "Initial dataset snapshot"
    fom.create_snapshot(dataset.name, snapshot_name, description)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **snapshot_name** â the name of the snapshot to create

  * **description** (_None_) â Optional description to attach to this snapshot




fiftyone.management.snapshot.delete_snapshot(_dataset_name : str_, _snapshot_name : str_)#
    

Delete snapshot `snapshot_name` from dataset `dataset_name`.

Note

Only users with `MANAGE` access can delete a snapshot.

Examples:
    
    
    import fiftyone.management as fom
    
    snapshot_name = "v0.1"
    description = "Initial dataset snapshot"
    fom.create_snapshot(dataset.name, snapshot_name, description)
    
    # Some time later ...
    
    fom.delete_snapshot(dataset, snapshot_name)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **snapshot_name** â the snapshot name




fiftyone.management.snapshot.get_dataset_latest_changes_summary(_dataset_name : str_) → SampleChangeSummary#
    

Gets change summary between most recent snapshot and HEAD of dataset

Note

This summary is not continuously computed, the result of this function may be stale. Use `calculate_dataset_latest_changes_summary()` to recalculate.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.get_dataset_latest_changes_summary(dataset.name)
    

Parameters:
    

**dataset_name** â the dataset name

Returns:
    

Change summary between most recent snapshot and HEAD of this dataset.
    

Or `None` if no summary has been calculated yet.

Raises:
    

**ValueError** â if dataset doesnât exist or no access

fiftyone.management.snapshot.get_snapshot_info(_dataset_name : str_, _snapshot_name : str_) → DatasetSnapshot | None#
    

Gets information about the specified dataset snapshot, or `None`
    

if `snapshot_name` doesnât exist.

Examples:
    
    
    import fiftyone.management as fom
    
    dataset = "quickstart"
    snapshot_name = "v0.1"
    
    fom.get_snapshot_info(dataset.name, snapshot_name)
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **snapshot_name** â the snapshot name



Raises:
    

**ValueError** â if dataset doesnât exist or no access

fiftyone.management.snapshot.list_snapshots(_dataset_name : str_) → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

Returns a list of all snapshots of a dataset in order of creation.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_snapshots(dataset.name)
    

Parameters:
    

**dataset_name** â the dataset name

Raises:
    

**ValueError** â if dataset doesnât exist or no access

Returns:
    

a list of `DatasetSnapshot` instances

fiftyone.management.snapshot.revert_dataset_to_snapshot(_dataset_name : str_, _snapshot_name : str_)#
    

Revert dataset to a previous snapshot state.

Reverts the current (HEAD) state of `dataset_name` to a previous state encapsulated by the snapshot `snapshot_name`. All changes since then are lost. All snapshots created after this one will be deleted as well.

If you are attempting to view the dataset at the point of a snapshot but not completely revert, you can do so with:

> snapshot = fo.load_dataset(dataset_name, snapshot=snapshot_name)

Note

Only users with `MANAGE` access can revert a dataset

Warning

This action is very destructive! All changes between `snapshot_name` and the current HEAD state of `dataset_name` will be destroyed! Including all snapshots created after `snapshot_name`.

Examples:
    
    
    import fiftyone.management as fom
    
    snapshot_name = "v0.1"
    description = "Initial dataset snapshot"
    fom.create_snapshot(dataset.name, snapshot_name, description)
    
    # Oops we deleted everything!
    dataset.delete_samples(dataset.values("id"))
    
    # Phew!
    fom.revert_dataset_to_snapshot(dataset.name, snapshot_name)
    dataset.reload()
    assert len(dataset) > 0
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **snapshot_name** â the snapshot name




fiftyone.management.snapshot.unarchive_snapshot(_dataset_name : str_, _snapshot_name : str_) → None#
    

Unarchive snapshot from the configured cold storage location.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.management as fom
    
    snapshot_name = "v0.1"
    description = "Initial dataset snapshot"
    
    # We don't use this regularly, archive it!
    fom.archive_snapshot(dataset.name, snapshot_name)
    fo.load_dataset(dataset.name, snapshot_name) # throws error, can't load!
    
    # Oops we need it now, unarchive it!
    fom.unarchive_snapshot(dataset.name, snapshot_name)
    fo.load_dataset(dataset.name, snapshot_name) # works now!
    

Parameters:
    

  * **dataset_name** â the dataset name

  * **snapshot_name** â the snapshot name




## Service account management#

Service accounts can be managed programmatically using the SDK. For an overview of service accounts, their roles, and UI management, see [Service accounts](enterprise__roles_and_permissions.md#enterprise-service-accounts).
    
    
    import fiftyone.management as fom
    
    # Create a service account
    sa = fom.create_service_account("my-pipeline-bot", fom.MEMBER)
    print(sa.id)
    
    # List all service accounts
    service_accounts = fom.list_service_accounts()
    
    # Retrieve a specific service account by ID
    sa = fom.get_service_account(sa.id)
    
    # Update a service account's name, role, or description
    fom.update_service_account(
        sa, role=fom.COLLABORATOR, description="Automation bot for dataset tasks"
    )
    
    # Delete a service account (irreversible)
    fom.delete_service_account(sa)
    

API keys can be generated, listed, and deleted for service accounts:
    
    
    import fiftyone.management as fom
    
    sa = fom.get_service_account("some-id")
    
    # Generate an API key for the service account
    key = fom.generate_api_key("pipeline-key", sa)
    
    # List all keys for a service account
    keys = fom.list_api_keys(sa)
    
    # Delete a specific key
    fom.delete_api_key(keys[0].id, sa)
    

Service account management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


exception fiftyone.management.service_account.FiftyOneManagementError(_message_)#
    

Exception raised for errors in the SDK.

message \-- explanation of the error
    

message#
    

add_note()#
    

Exception.add_note(note) â add a note to the exception

class args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.management.service_account.UserRole(_* args_, _** kwds_)#
    

User role enum.

ADMIN = 'ADMIN'#
    

MEMBER = 'MEMBER'#
    

COLLABORATOR = 'COLLABORATOR'#
    

LABELER = 'LABELER'#
    

GUEST = 'GUEST'#
    

name()#
    

The name of the Enum member.

value()#
    

The value of the Enum member.

class fiftyone.management.service_account.ServiceAccount#
    

Service account information dataclass.

id: str#
    

name: str#
    

role: fiftyone.management.users.UserRole#
    

description: str | None = None#
    

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

fiftyone.management.service_account.create_service_account(_name : str_, _role : str | fiftyone.management.users.UserRole_, _description : str | None = None_) → ServiceAccount#
    

Creates a new service account.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    sa = fom.create_service_account("my-bot", fom.MEMBER)
    print(sa.id)
    

Parameters:
    

  * **name** â the service account name

  * **role** â the `UserRole` to grant

  * **description** (_None_) â optional description



Returns:
    

a `ServiceAccount` instance

fiftyone.management.service_account.get_service_account(_service_account_id : str_) → ServiceAccount | None#
    

Gets information about the specified service account (if any).

Note

Only admins can retrieve information about service accounts.

Examples:
    
    
    import fiftyone.management as fom
    
    sa = fom.get_service_account("some-id")
    

Parameters:
    

**service_account_id** â a service account ID string

Returns:
    

a `ServiceAccount` instance, or `None` if not found

fiftyone.management.service_account.list_service_accounts() → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[ServiceAccount]#
    

Returns a list of all service accounts.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_service_accounts()
    

Returns:
    

a list of `ServiceAccount` instances

fiftyone.management.service_account.update_service_account(_service_account : str | ServiceAccount_, _name : str | None = None_, _role : str | fiftyone.management.users.UserRole | None = None_, _description : str | None = None_) → ServiceAccount#
    

Updates the given service account.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.update_service_account("some-id", role=fom.ADMIN)
    

Parameters:
    

  * **service_account** â a service account ID string or `ServiceAccount` instance

  * **name** (_None_) â optional new name

  * **role** (_None_) â optional new `UserRole`

  * **description** (_None_) â optional new description



Returns:
    

the updated `ServiceAccount` instance

fiftyone.management.service_account.delete_service_account(_service_account : str | ServiceAccount_) → None#
    

Deletes the given service account.

Note

Only admins can perform this action.

Warning

This action is irreversible!

Examples:
    
    
    import fiftyone.management as fom
    
    fom.delete_service_account("some-id")
    

Parameters:
    

**service_account** â a service account ID string or `ServiceAccount` instance

fiftyone.management.service_account.resolve_service_account_id(_service_account_or_id : str | ServiceAccount | Dict[str, Any] | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → str | None#
    

Resolves a service account ID from an ID string, ServiceAccount instance, or a dict containing an `"id"` key.

## User management#

User management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


class fiftyone.management.users.CloudCredential#
    

Cloud Credentials Info

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

prefixes: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

provider: str#
    

description: str | None = None#
    

scope: str | None = None#
    

sid: str | None = None#
    

class fiftyone.management.users.UserGroupRef#
    

dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping objectâs

> (key, value) pairs

dict(iterable) -> new dictionary initialized as if via:
    

d = {} for k, v in iterable:

> d[k] = v

dict(**kwargs) -> new dictionary initialized with the name=value pairs
    

in the keyword argument list. For example: dict(one=1, two=2)

id: str#
    

name: str#
    

clear()#
    

D.clear() -> None. Remove all items from D.

copy()#
    

D.copy() -> a shallow copy of D

get()#
    

Return the value for key if key is in the dictionary, else default.

items()#
    

D.items() -> a set-like object providing a view on Dâs items

keys()#
    

D.keys() -> a set-like object providing a view on Dâs keys

pop()#
    

D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem()#
    

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault()#
    

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update()#
    

D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

values()#
    

D.values() -> an object providing a view on Dâs values

class fiftyone.management.users.UserRole(_* args_, _** kwds_)#
    

User role enum.

ADMIN = 'ADMIN'#
    

MEMBER = 'MEMBER'#
    

COLLABORATOR = 'COLLABORATOR'#
    

LABELER = 'LABELER'#
    

GUEST = 'GUEST'#
    

name()#
    

The name of the Enum member.

value()#
    

The value of the Enum member.

class fiftyone.management.users.User#
    

User information dataclass.

id: str#
    

name: str#
    

email: str#
    

role: UserRole#
    

cloud_credentials: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.management.cloud_credentials.CloudCredential] | None = None#
    

user_groups: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[UserGroupRef] | None = None#
    

class fiftyone.management.users.Invitation#
    

Invitation dataclass.

id: str#
    

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

expires_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

invitee_email: str#
    

invitee_role: UserRole#
    

url: str#
    

fiftyone.management.users.delete_user(_user : str | User_) → None#
    

Deletes the given user.

Note

Only admins can perform this action.

Warning

This action is irreversible! Once deleted, the user will have to be re-invited to the organization to have access again.

Examples:
    
    
    import fiftyone.management as fom
    
    delete_user = "guest@company.com"
    
    fom.delete_user(delete_user)
    
    assert fom.get_user(delete_user) is None
    

Parameters:
    

**user** â a user ID, email string, or `User` instance

fiftyone.management.users.delete_user_invitation(_invitation : str_) → None#
    

Deletes/revokes a previously-sent invitation if it has not been accepted.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    new_guest = "guest@company.com"
    
    invite_id = fom.send_user_invitation(new_guest, fom.GUEST)
    
    # Delete by invitation ID
    fom.delete_user_invitation(invite_id)
    
    # Delete by user email
    fom.delete_user_invitation(new_guest)
    
    pending = fom.list_pending_invitations()
    assert not any(p.id == invite_id for p in pending)
    

Parameters:
    

**invitation** â an invitation ID as returned by `send_user_invitation()`, or email address

fiftyone.management.users.get_user(_user : str_) → User | None#
    

Gets information about the specified user (if any).

Note

Only admins can retrieve information about other users.

Examples:
    
    
    import fiftyone.management as fom
    
    known_user = "member@company.com"
    user = fom.get_user(known_user)
    assert user.email == known_user
    
    unknown_user = "unknown@company.com"
    assert fom.get_user(unknown_user) is None
    

Parameters:
    

**user** â a user ID or email string

Returns:
    

`User`, or `None` if no such user is found

fiftyone.management.users.list_pending_invitations() → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[Invitation]#
    

Returns a list of pending user invitations.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_pending_invitations()
    

Returns:
    

a list of `Invitation` instances

fiftyone.management.users.list_users(_verbose =True_) → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[User] | [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

Returns a list of all users.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_users()
    

Parameters:
    

**verbose** (_True_) â if True, return a list of `User` instances; if False, return a list of user emails

Returns:
    

a list of `User` instances

fiftyone.management.users.send_user_invitation(_email : str_, _role : UserRole_) → str#
    

Sends an email invitation to join your FiftyOne Enterprise organization.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    new_guest = "guest@company.com"
    
    invite_id = fom.send_user_invitation(new_guest, fom.GUEST)
    
    pending = fom.list_pending_invitations()
    assert any(p.invitee_email == new_guest for p in pending)
    

Parameters:
    

  * **email** â the email address

  * **role** â the `UserRole` to grant the new user



Returns:
    

the invitation ID string

fiftyone.management.users.set_user_role(_user : str | User_, _role : UserRole_) → None#
    

Sets the role of the given user.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    user = "user@company.com"
    
    #1.a set role from email
    fom.set_user_role(user, fom.MEMBER)
    
    #1.b set role from user instance
    user_obj = fom.get_user(user_obj)
    fom.set_user_role(user_obj, fom.MEMBER)
    
    assert fom.get_user(user).role == fom.MEMBER
    

Parameters:
    

  * **user** â a user ID, email string, or `User` instance

  * **role** â the `UserRole` to set




fiftyone.management.users.whoami() → User#
    

Returns information about the calling user.

Note

This function is only supported for human users. Service accounts should use `fiftyone.management.get_service_account()` instead.

Examples:
    
    
    import fiftyone.management as fom
    
    me = fom.whoami()
    
    assert fom.get_user(me.id) == me
    

Returns:
    

`User`

fiftyone.management.users.resolve_user_id(_user_or_id_or_email : str | User | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _pass_unknown_email : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → str | None#
    

Resolves user ID - by looking up user by email if it has to

## Group management#

Group management.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


fiftyone.management.user_groups.logger#
    

exception fiftyone.management.user_groups.FiftyOneEnterpriseAPIError#
    

Base error for the FiftyOne Enterprise API.

add_note()#
    

Exception.add_note(note) â add a note to the exception

class args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.management.user_groups.CloudCredential#
    

Cloud Credentials Info

created_at: [datetime.datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

prefixes: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

provider: str#
    

description: str | None = None#
    

scope: str | None = None#
    

sid: str | None = None#
    

class fiftyone.management.user_groups.APIClientConnection#
    

instance = None#
    

reload()#
    

property has_principal_endpoints: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

True if the connected API supports principal (user + SA) endpoints.

property client#
    

exception fiftyone.management.user_groups.FiftyOneManagementError(_message_)#
    

Exception raised for errors in the SDK.

message \-- explanation of the error
    

message#
    

add_note()#
    

Exception.add_note(note) â add a note to the exception

class args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.management.user_groups.User#
    

User information dataclass.

id: str#
    

name: str#
    

email: str#
    

role: UserRole#
    

cloud_credentials: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.management.cloud_credentials.CloudCredential] | None = None#
    

user_groups: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[UserGroupRef] | None = None#
    

fiftyone.management.user_groups.resolve_user_id(_user_or_id_or_email : str | User | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _pass_unknown_email : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → str | None#
    

Resolves user ID - by looking up user by email if it has to

class fiftyone.management.user_groups.UserGroup#
    

User Group information dataclass.

id: str#
    

name: str#
    

description: str | None#
    

principals: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[Any] | None = None#
    

cloud_credentials: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.management.cloud_credentials.CloudCredential] | None = None#
    

users: [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.management.users.User] | None = None#
    

fiftyone.management.user_groups.add_users_to_group(_user_group : str_, _users : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[Any] | str_, _resolved_users : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → UserGroup#
    

Adds users to the given group.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    group_id = "group id"
    user_ids = ["user id 1", "user id 2"]
    
    fom.add_users_to_group(user_group=group_id, user_ids=user_ids)
    

Parameters:
    

  * **user_group** â a group ID, name string, or `Group` instance

  * **users** (_None_) â list of users (email or ID strings or User instances or dictionary objects with valid fields) or a single user string/obj

  * **resolved_users** (_False_) â If True, the user_ids are already resolved/validated




fiftyone.management.user_groups.create_user_group(_name : str_, _description : str | None = None_, _users : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str | fiftyone.management.users.User] | None = None_) → UserGroup#
    

Creates a new user group.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    group_name = "Name"
    group_description = "Description"
    fom.add_user_group(name=group_name, description=group_description)
    
    assert fom.get_user_group(group_name) is not None
    

Parameters:
    

  * **name** â group name, string

  * **description** (_None_) â optional group description, string

  * **users** (_None_) â optional list of user_ids, names or Users instance




fiftyone.management.user_groups.delete_user_group(_user_group : str | UserGroup_) → None#
    

Deletes the given group.

Note

Only admins can perform this action.

Warning

This action is irreversible!

Examples:
    
    
    import fiftyone.management as fom
    
    group_name = "Group Name"
    fom.delete_user_group(group_name)
    
    assert fom.get_user_group(group_name) is None
    

Parameters:
    

**user_group** â a group ID, name string, or `Group` instance

fiftyone.management.user_groups.get_user_group(_user_group : str_) → UserGroup | None#
    

Gets information about the specified group (if any).

Note

Only admins can retrieve information about user groups.

Examples:
    
    
    import fiftyone.management as fom
    
    group_name = "Group Name"
    group = fom.get_user_group(group_name)
    assert group.name == group_name
    
    unknown_group = "Unknown Group"
    assert fom.get_user_group(unknown_group) is None
    

Parameters:
    

**user_group** â a group ID or name string

Returns:
    

`Group`, or `None` if no such group is found

fiftyone.management.user_groups.list_user_groups_for_user(_user : str | dict | fiftyone.management.users.User_, _verbose =False_) → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[UserGroup] | [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

Gets all user groups for the given user.

If the user_id does not exist, an empty list is returned.

if the email address is incorrect, an exception is raised.

If there is no group associated with the user, an empty list is returned.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    user_id = "user id"
    fom.list_user_groups_for_user(user_id)
    

Parameters:
    

  * **user** â a user ID or email string, or `User` instance

  * **verbose** (_True_) â If True, returns the list of groups, otherwise return the list of group names



Returns:
    

a list of `UserGroup` instances or a list of group names

fiftyone.management.user_groups.list_user_groups(_num_groups : int = 100_, _verbose =False_) → [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[UserGroup] | [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]#
    

Returns a list of all user groups.

Note

Only admins can retrieve this information.

Examples:
    
    
    import fiftyone.management as fom
    
    fom.list_user_groups()
    

Parameters:
    

  * **num_groups** (_100_) â The number of user groups to fetch

  * **verbose** (_False_) â If True, returns the list of groups, otherwise return

  * **names** (_the list_ _of_ _group_)



Returns:
    

a list of `Group` instances or a list of group names

fiftyone.management.user_groups.remove_users_from_group(_user_group : str_, _users : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[Any] | str_, _resolved_users : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → UserGroup#
    

Removes users from the given group.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    user_group = "group id"
    user_ids = ["user id 1", "user id 2"]
    
    fom.remove_users_from_group(user_group=group_id, user_ids=user_ids)
    

Parameters:
    

  * **user_group** â a group ID, name string, or `Group` instance

  * **users** (_None_) â list of users (email or ID strings or User instances or dictionary objects with valid fields) or a single user string/obj

  * **resolved_users** (_False_) â If True, the user_ids are already resolved/validated




fiftyone.management.user_groups.update_user_group(_user_group : str_, _name : str | None = None_, _description : str | None = None_, _users : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str | UserGroup] | None = None_) → UserGroup#
    

Updates the given group.

Note

Only admins can perform this action.

Examples:
    
    
    import fiftyone.management as fom
    
    group_id = "group id"
    group_name = "New Name"
    fom.update_user_group(user_group=group_id, name=group_name)
    
    assert fom.get_user_group(group_name) is not None
    

Parameters:
    

  * **user_group** â a group ID, name string, or `Group` instance

  * **name** (_None_) â group name, string

  * **description** (_None_) â group description, string

  * **users** (_None_) â list of user id, name string or User instance. Existing users not in this list will be removed.




fiftyone.management.user_groups.resolve_user_group_id(_group_or_id_or_name : str | UserGroup | None | dict_) → str#
    

Resolves group ID - by looking up group by name if it has to

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
