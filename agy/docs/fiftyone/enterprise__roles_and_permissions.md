---
source_url: https://docs.voxel51.com/enterprise/roles_and_permissions.html
---

# Roles and permissions#

FiftyOne Enterprise is built for collaboration, with the goal of making it as easy as possible for engineers, data scientists, and stakeholders to work together to build high quality datasets and computer vision models.

Accordingly, FiftyOne Enterprise gives you the flexibility to configure user roles, user groups and fine-grained permissions so that you can safely and securely collaborate both inside and outside your organization at all stages of your workflows.

This page introduces the basic roles and permissions available in FiftyOne Enterprise.

## Roles#

FiftyOne Enterprise has five user roles: Admin, Member, Collaborator, Labeler, and Guest.

Admins can access user management features by clicking on their account icon in the upper-right of the FiftyOne Enterprise App and navigating to the âSettings > Team > Usersâ page:

![admin-team-users-page](../_images/admin_team_users_page.png)

Admins can invite new users by clicking on âInvite peopleâ, as shown below. Invited users will receive an email invitation with a link to accept the invitation.

Note

Invited users may login using any identity provider that has been enabled on your deployment. If you need more information about configuring IdPs or increasing your user quotas, contact your Voxel51 support team.

![user-invitation](../_images/user_invitation.png)

### Admin#

Admins have full access to all of an organizationâs datasets and can create, edit, and delete any dataset.

Admins can also invite or remove users from the organization and change any other userâs roles, including promoting/demoting users to admins.

### Member#

Members can create new datasets and can be granted any desired level of permission on existing datasets. Members may also have a default access level to datasets that use this feature.

Members do not have the ability to see or manage an organizationâs users.

### Collaborator#

Collaborators only have access to datasets to which they have been specifically granted access (a datasetâs default access level does not apply to Collaborators), and they may only be granted **Can view** , **Can tag** or **Can edit** access to datasets.

Collaborators cannot create new datasets, clone existing datasets, or view other users of the deployment. Collaborators may export datasets to which theyâve been granted access.

### Labeler#

Labelers only have access to datasets to which they have been specifically granted access (a datasetâs default access level does not apply to Labelers), and they may only be granted **Can view** or **Can tag** access to datasets. Additionally, Labelers can update annotations and metadata on samples using FiftyOneâs [in-App annotation features](user_guide__annotation.md#in-app-annotation), but cannot make changes to the Annotation Schema.

Labelers cannot create new datasets, clone existing datasets, export datasets, or view other users of the deployment.

### Guest#

Guests only have access to datasets to which they have been specifically granted access (a datasetâs default access level does not apply to Guests), and they may only be granted **Can view** access to datasets.

Guests cannot create new datasets, clone existing datasets, export datasets, or view other users of the deployment.

### Groups#

User groups in FiftyOne Enterprise allow organization admins to manage a collection of users as a single entity. This simplifies the process of assigning permissions to multiple users, making it more efficient to control access to datasets.

Admins can manage groups through the âSettings > Team > Groupsâ page. Each group can be given specific dataset access permissions, which apply to all users within the group. Collaboratorsâ, labelersâ, and guestsâ access to the dataset is limited by the maximum dataset access level of the role.

![admin-team-groups-page](../_images/admin_team_groups_page.png)

Admins can create a new group by clicking on âCreate groupâ and then adding existing users to the group by clicking on âAdd usersâ.

![admin-create-group](../_images/admin_create_group.png) ![admin-team-add-users-to-team](../_images/admin_add_users_to_team.png)

Note

Non-existing users cannot be directly added to a group. Users must be invited and accept the invitation before they can be added to a group.

### Service accounts#

Service accounts are non-human principals designed for programmatic, automated, or machine-to-machine access to FiftyOne Enterprise. They authenticate exclusively via API keys and cannot log in interactively through the App.

Common use cases include:

  * CI/CD pipelines that run model evaluation or dataset quality checks

  * Data ingestion scripts that upload and curate samples automatically

  * Automated annotation workflows and model-in-the-loop jobs

  * Any process that needs to interact with FiftyOne without a human user




Unlike human users, service accounts have no email address, no user profile, and cannot receive invitations.

Note

Only admins can create, view, update, or delete service accounts.

**Roles**

Service accounts can only be assigned a role that has API key access enabled, since API keys are their only authentication mechanism. Which roles have this permission depends on your deploymentâs license configuration. You can check which roles support API keys by navigating to the âSettings > Security > Rolesâ page.

The assigned role determines what the service account can do, such as which datasets it can access by default and whether it can create new datasets.

**Groups**

Service accounts can be added to user groups in the same way as human users, allowing you to manage dataset permissions for a set of service accounts (or a mix of users and service accounts) as a single entity.

**Dataset permissions**

Service accounts can be granted individual or group-based dataset permissions using the same permission model as human users. All five permission levels â **No access** , **Can view** , **Can tag** , **Can edit** , and **Can manage** â apply, subject to the service accountâs role.

**Managing service accounts via the UI**

Admins can manage service accounts through the âSettings > Team > Service Accountsâ page:

![admin-team-service-accounts-page](../_images/admin_team_service_accounts_page.png)

Create a new service account by clicking âCreate service accountâ and providing a name, role, and optional description:

![admin-create-service-account](../_images/admin_create_service_account.png)

Click on a service account to view its details, edit its name, role, or description, and manage its API keys:

![admin-service-account-detail](../_images/admin_service_account_detail.png)

**Managing service accounts via the SDK**

Service accounts can be managed programmatically via the [Management SDK](enterprise__management_sdk.md#enterprise-sdk-service-account-management).

**API keys**

Service accounts authenticate via API keys. These can be generated through the UI on the âSettings > Team > Service Accountsâ page, or programmatically via the [Management SDK](enterprise__management_sdk.md#enterprise-sdk-api-keys). Once generated, configure the connection by following the steps in [API Connection](enterprise__api_connection.md#enterprise-api-connection).

## Permissions#

Admins and users with the **Can manage** permission on a dataset can configure a datasetâs permissions under the datasetâs [Manage tab](enterprise__app.md#enterprise-managing-datasets) in the FiftyOne Enterprise App.

In FiftyOne Enterprise, dataset permissions for a user are determined by both the access they receive from their groupsâ permissions and individual permissions assigned to them.

A userâs permissions on a dataset is the maximum of their permissions from the following sources:

  * Admins implicitly have full access to all datasets

  * Members have the datasetâs default access level

  * Users may be granted specific access to the dataset

  * Users may be members of one or more groups, each of which may have specific access to the dataset




Note

User role determines the highest level of access that a user can be granted to a dataset. For example, a user with Guest role can be added to a group with **Can edit** permission to a dataset, but this user will have **Can view** permission instead of **Can edit** permission of the dataset, because Guest role only allows **Can view** permission to datasets.

### Default access#

All datasets have a default access level, which defines a minimum permission level that all Members have on the dataset.

A datasetâs default access level can be set to **No access** , **Can view** , **Can tag** , **Can edit** , or **Can manage** as shown below:

![default-access](../_images/dataset_default_access.png)

Note

Default access level only applies to Members. Guests, Labelers, and Collaborators must be granted specific access to datasets.

### Specific access#

Authorized users can grant specific access to a dataset using the âPeople and groups with accessâ section shown below.

To give access to an existing user or group, simply click âShareâ button on the top right. A list of users with access to the dataset is shown. Click âAdd Userâ or âAdd Groupâ to grant access to a new user or group.

![specific-access](../_images/share_dataset.png) ![specific-access](../_images/dataset_specific_access.png)

The following permissions are available to each user role:

  * Groups may be granted **Can view** , **Can tag** , **Can edit** , or **Can manage** permissions

  * Members may be granted **Can view** , **Can tag** , **Can edit** , or **Can manage** permissions

  * Collaborators may be granted **Can view** , **Can tag** , or **Can edit** permissions

  * Labelers may be granted **Can view** or **Can tag** permissions

  * Guests may be granted **Can view** permissions




Note

Authorized users can use the âGrant accessâ workflow to give **Can view** , **Can tag** , or **Can edit** access to a dataset to an email address that is not yet user of a FiftyOne Enterprise deployment.

When the invitation is accepted, the user will become a Guest if the **Can view** permission is chosen, a Labeler if the **Can tag** permission is chosen, or a Collaborator if a higher permission is chosen, and an Admin can upgrade this user to another role if desired via the Team Settings page.

### No access#

If a user has no access to a dataset, the dataset will not appear in the userâs search results or show on their dataset listing page. Any direct links to this dataset that the user attempts to open will show a 404 page.

### Can view#

A user with **Can view** permissions on a dataset can find the dataset from their dataset listing page.

Users with **Can view** permissions cannot modify the dataset in any way, for example by adding or removing samples, tags, annotation runs, brain runs, etc.

Note

Members (but not Guests, Labelers, or Collaborators) with **Can view** access to a dataset may clone the dataset.

### Can tag#

A user with **Can tag** permissions on a dataset can find the dataset from their dataset listing page.

Users with **Can tag** permissions can modify sample/label tags but cannot modify the dataset in any other way.

### Can edit#

A user with **Can edit** permissions on a dataset has all permissions from **Can view** and, in addition, can modify the dataset, including:

  * Adding, editing, and deleting samples

  * Adding, editing, and deleting tags

  * Adding and deleting annotation runs, brain runs, etc.




Note

Deleting a dataset requires the **Can manage** permission.

### Can manage#

A user with **Can manage** permissions on a dataset has all permissions from **Can view** , **Can tag** and **Can edit** and, in addition, can delete the dataset and configure the permissions on the dataset of other users.

Remember that all admins can implicitly access and manage all datasets created on your teamâs deployment.

Note

Any member who creates a dataset (including cloning an existing dataset or view) will be granted **Can manage** permissions on the new dataset.

## Roles page#

Admins can review the actions and permissions available to each user role by navigating to the âSettings > Security > Rolesâ page:

![admin-roles-page](../_images/admin_roles_page.png)

IN THIS ARTICLE 
