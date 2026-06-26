---
source_url: https://docs.voxel51.com/enterprise/secrets.html
---

# FiftyOne Enterprise Secrets#

FiftyOne Enterprise provides a Secrets interface for storing sensitive information such as API tokens and login credentials in a secure manner for use by your [Teamâs plugins](enterprise__plugins.md#enterprise-plugins).

Managing secrets through the Enterprise App is a straightforward and secure way to configure connections to and integrations with external services and APIs such as GCP, OpenAI, CVAT, etc without the need to change the configuration or environment variables of your FiftyOne Enterprise containers and restarting them. Instead, you can simply add or remove secrets using the Enterprise UI and they will immediately be available to any plugins that require them.

## Adding secrets#

Admins can add, configure, and remove secrets in the FiftyOne Enterprise App by navigating to the Secrets Management page under Settings > Secrets:

![enterprise-secrets-page](../_images/secrets_page.png)

When you tap on the âAdd secretâ button, you will see that a secret is comprised of a key, value, and optional description:

![enterprise-create-secret-form](../_images/create_secret_form.png)

Secret keys must be upper snake case strings like `MY_SECRET_KEY`.

Secret values are stored encrypted in the database and are only available to and decrypted at runtime by _internal services_ that have access to your encryption key.

Note

Only Admins have access to the Secrets page. However, once added, any App component or [plugin](enterprise__plugins.md#enterprise-plugins) requiring secret values can access them via the Secrets interface.

## Using secrets#

In order to access secrets, [plugins](enterprise__plugins.md#enterprise-plugins) must declare the secrets that they may use by adding them to the pluginâs `fiftyone.yml` file.

For example, the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/annotation/fiftyone.yml) plugin declares the following secrets:
    
    
    1secrets:
    2  - FIFTYONE_CVAT_URL
    3  - FIFTYONE_CVAT_USERNAME
    4  - FIFTYONE_CVAT_PASSWORD
    5  - FIFTYONE_CVAT_EMAIL
    6  - FIFTYONE_LABELBOX_URL
    7  - FIFTYONE_LABELBOX_API_KEY
    8  - FIFTYONE_LABELSTUDIO_URL
    9  - FIFTYONE_LABELSTUDIO_API_KEY
    

At runtime, the pluginâs execution context will automatically be hydrated with any available secrets that are declared by the plugin. Operators access these secrets via the `ctx.secrets` dict:
    
    
    1def execute(self, ctx):
    2    url = ctx.secrets["FIFTYONE_CVAT_URL"]
    3    username = ctx.secrets["FIFTYONE_CVAT_USERNAME"]
    4    password = ctx.secrets["FIFTYONE_CVAT_PASSWORD"]
    5    email = ctx.secrets["FIFTYONE_CVAT_EMAIL"]
    

The `ctx.secrets` dict will also be automatically populated with the values of any environment variables whose name matches a secret key declared by a plugin. Therefore, a plugin written using the above pattern can run in all of the following environments with no code changes:

  * A FiftyOne Enterprise deployment that uses the Secrets interface

  * A FiftyOne Enterprise deployment that injects secrets directly as environment variables

  * A locally launched App via the Enterprise SDK

  * Open source FiftyOne




IN THIS ARTICLE 
