---
source_url: https://docs.voxel51.com/enterprise/agent.html
---

# FiftyOne Agent#

The FiftyOne Agent is an AI-powered assistant built into the [FiftyOne Enterprise App](enterprise__app.md#enterprise-app). It lets you work with your datasets using natural language. You can import data, run model inference, find duplicates, evaluate predictions, and more, all from a conversational interface.

![fiftyone-agent-demo](https://cdn.voxel51.com/voxel-agent/enterprise/voxel_agent_demo_1.webp)

## Setup#

  1. Contact your Customer Success representative to enable the FiftyOne Agent for your deployment.

  2. Open any dataset in the FiftyOne Enterprise App. You will see a new Agent button in the upper-right corner of the App.


![fiftyone-agent-button-location](https://cdn.voxel51.com/voxel-agent/enterprise/location_agent.webp)

## Configuring model providers#

The first time you open the Agent, you will be prompted to configure a model provider. The Agent supports over 100 providers, including Anthropic, OpenAI, Google, and more.

![fiftyone-agent-settings](https://cdn.voxel51.com/voxel-agent/enterprise/agent_settings.webp)

To add a provider, fill in the following fields:

  * **Name** : a label for this provider configuration

  * **Provider** : select from the list of supported providers

  * **Endpoint** (optional): use this to route requests to a custom URL, such as an internal enterprise gateway or a self-hosted model server

  * **API key** : your providerâs API key

  * **Models** : select one or more models to make available

  * **Custom model names** (optional): enter model identifiers that are not in the standard picker, such as `openai/aws:anthropic.claude-sonnet-4-6` for a custom gateway. When using a custom endpoint, prefix model names with `openai/` so the Agent uses the OpenAI-compatible wire format

  * **Extra headers** (optional): static key-value HTTP headers sent with every request (e.g. `User-Agent`, project tokens required by your gateway)

  * **Default** : mark this provider as the default


![fiftyone-agent-provider-details](https://cdn.voxel51.com/voxel-agent/enterprise/provider_more_details.webp)

You can click **Test connection** to verify your credentials before saving.

Note

Need help configuring a provider? Contact your Customer Success representative, or see [Secrets](enterprise__secrets.md#enterprise-secrets) for how to store API keys securely in your deployment.

## Custom endpoints and enterprise gateways#

If your organization routes LLM traffic through an internal gateway or proxy (for example, an OpenAI-compatible service that enforces usage quotas or applies custom authentication), you can point the Agent at it using the **Endpoint** and **Extra headers** fields.

![fiftyone-agent-custom-gateway](https://cdn.voxel51.com/voxel-agent/enterprise/custom_gateway_screenshot.webp)

A typical configuration looks like:

  * **Provider** : `openai`

  * **Endpoint** : the base URL of your gateway, e.g. `https://gateway.internal/api/openai/v1`

  * **API key** : the credential your gateway expects in the `Authorization: Bearer` header (OIDC token, service account key, or a dummy value if the gateway handles auth via certificates or headers)

  * **Custom model names** : the model identifier your gateway uses, prefixed with `openai/`, e.g. `openai/aws:anthropic.claude-sonnet-4-6`

  * **Extra headers** : any additional headers required by your gateway, such as `User-Agent: MyApp/1.0` or `X-Gateway-Project-Token: <token>`


![fiftyone-agent-extra-headers](https://cdn.voxel51.com/voxel-agent/enterprise/custom_gateway_headers_screenshot.webp)

**Per-user attribution**

When a custom endpoint is configured, the Agent automatically adds an `X-FiftyOne-User-Email` header to every request containing the email address of the currently logged-in user. Gateways can use this header to attribute requests to individual users rather than a shared system account, which is useful for enforcing per-user quotas or audit logging.

Note

Admins are responsible for ensuring that the configured endpointâs data handling and retention align with their organizationâs privacy policy.

## Using the agent#

Once a provider is configured, you can start a conversation with the Agent. Type any task in plain language and the Agent will execute it against your dataset.

![fiftyone-agent-chat](https://cdn.voxel51.com/voxel-agent/enterprise/agent_chat.webp)

Some examples of what you can ask:

  * _âFind and remove duplicate images from this datasetâ_

  * _âRun object detection and show me low-confidence predictionsâ_

  * _âExport this dataset to COCO formatâ_




To start a new conversation, click the **+** button.

![fiftyone-agent-new-conversation](https://cdn.voxel51.com/voxel-agent/enterprise/new_conversation.webp)

To return to a previous conversation, click **History**.

![fiftyone-agent-conversation-history](https://cdn.voxel51.com/voxel-agent/enterprise/conversation_history.webp)

## Skills#

The Agent ships with a set of built-in skills that cover the most common computer vision workflows. Skills are structured instructions that tell the agent exactly how to perform a task, step by step.

![fiftyone-agent-skills](https://cdn.voxel51.com/voxel-agent/enterprise/skills.webp)

Note

You can also build and add your own custom skills to extend the agentâs capabilities. See [Developing skills](agents__developing_skills.md#agents-developing) for full instructions.

[ Browse Enterprise Skills ](https://docs.voxel51.com/agents/index.html?tag=Enterprise)

IN THIS ARTICLE 
