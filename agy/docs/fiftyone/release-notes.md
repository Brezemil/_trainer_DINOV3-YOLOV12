---
source_url: https://docs.voxel51.com/release-notes.html
---

# FiftyOne Release Notes#

## FiftyOne Enterprise 2.20.0#

_Released June 8, 2026_

Includes all updates from FiftyOne 1.17.0. No additional Enterprise-specific changes in this release.

## FiftyOne 1.17.0#

_Released June 8, 2026_

App

  * Fixed a bug where the global âPixelatingâ¦â loading screen could re-appear when opening the modal or navigating between samples in explore mode [#7526](https://github.com/voxel51/fiftyone/pull/7526)

  * Fixed the same loading-screen flicker for grouped datasets when opening the modal, switching slices, or navigating between groups in the modal [#7551](https://github.com/voxel51/fiftyone/pull/7551)

  * Fixed a bug where the 3D viewer could fail to render when a grouped datasetâs active slice had no sample (sparse / pcd-only groups) [#7288](https://github.com/voxel51/fiftyone/pull/7288)

  * Fixed value tearing in the dynamic-groups pagination bar during slice transitions [#7599](https://github.com/voxel51/fiftyone/pull/7599)

  * Improved performance of image and mask decoding [#7711](https://github.com/voxel51/fiftyone/pull/7711)




In-App Annotation

  * Allowed persisting labels that have no `label` attribute set [#7639](https://github.com/voxel51/fiftyone/pull/7639)

  * Fixed a crash when changing the field of a polylines label [#7638](https://github.com/voxel51/fiftyone/pull/7638)

  * Fixed a bug where click-to-segment stopped working after navigating between samples in the modal [#7637](https://github.com/voxel51/fiftyone/pull/7637)

  * Improved annotation performance by coalescing hover handling via `requestAnimationFrame` and fixing duplicate polyline handler creation [#7597](https://github.com/voxel51/fiftyone/pull/7597)




Security

  * Updated `Pillow` to `>=12.2` to resolve CVE-2026-40192 [#7694](https://github.com/voxel51/fiftyone/pull/7694)

  * Updated `strawberry-graphql` to `>=0.312.3` to resolve CVE-2026-35523 [#7694](https://github.com/voxel51/fiftyone/pull/7694)

  * Updated App dependencies to resolve vulnerabilities: `minimatch` (9.0.7, CVE-2026-27904), `protobufjs` (>=7.6, CVE-2026-41242), and `brace-expansion` (>=5.0.6, CVE-2026-33750) [#7694](https://github.com/voxel51/fiftyone/pull/7694)

  * Made the App serverâs CORS policy configurable via `allowed_origins` and changed the default to same-origin [GHSA-q78p-hj9h-5466](https://github.com/advisories/GHSA-q78p-hj9h-5466)




General

  * Removed support for Python 3.9; FiftyOne now requires Python 3.10 or later [#7585](https://github.com/voxel51/fiftyone/pull/7585)




## FiftyOne Enterprise 2.19.0#

_Released May 28, 2026_

Includes all updates from FiftyOne 1.16.0, plus:

FiftyOne Agent

  * Added the [FiftyOne Agent](enterprise__agent.md#enterprise-agent): an AI-powered assistant built into the FiftyOne Enterprise App that lets you work with your datasets using natural language, including data import, model inference, duplicate detection, model evaluation, and annotation, all from a conversational interface [#7569](https://github.com/voxel51/fiftyone/pull/7569)

  * The Agent supports 100+ LLM providers, including Anthropic, OpenAI, and Google. Configure providers and API keys directly from the Agent settings panel

  * Ships with a set of built-in [skills](enterprise__agent.md#enterprise-agent-skills) covering the most common computer vision workflows, including data import, enrichment, quality checks, model evaluation, and annotation. You can also build your own custom skills with the [plugin skills framework](plugins__developing_plugins.md#plugins-design-skills)




App

  * Added new Observability page allowing admin users to monitor current and historical metrics and logs for deployed services

  * Upgraded the [Run page](enterprise__plugins.md#enterprise-run-page) of delegated operations with a full [metrics dashboard](enterprise__plugins.md#enterprise-run-page-metrics) that surfaces live system, database, and delegated-operation telemetry. The dashboard is admin-only by default, with dataset-permission-based access controls available for non-admin users

  * Live [log streaming](enterprise__plugins.md#enterprise-run-page-logs) during delegated operation execution is now powered by a sidecar that captures `stdout` and `stderr` and surfaces in-progress logs, progress bars, and package versions directly in the UI

  * Added a new Database panel on the live runs metrics page which is available to admin users

  * Fixed a bug where the app loading bar could remain visible indefinitely

  * Fixed a bug where the Cloud credentials âGroupsâ tab could show global credentials when no groups existed

  * Fixed a bug where cloud credentials were unnecessarily queried when no group was selected




Core

  * Added support for [per-deployment AI model weights](enterprise__installation.md#enterprise-ai-model-weights), allowing administrators to configure where models in the model zoo source their weights from, including private buckets and air-gapped mirrors

  * Fixed a bug in scheduled tasks where self-rescheduling on each tick could cause tasks to drift; tasks are now a self-contained loop




Auth and Users

  * Fixed a CAS lockout in legacy mode caused by unrestricted onboarding flows

  * Labeler and service accounts now appear in the CAS audit table

  * Improved redirect preservation across client-side session and auth errors




Security

  * Resolved CVE-2026-24049, CVE-2026-23949, and CVE-2026-6357 in the delegated-operation sidecar

  * Updated a number of dependencies in order to resolve security vulnerabilities: `pyjwt`, `ujson`, and `langchain-core`




Build

  * Bumped the minimum supported Redis version




## FiftyOne 1.16.0#

_Released May 28, 2026_

In-App Annotation

  * Added [Annotation Ontologies](user_guide__annotation.md#annotation-ontologies): a new framework for declaring an append-only, versioned schema for your labels and their attributes. Ontologies support [conditional attributes](user_guide__annotation.md#annotation-conditional-attributes) whose visibility is driven by composable `When` expressions (`WhenEquals`, `WhenIn`, and arbitrary `WhenAnd`/`WhenOr` trees), and they can be applied to any field via the [Schema Manager](user_guide__annotation.md#schema-manager).

  * Added support for editing instance segmentation masks in in-app annotation

  * Added click-to-segment functionality in the in-app annotation experience, allowing annotators to iteratively define masks using SAM2

  * Added support for editing 2D polylines in in-app annotation

  * Improved overall annotation canvas stability




Plugins and Operators

  * Added [plugin skills](plugins__developing_plugins.md#plugins-design-skills): plugins can now bundle agent-discoverable skills that are surfaced via the [FiftyOne Agent](enterprise__agent.md#enterprise-agent) and a new top-level `fiftyone skills` CLI command. Skills are first-class in the plugin framework and resolved by name rather than path [#7568](https://github.com/voxel51/fiftyone/pull/7568)

  * Added several new built-in operators, including operators to get and set view filters, list and open panels, get and set panel state and data, list brain runs, list evaluations, list model-evaluation scenarios, get field schemas, and update the color scheme

  * Plugins can now register custom components into arbitrary panel areas, including a new resizable right sidebar in the grid view and a header placement that lets plugins render content directly into the App header

  * Added a `risk_level` configuration option to operators, providing additional guardrails for high-impact actions

  * Added support for [request_params_overrides](plugins__developing_plugins.md#pipeline-request-params-overrides) on pipeline operators [#7277](https://github.com/voxel51/fiftyone/pull/7277)




App

  * Increased the default width of the panel area

  * Centered the BarChart within histogram containers

  * Stabilized navigation of dynamic group carousels [#7516](https://github.com/voxel51/fiftyone/pull/7516)

  * Improved synchronization of Explore and Annotate viewports, reducing rendering flicker and stale state when toggling between the two




Models

  * Added SAM3 to the model zoo [#7303](https://github.com/voxel51/fiftyone/pull/7303)

  * Fixed device allocation for the Qwen3-VL model so that it correctly uses the user-selected device




Core

  * Improved HTTP error responses: malformed JSON now returns 400 instead of 500, missing filepaths now return 400, and 404 coverage was broadened for the `/media` endpoint

  * Fixed a bug where serialized segmentation masks could be persisted in an incompatible binary format




Build

  * Removed the upper bound on supported Python versions. The Windows installer now emits a warning when an unsupported Python version is detected rather than failing the install




Documentation

  * Updated the [in-App annotation](user_guide__annotation.md#in-app-annotation) documentation to cover the new ontology, segmentation, polyline, and AI-assisted workflows

  * Added [logs](enterprise__plugins.md#enterprise-run-page-logs) and [metrics](enterprise__plugins.md#enterprise-run-page-metrics) sections to the delegated operation Run page docs [#7611](https://github.com/voxel51/fiftyone/pull/7611)

  * Added documentation for the [AI model weights](enterprise__installation.md#enterprise-ai-model-weights) endpoint [#7556](https://github.com/voxel51/fiftyone/pull/7556)

  * Documented the new [plugin skills](plugins__developing_plugins.md#plugins-design-skills) framework and updated the plugin development guide accordingly

  * Added a new [Agent Ecosystem](https://docs.voxel51.com/agents/index.html#agents-ecosystem) section to the docs covering the FiftyOne MCP server, the Skills Ecosystem, and guides for developing custom skills [#7509](https://github.com/voxel51/fiftyone/pull/7509)




## FiftyOne Enterprise 2.18.1#

_Released May 7, 2026_

App

  * Fixed a bug that caused global cloud credentials to incorrectly appear under the âGroupsâ tab on the Cloud credentials settings page when no groups existed in the system




Security

  * Updated a number of dependencies in the FiftyOne Enterprise App in order to resolve security vulnerabilities: `picomatch`, `protobufjs`, `@xmldom/xmldom`, and `langchain-core`

  * Updated a number of dependencies in the FiftyOne Enterprise API in order to resolve security vulnerabilities: `ujson` and `pyjwt`




## FiftyOne Enterprise 2.18.0#

_Released May 1, 2026_

Includes all updates from FiftyOne 1.15.0, plus:

Core

  * Added support for [Service Accounts](enterprise__roles_and_permissions.md#enterprise-service-accounts), allowing teams to create non-human accounts designed for programmatic, automated, or machine-to-machine access to FiftyOne Enterprise

  * Removed immediate execution option from builtin operators that should always be [delegated](enterprise__plugins.md#enterprise-delegated-operations) due to their compute needs

  * Fixed a bug where nonstandard file prefixes could cause a deployment to hang indefinitely and crash silently

  * Fixed a misleading error on the login page




App

  * Added an Orchestrators tab to the Settings page that lists all configured [Orchestrators](enterprise__plugins.md#enterprise-delegated-orchestrator) and provides links for admins to deploy new orchestrators

  * Added a âYour recent runsâ component to the dataset listing page that provides quick access to your most recent [delegated operations](enterprise__plugins.md#enterprise-delegated-operations)

  * Upgraded to the Logs tab of a delegated operationâs [Run page](enterprise__plugins.md#enterprise-run-page) to support live streaming during execution

  * Added more metrics to delegated operation logs to assist with debugging resource usage




## FiftyOne 1.15.0#

_Released May 1, 2026_

App

  * Added a [Similarity Search Panel](user_guide__app.md#app-similarity-search-panel) that provides a full-featured experience for performing visual/text similarity searches in the App, including a list of historical searches, the ability to alt-click in the grid to add negative examples to a search, and much more

  * You can now create [3D datasets](https://docs.voxel51.com/user_guide/using_datasets.html#d-datasets) composed of samples whose filepaths point directly to 3D media assets such as meshes and point clouds. Just declare the sampleâs media type as `media_type="3d"`

  * The App and SDK can now automatically resolve unambiguous `source -> world` static transforms through intermediate frames




Plugins

  * Optimized the [`FileExplorerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView "fiftyone.operators.types.FileExplorerView") component to provide faster load times when working with folders that contain many files/subfolders

  * Plugins can now register [custom media renderers](plugins__developing_plugins.md#custom-sample-renderers) to support visualizing non-native media types in the App grid/modal [#7164](https://github.com/voxel51/fiftyone/pull/7164)




## FiftyOne Enterprise 2.17.2#

_Released April 22, 2026_

App

  * Fixed a bug where signed URLs for point cloud assets in FO3D scenes could be stripped before rendering, causing some cloud-backed 3D scenes to fail to load.




Cloud Media

  * Fixed a bug where HTTP-backed media could hang or fail to load when the media cache performed unauthenticated server-side access checks.




Auth and Users

  * Improved unauthenticated redirect handling on the sign-in page.




## FiftyOne 1.14.2#

_Released April 22, 2026_

This release does not include any open-source updates.

## FiftyOne Enterprise 2.17.1#

_Released April 6, 2026_

Includes all updates from FiftyOne 1.14.1, plus:

  * Added full support for the [Labeler](enterprise__roles_and_permissions.md#enterprise-labeler) role in the [Enterprise Management SDK](enterprise__management_sdk.md#enterprise-management-sdk).




## FiftyOne 1.14.1#

_Released April 6, 2026_

  * Fixed: Now, if an [Operator](plugins__using_plugins.md#using-operators) defines `default_choice_to_delegated=True` and allows immediate execution, the UI will not default to âExecuteâ but correctly default to âScheduleâ and select an [Orchestrator](enterprise__plugins.md#enterprise-delegated-orchestrator). [#7285](https://github.com/voxel51/fiftyone/pull/7285)




## FiftyOne Enterprise 2.17.0#

_Released March 31, 2026_

Includes all updates from FiftyOne 1.14.0, plus:

App

  * Introduced a âYour recent runsâ widget on the Datasets page, showing run status with visual indicators and direct links to run details.

  * FiftyOne can now automatically resolve unambiguous `source -> world` static transforms through intermediate frames like `camera -> ego -> world` when `chain_via` is omitted.

  * Improved logic when user attempts to follow a link but is not logged in. We will now more consistently remember the original destination and redirect on login.

  * Fixed a bug where saving a valid auth config would result in a validation error.

  * Fixed search logic on Runs page.




Core

  * Added support for Azure SAS token credentials for cloud authentication. If an Azure SAS token is provided when setting Azure cloud credentials, we will only use that token and not generate one on your behalf.




Auth and Users

  * Introduced a new [Labeler](enterprise__roles_and_permissions.md#enterprise-labeler) role. This role only allows explicit dataset access, tagging of samples, and manual annotation in those datasets.

  * Added `lastUpdatedAt` field to account data to provide a more accurate measure of user activity.




## FiftyOne 1.14.0#

_Released March 31, 2026_

In-App Annotation

  * Fixed a bug which could cause erroneous patch requests while annotating samples [#7224](https://github.com/voxel51/fiftyone/pull/7224)

  * Fixed a bug in âCreate new Detectionsâ mode where clicking to exit would create a new Detection with neither width nor height. [#7205](https://github.com/voxel51/fiftyone/pull/7205)

  * Fixed a bug where newly created fields in the Schema Manager were not available for annotation. [#7140](https://github.com/voxel51/fiftyone/pull/7140)

  * Fixed an issue where being in annotation mode, then closing the modal, could cause display options to be removed. [#7158](https://github.com/voxel51/fiftyone/pull/7158)

  * Fixed a bug where tooltips would improperly render above Schema Manager [#7102](https://github.com/voxel51/fiftyone/pull/7102)

  * Fixed a crash for users with only tagging permissions when attempting to load the schema management UI. [#7182](https://github.com/voxel51/fiftyone/pull/7182)




CVAT Integration

  * Improved handling of mask data when downloading [CVAT](integrations__cvat.md#cvat-integration) annotations to correctly convert masks to polylines, polygons, and segmentation formats based on expected label types. [#7056](https://github.com/voxel51/fiftyone/pull/7056)

  * Fixed [#7024](https://github.com/voxel51/fiftyone/issues/7024). In the [CVAT integration](integrations__cvat.md#cvat-integration), annotations could fail to load when calling [`load_annotations()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.load_annotations "fiftyone.utils.annotations.load_annotations") if there were >10 CVAT projects. [#7058](https://github.com/voxel51/fiftyone/pull/7058)




App

  * Added direct support for many 3D formats (PCD, PLY, STL, FBX, GLTF) as well as support for mixed formats alongside FO3D. [#7164](https://github.com/voxel51/fiftyone/pull/7164)

  * Added an affordance to jump between different saved camera poses associated with a sample. [#7164](https://github.com/voxel51/fiftyone/pull/7164)

  * Improved support of sparse / imbalanced group datasets. [#7164](https://github.com/voxel51/fiftyone/pull/7164)

  * Updated Adaptive Toolbar to prefer rendering action buttons over âmore optionsâ button where possible. [#6990](https://github.com/voxel51/fiftyone/pull/6990)

  * Improved hover styling for buttons in the Nav Bar. [#7092](https://github.com/voxel51/fiftyone/pull/7092)

  * Standardized timestamp display and generally improved UI for range filters in grid sidebar. [#7027](https://github.com/voxel51/fiftyone/pull/7027)

  * Fixed bugs in camera position persistence across scene/sample/navigation changes. [#7164](https://github.com/voxel51/fiftyone/pull/7164)

  * Fixed [#6388](https://github.com/voxel51/fiftyone/issues/6388). Exclude samples by label tags now works as expected. [#7174](https://github.com/voxel51/fiftyone/pull/7174)

  * Fixed an issue where frame labels (detections) permanently disappear on videos longer than ~5100 frames by detecting LRU cache misses and correctly restarting the frame stream. [#7053](https://github.com/voxel51/fiftyone/pull/7053)

  * Fixed [#2010](https://github.com/voxel51/fiftyone/issues/2010). Blank page when running on windows systems. [#7152](https://github.com/voxel51/fiftyone/pull/7152)

  * Fixed a bug where the FiftyOne App crashed when loading datasets if Python or FiftyOne plugins were installed under non-standard filesystem paths (e.g., `/sc/home/...`). Plugins are now registered using synthetic module names that donât depend on filesystem location. [#6749](https://github.com/voxel51/fiftyone/pull/6749)




Plugins and Operators

  * Added [async data loading](plugins__developing_plugins.md#operator-async-data-loading) to [Operators](plugins__using_plugins.md#using-operators). Added `LoaderView` and `Object.loader()` to enable operators to load data asynchronously in forms without blocking user input. The loader executes an operator and tracks state (`idle`/`loading`/`loaded`/`errored`) with the result stored at the property path. [#6723](https://github.com/voxel51/fiftyone/pull/6723)

  * When constructing a [`PipelineStage`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage "fiftyone.operators.types.PipelineStage"), you can now pass `request_params_overrides`, which will override any of the corresponding params in the parent operatorâs request params. [#6954](https://github.com/voxel51/fiftyone/pull/6954)

  * Added ability to detect failed operator loading for `useOperatorExecutor` consumers. [#7203](https://github.com/voxel51/fiftyone/pull/7203)

  * All builtin operators that are expensive to execute on large datasets now default to delegated execution if [orchestrators](enterprise__plugins.md#enterprise-delegated-orchestrator) are available. [#6985](https://github.com/voxel51/fiftyone/pull/6985)

  * Fixed missing Delegated [Operators](plugins__using_plugins.md#using-operators) logs for builtin plugins. [#7111](https://github.com/voxel51/fiftyone/pull/7111)




Models

  * Added new Depth Anything V3 models to the model zoo: `depth-anything-v3-small-torch`, `depth-anything-v3-base-torch`, and `depth-anything-v3-large-torch` variants. [#6718](https://github.com/voxel51/fiftyone/pull/6718)

  * Added text-based similarity search support to `Qwen3VLModel`. Implemented `embed_prompt()` / `embed_prompts()` for text embedding. Text embeddings use the same pipeline as image embeddings (same chat template args, same _postprocess_embedding) so vectors share a common space. [#7132](https://github.com/voxel51/fiftyone/pull/7132)

  * Added native video embedding support to Qwen3-VL. Now [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings") will route to the native video path when `model.media_type == "video"`, producing one embedding per video. [#7049](https://github.com/voxel51/fiftyone/pull/7049)

  * Added Apple SHARP single-image to 3D Gaussian splat model. Outputs `.ply` files stored in `splat_path` attribute. [#6833](https://github.com/voxel51/fiftyone/pull/6833)

  * New argument `pin_memory` in [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") and [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"). This argument allows you to use more memory to get faster inference in cases when inference is bottlenecked by CPU to GPU transfer times. [#7184](https://github.com/voxel51/fiftyone/pull/7184)

  * Fixed a bug where YOLO segmentation model masks were not properly scaled when inference results were converted using [`fiftyone.utils.ultralytics.to_instances()`](api__fiftyone.utils.ultralytics.md#fiftyone.utils.ultralytics.to_instances "fiftyone.utils.ultralytics.to_instances"). [#7186](https://github.com/voxel51/fiftyone/pull/7186)

  * Fixed field name mismatch in `_to_sam_points` that prevents object-level point labels from working. [#6941](https://github.com/voxel51/fiftyone/pull/6941)




Core

  * Improved exception handling robustness across multiple modules by refining catch clauses to explicitly target standard exceptions. [#7214](https://github.com/voxel51/fiftyone/pull/7214)

  * Fixed metadata computations for urls without `Content-Length` set. [#6998](https://github.com/voxel51/fiftyone/pull/6998)




Build

  * Installer now exposes `-u` flag that switches the `pip` backend to `uv pip` for the duration of the install. [#7129](https://github.com/voxel51/fiftyone/pull/7129)

  * Fixed [#7151](https://github.com/voxel51/fiftyone/issues/7151). Windows source install reports âerror: File not found: requirements.txtâ. [#7129](https://github.com/voxel51/fiftyone/pull/7129)

  * Fixed nvm installation issue in install.sh. Bumped nvm version to 0.40.4. [#7157](https://github.com/voxel51/fiftyone/pull/7157)




Documentation

  * Updated example operating system versions in bug report and installation issue templates to reflect current platform versions. [#6898](https://github.com/voxel51/fiftyone/pull/6898)

  * Updated contribution guidelines, adding a Windows-specific instruction for running the install script. [#6900](https://github.com/voxel51/fiftyone/pull/6900)

  * Fixed [#4553](https://github.com/voxel51/fiftyone/issues/4553). Added documentation for the `tolerance` parameter, which controls polygon simplification when exporting instance segmentations, to the [COCO integration docs](integrations__coco.md#coco-format). [#7175](https://github.com/voxel51/fiftyone/pull/7175)

  * Fixed incorrect examples in docstring for the [`match()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match "fiftyone.core.collections.SampleCollection.match") function. [#7127](https://github.com/voxel51/fiftyone/pull/7127)




## FiftyOne Enterprise 2.16.5#

_Released March 23, 2026_

Includes all updates from FiftyOne 1.13.5, plus:

Cloud Media

  * Fixed a bug where wildcard bucket-prefix cloud credentials (e.g. `https://account.blob.core.windows.net/*`) could incorrectly match buckets belonging to different storage accounts.




Security

  * Updated a number of dependencies in order to resolve security vulnerabilities: `aiohttp`, `axios`, `cryptography`, `dompurify`, `eslint`, `immutable`, `lodash`, `minimatch`, `pillow`, `protobuf`, `pynacl`, `qs`, `rollup`, and `tar`.




## FiftyOne 1.13.5#

_Released March 23, 2026_

Models

  * Fixed issue with grounded zero shot object detection transformer adaptor. [#7197](https://github.com/voxel51/fiftyone/pull/7197)




## FiftyOne Enterprise 2.16.4#

_Released March 9, 2026_

Includes all updates from FiftyOne 1.13.4, plus:

Cloud Media

  * Fixed a race condition where concurrent reads and writes of cloud credential files could cause credential loading to fail.

  * Fixed a bug where Azure `load_credentials()` was not forwarding the profile parameter.

  * Fixed a bug with cloud credentials priority resolution order, ensuring the correct credential is selected first.




Auto-Labeling

  * Fixed a bug where [auto-labeling](enterprise__verified_auto_labeling.md#verified-auto-labeling) may fail if a mounted directory is not yet initialized.




## FiftyOne 1.13.4#

_Released March 9, 2026_

App

  * Ensured the release of `starlette 1.0` will not negatively impact the App. [#7137](https://github.com/voxel51/fiftyone/pull/7137)




## FiftyOne Enterprise 2.16.3#

_Released March 3, 2026_

Includes all updates from FiftyOne 1.13.3, plus:

[In-App Annotation](user_guide__annotation.md#in-app-annotation)

  * Adjusted permissions for annotation-related actions, so that users with `can_tag` level permissions will be able to perform all annotation workflows.




Cloud Media

  * Optimized cloud media access checks in order to reduce the number of requests being made.

  * Updated default behavior for local SDK use of cloud credentials, checking for credentials configured locally before attempting to download [managed cloud credentials](enterprise__installation.md#enterprise-cloud-storage-page), and disabling download of managed credentials by default. Both [local vs remote precedence](enterprise__installation.md#enterprise-cloud-creds-origin-preference), and [enabling vs disabling download of managed credentials](enterprise__installation.md#enterprise-cloud-creds-local-download) are configurable.

  * Fixed a bug where some cloud credentials would fail if they were uploaded by a user who no longer exists in the database.




Models

  * Constrained `timm<1.0.24` in enterprise docker images to better support `omdet` models.




## FiftyOne 1.13.3#

_Released March 3, 2026_

[In-App Annotation](user_guide__annotation.md#in-app-annotation)

  * New feature: Annotation support for detections while in a [patches views](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views). [#7012](https://github.com/voxel51/fiftyone/pull/7012)

  * Improved UX around bounding box annotation by implementing improved heuristics and disabling pan/zoom when drawing and selecting. [#7034](https://github.com/voxel51/fiftyone/pull/7034)

  * Improved UX around schema management. Changes now more consistently require the user to hit âSaveâ before being persisted. [#7008](https://github.com/voxel51/fiftyone/pull/7008)

  * Improved UX around field visibility. Hiding or showing fields in Explore view is also now reflected in the Annotation view. [#6993](https://github.com/voxel51/fiftyone/pull/6993)

  * Unified the detection-creation process. [#7019](https://github.com/voxel51/fiftyone/pull/7019)

  * Added keyboard shortcut to reset zoom and pan in annotation mode. Press ârâ to return to the default zoom level and pan position while annotating. [#7073](https://github.com/voxel51/fiftyone/pull/7073)

  * Fixed undo/redo inconsistencies for detections. [#7019](https://github.com/voxel51/fiftyone/pull/7019)

  * Fixed a bug where a detection could lose attribute values when switching between different fields. [#7067](https://github.com/voxel51/fiftyone/pull/7067)

  * Fixed a memory leak in the annotation UI. [#7047](https://github.com/voxel51/fiftyone/pull/7047)

  * Added comprehensive test suite for data normalization utilities. [#6995](https://github.com/voxel51/fiftyone/pull/6995)




## FiftyOne Enterprise 2.16.2#

_Released February 20, 2026_

Includes all updates from FiftyOne 1.13.2, plus:

  * Fixed a bug where Guest users were unable to load datasets.




## FiftyOne 1.13.2#

_Released February 20, 2026_

[In-App Annotation](user_guide__annotation.md#in-app-annotation)

  * Added some 3D annotation polish. We now zoom to the selected vertex for 3D polylines. Label selection now uses heuristics to select the right label by default. Tooltips are now hidden while editing a 3D label. [#7022](https://github.com/voxel51/fiftyone/pull/7022), [#7043](https://github.com/voxel51/fiftyone/pull/7043)

  * Fixed a bug with undo/redo when deleting 3D labels. [#7022](https://github.com/voxel51/fiftyone/pull/7022)




App

  * Fixed issues with video timeline sync: timeline subscribers were not receiving frame updates during video playback, and frame stepping (using `.` and `,` keys) had a momentary off-by-one flicker. [#7044](https://github.com/voxel51/fiftyone/pull/7044)




## FiftyOne Enterprise 2.16.1#

_Released February 18, 2026_

Includes all updates from FiftyOne 1.13.1, plus:

  * Reduced the need for manual refreshes in the App by disabling the in-memory singleton cache in the App server

  * Disabled, by default, the task-based `disable_sample_fields` behavior that reduces timeouts. New behavior can still be enabled by setting the `FIFTYONE_ENABLE_RPC` environment variable to `True`. Note: Configuration for `teams-api` may need to be [updated](https://github.com/voxel51/fiftyone-teams-app-deploy/blob/main/docker/docs/upgrading.md#fiftyone-enterprise-v215-additional-api-routes) given the new `/rpc` routes.

  * [Updated documentation](https://github.com/voxel51/fiftyone-teams-app-deploy/blob/main/docker/docs/expose-teams-api.md) with updated configuration for exposing the new teams-api routes `/rpc` and `/cloud_credentials`.




## FiftyOne 1.13.1#

_Released February 18, 2026_

App
    

  * Fixed a bug where a new release of the `strawberry-graphql` library was incompatible with the application. [#7017](https://github.com/voxel51/fiftyone/pull/7017), [#7029](https://github.com/voxel51/fiftyone/pull/7029)

  * Fixed a bug where annotation state wasnât always updating properly when switching between samples. [#7001](https://github.com/voxel51/fiftyone/pull/7001)




## FiftyOne Enterprise 2.16.0#

_Released February 12, 2026_

Includes all updates from FiftyOne 1.13.0, plus:

Cloud Media

  * New Feature: Scoped Cloud Credentials. Cloud credentials for accessing cloud media can now be assigned to one of three different scopes: per-user, per-user-group, and (as always) globally. All scopes of credentials support being further scoped by bucket-name filters, restricting their use to matching bucket names. Via the Settings / Cloud Credentials page, admins can manage all scopes of credentials, while any user can manage their own credentials. Scoped cloud credentials can also be managed using [`add_cloud_credentials()`](enterprise__management_sdk.md#fiftyone.management.cloud_credentials.add_cloud_credentials "fiftyone.management.cloud_credentials.add_cloud_credentials") and [`delete_cloud_credentials()`](enterprise__management_sdk.md#fiftyone.management.cloud_credentials.delete_cloud_credentials "fiftyone.management.cloud_credentials.delete_cloud_credentials"). Note: Configuration for `teams-api` may need to be [updated](https://github.com/voxel51/fiftyone-teams-app-deploy/blob/main/docker/docs/upgrading.md#fiftyone-enterprise-v216-additional-api-routes) given the new `/cloud_credentials` routes.

  * Users can configure their preferences for accessing cloud credentials locally. Both [local vs remote precedence](enterprise__installation.md#enterprise-cloud-creds-origin-preference), and [enabling vs disabling download of managed credentials](enterprise__installation.md#enterprise-cloud-creds-local-download) are configurable.




Plugins and Operators

  * Disabled the plugins cache (`plugins_cache_enabled=False`) by default when launching the Enterprise App locally.

  * Exposed the [Data Quality panelâs](enterprise__data_quality.md#data-quality) underlying operators for direct invocation by users if desired.




App

  * Fixed a bug on the Runs page, where filtering would incorrectly filter out certain runs.




Security

  * Updated a number of dependencies in order to resolve security vulnerabilities: `azure-core`, `eslint`, `js-yaml`, `tar`, and `wheel`




## FiftyOne 1.13.0#

_Released February 12, 2026_

App

  * New Feature: [In-App Annotation](user_guide__annotation.md#in-app-annotation) Create, edit, and delete classification and detection labels on images, as well as cuboid and 3d polylines on 3d datasets. [Dataset Managers](enterprise__roles_and_permissions.md#enterprise-can-edit) can define an annotation schema to constrain all metadata edits, either manually or by scanning an existing dataset. But, when no schema exists, labelers can choose to bypass a schema and quick-edit right away.

  * New Feature: 3D â 2D projection overlays for cuboids and polylines on image slices, including crosshair with coordinate tooltip. [#6935](https://github.com/voxel51/fiftyone/pull/6935)

  * Improved cursor tracking and raycasting logic for 3D multi-panel visualizations. [#6886](https://github.com/voxel51/fiftyone/pull/6886), [#6921](https://github.com/voxel51/fiftyone/pull/6921)

  * Optimization: Significantly reduced time to fetch data to populate the grid for datasets with many label fields. [#6934](https://github.com/voxel51/fiftyone/pull/6934)

  * Fixed a bug where RGB segmentation masks stored directly in MongoDB as 3-channel arrays were not rendering correctly. [#6805](https://github.com/voxel51/fiftyone/pull/6805)

  * Fixed a bug where img icons for plugins were not sized correctly. [#6937](https://github.com/voxel51/fiftyone/pull/6937)




Core

  * Fix file descriptor leak when loading images during model inference. [#6773](https://github.com/voxel51/fiftyone/pull/6773)




Models

  * Pinned `timm<1.0.24` for omdet-turbo-swin-tiny-torch to fix inference failure. [#6891](https://github.com/voxel51/fiftyone/pull/6891)




CLI

  * Added a `fiftyone app debug` command that launches the App in debug mode. In debug mode, server logs are printed to the shell, which is useful, eg, when developing plugins. [#6848](https://github.com/voxel51/fiftyone/pull/6848)




## FiftyOne Enterprise 2.15.0#

_Released February 4, 2026_

Includes all updates from FiftyOne 1.12.0, plus:

Core

  * Introduced the `scan_for_label_mistakes` operator. This operator allows you to identify incorrect classification labels, for example those generated by a foundation model, by manually selecting a small number of âverifiedâ labels.

  * Migrated more methods to use a more robust approach for communication with the API: `add_samples()`, `set_values()` now join `delete_sample_fields()`. This will significantly increase the reliability and consistency of long running requests. This change is disabled by default, but can be enabled by setting the `FIFTYONE_ENABLE_RPC` environment variable to `True`.




Plugins, Operators, and Orchestrators

  * From the Runs page, users can now rerun an [`PipelineOperator`](api__fiftyone.operators.md#fiftyone.operators.PipelineOperator "fiftyone.operators.PipelineOperator") starting at a failed stage â rerunning the entire stage, or a single [Operator](plugins__using_plugins.md#using-operators). Original runs are archived and hidden by default in the UI, but can be made visible using the âshow archivedâ toggle.

  * Improved reliability of push-based [orchestrators](enterprise__plugins.md#enterprise-delegated-orchestrator). The system will now automatically retry operations stuck in the queued state for push-based orchestrators. Users can configure their API to automatically requeue operations targeting push-based orchestrators after a delay or a certain number of attempts.

  * New default expiration time for monitored Delegated [Operators](plugins__using_plugins.md#using-operators) is now 30 minutes, allowing for more accurate termination of stuck pods while respecting non-monitored operations.

  * Fixed distributed execution to prevent sample skipping, introducing new default ID-range batching strategy, and now use a strategy pattern to select between slice-based batching and ID-range batching.

  * For [Kubernetes Orchestrator](https://github.com/voxel51/fiftyone-teams-app-deploy/blob/main/docs/orchestrators/configuring-kubernetes-orchestrator.md), made both `image` and `kubeConfig` parameters optional, allowing users to specify them via configuration if desired.




Authorization

  * The restriction on role re-upgrades is no longer based on âroleâ but now âlicense tierâ. For example, Admin and Member are considered the same tier since they both use up the same seat type, so users are free to switch between those roles without restrictions.




App

  * Added a multi-scope cloud credentials UI to the Adminâs Settings page. Available scopes are GLOBAL, GROUP, and USER, each with its own tab.

  * Updated UI to show downgrade warning based on tiers.




Security

  * Updated a number of dependencies in order to resolve security vulnerabilities: `diff`, `fonttools`, `glob`, `h2`, `js-yaml`, `langchain-core`, `nodemailer`, `qs`, and `starlette`.




## FiftyOne 1.12.0#

_Released February 4, 2026_

Core

  * Added a first-class camera module with [intrinsics/extrinsics data models](https://docs.voxel51.com/user_guide/using_datasets.html#camera-intrinsics-extrinsics), [dataset-level refs](https://docs.voxel51.com/user_guide/using_datasets.html#storing-camera-calibration), and projection utilities for 3D. [#6700](https://github.com/voxel51/fiftyone/pull/6700), [#6780](https://github.com/voxel51/fiftyone/pull/6780), [#6703](https://github.com/voxel51/fiftyone/pull/6703), [#6730](https://github.com/voxel51/fiftyone/pull/6730)

  * Added a builtin `reload_saved_view` [operator](plugins__using_plugins.md#using-operators) that allows for checking + reloading saved generated views. Calling `reload()` on a saved generated view will now automatically update the saved viewâs metadata. Backing datasets for saved generated views are now marked as persistent so that they are not affected by non-persistent dataset cleanup. Deleting a dataset or specific generated saved views will automatically mark the now-deprecated backing dataset as non-persistent. Switch to `_state["dataset_id"]` in generated views to prevent unnecessary reloads when the parent dataset is renamed. [#6067](https://github.com/voxel51/fiftyone/pull/6067)

  * Added [`get_cpu_count()`](api__fiftyone.core.utils.md#fiftyone.core.utils.get_cpu_count "fiftyone.core.utils.get_cpu_count") which properly accounts for docker / kubernetes CPU limits. Updated [`recommend_thread_pool_workers()`](api__fiftyone.core.utils.md#fiftyone.core.utils.recommend_thread_pool_workers "fiftyone.core.utils.recommend_thread_pool_workers") and [`recommend_process_pool_workers()`](api__fiftyone.core.utils.md#fiftyone.core.utils.recommend_process_pool_workers "fiftyone.core.utils.recommend_process_pool_workers") to use this new function. [#6290](https://github.com/voxel51/fiftyone/pull/6290)




Plugins and Operators

  * Expanded support for rerunning Delegated [Operators](plugins__using_plugins.md#using-operators). Set `rerunnable` to True or False on the operator config of your Operator or [`PipelineStage`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage "fiftyone.operators.types.PipelineStage") to control whether users can rerun that operation. Note: the PipelineStage config takes precedence over the Operator config, or set the stage config to `None` to default to the Operator `rerunnable` value. [#6729](https://github.com/voxel51/fiftyone/pull/6729)

  * You can now use `fiftyone delegated rerun <operatorId>` to rerun Delegated [Operators](plugins__using_plugins.md#using-operators). [#6729](https://github.com/voxel51/fiftyone/pull/6729)

  * Added support for archiving Delegated [Operators](plugins__using_plugins.md#using-operators), in addition to deleting them. Archived Delegated Operators will automatically be filtered out when calling `list_operations`. [#6716](https://github.com/voxel51/fiftyone/pull/6716)

  * Added support for immediate [`PipelineOperator`](api__fiftyone.operators.md#fiftyone.operators.PipelineOperator "fiftyone.operators.PipelineOperator") execution, with added live pipeline execution capability and enhanced error handling. [#6628](https://github.com/voxel51/fiftyone/pull/6628)

  * Fixed a bug for multi-select autocomplete fields when setting a default value. [#6748](https://github.com/voxel51/fiftyone/pull/6748)




Model Zoo

  * SAM2 models now support negative prompts for refined segmentation control. Users can specify a `negative_prompt_field` parameter when applying SAM2 models to exclude unwanted regions from segmentation masks. This enables more precise segmentation by providing both positive prompts (regions to segment) and negative prompts (regions to exclude). Works with both image and video SAM2 models using Detections or Keypoints. [#6520](https://github.com/voxel51/fiftyone/pull/6520)

  * Added YOLO26 model family to the model zoo, including classification, detection, and instance segmentation models, based on the January 2026 Ultralytics release. [#6760](https://github.com/voxel51/fiftyone/pull/6760)

  * Added three LLMDet open-vocabulary zero-shot object detectors (tiny/base/large) to the Torch model zoo. [#6248](https://github.com/voxel51/fiftyone/pull/6248)

  * Updated [`get_implied_field_kwargs()`](api__fiftyone.core.odm.md#fiftyone.core.odm.get_implied_field_kwargs "fiftyone.core.odm.get_implied_field_kwargs") to correctly handle values that contain subclasses of `EmbeddedDocumentField`. [#6639](https://github.com/voxel51/fiftyone/pull/6639)




Brain

  * Fixed: When subselecting samples from the lancedb table, ensure the samples being selected exist in the table. [#272](https://github.com/voxel51/fiftyone-brain/pull/272)




ETA

  * Fixed an incompatibility with `numpy>=2` and the `FFmpegVideoReader`. [#686](https://github.com/voxel51/eta/pull/686)




Docs

  * Expanded user guide with comprehensive camera calibration coverage: [Storing Camera Calibration](https://docs.voxel51.com/user_guide/using_datasets.html#storing-camera-calibration), [Camera Intrinsics/Extrinsics](https://docs.voxel51.com/user_guide/using_datasets.html#camera-intrinsics-extrinsics), and 3D. [#6711](https://github.com/voxel51/fiftyone/pull/6711)

  * Fixed broken active projects reference in CONTRIBUTING.md [#6770](https://github.com/voxel51/fiftyone/pull/6770)




## FiftyOne Enterprise 2.14.1#

_Released January 14, 2026_

Includes all updates from FiftyOne 1.11.1, plus:

Security

  * Updated a number of dependencies in order to resolve security vulnerabilities: `jws`, `next`, `node-forge`, and `validator`.




## FiftyOne 1.11.1#

_Released January 14, 2026_

Core

  * Fixed an incompatibility with `sklearn>=1.8` [#6657](https://github.com/voxel51/fiftyone/pull/6657)




Security

  * Updated `httplib2` in order to resolve a security vulnerability [#6726](https://github.com/voxel51/fiftyone/pull/6726), [eta#683](https://github.com/voxel51/eta/pull/683)




## FiftyOne Enterprise 2.14.0#

_Released December 5, 2025_

Includes all updates from FiftyOne 1.11.0, plus:

Annotation

  * Introducing the [Auto-Labeling](enterprise__verified_auto_labeling.md#verified-auto-labeling) Panel! This panel allows you to (1) select and configure a model for label generation, (2) generate labels using an [orchestrator](enterprise__plugins.md#enterprise-delegated-orchestrator), and (3) use the panel along with the sample grid to review and selectively approve the generated labels.




Plugins and Orchestrators

  * Introducing a built-in [Kubernetes Orchestrator](https://github.com/voxel51/fiftyone-teams-app-deploy/blob/main/docs/orchestrators/configuring-kubernetes-orchestrator.md)! Delegated [Operators](plugins__using_plugins.md#using-operators) can now be scheduled on an on-demand Kubernetes cluster, supporting both CPU and GPU configurations. This feature is fully available, but considered Beta for self-hosted deployments.

  * Fixed a bug: terminating / marking a [Delegated Operator Pipeline](plugins__developing_plugins.md#writing-operator-pipelines) as failed now fails all non-terminal children as well.

  * Improved error handling and messaging for the Runs > Log tab.

  * Improved state transition logic for Delegated [Operators](plugins__using_plugins.md#using-operators) to reduce flipping back and forth between states.




Core

  * Added `user_group`, `id`, and `name` to user and viewer queries to easily know if a user is part of a group without additional queries.

  * Users with `manage` permissions now have appropriate access to generated datasets.

  * Snapshot deletion is now more robust to errors.




App

  * Added x-axis labels to charts in the [Data Quality Panel](enterprise__data_quality.md#data-quality).

  * Fixed a bug on the dataset list page: âAllâ | âMineâ radio button state wasnât resetting when navigating back to dataset listing page.

  * Increased the 10mb upload limit to 100mb.

  * Improved cache invalidation when groups are updated.




Docs

  * Added comprehensive [Auto Labeling documentation](enterprise__verified_auto_labeling.md#verified-auto-labeling), including detailed guides on feature concepts, end-to-end user workflows, configuration options, running and monitoring operations, label review and approval processes, infrastructure requirements, and troubleshooting.




Security

  * Upgraded a number of packages to resolve security vulnerabilities: `aiohttp`, `brotli`, `glob`, `h2`, `next-auth`, `nodemailer`, `starlette`, and `validator`.




## FiftyOne 1.11.0#

_Released December 5, 2025_

Core

  * Added support for importing/exporting instance segmentations in YOLOv4/5 format. Exports `Polyline` objects that contain multiple shapes as separate rows in YOLOv4/5 format. [#6490](https://github.com/voxel51/fiftyone/pull/6490)

  * Added support for filtering model predictions by class via a new [`SampleCollection.apply_model(..., classes=)`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") syntax. [#6494](https://github.com/voxel51/fiftyone/pull/6494)

  * Added low-level utilities for managing workspaces, for consistency with existing utilities for other aspects of the data model (saved views, runs, etc) [#6598](https://github.com/voxel51/fiftyone/pull/6598)

  * Added builtin operators `add_dynamic_sample_fields`, `add_dynamic_frame_fields`, `remove_dynamic_sample_fields`, and `remove_dynamic_frame_fields` to add/remove [dynamic attributes](https://docs.voxel51.com/user_guide/using_datasets.html#dynamic-attributes) from dataset schemas in the App. [#6486](https://github.com/voxel51/fiftyone/pull/6486)

  * Added a new syntax where dicts generated by `get_dynamic_field_schema()` and `get_dynamic_frame_field_schema()` may be passed directly to `add_dynamic_sample_fields()` and `add_dynamic_frame_fields()`, respectively. [#6486](https://github.com/voxel51/fiftyone/pull/6486)

  * Optimized the performance of `bool(view)`. [#6552](https://github.com/voxel51/fiftyone/pull/6552)

  * Update error message for failed run loading to make it more clear that the error only might be due to a version mismatch and to more clearly expose the underlying error. [#6573](https://github.com/voxel51/fiftyone/pull/6573)

  * Fixed a bug in [`fiftyone.core.odm.get_implied_field_kwargs()`](api__fiftyone.core.odm.md#fiftyone.core.odm.get_implied_field_kwargs "fiftyone.core.odm.get_implied_field_kwargs") when parsing embedded documents with >=2 levels of nesting [#6609](https://github.com/voxel51/fiftyone/pull/6609)

  * Fixed a bug with LFW download URLs, and now handle overlapping splits. [#6611](https://github.com/voxel51/fiftyone/pull/6611)

  * Fixed MongoDB serialization error when running keypoint detection with numpy >= 2.0. [#6407](https://github.com/voxel51/fiftyone/pull/6407)

  * Fixed bug where interactions with Windows file paths would fail [#6578](https://github.com/voxel51/fiftyone/pull/6578)

  * Updated HMDB51 dataset download links to working Google Drive mirrors. [#6528](https://github.com/voxel51/fiftyone/pull/6528)




Model Zoo

  * Added âembeddingsâ tag to 27 models, and removed it from two, to more accurately represent which models can be used to compute embeddings. [#6587](https://github.com/voxel51/fiftyone/pull/6587), [#6575](https://github.com/voxel51/fiftyone/pull/6575)




App

  * More reliable camera initialization and positioning by recalculating lazily if needed. [#6545](https://github.com/voxel51/fiftyone/pull/6545)

  * Removed mAP metric from available model performance metrics options in model evaluation [scenarios](user_guide__app.md#app-scenario-analysis). [#6524](https://github.com/voxel51/fiftyone/pull/6524)

  * Fixed ability to select dynamic embedded doc fields in the sidebar. [#6580](https://github.com/voxel51/fiftyone/pull/6580)

  * Fixed a bug where an [Operator](plugins__using_plugins.md#using-operators) prompt would sometimes get stuck in the loading state. [#6572](https://github.com/voxel51/fiftyone/pull/6572)

  * Fixed [sorting by similarity](user_guide__app.md#app-similarity) for group datasets in the App [#6562](https://github.com/voxel51/fiftyone/pull/6562)

  * Fixed a bug where disabling preview when creating scenarios would sometimes block user from creating a scenario. [#6535](https://github.com/voxel51/fiftyone/pull/6535)

  * Fixed bug where grid selections would be cleared when closing a modal using the escape key. Also added a confirmation dialog when clearing grid selections using the escape key. [#6387](https://github.com/voxel51/fiftyone/pull/6387)




Brain

  * Add support for âpromptâ similarity queries with Model instances in the current session. [#263](https://github.com/voxel51/fiftyone-brain/pull/263)

  * Make `compute_visualization` with TSNE compatible with `scikit-learn` versions 1.7.0+ [#264](https://github.com/voxel51/fiftyone-brain/pull/264)




Docs

  * Added a new docs section on caching expensive operator inputs to the [operator dev docs](plugins__developing_plugins.md#developing-operators). [#6486](https://github.com/voxel51/fiftyone/pull/6486)

  * Corrected typo and improved clarity in [`SelectGroupSlices`](api__fiftyone.core.stages.md#fiftyone.core.stages.SelectGroupSlices "fiftyone.core.stages.SelectGroupSlices") documentation regarding performance characteristics. [#6561](https://github.com/voxel51/fiftyone/pull/6561)




Plugins

  * Added a new [Operator](plugins__developing_plugins.md#developing-operators) input type `ResolvableProperty` and a corresponding new view `ResolvablePropertyView` to enable asynchronously resolving a property in an [Operatorâs](plugins__using_plugins.md#using-operators) input. [#6544](https://github.com/voxel51/fiftyone/pull/6544)

  * Added option to provide a custom view via context parameters when invoking an [Operator](plugins__developing_plugins.md#developing-operators) programmatically. [#6592](https://github.com/voxel51/fiftyone/pull/6592)

  * [Pipeline child operators](plugins__developing_plugins.md#writing-operator-pipelines) now have access to a mapping of failed child ID to error message in the [`PipelineExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext "fiftyone.operators.executor.PipelineExecutionContext") `child_errors` field. [#6565](https://github.com/voxel51/fiftyone/pull/6565)




Database

  * The `fiftyone-db` library now defaults to MongoDB 7 when possible. [#6533](https://github.com/voxel51/fiftyone/pull/6533)




## FiftyOne Enterprise 2.13.1#

_Released November 19, 2025_

Plugins

  * Fixed a bug where, in some cases, an Operator input form would get stuck in validation.




Security

  * Updated a number of dependencies in order to resolve security vulnerabilities: `h2`, `starlette`, `aiohttp`, and `brotli`.




## FiftyOne Enterprise 2.13.0#

_Released October 31, 2025_

Includes all updates from FiftyOne 1.10.0, plus:

Plugins

  * Introduced [`PipelineOperator`](api__fiftyone.operators.md#fiftyone.operators.PipelineOperator "fiftyone.operators.PipelineOperator"), allowing a single Operator to kick off execution of a sequence of Operators. Plugin authors define a [`Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline") consisting of [`PipelineStages`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage "fiftyone.operators.types.PipelineStage"), and each stage will be executed in sequence. This enables quite complex operations to be defined, including distributed execution in any stage, and finalization stages. See [documentation](plugins__developing_plugins.md#writing-operator-pipelines) for more.

  * Fixed a bug in distributed operations when `target_view` is set to âentire datasetâ and filters are set, preventing incorrect application of filters.




App

  * Increased maximum length for the name of a dataset or view to over 1000 characters.

  * Fixed a bug where the UI would allow exporting media greater than 100 MB, even though that is not supported, resulting in the download hanging.




Core

  * Optimized [`instances_to_polylines()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.instances_to_polylines "fiftyone.utils.labels.instances_to_polylines") conversion of instance segmentations whose masks are stored in the cloud.




Compliance

  * Fixed a bug where a license compliance error could be raised even after the compliance issue had been resolved.

  * Modified our builds to remove lock files that were causing some scanners (e.g. AWS Inspector) to erroneously report vulnerabilities for dependencies not included in our build.




## FiftyOne 1.10.0#

_Released October 31, 2025_

Model Zoo

  * Added `FiftyOneTransformerForPoseEstimation` to support transformer-based keypoint prediction models ( [ViTPose](https://huggingface.co/docs/transformers/model_doc/vitpose#vitpose) ) to the fiftyone model zoo. [#6371](https://github.com/voxel51/fiftyone/pull/6371)




Core

  * [`add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples") now includes a kwarg for a batcher, which can be a [`fiftyone.core.utils.Batcher`](api__fiftyone.core.utils.md#fiftyone.core.utils.Batcher "fiftyone.core.utils.Batcher"), `None` to use the default defined in the config, or `False` to disable batching for the request. [#6400](https://github.com/voxel51/fiftyone/pull/6400)

  * Increased maximum resource (dataset, view, snapshot) name size from 100 to 1551\. [#6458](https://github.com/voxel51/fiftyone/pull/6458)




App

  * Fixed a bug in [Model Evaluation Panelâs](user_guide__app.md#app-model-evaluation-panel) confusion matrix, where it was possible for the x,y values to get inverted. [#6471](https://github.com/voxel51/fiftyone/pull/6471)

  * Fixed a bug where the user could not save a [custom color scheme](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-color-scheme). [#6437](https://github.com/voxel51/fiftyone/pull/6437)




## FiftyOne Enterprise 2.12.0#

_Released October 20, 2025_

Includes all updates from FiftyOne 1.9.0, plus:

Plugins, Operators, and Orchestrators

  * Added ability to manually terminate an [Operator](plugins__using_plugins.md#using-operators) while itâs running in any supported [orchestrator](enterprise__plugins.md#enterprise-delegated-orchestrator): builtin, Databricks, and Anyscale.

  * Updated expiration logic for Delegated [Operators](plugins__using_plugins.md#using-operators), and introduced `FIFTYONE_DO_EXPIRATION_MINUTES`. Instead of considering an Operator terminated one day after _starting_ , we now only kill an Operator if it hasnât _updated_ in `FIFTYONE_DO_EXPIRATION_MINUTES` minutes. This enables tighter control over execution, and allows for jobs to run for more than one day.

  * Added connection retry logic to a number of [orchestrators](enterprise__plugins.md#enterprise-delegated-orchestrator)-related requests in order to improve resilience.

  * Improved logging and logging levels when plugin secrets are not provided.




App

  * Added a plugin secret `FIFTYONE_ZOO_ALLOWED_MODEL_NAMES` that allows Enterprise admins to configure which zoo models should be available to users when using builtin App features, such as the [Embeddings Panel](user_guide__app.md#app-embeddings-panel) and the [Data Quality Panel](enterprise__data_quality.md#data-quality).

  * Ensure that user-provided brain/eval keys are valid in the [Embeddings Panel](user_guide__app.md#app-embeddings-panel) and the [Model Evaluation Panel](user_guide__app.md#app-model-evaluation-panel) to prevent runtime errors.

  * Fixed a bug where, after a user first logged in, media in the Grid would fail to load because the userâs cloud credentials were delayed.




Core

  * Reduced likelihood of timeouts when performing `delete_sample_fields`.

  * Improved performance of various operations on media files that can be executed without downloading the full media file.

  * Added some additional logging in the API to aid in debugging and performance monitoring.

  * Added âUser-Agentâ to a few requests that were missing it.




Security

  * Updated a number of dependencies in order to resolve security vulnerabilities: `axios`, `brace-expansion`, `next`, and `starlette`.




## FiftyOne 1.9.0#

_Released October 20, 2025_

Plugins and Operators

  * Added `download_file` [Operator](plugins__using_plugins.md#using-operators) to download files in-browser. [#6369](https://github.com/voxel51/fiftyone/pull/6369)

  * Added new hook for easily invoking [Python Panel](plugins__developing_plugins.md#developing-panels) events from JS. [#6179](https://github.com/voxel51/fiftyone/pull/6179)

  * [Panel](plugins__developing_plugins.md#developing-panels) events now return their return-value as an operator result. NOTE: operator results must be serializable. With this change, non-serializable operator results will produce an error. [#6179](https://github.com/voxel51/fiftyone/pull/6179)

  * Improved reliability when queuing delegated [Operators](plugins__using_plugins.md#using-operators) by excluding non-serializable fields during serialization. [#6406](https://github.com/voxel51/fiftyone/pull/6406)

  * Improved [Operator](plugins__using_plugins.md#using-operators) monitoring with periodic backend pings and stronger handling of ping/get failures. [#6359](https://github.com/voxel51/fiftyone/pull/6359)

  * Fixed: [Operators](plugins__using_plugins.md#using-operators) now honor the active view when one is set, instead of silently falling back to the full dataset. [#6375](https://github.com/voxel51/fiftyone/pull/6375)




Core

  * Optimizes and hardens the implementation of [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") when applied to video collections. [#6370](https://github.com/voxel51/fiftyone/pull/6370)

  * Added support for updating existing indexes in-place (e.g. converting between unique and non-unique). [#6365](https://github.com/voxel51/fiftyone/pull/6365)

  * Allow [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings") to write to embedded fields. [#6374](https://github.com/voxel51/fiftyone/pull/6374)

  * Updated the [`fiftyone.utils.labels`](api__fiftyone.utils.labels.md#module-fiftyone.utils.labels "fiftyone.utils.labels") utilities with `overwrite=True` options so that they now only overwrite the specific files being exported (rather than deleting the entire directory). [#6364](https://github.com/voxel51/fiftyone/pull/6364)

  * Optimization: Updated the default behavior of the [`sort_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by "fiftyone.core.collections.SampleCollection.sort_by"), [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by"), [`geo_within()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.geo_within "fiftyone.core.collections.SampleCollection.geo_within"), and [`geo_near()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.geo_near "fiftyone.core.collections.SampleCollection.geo_near") view stages to NOT automatically create an index when used. Indexing is opt-in via `create_index=True`. [#6344](https://github.com/voxel51/fiftyone/pull/6344)

  * Improved reliability of database connections by detecting closed synchronous and asynchronous clients and automatically re-establishing connections to avoid errors from stale or closed clients in long-running sessions. [#6354](https://github.com/voxel51/fiftyone/pull/6354)

  * Fixed a bug where [`fiftyone.utils.labels`](api__fiftyone.utils.labels.md#module-fiftyone.utils.labels "fiftyone.utils.labels") utilities with `overwrite=False` options would erroneously start overwriting existing files if repeatedly executed more than 2 times. [#6364](https://github.com/voxel51/fiftyone/pull/6364)

  * Fix for [#6069](https://github.com/voxel51/fiftyone/pull/6069) where [YOLO classification models](integrations__ultralytics.md#ultralytics-image-classification) were failing for ultralytics>=8.3.158 [#6367](https://github.com/voxel51/fiftyone/pull/6367)




App

  * Fixed a bug in rare situations where an incorrect header was set that resulted in a CORS error. [#6405](https://github.com/voxel51/fiftyone/pull/6405)




Security

  * Updated the `brace-expansion` dependency in order to resolve a security vulnerability [#6413](https://github.com/voxel51/fiftyone/pull/6413)




## FiftyOne Enterprise 2.11.2#

_Released September 25, 2025_

Includes all updates from FiftyOne 1.8.1, plus:

  * Fixed a security vulnerability in `formidable`




## FiftyOne 1.8.1#

_Released September 25, 2025_

  * Fixed a bug where certain plugin form inputs would cause the form to not render properly. [#6351](https://github.com/voxel51/fiftyone/pull/6351)




## FiftyOne Enterprise 2.11.1#

_Released September 11, 2025_

  * Fixed a permissioning edge case that could cause users to view the names of datasets they didnât have access to.




## FiftyOne Enterprise 2.11.0#

_Released September 3, 2025_

Includes all updates from FiftyOne 1.8.0, plus:

  * Introduced support for [running delegated operations on-demand](enterprise__plugins.md#enterprise-on-demand-compute) on a connected Databricks or Anyscale cluster

  * Introduced support for [distributed execution of delegated operations](enterprise__plugins.md#enterprise-distributed-execution), which splits execution of compatible operations across multiple parallel workers, enabling large operations to complete in less time. Users can easily modify their existing operators to support distribution by following [these simple instructions](plugins__developing_plugins.md#writing-distributed-operators)

  * Added support for identity pool credentials (WIF) and impersonated credentials when configuring [cloud credentials](enterprise__installation.md#enterprise-cloud-credentials)

  * Fixed `sizeEstimate` fields on datasets and dataset snapshots to return floats indicating size in megabytes instead of bytes, preventing GraphQL errors with large estimates

  * Fixed a memory leak in the server




Logging

  * Logging now outputs in structured JSON format when the `FIFTYONE_LOGGING_FORMAT='json'` environment variable is set

  * Removed duplicate and otherwise noisy server logs to improve performance and reduce unnecessary logging

  * Ensure timestamp is included on more logs

  * Distinguish more clearly between missing token and invalid token errors when authentication fails




Dependencies

  * Updated `urllib3` dependency to resolve CVE-2025-50181

  * Updated `sha.js` dependency to resolve CVE-2025-9288

  * Pinned `libssl-dev`, `libssl3`, and `openssl` dependencies to avoid issues caused by OpenSSL 3.0.17




## FiftyOne 1.8.0#

_Released September 3, 2025_

App

  * Optimized lasso performance in the [Map panel](user_guide__app.md#app-map-panel) [#6150](https://github.com/voxel51/fiftyone/pull/6150)

  * Introduced a number of point-cloud fixes: point-cloud height shader and tooltip hover coordinates account for asset-level transformations, PLY point clouds that have vertex normals render with correct shading [#6254](https://github.com/voxel51/fiftyone/pull/6254)

  * Reduced the need for manual refreshes in the App by disabling the in-memory singleton cache in the App server [#6161](https://github.com/voxel51/fiftyone/pull/6161)




Plugins

  * Added a [target view utility](plugins__developing_plugins.md#operator-target-view) to the operator framework that provides a builtin mechanism for giving users the choice of operating on a full dataset, current view, or current selection [#6235](https://github.com/voxel51/fiftyone/pull/6235)




Annotation

  * Fixed a bug in [CVAT](integrations__cvat.md#cvat-integration) and IoU utilities handling of instance segmentation masks [#6274](https://github.com/voxel51/fiftyone/pull/6274)

  * Fixed [CVAT](integrations__cvat.md#cvat-integration) instance segmentation mask resolution [#5972](https://github.com/voxel51/fiftyone/pull/5972)

  * Fixed an error when loading non-list tag attributes from [CVAT](integrations__cvat.md#cvat-integration) [#6094](https://github.com/voxel51/fiftyone/pull/6094)




Model Zoo

  * Added 6 SegFormer semantic segmentation models to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) (b0-b5 variants) [#6217](https://github.com/voxel51/fiftyone/pull/6217)

  * Added OWL-ViT large-patch14 to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) for zero-shot object detection [#6196](https://github.com/voxel51/fiftyone/pull/6196)

  * Added 5 new D-FINE real-time object detection models to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) (nano through xlarge) [#6143](https://github.com/voxel51/fiftyone/pull/6143)

  * Added 2 new RT-DETRv2 real-time object detection models to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) (small and medium variants) [#6106](https://github.com/voxel51/fiftyone/pull/6106)

  * Added OWL-ViT base-patch32 model to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) for zero-shot object detection [#6140](https://github.com/voxel51/fiftyone/pull/6140)

  * Added 4 new Swin V2 hierarchical transformer models to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) (tiny, small, base, large) [#6100](https://github.com/voxel51/fiftyone/pull/6100)

  * Added 13 new image classification models to the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo): ConvNeXt (tiny, small, base, large, xlarge) and EfficientNet (b0-b7) [#6084](https://github.com/voxel51/fiftyone/pull/6084)

  * Zero-shot HuggingFace models no longer require classes to be set by the user when using [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model") [#6159](https://github.com/voxel51/fiftyone/pull/6159)

  * All semantic segmentation torch models in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) now support confidence thresholding and the class indices start at 1 for segmentation masks [#6231](https://github.com/voxel51/fiftyone/pull/6231)

  * All models in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) now have clear, user-friendly descriptions that explain what each model does and its intended use case, making it easier to find the right model for your task [#6184](https://github.com/voxel51/fiftyone/pull/6184)

  * Official models in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) are now consistently marked with the `official` tag to help users identify authoritative model implementations [#6192](https://github.com/voxel51/fiftyone/pull/6192)

  * TensorFlow 1.x models in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) are now tagged as `legacy` to indicate they are no longer actively maintained due to TF1âs deprecation [#6187](https://github.com/voxel51/fiftyone/pull/6187)

  * YOLO segmentation models in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) are now tagged as `instances` rather than `segmentation` to reflect that they perform instance segmentation [#6219](https://github.com/voxel51/fiftyone/pull/6219)

  * Fixed incorrect file size metadata for the ConvNeXt-XLarge model in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) [#6195](https://github.com/voxel51/fiftyone/pull/6195)

  * Fixed missing file sizes for ConvNeXt and EfficientNet models in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo), enabling accurate download progress tracking and storage requirement validation [#6104](https://github.com/voxel51/fiftyone/pull/6104)

  * Fixed missing model size information in the [model zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) for vit-base-patch16-224-imagenet-torch, siglip-base-patch16-224-torch, and group-vit-segmentation-transformer-torch models [#6175](https://github.com/voxel51/fiftyone/pull/6175)

  * Fixed a bug that prevented extracting embeddings from zero-shot transformer models [#6109](https://github.com/voxel51/fiftyone/pull/6109)

  * Fixed issue when computing DINO patch embeddings on patches of size <14 [#6172](https://github.com/voxel51/fiftyone/pull/6172)




Docs

  * Introduced a [getting started page](https://docs.voxel51.com/getting_started/index.html#getting-started-guides) organized by use case to help users quickly discover guides relevant to their needs [#6237](https://github.com/voxel51/fiftyone/pull/6237)

  * Added comprehensive [getting started guides](https://docs.voxel51.com/getting_started/index.html#getting-started-guides) for object detection, medical imaging, model evaluation, self-driving, and 3D visual AI [#5967](https://github.com/voxel51/fiftyone/pull/5967)

  * Added the Kapa AI agent widget to the documentation site to assist users with AI-powered support [#6218](https://github.com/voxel51/fiftyone/pull/6218)

  * Added a new example notebook showing how to use DINOv3 from Hugging Face with FiftyOne for classification, visual search, and PCA-based foreground segmentation [#6261](https://github.com/voxel51/fiftyone/pull/6261)




Logging

  * Added support for specifying additional debug loggers via configuration or environment variable [#6220](https://github.com/voxel51/fiftyone/pull/6220)




Deprecations

  * FiftyOne no longer supports MongoDB <6\. Users running MongoDB 5 or older are [advised to upgrade](deprecation.md#deprecation-mongodb-5-0) their instance [#6091](https://github.com/voxel51/fiftyone/pull/6091), [#5984](https://github.com/voxel51/fiftyone/pull/5984)




## FiftyOne Enterprise 2.10.2#

_Released Aug 5, 2025_

Includes all updates from FiftyOne 1.7.2, plus:

  * Fixed security vulnerabilities in `form-data`, `next`, and `@babel/runtime` libraries.




## FiftyOne 1.7.2#

_Released Aug 5, 2025_

Core

  * Added a new syntax to [`set_label_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_label_values "fiftyone.core.collections.SampleCollection.set_label_values") that allows users to provide sample IDs in addition to label IDs for each update, for efficiency. [#6149](https://github.com/voxel51/fiftyone/pull/6149)

  * Added a new syntax to [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") where users can update frame fields by directly providing a mapping from frame IDs to values. [#6149](https://github.com/voxel51/fiftyone/pull/6149)

  * Added a new `fiftyone.utils.data.map_values()` utility that performs the same operation as [`SampleCollection.map_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.map_values "fiftyone.core.collections.SampleCollection.map_values") but it immediately saves the mapped values to the database rather than creating a view. [#6149](https://github.com/voxel51/fiftyone/pull/6149)

  * Added support for signed URLs when using GCS impersonated credentials and identity pool credentials (WIF). [#658](https://github.com/voxel51/eta/pull/658)




Labels

  * Fixed: The builtin `edit_field_values` operator can now safely be applied to views that filter label fields. [#6149](https://github.com/voxel51/fiftyone/pull/6149)

  * Fixed a bug with [CVAT](integrations__cvat.md#cvat-integration) rotation attribute of 3d labels. [#6163](https://github.com/voxel51/fiftyone/pull/6163)




App

  * Introduced tooltip behavior for PLY files similar to PCD files in [3D visualizer](user_guide__app.md#app-3d-visualizer). [#6202](https://github.com/voxel51/fiftyone/pull/6202)

  * Fixed: PLY point clouds were not always rendering in [3D visualizer](user_guide__app.md#app-3d-visualizer). [#6202](https://github.com/voxel51/fiftyone/pull/6202)

  * Improved top and ego view heuristics in [3D visualizer](user_guide__app.md#app-3d-visualizer), improving consistency. [#6168](https://github.com/voxel51/fiftyone/pull/6168)

  * Fixed a bug where camera `lookAt` wasnât being persisted across navigations. [#6168](https://github.com/voxel51/fiftyone/pull/6168)

  * Fixed a bug with the crop view of 3D labels. [#6168](https://github.com/voxel51/fiftyone/pull/6168)

  * Fixed: Image-based video playback now correctly renders segmentation maps during playback. [#6165](https://github.com/voxel51/fiftyone/pull/6165)




Model Evaluation

  * Display a trophy icon, when applicable, for the compare evaluation summary in the âoverviewâ tab of the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel). [#6189](https://github.com/voxel51/fiftyone/pull/6189)

  * Fixed: [Scenario Analysis](user_guide__app.md#app-scenario-analysis) tab loads for segmentation evaluations. [#6188](https://github.com/voxel51/fiftyone/pull/6188)




Plugins

  * Fixed a bug that caused file inputs to be submitted multiple times. [#6164](https://github.com/voxel51/fiftyone/pull/6164)




Zoo

  * Fixed [#6156](https://github.com/voxel51/fiftyone/issues/6156): setting classes for zero-shot models in Hugging Face [transformers](integrations__huggingface.md#huggingface-transformers) integration is now optional. [#6159](https://github.com/voxel51/fiftyone/pull/6159)




Security

  * Upgraded `pillow` to mitigate [CVE-2025-48379](https://www.cve.org/CVERecord?id=CVE-2025-48379) vulnerability. [#6216](https://github.com/voxel51/fiftyone/pull/6216)




## FiftyOne Enterprise 2.10.1#

_Released July 21, 2025_

Includes all updates from FiftyOne 1.7.1, plus:

  * Optimized the [pinned datasets widget](enterprise__app.md#enterprise-pinned-datasets)

  * Enhanced connection handling for HTTP requests, allowing faster failure and more robust retry behavior after a successful connection has been established

  * Changed the `sizeEstimate` fields on both datasets and dataset snapshots to return a float indicating size in megabytes, rather than in bytes

  * Fixed an error that could prevent [dataset snapshots](enterprise__dataset_versioning.md#dataset-versioning) from loading in the App in certain contexts




## FiftyOne 1.7.1#

_Released July 21, 2025_

App

  * Updated the [Scenario Analysis](user_guide__app.md#app-scenario-analysis) summary table to correctly interpret and display metrics where a lower value is better, such as the âIncorrectâ metric [#6111](https://github.com/voxel51/fiftyone/pull/6111)

  * Improved error handling in [Scenario Analysis](user_guide__app.md#app-scenario-analysis) when empty subsets are defined [#6127](https://github.com/voxel51/fiftyone/pull/6127)

  * Added calendar picker support for [`DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField") and [`DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField") inputs in the sidebar [#6120](https://github.com/voxel51/fiftyone/pull/6120)

  * Polished the sidebarâs slider UX to improve how we handle numeric precision [#6147](https://github.com/voxel51/fiftyone/pull/6147)

  * The [Embeddings panel](user_guide__app.md#app-embeddings-panel) now supports [frame patch views](https://docs.voxel51.com/user_guide/using_views.html#frame-patches-views) [#6129](https://github.com/voxel51/fiftyone/pull/6129)

  * Updated [custom color scheme](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-color-scheme) to allow `color_pool` to be optional [#6128](https://github.com/voxel51/fiftyone/pull/6128)

  * Fixed an issue where renaming a [saved workspace](user_guide__app.md#app-workspaces) would create a new workspace instead [#6125](https://github.com/voxel51/fiftyone/pull/6125)

  * Fixed search results for `label tags` in the sidebar when [Query Performance](user_guide__app.md#app-optimizing-query-performance) is disabled [#6095](https://github.com/voxel51/fiftyone/pull/6095)

  * Fixed an issue where the `useBrowserStorage` utility would persist an invalid `undefined` value in localStorage [#6116](https://github.com/voxel51/fiftyone/pull/6116)




Core

  * Improved handling of path resolution on Windows machines with multiple drives [#6088](https://github.com/voxel51/fiftyone/pull/6088), [#6136](https://github.com/voxel51/fiftyone/pull/6136)

  * Fixed a recent regression that prevented calling evaluation methods like [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") without providing an `eval_key` [#6126](https://github.com/voxel51/fiftyone/pull/6126)

  * Added a [deprecation notice for Kubernetes 1.30](deprecation.md#deprecation-kubernetes-1-30) indicating support will end on July 11, 2025 and future releases may not be compatible with this version [#6132](https://github.com/voxel51/fiftyone/pull/6132)




Zoo

  * Improved semantics when performing inference with [Ultralytics models](integrations__ultralytics.md#ultralytics-integration) and no suitable objects were found in an image [#6131](https://github.com/voxel51/fiftyone/pull/6131)

  * Fixed a bug that prevented applying models to image patches with `num_workers>0` on macOS [#6138](https://github.com/voxel51/fiftyone/pull/6138)

  * Fixed a bug that would prevent extracting embeddings from zero-shot transformer models with preprocessing disabled [#6122](https://github.com/voxel51/fiftyone/pull/6122)




## FiftyOne Enterprise 2.10.0#

_Released July 1, 2025_

Includes all updates from FiftyOne 1.7.0, plus:

Management SDK

  * Added a [fiftyone.management.orchestrator](enterprise__management_sdk.md#enterprise-sdk-orchestrator-management) module to support programmatically managing [orchestrators](enterprise__plugins.md#enterprise-delegated-orchestrator)

  * Added a [fiftyone.management.secret](enterprise__management_sdk.md#enterprise-sdk-secrets) module to support programmatically managing [secrets](enterprise__secrets.md#enterprise-secrets)




CLI

  * [Orchestrators](enterprise__plugins.md#enterprise-delegated-orchestrator) can now be managed from the command line. Use `fiftyone orchestrator --help` to get started




Other

  * Optimized executors by skipping the sleep step if there is immediately more work to execute

  * Introduced settings to enable configuration of the Sanic worker timeout threshold (default is 60 seconds)

  * Fixed a ânot consumedâ error that could occur when receiving an OPTIONS request with a body

  * Fixed an access issue with some temporary datasets that would prevent authorized users from accessing them

  * Fixed vulnerabilities in `cryptography`, `requests`, and `protobuf` libraries




## FiftyOne 1.7.0#

_Released July 1, 2025_

3D point clouds

  * Added support coloring point clouds by [dynamically chosen fields](user_guide__app.md#app-3d-dynamic-coloring) in the Appâs 3D visualizer [#5973](https://github.com/voxel51/fiftyone/pull/5973), [#5995](https://github.com/voxel51/fiftyone/pull/5995)

  * The [3D visualizer](user_guide__app.md#app-3d-visualizer) now recognizes point cloud intensities stored in an `intensity` field of PCD files [#5935](https://github.com/voxel51/fiftyone/pull/5935)

  * Added interactive tooltips that appear when hovering over point clouds in the [3D visualizer](user_guide__app.md#app-3d-visualizer) that show point metadata (RGB, intensity, index, position) [#5951](https://github.com/voxel51/fiftyone/pull/5951)

  * Added support for manipulating the âupâ vector dynamically in the App [#5935](https://github.com/voxel51/fiftyone/pull/5935), [#6035](https://github.com/voxel51/fiftyone/pull/6035)

  * Added configurable ray casting sensitivity to the [3D visualizer](user_guide__app.md#app-3d-visualizer) for better point selection [#5951](https://github.com/voxel51/fiftyone/pull/5951)

  * Introduced a new auto-rotate camera option that is persisted across sessions [#5951](https://github.com/voxel51/fiftyone/pull/5951)

  * Improved point cloud material handling for intensity-based coloring [#5951](https://github.com/voxel51/fiftyone/pull/5951)

  * Updated the FPS viewer to better support air-gapped deployments [#5951](https://github.com/voxel51/fiftyone/pull/5951)

  * Fixed an asset shifting artifact that would sometimes appear when loading point clouds in the 3D visualizer [#5951](https://github.com/voxel51/fiftyone/pull/5951)

  * Improved 3D visualization in the grid with enhanced background and overlay features [#5976](https://github.com/voxel51/fiftyone/pull/5976)




App

  * [Dynamic groups](user_guide__app.md#app-query-performant-stages) can now be optimized by providing the new `order_by_key` parameter [#5961](https://github.com/voxel51/fiftyone/pull/5961)

  * Optimized performance and resource usage of the sidebar and grid [#5842](https://github.com/voxel51/fiftyone/pull/5842), [#6056](https://github.com/voxel51/fiftyone/pull/6056)

  * Added a new configuration option for maximum query time (defaults to 60 seconds) [#5842](https://github.com/voxel51/fiftyone/pull/5842)

  * Added manual input fields to set the endpoints of int/float field filters in the sidebar [#5996](https://github.com/voxel51/fiftyone/pull/5996)

  * Fixed a regression from `fiftyone==1.6.0` that would cause incorrect query results when filtering an object list field by a numeric attribute with a min or max value (but not both) in the sidebar [#6078](https://github.com/voxel51/fiftyone/pull/6078)

  * Improved the layout of the stacked bar charts in the [Scenario Analysis](user_guide__app.md#app-scenario-analysis) tab [#6060](https://github.com/voxel51/fiftyone/pull/6060)

  * Fixed a bug that could cause incorrect confusion matrix colorscales in the [Scenario Analysis](user_guide__app.md#app-scenario-analysis) tab [#6057](https://github.com/voxel51/fiftyone/pull/6057)

  * Improved handling and displaying of embeddings plot loading errors in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#5997](https://github.com/voxel51/fiftyone/pull/5997), [#6077](https://github.com/voxel51/fiftyone/pull/6077)




Core

  * FiftyOne will now use multiple workers by default on macOS when applying Torch models that support data loaders via methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") and [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings") [#5939](https://github.com/voxel51/fiftyone/pull/5939)

  * Added a `beam_map()` utility that demonstrates how to perform parallelized map-reduce operations via [Apache Beam](https://beam.apache.org) [#6063](https://github.com/voxel51/fiftyone/pull/6063)

  * Fixed a filename clash bug when exporting multiple nested subdirectories that contain matching filenames into a single output directory [#6064](https://github.com/voxel51/fiftyone/pull/6064)




Zoo

  * Added [group-vit-segmentation-transformer-torch](model_zoo__models__group_vit_segmentation_transformer_torch.md#model-zoo-group-vit-segmentation-transformer-torch) to the model zoo [#5924](https://github.com/voxel51/fiftyone/pull/5924)

  * Added full support for configuring the confidence threshold of [Ultralytics models](integrations__ultralytics.md#ultralytics-integration) when running inference via [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") [#5893](https://github.com/voxel51/fiftyone/pull/5893)

  * Clarified how to achieve [batch inference](integrations__ultralytics.md#ultralytics-batch-inference) with Ultralytics models [#5895](https://github.com/voxel51/fiftyone/pull/5895)

  * Updated all [YOLOv5 models](integrations__ultralytics.md#ultralytics-object-detection) to use `ultralytics` [#5938](https://github.com/voxel51/fiftyone/pull/5938)

  * Fixed a regression from `fiftyone==1.6.0` that would prevent [YOLOv8 classification models](integrations__ultralytics.md#ultralytics-image-classification) from loading [#6073](https://github.com/voxel51/fiftyone/pull/6073)

  * Fixed [centernet-mobilenet-v2-fpn-512-coco-tf2](model_zoo__models__centernet_mobilenet_v2_fpn_512_coco_tf2.md#model-zoo-centernet-mobilenet-v2-fpn-512-coco-tf2) so that it downloads and loads correctly on all platforms [#5977](https://github.com/voxel51/fiftyone/pull/5977)

  * Added the missing `sam2` requirement so that all [SAM 2](model_zoo__models__segment_anything_2_hiera_base_plus_image_torch.md#model-zoo-segment-anything-2-hiera-base-plus-image-torch) and [SAM 2.1](model_zoo__models__segment_anything_2_1_hiera_base_plus_image_torch.md#model-zoo-segment-anything-2-1-hiera-base-plus-image-torch) models now load out-of-the-box [#5920](https://github.com/voxel51/fiftyone/pull/5920)

  * Improved the warning messages generated by [Transformers models](integrations__huggingface.md#huggingface-transformers) to provide clearer guidance on handling class conflicts [#5913](https://github.com/voxel51/fiftyone/pull/5913)

  * Corrected the `size_bytes` metadata for a variety of zoo models [#5936](https://github.com/voxel51/fiftyone/pull/5936), [#5919](https://github.com/voxel51/fiftyone/pull/5919), [#5950](https://github.com/voxel51/fiftyone/pull/5950), [#5898](https://github.com/voxel51/fiftyone/pull/5898)




## FiftyOne Enterprise 2.9.1#

_Released June 24, 2025_

Includes all updates from FiftyOne 1.6.0, plus:

  * All builtin delegated operations triggered from the App, such as [evaluating models](user_guide__app.md#app-model-evaluation-panel), generating [embedding visualizations](user_guide__app.md#app-embeddings-panel), and [data qualitiy](enterprise__data_quality.md#data-quality) scans, now automatically [report their progress](enterprise__plugins.md#enterprise-runs-monitoring-progress) every 10 seconds during execution

  * All delegated operations triggered from the App by [core plugins](https://github.com/voxel51/fiftyone-plugins?tab=readme-ov-file#core-plugins) now automatically [report their progress](enterprise__plugins.md#enterprise-runs-monitoring-progress) every 10 seconds during execution

  * Removed spurious log messages when resolving database secrets during plugin execution

  * Fixed an API connection error with `websocket-client<1.7`

  * Fixed support for chunked cookies (cookies larger than 4kb)

  * Fixed a bug in executing delegated operators that occurred because of a missing `request_token`

  * Fixed a bug in the [Data Quality Panel](enterprise__data_quality.md#data-quality) when an expected field is deleted

  * Fixed vulnerabilities in `prismjs`, `jinja2`, and `@babel`

  * Kubernetes 1.29 transitioned to end-of-life effective February of 2025, so in accordance with our [deprecation schedule](deprecation.md#deprecation-kubernetes-1-29), FiftyOne Enterprise 2.9 and later might not be compatible with it




## FiftyOne 1.6.0#

_Released June 24, 2025_

News

  * Added [Scenario Analysis](user_guide__app.md#app-scenario-analysis) to the Model Evaluation panel, allowing you to deep dive into the behavior of your models in different scenarios of interest [#5626](https://github.com/voxel51/fiftyone/pull/5626)




App

  * All fields added when performing [model evaluations](user_guide__evaluation.md#evaluating-models) are now automatically added to a [sidebar group](user_guide__app.md#app-sidebar-groups) with name `eval_key` by default [#5725](https://github.com/voxel51/fiftyone/pull/5725)

  * The current state of the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) is now persisted when you refresh the App [#6031](https://github.com/voxel51/fiftyone/pull/6031)

  * Added support for displaying only specific classes of interest in confusion matrices in the Model Evaluation panel [#6031](https://github.com/voxel51/fiftyone/pull/6031)

  * Upgraded the builtin `delete_selected_labels` operator to support deleting some/all labels in selected samples in the App [#5956](https://github.com/voxel51/fiftyone/pull/5956)

  * Improved stability when rendering objects with [instance IDs](user_guide__app.md#app-linking-labels) [#5944](https://github.com/voxel51/fiftyone/pull/5944)

  * Standardized hover and selection states across detection, keypoint, and polyline overlays [#5902](https://github.com/voxel51/fiftyone/pull/5902)

  * Fixed handling of indexes for dynamic embedded fields that are not declared in the datasetâs schema [#5965](https://github.com/voxel51/fiftyone/pull/5965)

  * Fixed unwanted index creation for grid sorting when a compound index already applies [#5900](https://github.com/voxel51/fiftyone/pull/5900)




Core

  * Added a [`Dataset.last_deletion_at`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.last_deletion_at "fiftyone.core.dataset.Dataset.last_deletion_at") property that is [automatically updated](https://docs.voxel51.com/user_guide/using_datasets.html#builtin-datetime-fields) when samples are deleted [#5853](https://github.com/voxel51/fiftyone/pull/5853)

  * [`Dataset.last_modified_at`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.last_modified_at "fiftyone.core.dataset.Dataset.last_modified_at") is no longer [automatically updated](https://docs.voxel51.com/user_guide/using_datasets.html#builtin-datetime-fields) when samples are deleted [#5853](https://github.com/voxel51/fiftyone/pull/5853)

  * Custom indexes are now automatically preserved when calling [`reload()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.reload "fiftyone.core.view.DatasetView.reload") on generated views [#5955](https://github.com/voxel51/fiftyone/pull/5955)

  * Custom indexes are no longer included by default when cloning views [#5955](https://github.com/voxel51/fiftyone/pull/5955)

  * Added an `include_indexes` parameter to [`clone()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone "fiftyone.core.dataset.Dataset.clone"), [`to_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_patches "fiftyone.core.collections.SampleCollection.to_patches"), [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames"), and [`to_clips()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_clips "fiftyone.core.collections.SampleCollection.to_clips") that allows for manually controlling what indexes are created on cloned datasets and generated views [#5955](https://github.com/voxel51/fiftyone/pull/5955)

  * Added `instance_ids` arguments to [`select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels"), [`match_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_labels "fiftyone.core.collections.SampleCollection.match_labels"), [`exclude_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_labels "fiftyone.core.collections.SampleCollection.exclude_labels"), and [`delete_labels()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_labels "fiftyone.core.dataset.Dataset.delete_labels") [#5918](https://github.com/voxel51/fiftyone/pull/5918)

  * Added an [`index_to_instance()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.index_to_instance "fiftyone.utils.labels.index_to_instance") utility for converting old-style `index` properties to [instances](user_guide__app.md#app-linking-labels) [#5918](https://github.com/voxel51/fiftyone/pull/5918)

  * Added a new `merge_embedded_docs=True` option to [`merge_sample()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_sample "fiftyone.core.dataset.Dataset.merge_sample") and [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") that causes the attributes of embedded documents to be merged individually, rather than as a single âvalueâ [#5704](https://github.com/voxel51/fiftyone/pull/5704)

  * Added support for passing `output_dir` to [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") to store instance segmentation masks on disk rather than in the database [#5953](https://github.com/voxel51/fiftyone/pull/5953)

  * Optimized label deletion on generated views [#5956](https://github.com/voxel51/fiftyone/pull/5956)

  * Enhanced [`update_samples()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.update_samples "fiftyone.core.collections.SampleCollection.update_samples") by automatically reflecting schema changes that are performed via its subprocess workers [#5957](https://github.com/voxel51/fiftyone/pull/5957)

  * Fixed a bug when using `[]` notation to unwind a terminal list field in [`values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values") aggregations [#5941](https://github.com/voxel51/fiftyone/pull/5941)

  * Fixed compound key [groups](https://docs.voxel51.com/user_guide/using_views.html#view-groups) when `order_by` is provided to [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by") [#5867](https://github.com/voxel51/fiftyone/pull/5867)

  * Fixed a bug where [`histogram_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.histogram_values "fiftyone.core.collections.SampleCollection.histogram_values") would raise an error when processing datetime fields that contain a very small range of values [#5971](https://github.com/voxel51/fiftyone/pull/5971)

  * Fixed a bug with [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") when setting frame fields via dict syntax where not all frame numbers are present [#5918](https://github.com/voxel51/fiftyone/pull/5918)

  * Fixed [#5921](https://github.com/voxel51/fiftyone/pull/5921), which would previously cause runtime errors when using [`GroupDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter "fiftyone.utils.data.importers.GroupDatasetImporter") instances that declare `has_sample_field_schema=True` [#5926](https://github.com/voxel51/fiftyone/pull/5926)

  * Fixed a bug where confidence was not applied to [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") instances correctly in [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") and [`add_labels()`](api__fiftyone.core.sample.md#fiftyone.core.sample.Sample.add_labels "fiftyone.core.sample.Sample.add_labels") [#5894](https://github.com/voxel51/fiftyone/pull/5894)

  * Added an [`apply_confidence_threshold()`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.apply_confidence_threshold "fiftyone.core.labels.Keypoint.apply_confidence_threshold") method that permanently deletes all keypoints below the provided threshold [#5894](https://github.com/voxel51/fiftyone/pull/5894)

  * Enhanced analytics by including FiftyOne in the Databricks user agent when possible [#5708](https://github.com/voxel51/fiftyone/pull/5708)




Plugins

  * Added [`ctx.active_fields`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.active_fields "fiftyone.operators.executor.ExecutionContext.active_fields") and [`ctx.ops.clear_active_fields()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_active_fields "fiftyone.operators.operations.Operations.clear_active_fields") to the operator execution context, allowing operators to get and set the currently active fields in the App sidebar [#5952](https://github.com/voxel51/fiftyone/pull/5952)

  * Added [`resolve_run_name()`](api__fiftyone.operators.md#fiftyone.operators.Operator.resolve_run_name "fiftyone.operators.Operator.resolve_run_name"), allowing operators to dynamically resolve their run name from the current execution context [#5916](https://github.com/voxel51/fiftyone/pull/5916)

  * Gracefully continue when [`ctx.set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") fails during operator execution to prevent things like intermittent network errors from killing otherwise functional long-running operations [#5974](https://github.com/voxel51/fiftyone/pull/5974)

  * Fixed a bug where passing a [progress callback](plugins__developing_plugins.md#operator-reporting-progress) to a delegated operation would fail to report its progress [#5974](https://github.com/voxel51/fiftyone/pull/5974)




Zoo

  * Formalized and officially documented the [`to_torch()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_torch "fiftyone.core.collections.SampleCollection.to_torch") interface for optimized model inference [#5711](https://github.com/voxel51/fiftyone/pull/5711)

  * All inference with [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel") instances now uses [`to_torch()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_torch "fiftyone.core.collections.SampleCollection.to_torch") [#5711](https://github.com/voxel51/fiftyone/pull/5711)

  * Converted all [Ultralytics](integrations__ultralytics.md#ultralytics-integration) and [Hugging Face Transformers](integrations__huggingface.md#huggingface-transformers) models in the zoo to [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel") format so that they can leverage performance improvements offered by [`to_torch()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_torch "fiftyone.core.collections.SampleCollection.to_torch") [#5729](https://github.com/voxel51/fiftyone/pull/5729), [#5761](https://github.com/voxel51/fiftyone/pull/5761)

  * Added support for batch inference with [Ultralytics models](integrations__ultralytics.md#ultralytics-integration) [#5836](https://github.com/voxel51/fiftyone/pull/5836)

  * Torch models can now provide custom collate functions via the new [`collate_fn`](api__fiftyone.core.models.md#fiftyone.core.models.TorchModelMixin.collate_fn "fiftyone.core.models.TorchModelMixin.collate_fn") method [#5834](https://github.com/voxel51/fiftyone/pull/5834)




Annotation

  * Added support for [CVAT v2.31.0](integrations__cvat.md#cvat-integration) servers [#5885](https://github.com/voxel51/fiftyone/pull/5885)

  * Fixed an issue with duplicate filenames when uploading data to [CVAT](integrations__cvat.md#cvat-integration) [#5927](https://github.com/voxel51/fiftyone/pull/5927)




Docs

  * Added a top-level [Importing data into FiftyOne](user_guide__import_datasets.md#importing-datasets) page that consolidates all information related to importing data into a single location [#5933](https://github.com/voxel51/fiftyone/pull/5933)

  * Added a [new section](user_guide__app.md#app-persistent-selections) to the user guide explaining how persistent selections of samples and labels work in the App [#5959](https://github.com/voxel51/fiftyone/pull/5959)




## FiftyOne Enterprise 2.8.2#

_Released May 9, 2025_

Includes all updates from FiftyOne 1.5.2

## FiftyOne 1.5.2#

_Released May 9, 2025_

Core

  * Fixed a bug where the system would sometimes detect a multiprocess environment incorrectly. [#5884](https://github.com/voxel51/fiftyone/pull/5884)




## FiftyOne Enterprise 2.8.1#

_Released May 8, 2025_

Includes all updates from FiftyOne 1.5.1

## FiftyOne 1.5.1#

_Released May 8, 2025_

App

  * Fixed a bug with plot interactivity in the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) [#5844](https://github.com/voxel51/fiftyone/pull/5844)

  * Fixed a bug where certain modal sidebar queries would error [#5848](https://github.com/voxel51/fiftyone/pull/5848)

  * Fixed a bug which caused some SVG icons to not render correctly in deployed environments [#5849](https://github.com/voxel51/fiftyone/pull/5849)

  * Fixed a bug which resulted in the UI displaying a stale set of saved views [#5858](https://github.com/voxel51/fiftyone/pull/5858)




Brain

  * Fixed a bug when passing a custom non-sklearn `similarity_index` to [`compute_uniqueness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_uniqueness "fiftyone.brain.compute_uniqueness") [#254](https://github.com/voxel51/fiftyone-brain/pull/254)




Core

  * Ensure that read access to the `admin` database is not required in order to use FiftyOne [#5872](https://github.com/voxel51/fiftyone/pull/5872)

  * The [fiftyone migrate âall](https://docs.voxel51.com/cli/index.html#cli-fiftyone-migrate) command now includes private datasets like patches, frames, and clips [#5868](https://github.com/voxel51/fiftyone/pull/5868)

  * Fixed [#5852](https://github.com/voxel51/fiftyone/issues/5852) by upgrading strawberry-graphql library [#5855](https://github.com/voxel51/fiftyone/pull/5855)




Docs

  * Added a docs warning and raises an error when attempting to use the [CVAT integration](integrations__cvat.md#cvat-integration) with a CVAT server > 2.30 [#5857](https://github.com/voxel51/fiftyone/pull/5857)




## FiftyOne Enterprise 2.8.0#

_Released May 2, 2025_

Includes all updates from FiftyOne 1.5.0, plus:

  * Optimized API performance by enabling [compression and byte-encoding](enterprise__api_connection.md#enterprise-api-connection)

  * Optimized plugin response times by using the Management API as the source of truth instead of the filesystem

  * Added support for local log file streaming for [delegated operations](enterprise__plugins.md#enterprise-delegated-operations)

  * Added a warning dialog about role re-upgrade limitations before admins downgrade users

  * Enabled override of the API batcher via the `override_api_dynamic_batching` config setting

  * Enabled use of local directories when configuring the log storage location for delegated operations

  * Introduced FiftyOne versions for Sanic configuration variables, and increased default values for keep-alive, request-timeout, response-timeout, websocket-max-size, and websocket-ping-timeout

  * Fixed a concurrency issue that could previously cause errors such as `KeyError: 's3'` during long-running operations like [downloading media](enterprise__cloud_media.md#enterprise-cloud-media-python) that need to refresh cloud credentials mid-operation

  * Fixed a misleading message during snapshot creation. Message now makes clear the snapshot may still be in progress of being created

  * Fixed a bug where certain transient 5xx errors were not being correctly retried

  * Fixed a bug where users with read-only access were unable to load a saved view from a snapshot

  * Fixed a bug where the dataset access page UI displayed No Access instead of the accurate value




## FiftyOne 1.5.0#

_Released May 2, 2025_

App

  * Optimized the performance of the sidebar when interacting with dropdowns and other field inputs by leveraging indexes when possible and otherwise showing [partial scan results](user_guide__app.md#app-unindexed-sidebar-results) [#5732](https://github.com/voxel51/fiftyone/pull/5732)

  * The sidebar can now make use of [compound indexes](user_guide__app.md#app-compound-indexes-for-query-performance) to support multiple filters on massive datasets [#5732](https://github.com/voxel51/fiftyone/pull/5732)

  * Optimized the performance of the builtin [sort by similarity](user_guide__app.md#app-similarity) action by removing unnecessary duplicate queries when scrolling/bookmarking [#5757](https://github.com/voxel51/fiftyone/pull/5757)

  * Added a `Sort by` input field to the upper right of the grid [#5732](https://github.com/voxel51/fiftyone/pull/5732)

  * Added support for linking objects across [group slices](https://docs.voxel51.com/user_guide/groups.html#linking-labels-across-slices) and [video frames](https://docs.voxel51.com/user_guide/using_datasets.html#linking-labels-across-frames) via the new [`Instance`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Instance "fiftyone.core.labels.Instance") class [#5577](https://github.com/voxel51/fiftyone/pull/5577)

  * Added new [on-hover and shift+click](user_guide__app.md#app-linking-labels) interactions for objects that use the new [`Instance`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Instance "fiftyone.core.labels.Instance") class to represent correspondence across group slices and video frames [#5577](https://github.com/voxel51/fiftyone/pull/5577)

  * Optimized [Map panel](user_guide__app.md#app-map-panel) loading and rendering [#5775](https://github.com/voxel51/fiftyone/pull/5775), [#5794](https://github.com/voxel51/fiftyone/pull/5794)

  * Fixed [#5327](https://github.com/voxel51/fiftyone/issues/5327) improving user experience when tagging [#5638](https://github.com/voxel51/fiftyone/pull/5638)

  * Fixed a z-order issue that would block some clicks in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#5627](https://github.com/voxel51/fiftyone/pull/5627)

  * Fixed `edit_field_values` operator when values are missing from some samples [#5662](https://github.com/voxel51/fiftyone/pull/5662)




Plugins

  * Added a new [execution_cache](plugins__developing_plugins.md#panel-execution-cache) decorator for caching intermediate results of dynamic operators and panels [#5680](https://github.com/voxel51/fiftyone/pull/5680)

  * Added a new `residency` parameter to [`@execution_cache`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache "fiftyone.operators.cache.execution_cache"), enabling `transient`, `ephemeral`, or `hybrid` caching strategies with optional in-memory cache size limits and automatic LRU eviction [#5736](https://github.com/voxel51/fiftyone/pull/5736)

  * Added [`ctx.prompt_id`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.prompt_id "fiftyone.operators.executor.ExecutionContext.prompt_id") to the execution context [#5678](https://github.com/voxel51/fiftyone/pull/5678)

  * Added [`ctx.operator_uri`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.operator_uri "fiftyone.operators.executor.ExecutionContext.operator_uri") to the execution context [#5678](https://github.com/voxel51/fiftyone/pull/5678)

  * Added a new `policy` param for creating [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore") items with explicit eviction policies [#5679](https://github.com/voxel51/fiftyone/pull/5679)




Core

  * Introduced [map_samples()](https://docs.voxel51.com/user_guide/using_datasets.html#map-operations) and [update_samples()](https://docs.voxel51.com/user_guide/using_datasets.html#updating-samples) methods that enable efficient, parallelized sample iteration and modification. These methods provide significant performance improvements for large datasets and include flexible options for batching, parallelization, and progress monitoring [#5642](https://github.com/voxel51/fiftyone/pull/5642)

  * Added support for creating samples with [arbitrary media types](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-media-type) [#5506](https://github.com/voxel51/fiftyone/pull/5506)

  * Optimized the content size batcher to account for compressed or encoded payloads [#5740](https://github.com/voxel51/fiftyone/pull/5740)

  * Optimized frame lookups to be as late as possible in aggregation pipelines [#5705](https://github.com/voxel51/fiftyone/pull/5705)

  * Optimized [`values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values") when retrieving an indexed field value in specific cases [#5743](https://github.com/voxel51/fiftyone/pull/5743)

  * [`Dataset.last_modified_at`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.last_modified_at "fiftyone.core.dataset.Dataset.last_modified_at") is now automatically updated when samples are deleted [#5723](https://github.com/voxel51/fiftyone/pull/5723)

  * The `last_modified_at` field of [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects is now automatically updated when frames are deleted [#5723](https://github.com/voxel51/fiftyone/pull/5723)

  * Optimized [`split_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.split_labels "fiftyone.core.collections.SampleCollection.split_labels") and [`delete_labels(view=view)`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_labels "fiftyone.core.dataset.Dataset.delete_labels") by using per-sample update operations rather than requiring full collection scans [#5730](https://github.com/voxel51/fiftyone/pull/5730)

  * Optimized [save contexts](https://docs.voxel51.com/user_guide/using_datasets.html#save-contexts) to use a more optimal batching strategy [#5747](https://github.com/voxel51/fiftyone/pull/5747)

  * Optimized the performance of [similarity queries](brain.md#brain-similarity) on full indexes [#209](https://github.com/voxel51/fiftyone-brain/pull/209)

  * Added support for similarity queries on filtered views via the [MongoDB backend](integrations__mongodb.md#mongodb-integration) [#248](https://github.com/voxel51/fiftyone-brain/pull/248)

  * Added an optional `generator=True` parameter to methods like [`add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples") that yields control to the caller after each batch of samples is added [#5666](https://github.com/voxel51/fiftyone/pull/5666)

  * Added support for automatically declaring new embedded document fields when setting sample fields [#5785](https://github.com/voxel51/fiftyone/pull/5785)

  * Added support for listing schemas without traversing embedded list fields by introducing `subfield` and `unwind` parameters to [`get_field_schema()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_field_schema "fiftyone.core.collections.SampleCollection.get_field_schema") [#5663](https://github.com/voxel51/fiftyone/pull/5663)

  * Fixed a bug that would cause spurious warnings when calling [`rename_evaluation()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_evaluation "fiftyone.core.collections.SampleCollection.rename_evaluation") on an evaluation run with [custom metrics](user_guide__evaluation.md#custom-evaluation-metrics) [#5724](https://github.com/voxel51/fiftyone/pull/5724)

  * Fixed [#5335](https://github.com/voxel51/fiftyone/issues/5335) which was causing false positives in [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") when `classwise=False` [#5697](https://github.com/voxel51/fiftyone/pull/5697)

  * Fixed a âBSON too largeâ error that would previously occur when deleting a sufficiently long list of IDs via [`delete_labels(ids=ids)`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_labels "fiftyone.core.dataset.Dataset.delete_labels") [#5730](https://github.com/voxel51/fiftyone/pull/5730)

  * Fixed a bug where default dataset name generation could result in a collision [#5759](https://github.com/voxel51/fiftyone/pull/5759)

  * Fixed vulnerabilities in `setuptools` and CVE-2025-22151 in `strawberry-graphql` [#5719](https://github.com/voxel51/fiftyone/pull/5719), [#5735](https://github.com/voxel51/fiftyone/pull/5735)




Zoo

  * Added [YOLOE](model_zoo__models__yoloev8s_seg_torch.md#model-zoo-yoloev8s-seg-torch) instance segmentation models to the Model Zoo [#5712](https://github.com/voxel51/fiftyone/pull/5712)

  * Optimized [`FiftyOneTorchDataset`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.FiftyOneTorchDataset "fiftyone.utils.torch.FiftyOneTorchDataset") to speed up model inference [#5703](https://github.com/voxel51/fiftyone/pull/5703)




Database

  * FiftyOne now [automatically manages](https://docs.voxel51.com/installation/index.html#upgrading-fiftyone) the feature compatibility version of FiftyOne-managed MongoDB instances [#5639](https://github.com/voxel51/fiftyone/pull/5639)

  * Added support for enabling [MongoDB network compression](user_guide__config.md#mongodb-network-compression) [#5693](https://github.com/voxel51/fiftyone/pull/5693)

  * Improved performance of [fiftyone migrate âinfo](https://docs.voxel51.com/cli/index.html#cli-fiftyone-migrate) [#5672](https://github.com/voxel51/fiftyone/pull/5672)

  * Raised the minimum MongoDB version from 4.4 to 5.0 in accordance with our [deprecation schedule](deprecation.md#deprecation-mongodb-4-4). FiftyOne will now raise exceptions if the MongoDB version is lower than 5.0 unless [database validation is disabled](user_guide__config.md#using-a-different-mongodb-version) [#5682](https://github.com/voxel51/fiftyone/pull/5682)




## FiftyOne Enterprise 2.7.2#

_Released April 4, 2025_

Includes all updates from FiftyOne 1.4.1

## FiftyOne 1.4.1#

_Released April 4, 2025_

App

  * Fixed rendering of samples in the App that are missing a label tags list [#5686](https://github.com/voxel51/fiftyone/pull/5686)

  * Fixed built-in sort by similarity for patches views [#5685](https://github.com/voxel51/fiftyone/pull/5685)

  * Enabled sample tagging in the modal when a selection is present regardless of sidebar filters [#5684](https://github.com/voxel51/fiftyone/pull/5684)

  * Fixed tagging in the modal for video samples [#5683](https://github.com/voxel51/fiftyone/pull/5683)

  * Fixed label tags filtering in the [Query Performance](user_guide__app.md#app-optimizing-query-performance) sidebar [#5675](https://github.com/voxel51/fiftyone/pull/5675)

  * Fixed bug when entering invalid id into sidebar id filter [#5655](https://github.com/voxel51/fiftyone/pull/5655)




## FiftyOne Enterprise 2.7.1#

_Released March 24, 2025_

  * Fixed the [CVE-2025-29927](https://github.com/advisories/GHSA-f82v-jwr5-mffw) vulnerability related to next.js




## FiftyOne Enterprise 2.7.0#

_Released March 21, 2025_

Includes all updates from FiftyOne 1.4.0, plus:

  * Renamed FiftyOne Teams to FiftyOne Enterprise

  * Expanded functionality of the [Runs page](enterprise__plugins.md#enterprise-runs-page), including providing Admins a view of [delegated operations](enterprise__plugins.md#enterprise-delegated-operations) across all datasets and users, and adding support for viewing and downloading logs in a new [Logs tab](enterprise__plugins.md#enterprise-run-page-logs)

  * Added support for adding [spatial indexes](brain.md#brain-optimizing-lassoing-performance) when creating visualizations via the [Embeddings panel](user_guide__app.md#app-embeddings-panel) to optimize lasso performance

  * Added a new builtin `manage_visualization_indexes` operator for adding/removing [spatial indexes](brain.md#brain-optimizing-lassoing-performance) to existing visualization results from the App

  * Added support for selecting embedded fields in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) and [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel)

  * Added a new `cloud_storage_id` argument to the [CVAT integration](integrations__cvat.md#cvat-integration) to specify the ID of the cloud storage to use for the CVAT tasks that are created

  * Added configurable connect and read timeouts for the API client

  * Added support for filepath aliases/prefixes when using per-user cloud credentials

  * Added support for 3D media to per-user cloud credentials

  * Optimized the [Data Quality Panel](enterprise__data_quality.md#data-quality) when loading large datasets

  * Optimized streaming API responses

  * Improved error messages related to license files and compliance

  * Security fixes for vitest, nanoid, dompurify, setuptools, and axios

  * Fixed a bug where using the [Query Performance Panel](enterprise__query_performance.md#query-performance) to create an index could result in an error message

  * Fixed a bug that allowed users to accidentally exceed license limits when auto-join was enabled

  * Fixed a bug where, in certain cases, the system would incorrectly retry `insert_many` operations




## FiftyOne 1.4.0#

_Released March 21, 2025_

App

  * Improved grid performance by only rendering labels when they are actually visible and hiding dense label fields like [heatmaps](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) and [semantic segmentations](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation) by default [#5356](https://github.com/voxel51/fiftyone/pull/5356)

  * Added support for configuring the [default visibility](user_guide__app.md#app-fields-sidebar) of fields [#5356](https://github.com/voxel51/fiftyone/pull/5356)

  * Improved performance and stability of the grid by explicitly managing memory usage of the grid cache and allowing users to set the memory limit of that cache [#5214](https://github.com/voxel51/fiftyone/pull/5214), [#5548](https://github.com/voxel51/fiftyone/pull/5548)

  * Improved buffering behavior, particularly for longer videos [#5515](https://github.com/voxel51/fiftyone/pull/5515)

  * [Query Performance](user_guide__app.md#app-optimizing-query-performance) mode now supports views that select/exclude slices of group datasets [#5428](https://github.com/voxel51/fiftyone/pull/5428), [#5460](https://github.com/voxel51/fiftyone/pull/5460)

  * Improved performance of sample field filtering on large video samples in the grid [#5450](https://github.com/voxel51/fiftyone/pull/5450)

  * Optimized sidebar counts when [Query Performance](user_guide__app.md#app-optimizing-query-performance) is enabled [#5538](https://github.com/voxel51/fiftyone/pull/5538)

  * Removed an inapplicable sidebar sorting option from the settings menu when [Query Performance](user_guide__app.md#app-optimizing-query-performance) is enabled [#5531](https://github.com/voxel51/fiftyone/pull/5531)

  * Fixed hard errors related to invalid ID searches in the sidebar [#5415](https://github.com/voxel51/fiftyone/pull/5415)

  * Fixed a mask rendering bug related to missing MIME type [#5419](https://github.com/voxel51/fiftyone/pull/5419)

  * Fixed a bug where [`session.wait()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.wait "fiftyone.core.session.Session.wait") would prematurely exit while App windows remained open [#5437](https://github.com/voxel51/fiftyone/pull/5437)

  * Fixed a bug when animating frame sequences with 0 or 1 frames [#5442](https://github.com/voxel51/fiftyone/pull/5442)

  * Fixed a bug where color schemes may not correctly reset when switching datasets [#5485](https://github.com/voxel51/fiftyone/pull/5485)

  * Fixed sample updates after tagging in the modal [#5514](https://github.com/voxel51/fiftyone/pull/5514)

  * Fixed a data formatting bug in [`Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels") [#5533](https://github.com/voxel51/fiftyone/pull/5533)

  * Fixed a bug when deleting [custom workspaces](user_guide__app.md#app-workspaces) [#5590](https://github.com/voxel51/fiftyone/pull/5590)




Embeddings Panel

  * Added support for adding [spatial indexes](brain.md#brain-optimizing-lassoing-performance) to embeddings visualizations to optimize lasso performance when using the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#5500](https://github.com/voxel51/fiftyone/pull/5500), [#5534](https://github.com/voxel51/fiftyone/pull/5534), [#5539](https://github.com/voxel51/fiftyone/pull/5539)




Model Evaluation Panel

  * Users can now rename and delete evaluations from the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) [#5553](https://github.com/voxel51/fiftyone/pull/5553), [#5559](https://github.com/voxel51/fiftyone/pull/5559)

  * Evaluation types are now clearly indicated [#5509](https://github.com/voxel51/fiftyone/pull/5509)

  * Model comparisons are now restricted to evaluation runs of compatible types [#5541](https://github.com/voxel51/fiftyone/pull/5541)

  * Custom metrics can now be added to existing evaluations via a new [`results.add_custom_metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.add_custom_metrics "fiftyone.utils.eval.base.BaseEvaluationResults.add_custom_metrics") method [#5436](https://github.com/voxel51/fiftyone/pull/5436)

  * Fixed a bug when rendering performance charts for semantic segmentations with no provided mask targets [#5504](https://github.com/voxel51/fiftyone/pull/5504)




Core

  * Relaxed SDK <> database compatibility to allow connections when both are within the same major version, starting from this release [#5581](https://github.com/voxel51/fiftyone/pull/5581)

  * Added a [`map_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.map_values "fiftyone.core.collections.SampleCollection.map_values") view stage that generalizes [`map_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.map_labels "fiftyone.core.collections.SampleCollection.map_labels") to any field or embedded field

  * Added a builtin `edit_field_values` operator that allows for bulk editing field values from the App

  * [`ViewExpression.map_values(mapping)`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.map_values "fiftyone.core.expressions.ViewExpression.map_values") now supports mapping dicts with None keys [#5561](https://github.com/voxel51/fiftyone/pull/5561)

  * Added a [`to_torch()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_torch "fiftyone.core.collections.SampleCollection.to_torch") method for converting FiftyOne datasets into Torch Datasets [#5321](https://github.com/voxel51/fiftyone/pull/5321)

  * Added a [`select_group_slices(..., flat=False)`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_group_slices "fiftyone.core.collections.SampleCollection.select_group_slices") syntax for selecting group slices without flattening [#5198](https://github.com/voxel51/fiftyone/pull/5198)

  * Added an [`exclude_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_group_slices "fiftyone.core.collections.SampleCollection.exclude_group_slices") method for excluding group slices [#5198](https://github.com/voxel51/fiftyone/pull/5198)

  * Optimized [`compute_metadata()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_metadata "fiftyone.core.collections.SampleCollection.compute_metadata") for PNGs [#5564](https://github.com/voxel51/fiftyone/pull/5564)

  * Added a [`binarize_instances()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.binarize_instances "fiftyone.utils.labels.binarize_instances") utility for converting instance segmentation masks in `[0, 255]` into binary instance masks [#5516](https://github.com/voxel51/fiftyone/pull/5516)

  * Updated the runs interface to correctly record when runs are performed on full datasets [#5519](https://github.com/voxel51/fiftyone/pull/5519)

  * Added support for list values to [`deserialize_value()`](api__fiftyone.core.odm.md#fiftyone.core.odm.deserialize_value "fiftyone.core.odm.deserialize_value")

  * Added support for setting nested list attributes directly via `Sample.__setitem__` [#5582](https://github.com/voxel51/fiftyone/pull/5582)

  * Fixed a bug that prevented importing data in [FiftyOneDataset](user_guide__import_datasets.md#fiftyonedataset-import) format to non-empty datasets [#5586](https://github.com/voxel51/fiftyone/pull/5586)

  * Fixed recomputing frames on a video dataset [#5554](https://github.com/voxel51/fiftyone/pull/5554)

  * Fixed installation on Windows from source [#5481](https://github.com/voxel51/fiftyone/pull/5481)




Annotation

  * Added support for [3D cuboid annotation](integrations__cvat.md#cvat-3d) on point clouds with CVAT [#5458](https://github.com/voxel51/fiftyone/pull/5458)

  * Added support for annotating rotated bounding boxes with CVAT [#5457](https://github.com/voxel51/fiftyone/pull/5457)

  * Annotation label schema attributes now support custom attributes for annotation backends [#5502](https://github.com/voxel51/fiftyone/pull/5502)




Brain

  * Added a new [Pgvector vector search](integrations__pgvector.md#pgvector-integration) integration [#234](https://github.com/voxel51/fiftyone-brain/pull/234), [#222](https://github.com/voxel51/fiftyone-brain/pull/222)

  * Added a new [Mosaic AI vector search](integrations__mosaic.md#mosaic-integration) integration [#233](https://github.com/voxel51/fiftyone-brain/pull/233)

  * Added optional `create_index=True` and `points_field` arguments to [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") to allow users to add [spatial indexes](brain.md#brain-optimizing-lassoing-performance) when creating visualizations to optimize lasso performance in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#236](https://github.com/voxel51/fiftyone-brain/pull/236)

  * Optimized usage of [similarity indexes](brain.md#brain-similarity) initially defined on views by registering the full dataset [#238](https://github.com/voxel51/fiftyone-brain/pull/238)

  * The [Redis vector search](integrations__redis.md#redis-integration) backend now supports similarity queries with more than 10 results [#240](https://github.com/voxel51/fiftyone-brain/pull/240)




Zoo

  * Populated author and license information for all zoo models/datasets [#5438](https://github.com/voxel51/fiftyone/pull/5438)

  * Adds support for filtering zoo models by license via [`list_zoo_models(..., license="MIT")`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_zoo_models "fiftyone.zoo.models.list_zoo_models") [#5438](https://github.com/voxel51/fiftyone/pull/5438)

  * Adds support for filtering zoo datasets by license via [`list_zoo_datasets(..., license="CC-BY-4.0")`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.list_zoo_datasets "fiftyone.zoo.datasets.list_zoo_datasets") [#5438](https://github.com/voxel51/fiftyone/pull/5438)

  * Added support for [declaring custom parameters](model_zoo__remote.md#model-zoo-remote-creation) when defining remote zoo models [#5439](https://github.com/voxel51/fiftyone/pull/5439)




CLI

  * Added support for glob patterns when listing operators via the CLI [#5587](https://github.com/voxel51/fiftyone/pull/5587)




Docs

  * Fixed some documentation typos/broken links [#5558](https://github.com/voxel51/fiftyone/pull/5558), [#235](https://github.com/voxel51/fiftyone-brain/pull/235)




## FiftyOne Enterprise 2.6.2#

_Released March 12, 2025_

Includes all updates from FiftyOne 1.3.2

## FiftyOne 1.3.2#

_Released March 12, 2025_

SDK

  * Fixed a bug [#5486](https://github.com/voxel51/fiftyone/issues/5486) that caused model evaluation to fail in certain cases [#5472](https://github.com/voxel51/fiftyone/pull/5472)




## FiftyOne Enterprise 2.6.1#

_Released February 28, 2025_

Includes all updates from FiftyOne 1.3.1, plus:

  * Per-user cloud credentials now support masks and 3D media

  * Security fixes for nextjs, cookie, cross-spawn, and lodash

  * Bump node version to 22




## FiftyOne 1.3.1#

_Released February 28, 2025_

App

  * Optimized modal tagger to support massive datasets [#5417](https://github.com/voxel51/fiftyone/pull/5417)

  * Fixed a bug with sample updates after tagging in the modal [#5514](https://github.com/voxel51/fiftyone/pull/5514)




## FiftyOne Enterprise 2.6.0#

_Released February 10, 2025_

  * Improved backwards compatibility between an older SDK and newer deployment.

  * Added a configurable banner which appears at top and bottom of every page, often used for compliance reasons.

  * Fixed a bug where invite email smtp configuration was not saving correctly.




## FiftyOne Enterprise 2.5.1#

_Released February 3, 2025_

  * Fixed a bug where we displayed a session error before initial user login




## FiftyOne Enterprise 2.5.0#

_Released January 24, 2025_

Includes all updates from FiftyOne 1.3.0, plus:

  * Fixed a bug which prevented very large media from being fetched

  * Fixed a race condition which prevented downloading initial batches of cloud media




## FiftyOne 1.3.0#

_Released January 24, 2025_

App

  * Reduced memory requirements for [heatmap fields](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) by 4x! [#5340](https://github.com/voxel51/fiftyone/pull/5340)

  * Optimized rendering of dense label masks like segmentations and heatmaps [#5337](https://github.com/voxel51/fiftyone/pull/5337)

  * Added support for rendering 16 bit PNG label masks [#5413](https://github.com/voxel51/fiftyone/pull/5413)

  * Added support for rendering JPG label masks [#5406](https://github.com/voxel51/fiftyone/pull/5406)

  * Improved robustness when label mask MIME type is missing [#5419](https://github.com/voxel51/fiftyone/pull/5419)

  * Added support for [multiple media fields](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-media-fields) when viewing [dynamic groups](user_guide__app.md#app-dynamic-groups) of image frames [#5394](https://github.com/voxel51/fiftyone/pull/5394)

  * Improved stability of the [tagging menu](user_guide__app.md#app-tagging) when adding new sample/label tags [#5378](https://github.com/voxel51/fiftyone/pull/5378)

  * Added a `dynamic_groups_target_frame_rate` setting to the [dataset app config](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config) that allows users to configure the target frame rate when animating [dynamic groups](user_guide__app.md#app-dynamic-groups) in the modal [#5368](https://github.com/voxel51/fiftyone/pull/5368)

  * Fixed a bug that prevented expanding the `label tags` sidebar facet for datasets that contain [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields [#5322](https://github.com/voxel51/fiftyone/pull/5322)

  * Improved reliability when running the App in GitHub Codespaces [#5349](https://github.com/voxel51/fiftyone/pull/5349)




SDK

  * Significantly optimized `len(dataset)` and [`dataset.count()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.count "fiftyone.core.dataset.Dataset.count") by using estimated document counts when possible [#5398](https://github.com/voxel51/fiftyone/pull/5398)

  * Added index usage info to [`get_index_information()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_index_information "fiftyone.core.collections.SampleCollection.get_index_information") [#5320](https://github.com/voxel51/fiftyone/pull/5320)

  * Improved error messaging when attempting to add [dynamic attributes](https://docs.voxel51.com/user_guide/using_datasets.html#dynamic-attributes) whose names clash with reserved attributes [#5357](https://github.com/voxel51/fiftyone/pull/5357)

  * [`Polyline.to_detection()`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.to_detection "fiftyone.core.labels.Polyline.to_detection") now gracefully handles polylines with no vertices [#642](https://github.com/voxel51/eta/pull/642)

  * Added a `create_index` parameter to the [`geo_near()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.geo_near "fiftyone.core.collections.SampleCollection.geo_near") and [`geo_within()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.geo_within "fiftyone.core.collections.SampleCollection.geo_within") view stages for consistency with [`sort_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by "fiftyone.core.collections.SampleCollection.sort_by") and [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by") [#5325](https://github.com/voxel51/fiftyone/pull/5325)




Annotation

  * A datasetâs [mask targets](https://docs.voxel51.com/user_guide/using_datasets.html#storing-mask-targets) are now automatically used by default when annotating existing segmentation fields [#5318](https://github.com/voxel51/fiftyone/pull/5318)

  * The [CVAT integration](integrations__cvat.md#cvat-integration) now supports annotating instance segmentations via the brush tool when connected to [CVAT Server >=- 2.5](https://github.com/cvat-ai/cvat/releases/tag/v2.3.0) [#5319](https://github.com/voxel51/fiftyone/pull/5319)




Evaluation

  * Added support for defining [custom evaluation metrics](user_guide__evaluation.md#custom-evaluation-metrics) and applying them when evaluating models [#5279](https://github.com/voxel51/fiftyone/pull/5279)

  * Added COCO-style Mean Average Recall (mAR) to [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") [#5274](https://github.com/voxel51/fiftyone/pull/5274)

  * Clicking the class performance bars and confusion matrix cells in the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) will now automatically load the corresponding views in the samples panel for [segmentation evaluations](user_guide__evaluation.md#evaluating-segmentations) [#5332](https://github.com/voxel51/fiftyone/pull/5332)

  * Added a display options settings cog to the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) when viewing results in table view [#5367](https://github.com/voxel51/fiftyone/pull/5367)

  * Added an `include_missing=True` option to [`plot_confusion_matrix()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseClassificationResults.plot_confusion_matrix "fiftyone.utils.eval.base.BaseClassificationResults.plot_confusion_matrix") [#5408](https://github.com/voxel51/fiftyone/pull/5408)

  * Fixed a bug where [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") would fail when applied to [keypoint fields](https://docs.voxel51.com/user_guide/using_datasets.html#keypoints) [#5344](https://github.com/voxel51/fiftyone/pull/5344)




Brain

  * Added support for cloud URIs to the [LanceDB integration](integrations__lancedb.md#lancedb-integration) [#228](https://github.com/voxel51/fiftyone-brain/pull/228)

  * Removed usage of the deprecated `InsetPosition` class when [visualizing embeddings](user_guide__plots.md#embeddings-plots) via the `matplotlib` backend [#5343](https://github.com/voxel51/fiftyone/pull/5343)




Zoo

  * Added [DINOv2 with registers](model_zoo__models__dinov2_vits14_reg_torch.md#model-zoo-dinov2-vits14-reg-torch) to the model zoo! [#5201](https://github.com/voxel51/fiftyone/pull/5201)

  * All Torch models in the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) will now automatically use GPU resources when available [#5026](https://github.com/voxel51/fiftyone/pull/5026)




Plugins

  * Upgraded all applicable [`builtin operators`](plugins__api__plugins.operators.md#module-plugins.operators "plugins.operators") to support bulk actions on multiple fields at once [#5379](https://github.com/voxel51/fiftyone/pull/5379)

  * Added [`show_sidebar()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.show_sidebar "fiftyone.operators.operations.Operations.show_sidebar"), [`hide_sidebar()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.hide_sidebar "fiftyone.operators.operations.Operations.hide_sidebar"), and [`toggle_sidebar()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.toggle_sidebar "fiftyone.operators.operations.Operations.toggle_sidebar") operations to programmatically show/hide/toggle the visibility of the Appâs sidebar [#5297](https://github.com/voxel51/fiftyone/pull/5297)

  * Automatically coerce empty input fields back to `None` in [`str()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.str "fiftyone.operators.types.Object.str") and [`list()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.list "fiftyone.operators.types.Object.list") properties [#5375](https://github.com/voxel51/fiftyone/pull/5375)

  * Improved default user interface of [`DropdownView(multiple=True)`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView "fiftyone.operators.types.DropdownView") views to support autocomplete, tag bubbles, and easy deletion via the `ESC` keyboard shortcut [#5375](https://github.com/voxel51/fiftyone/pull/5375)

  * The [`download_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.download_plugin "fiftyone.plugins.core.download_plugin") method and [@voxel51/plugins/install_plugin](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/plugins) operator now support installing plugins from GitHub branches that contain slashes and/or nested tree paths [#5324](https://github.com/voxel51/fiftyone/pull/5324)




CLI

  * Added metadata about builtin plugins to the [fiftyone plugins list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-list) command [#5333](https://github.com/voxel51/fiftyone/pull/5333)




## FiftyOne Enterprise 2.4.0#

_Released January 10, 2025_

  * Added ability to set a user-specific auth header when making media queries.




## FiftyOne Enterprise 2.3.0#

_Released December 20, 2024_

Includes all updates from FiftyOne 1.2.0, plus:

  * Added an example [Databricks connector](enterprise__data_lens.md#data-lens-databricks) showing how to connect FiftyOne Enterprise to your lakehouse via [Data Lens](enterprise__data_lens.md#data-lens)

  * Added a [Data Lens connector](enterprise__data_lens.md#data-lens-snippet-remap-fields) that demonstrates how to allow users to dynamically configure the field(s) that are imported

  * [Data Lens](enterprise__data_lens.md#data-lens) now supports previewing 3D data imports

  * Guest users can now open [Data Lens](enterprise__data_lens.md#data-lens)

  * When scanning for issues with the [Data Quality Panel](enterprise__data_quality.md#data-quality), any fields created are now added to a `DATA QUALITY` sidebar group

  * Prevented unnecessary scrollbars from appearing when using the [Data Quality Panel](enterprise__data_quality.md#data-quality)

  * AWS session tokens are now supported when configuring [cloud credentials](enterprise__installation.md#enterprise-cloud-credentials)

  * Fixed a bug that could cause `StopIteration` errors when performing long-running operations like computing embeddings when using [API connections](enterprise__api_connection.md#enterprise-api-connection)




## FiftyOne 1.2.0#

_Released December 20, 2024_

App

  * Added support for [instance segmentations](https://docs.voxel51.com/user_guide/using_datasets.html#instance-segmentation) whose masks are stored on-disk [#5120](https://github.com/voxel51/fiftyone/pull/5120), [#5256](https://github.com/voxel51/fiftyone/pull/5256)

  * Optimized overlay rendering for dense label fields like segmentations and heatmaps [#5156](https://github.com/voxel51/fiftyone/pull/5156), [#5169](https://github.com/voxel51/fiftyone/pull/5169), [#5247](https://github.com/voxel51/fiftyone/pull/5247)

  * Improved stability of frame rendering for videos [#5199](https://github.com/voxel51/fiftyone/pull/5199), [#5293](https://github.com/voxel51/fiftyone/pull/5293)

  * Sidebar groups that contain only list fields are no longer collapsed by default [#5280](https://github.com/voxel51/fiftyone/pull/5280)

  * The [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) now filters both ground truth and prediction fields when you perform interactive filters via the TP/FP/FN icons, per-class histograms, and confusion matrices [#5268](https://github.com/voxel51/fiftyone/pull/5268)

  * When comparing two models in the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel), interactive filters now apply to both evaluation runs [#5268](https://github.com/voxel51/fiftyone/pull/5268)

  * The [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) now supports evaluations that were performed on subsets (views) of the full dataset [#5267](https://github.com/voxel51/fiftyone/pull/5267)

  * The [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) now shows mask targets for segmentation evaluations when they are available [#5281](https://github.com/voxel51/fiftyone/pull/5281)

  * The [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) now hides metrics that arenât applicable to a given evaluation type [#5281](https://github.com/voxel51/fiftyone/pull/5281)

  * Fixed an issue where backtick canât be typed when editing markdown notes in the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) [#5233](https://github.com/voxel51/fiftyone/pull/5233)

  * Fixed a race condition that could cause errors when performing [text similarity searches](brain.md#brain-similarity-text) [#5273](https://github.com/voxel51/fiftyone/pull/5273)

  * Fixed a caching bug that prevented label overlay font sizes from dynamically resizing as expected in some cases [#5287](https://github.com/voxel51/fiftyone/pull/5287)

  * Fixed a bug that excluded selected samples from the counter above the Samples panel [#5286](https://github.com/voxel51/fiftyone/pull/5286)




SDK

  * Optimized [`dataset.first()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.first "fiftyone.core.dataset.Dataset.first") calls [#5305](https://github.com/voxel51/fiftyone/pull/5305)




Brain

  * Upgraded the [MongoDB vector search integration](integrations__mongodb.md#mongodb-integration) to use the `vectorSearch` type [#218](https://github.com/voxel51/fiftyone-brain/pull/218)




Zoo

  * Fixed a bug with loading the [rtdetr-l-coco-torch](model_zoo__models__rtdetr_l_coco_torch.md#model-zoo-rtdetr-l-coco-torch) and [rtdetr-x-coco-torch](model_zoo__models__rtdetr_x_coco_torch.md#model-zoo-rtdetr-x-coco-torch) zoo models [#5220](https://github.com/voxel51/fiftyone/pull/5220)




## FiftyOne Enterprise 2.2.0#

_Released December 6, 2024_

Includes all updates from FiftyOne 1.1.0, plus:

  * All Enterprise deployments now have builtin compute capacity for executing [delegated operations](enterprise__plugins.md#enterprise-delegated-operations) in the background while you work in the App

  * Introduced [Data Lens](enterprise__data_lens.md#data-lens), which allows you to explore and import samples from external data sources into FiftyOne

  * Added a [Data Quality Panel](enterprise__data_quality.md#data-quality) that automatically scans your data for quality issues and helps you take action to resolve them

  * Added a [Query Performance Panel](enterprise__query_performance.md#query-performance) that helps you create the necessary indexes to optimize queries on large datasets

  * Added support for creating embeddings visualizations natively from the [Embeddings panel](user_guide__app.md#app-embeddings-panel)

  * Added support for evaluating models natively from the [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel)

  * Added support for [configuring an SMTP server](enterprise__pluggable_auth.md#identity-providers) for sending user invitations via email when running in [Internal Mode](enterprise__pluggable_auth.md#internal-mode)




## FiftyOne 1.1.0#

_Released December 6, 2024_

Whatâs New

  * Added a [Model Evaluation panel](user_guide__app.md#app-model-evaluation-panel) for visually and interactively evaluating models in the FiftyOne App

  * Introduced [Query Performance](user_guide__app.md#app-optimizing-query-performance) in the App, which automatically nudges you to create the necessary indexes to greatly optimize queries on large datasets

  * Added a [leaky splits method](brain.md#brain-leaky-splits) for automatically detecting near-duplicate samples in different splits of your datasets

  * Added a [near duplicates method](brain.md#brain-near-duplicates) that scans your datasets and detects potential duplicate samples




App

  * Added zoom-to-crop and set-look-at for selected labels in the [3D visualizer](user_guide__app.md#app-3d-visualizer) [#4931](https://github.com/voxel51/fiftyone/pull/4931)

  * Gracefully handle deleted + recreated datasets of the same name [#5183](https://github.com/voxel51/fiftyone/pull/5183)

  * Added a `referrerPolicy` so the App can run behind reverse proxies [#4944](https://github.com/voxel51/fiftyone/pull/4944)

  * Fixed a bug that prevented video playback from working for videos with unknown frame rate [#5155](https://github.com/voxel51/fiftyone/pull/5155)




SDK

  * Added [`min()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.min "fiftyone.core.collections.SampleCollection.min") and [`max()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.max "fiftyone.core.collections.SampleCollection.max") and aggregations [#5029](https://github.com/voxel51/fiftyone/pull/5029)

  * Optimized object detection evaluation with r-trees [#4758](https://github.com/voxel51/fiftyone/pull/4758)

  * Improved support for creating summary fields and indexes [#5091](https://github.com/voxel51/fiftyone/pull/5091)

  * Added support for creating compound indexes when using the builtin [`create_index`](plugins__api__plugins.operators.md#plugins.operators.CreateIndex "plugins.operators.CreateIndex") operator that optimize sidebar queries for group datasets [#5174](https://github.com/voxel51/fiftyone/pull/5174)

  * The builtin [`clear_sample_field`](plugins__api__plugins.operators.md#plugins.operators.ClearSampleField "plugins.operators.ClearSampleField") and [`clear_frame_field`](plugins__api__plugins.operators.md#plugins.operators.ClearFrameField "plugins.operators.ClearFrameField") operators now support clearing fields of views, in addition to full datasets [#5122](https://github.com/voxel51/fiftyone/pull/5122)

  * Fixed a bug that prevented users with `pydantic` installed from loading the [quickstart-3d dataset](dataset_zoo__datasets__quickstart_3d.md#dataset-zoo-quickstart-3d) from the zoo [#4994](https://github.com/voxel51/fiftyone/pull/4994)

  * Added optional `email` parameter to the [CVAT integration](integrations__cvat.md#cvat-integration) [#5218](https://github.com/voxel51/fiftyone/pull/5218)




Brain

  * Added support for passing existing [similarity indexes](brain.md#brain-similarity) to [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization"), [`compute_uniqueness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_uniqueness "fiftyone.brain.compute_uniqueness"), and [`compute_representativeness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_representativeness "fiftyone.brain.compute_representativeness") [#201](https://github.com/voxel51/fiftyone-brain/pull/201), [#204](https://github.com/voxel51/fiftyone-brain/pull/204)

  * Upgraded the [Pinecone integration](integrations__pinecone.md#pinecone-integration) to support `pinecone-client>=3.2` [#202](https://github.com/voxel51/fiftyone-brain/pull/202)




Plugins

  * Added an [Execution Store](plugins__developing_plugins.md#panel-execution-store) that provides a key-value interface for persisting data beyond the lifetime of a panel [#4827](https://github.com/voxel51/fiftyone/pull/4827), [#5144](https://github.com/voxel51/fiftyone/pull/5144)

  * Added [`ctx.spaces`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.spaces "fiftyone.operators.executor.ExecutionContext.spaces") and [`set_spaces()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_spaces "fiftyone.operators.operations.Operations.set_spaces") to the operator execution context [#4902](https://github.com/voxel51/fiftyone/pull/4902)

  * Added [`open_sample()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.open_sample "fiftyone.operators.operations.Operations.open_sample") and [`close_sample()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.close_sample "fiftyone.operators.operations.Operations.close_sample") methods for programmatically controlling what sample(s) are displayed in the Appâs sample modal [#5168](https://github.com/voxel51/fiftyone/pull/5168)

  * Added a `skip_prompt` option to [`ctx.prompt`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.prompt "fiftyone.operators.executor.ExecutionContext.prompt"), allowing users to bypass prompts during operation execution [#4992](https://github.com/voxel51/fiftyone/pull/4992)

  * Introduced a new [`StatusButtonView`](api__fiftyone.operators.types.md#fiftyone.operators.types.StatusButtonView "fiftyone.operators.types.StatusButtonView") type for rendering buttons with status indicators [#5105](https://github.com/voxel51/fiftyone/pull/5105)

  * Added support for giving [`ImageView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ImageView "fiftyone.operators.types.ImageView") components click targets [#4996](https://github.com/voxel51/fiftyone/pull/4996)

  * Added an [allow_legacy_orchestrators](user_guide__config.md#configuring-fiftyone) config flag to enable running delegated operations [locally](plugins__using_plugins.md#delegated-orchestrator-open-source) [#5176](https://github.com/voxel51/fiftyone/pull/5176)

  * Fixed a bug when running delegated operations [programmatically](plugins__using_plugins.md#direct-operator-execution) [#5180](https://github.com/voxel51/fiftyone/pull/5180)

  * Fixed a bug when running delegated operations with output schemas on MongoDB <v5 [#5181](https://github.com/voxel51/fiftyone/pull/5181)




## FiftyOne Enterprise 2.1.3#

_Released November 8, 2024_

Includes all updates from FiftyOne 1.0.2.

## FiftyOne 1.0.2#

_Released November 8, 2024_

Zoo

  * Added [SAM 2.1](model_zoo__models__segment_anything_2_1_hiera_base_plus_image_torch.md#model-zoo-segment-anything-2-1-hiera-base-plus-image-torch) to the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) [#4979](https://github.com/voxel51/fiftyone/pull/4979)

  * Added [YOLO11](integrations__ultralytics.md#ultralytics-instance-segmentation) to the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) [#4899](https://github.com/voxel51/fiftyone/pull/4899)

  * Added generic model architecture and backbone tags to all relevant models [in the zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) for easier navigation [#4899](https://github.com/voxel51/fiftyone/pull/4899)




Core

  * Fixed input shape in the depth estimation transformer [#5035](https://github.com/voxel51/fiftyone/pull/5035)

  * Added graceful handling of empty datasets when computing embeddings [#5043](https://github.com/voxel51/fiftyone/pull/5043)




App

  * Added a new [`TimelineView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimelineView "fiftyone.operators.types.TimelineView") for building custom animations [#4965](https://github.com/voxel51/fiftyone/pull/4965)

  * Fixed overlay z-index and overflow for panels [#4956](https://github.com/voxel51/fiftyone/pull/4956)

  * Fixed bug where timeline name wasnât being forwarded in seek utils [#4975](https://github.com/voxel51/fiftyone/pull/4975)

  * Performance improvements in the grid and modal [#5009](https://github.com/voxel51/fiftyone/pull/5009), [#5015](https://github.com/voxel51/fiftyone/pull/5015), [#5018](https://github.com/voxel51/fiftyone/pull/5018), [#5019](https://github.com/voxel51/fiftyone/pull/5019), [#5022](https://github.com/voxel51/fiftyone/pull/5022)

  * Fixed batch selection with ctrl + click in the grid [#5046](https://github.com/voxel51/fiftyone/pull/5046)




## FiftyOne Enterprise 2.1.2#

_Released October 31, 2024_

  * Fixed an issue that prevented `delegation_target` from being properly set when running delegated operations with orchestrator registration enabled




## FiftyOne Enterprise 2.1.1#

_Released October 14, 2024_

Includes all updates from FiftyOne 1.0.1, plus:

  * Fixed an issue with Auth0 connections for deployments behind proxies

  * Bumped dependency requirement `voxel51-eta>=0.13`




## FiftyOne 1.0.1#

_Released October 14, 2024_

App

  * Video playback now supports the timeline API [#4878](https://github.com/voxel51/fiftyone/pull/4878)

  * Added utils to support a [rerun](https://rerun.io) panel [#4876](https://github.com/voxel51/fiftyone/pull/4876)

  * Fixed a bug that prevented [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") labels from rendering [#4891](https://github.com/voxel51/fiftyone/pull/4891)

  * Fixed a bug that prevented the `fiftyone quickstart` and `fiftyone app launch` commands from launching the App [#4888](https://github.com/voxel51/fiftyone/pull/4888)




Core

  * COCO exports now use 1-based categories [#4884](https://github.com/voxel51/fiftyone/pull/4884)

  * Fixed a bug when passing the `classes` argument to load specific classes in [COCO format](user_guide__import_datasets.md#cocodetectiondataset-import) [#4884](https://github.com/voxel51/fiftyone/pull/4884)




## FiftyOne Enterprise 2.1.0#

_Released October 1, 2024_

Includes all updates from FiftyOne 1.0.0, plus:

  * Super admins can now migrate their deployments to [Internal Mode](enterprise__pluggable_auth.md#internal-mode) via the [Super Admin UI](enterprise__pluggable_auth.md#super-admin-ui)

  * Added support for sending user invitations in [Internal Mode](enterprise__pluggable_auth.md#internal-mode)

  * Optimized performance of the [dataset page](enterprise__app.md#enterprise-homepage)

  * Fixed a BSON serialization bug that could cause errors when cloning or exporting certain dataset views from the Enterprise UI




## FiftyOne 1.0.0#

_Released October 1, 2024_

Whatâs New

  * The [FiftyOne Brain](https://github.com/voxel51/fiftyone-brain) is now fully open source. Contributions are welcome!

  * Added [Modal Panels](plugins__developing_plugins.md#panel-config), bringing the ability to develop and use panels in the Appâs sample modal [#4625](https://github.com/voxel51/fiftyone/pull/4625)

  * All datasets now have [automatically populated](https://docs.voxel51.com/user_guide/using_datasets.html#default-sample-fields) `created_at` and `last_modified_at` fields on their samples and frames [#4597](https://github.com/voxel51/fiftyone/pull/4597)

  * Added support for loading [remotely-sourced zoo datasets](dataset_zoo__remote.md#dataset-zoo-remote) whose download/preparation instructions are stored in GitHub or public URLs [#4752](https://github.com/voxel51/fiftyone/pull/4752)

  * Added support for loading [remotely-sourced zoo models](model_zoo__remote.md#model-zoo-remote) whose definitions are stored in GitHub or public URLs [#4786](https://github.com/voxel51/fiftyone/pull/4786)

  * Added [Med-SAM2](https://arxiv.org/abs/2408.00874) to the [model zoo](model_zoo__models__med_sam_2_video_torch.md#model-zoo-med-sam-2-video-torch)! [#4733](https://github.com/voxel51/fiftyone/pull/4733), [#4828](https://github.com/voxel51/fiftyone/pull/4828)




App

  * Added dozens of [builtin operators](plugins__using_plugins.md#using-operators) for performing common operations directly from the App [#4830](https://github.com/voxel51/fiftyone/pull/4830)

  * Label overlays in the grid are now scaled proportionally to grid zoom [#4747](https://github.com/voxel51/fiftyone/pull/4747)

  * Improved support for visualizing and filtering [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument") list fields [#4833](https://github.com/voxel51/fiftyone/pull/4833)

  * Added a new timeline API for synchronizing playback of multiple modal panels [#4772](https://github.com/voxel51/fiftyone/pull/4772)

  * Improved UI, documentation, and robustness when working with [custom color schemes](user_guide__app.md#app-color-schemes-app) [#4763](https://github.com/voxel51/fiftyone/pull/4763)

  * Fixed a bug where the active group slice was not being persisted when navigating between groups in the modal [#4836](https://github.com/voxel51/fiftyone/pull/4836)

  * Fixed a bug when selecting samples in grouped datasets in the modal [#4789](https://github.com/voxel51/fiftyone/pull/4789)

  * Fixed [heatmaps](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) rendering for values outside of the `range` attribute [#4865](https://github.com/voxel51/fiftyone/pull/4865)




Core

  * Added support for creating [summary fields](https://docs.voxel51.com/user_guide/using_datasets.html#summary-fields) to optimize queries on large datasets with many objects [#4765](https://github.com/voxel51/fiftyone/pull/4765)

  * Dataset fields now have automatically populated `created_at` attributes [#4730](https://github.com/voxel51/fiftyone/pull/4730)

  * Upgraded the [`delete_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_samples "fiftyone.core.dataset.Dataset.delete_samples") and [`clear_frames()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clear_frames "fiftyone.core.dataset.Dataset.clear_frames") methods to support bulk deletions of 100k+ samples/frames [#4787](https://github.com/voxel51/fiftyone/pull/4787)

  * The [`default_sidebar_groups()`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.DatasetAppConfig.default_sidebar_groups "fiftyone.core.odm.dataset.DatasetAppConfig.default_sidebar_groups") method now correctly handles datetime fields [#4815](https://github.com/voxel51/fiftyone/pull/4815)

  * Fixed an off-by-one error when converting semantic segmentations to/from instance segmentations [#4826](https://github.com/voxel51/fiftyone/pull/4826)

  * Protect against infinitely growing content size batchers [#4806](https://github.com/voxel51/fiftyone/pull/4806)

  * Removed the deprecated `remove_sample()` and `remove_samples()` methods from the [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") class [#4832](https://github.com/voxel51/fiftyone/pull/4832)

  * Deprecated [Python 3.8 support](deprecation.md#deprecation-python-3-8)




Plugins

  * Added [`ctx.group_slice`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.group_slice "fiftyone.operators.executor.ExecutionContext.group_slice") to the operator execution context [#4850](https://github.com/voxel51/fiftyone/pull/4850)

  * Added [`set_group_slice()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_group_slice "fiftyone.operators.operations.Operations.set_group_slice") to the operator execution context [#4844](https://github.com/voxel51/fiftyone/pull/4844)

  * Improved styling for [`GridView`](api__fiftyone.operators.types.md#fiftyone.operators.types.GridView "fiftyone.operators.types.GridView") components [#4764](https://github.com/voxel51/fiftyone/pull/4764)

  * A loading error is now displayed in the actions row when operators with [placements](plugins__developing_plugins.md#operator-placement) fail to load [#4714](https://github.com/voxel51/fiftyone/pull/4714)

  * Ensure the App loads when plugins fail to load [#4769](https://github.com/voxel51/fiftyone/pull/4769)




## FiftyOne 0.25.2#

_Released September 19, 2024_

  * Require `pymongo<4.9` to fix database connections

  * Require `pydicom<3` for [DICOM datasets](user_guide__import_datasets.md#dicomdataset-import)




## FiftyOne Enterprise 2.0.1#

_Released September 6, 2024_

Includes all updates from FiftyOne 0.25.1, plus:

  * Optimized the `Manage > Access` page for datasets

  * Added support for configuring a deployment to allow Guests to run custom plugins

  * Fixed a bug where dataset permissions assigned to [groups](enterprise__roles_and_permissions.md#enterprise-groups) were not correctly applied to users that do not otherwise have access to the dataset

  * Fixed a bug where a deploymentâs default user role as configured on the `Security > Config` page would not be respected

  * Fixed a bug that could cause 3D scenes stored in Azure to fail to load

  * Fixed a bug that erroneously caused the currently selected samples to be cleared when navigating between samples or closing the sample modal




## FiftyOne 0.25.1#

_Released September 6, 2024_

App

  * Fixed an issue with sidebar state persistence when opening and closing the sample modal [#4745](https://github.com/voxel51/fiftyone/pull/4745)

  * Fixed a bug with sample selection in the [Map panel](user_guide__app.md#app-map-panel) when the grid is reset [#4739](https://github.com/voxel51/fiftyone/pull/4739)

  * Fixed a bug when filtering [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") fields using the App sidebar [#4735](https://github.com/voxel51/fiftyone/pull/4735)

  * Fixed a bug when tagging in the sample modal with active sidebar filters [#4723](https://github.com/voxel51/fiftyone/pull/4723)

  * Disabled `fiftyone-desktop` builds until package size can be optimized [#4746](https://github.com/voxel51/fiftyone/pull/4746)




SDK

  * Added support for loading lists of TXT files in [YOLOv5 format](user_guide__import_datasets.md#yolov5dataset-import) [#4742](https://github.com/voxel51/fiftyone/pull/4742)

  * Fixed a bug with the `match_expr` argument of [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by") [#4754](https://github.com/voxel51/fiftyone/pull/4754)

  * Fixed a regression when running inference with [Ultralytics models](integrations__ultralytics.md#ultralytics-integration) that donât support track IDs [#4720](https://github.com/voxel51/fiftyone/pull/4720)




Plugins

  * Fixed a bug that caused [`TabsView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView "fiftyone.operators.types.TabsView") components to erroneously reset to their default state [#4732](https://github.com/voxel51/fiftyone/pull/4732)

  * Fixed a bug where calling [`set_state()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.set_state "fiftyone.operators.panel.PanelRef.set_state") and [`set_data()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.set_data "fiftyone.operators.panel.PanelRef.set_data") to patch state/data would inadvertently clobber other existing values [#4753](https://github.com/voxel51/fiftyone/pull/4753)

  * Fixed a spurious warning that would appear for delegated operations that donât return outputs [#4715](https://github.com/voxel51/fiftyone/pull/4715)




## FiftyOne Enterprise 2.0.0#

_Released August 20, 2024_

Includes all updates from FiftyOne 0.25.0, plus:

Whatâs New

  * Added a [Can tag](enterprise__roles_and_permissions.md#enterprise-can-tag) permission to allow users to tag samples/labels but not otherwise perform edits

  * Added support for authorized user credentials and external account credentials when configuring [GCP credentials](enterprise__installation.md#enterprise-google-cloud)

  * All [plugin execution](enterprise__plugins.md#enterprise-plugins) is now user-aware and will respect the executing userâs role and dataset permissions

  * All deployments now include a LICENSE file that enforces user quotas

  * Guests can no longer access operators/panels in custom plugins




App

  * Added a caching layer to optimize media serving in the App

  * Cloning an entire dataset via the `Clone` button now includes saved views, saved workspaces, and runs

  * Optimized the performance and UX of the `Settings > Users` page

  * The users table on the `Settings > Users` page is now sortable

  * Fixed a bug when updating the user role of a pending invitation

  * Fixed a bug that prevented the Recent views widget from showing all recently loaded views as intended




CAS

  * Added an `Audit` page to the [Super Admin UI](enterprise__pluggable_auth.md#super-admin-ui) that shows current license utilization and RBAC settings

  * Super admins can now disable manual group management in the App. This is useful, for example, if groups are defined via hooks

  * Legacy mode deployments now have access to the relevant pages of the Super Admin UI




SDK

  * Added a [fiftyone.management.user_groups](enterprise__management_sdk.md#enterprise-sdk-group-management) module to the Management SDK for programmatically managing user groups

  * The `fiftyone delegated` CLI command is now available to Enterprise users

  * Upgraded the [upload_media()](enterprise__cloud_media.md#enterprise-cloud-media-python) function to gracefully support fields with missing media paths

  * Added an `overwrite` parameter to [`add_cloud_credentials()`](enterprise__management_sdk.md#fiftyone.management.cloud_credentials.add_cloud_credentials "fiftyone.management.cloud_credentials.add_cloud_credentials") to control whether existing cloud credentials with the same prefix for a provider are overwritten




## FiftyOne 0.25.0#

_Released August 20, 2024_

Whatâs New

  * Introducing [Python panels](plugins__developing_plugins.md#developing-panels), a powerful framework for building custom App panels via a simple Python interface that includes a wealth of builtin components to convey information, create tutorials, show interactive graphs, trigger operations, and more

  * Released a [Dashboard panel](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/dashboard) that allows users to build custom no-code dashboards that display statistics of interest about the current dataset (and beyond)

  * Added [Segment Anything 2](https://ai.meta.com/sam2) to the [model zoo](model_zoo__models__segment_anything_2_hiera_small_video_torch.md#model-zoo-segment-anything-2-hiera-small-video-torch)! [#4671](https://github.com/voxel51/fiftyone/pull/4671)

  * Added an [Elasticsearch integration](integrations__elasticsearch.md#elasticsearch-integration) for native text and image searches on FiftyOne datasets!

  * Added an [image representativeness](brain.md#brain-image-representativeness) method to the Brain that can be used to find the most common/uncommon types of images in your datasets




App

  * You can now [link directly to a sample or group](user_guide__app.md#loading-a-sample-or-group) in the App by copy + pasting URLs into your browser bar or programmatically via your App `session` [#4281](https://github.com/voxel51/fiftyone/pull/4281)

  * Added a config option to [disable frame filtering](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-disable-frame-filtering) in the App globally or on specific datasets [#4604](https://github.com/voxel51/fiftyone/pull/4604)

  * Added support for dynamically adjusting 3D label linewidths [#4590](https://github.com/voxel51/fiftyone/pull/4590)

  * Added a status bar when loading large 3D assets in the modal [#4546](https://github.com/voxel51/fiftyone/pull/4546)

  * Added support for visualizing [heatmaps](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) in `.jpg` format [#4531](https://github.com/voxel51/fiftyone/pull/4531)

  * Exposed camera position as a recoil atom [#4535](https://github.com/voxel51/fiftyone/pull/4535)

  * Added anonymous analytics collection on an opt-in basis [#4559](https://github.com/voxel51/fiftyone/pull/4559)

  * Fixed a bug when viewing [dynamic groups](user_guide__app.md#app-dynamic-groups) of 3D scenes in the modal [#4527](https://github.com/voxel51/fiftyone/pull/4527)

  * Fixed a bug when rendering scenes with relative 3D asset paths on Windows [#4579](https://github.com/voxel51/fiftyone/pull/4579)

  * Fixed keyboard shortcuts when viewing dynamic groups in the modal [#4510](https://github.com/voxel51/fiftyone/pull/4510)




Annotation

  * Added support for annotating [frame views](https://docs.voxel51.com/user_guide/using_views.html#frame-views) [#4477](https://github.com/voxel51/fiftyone/pull/4477)

  * Added support for annotating [clip views](https://docs.voxel51.com/user_guide/using_views.html#clip-views) [#4511](https://github.com/voxel51/fiftyone/pull/4511)

  * Added support for preserving existing COCO IDs when exporting in [COCO format](user_guide__export_datasets.md#cocodetectiondataset-export) [#4530](https://github.com/voxel51/fiftyone/pull/4530)




Core

  * Added support for [save contexts](https://docs.voxel51.com/user_guide/using_datasets.html#save-contexts) to generated views (patches, frames, and clips) [#4636](https://github.com/voxel51/fiftyone/pull/4636)

  * Added support for downloading plugins from branches that contain slashes `/` [#4614](https://github.com/voxel51/fiftyone/pull/4614)

  * Added support for including index statistics in [`Dataset.stats()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.stats "fiftyone.core.dataset.Dataset.stats") [#4653](https://github.com/voxel51/fiftyone/pull/4653)

  * Added a source install script for Windows [#4582](https://github.com/voxel51/fiftyone/pull/4582)

  * Ubuntu 24.04 users no longer have to manually install MongoDB [#4533](https://github.com/voxel51/fiftyone/pull/4533)

  * Removed Python 3.7 support and marked Python 3.8 as [deprecated](deprecation.md#deprecation-notices) [#4538](https://github.com/voxel51/fiftyone/pull/4538)

  * Fixed a bug that could cause side effects when creating clip views defined by expressions [#4492](https://github.com/voxel51/fiftyone/pull/4492)

  * Fixed a concatenation bug when downloading videos from [CVAT](integrations__cvat.md#cvat-integration) [#4674](https://github.com/voxel51/fiftyone/pull/4674)




Plugins

  * The actions row now automatically overflows into a `More items` menu as necessary when there is insufficient horizontal space [#4595](https://github.com/voxel51/fiftyone/pull/4595)

  * Added a [`set_active_fields()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_active_fields "fiftyone.operators.operations.Operations.set_active_fields") operator for programmatically controlling the selected fields in the sidebar [#4482](https://github.com/voxel51/fiftyone/pull/4482)

  * Added a [`notify()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.notify "fiftyone.operators.operations.Operations.notify") operator for programmatically showing notifications in the App [#4344](https://github.com/voxel51/fiftyone/pull/4344)

  * Added [`ctx.extended_selection`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.extended_selection "fiftyone.operators.executor.ExecutionContext.extended_selection") to retrieve the current extended selection [#4413](https://github.com/voxel51/fiftyone/pull/4413)

  * Added a [`set_extended_selection()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_extended_selection "fiftyone.operators.operations.Operations.set_extended_selection") operator for programmatically setting the extended selection [#4409](https://github.com/voxel51/fiftyone/pull/4409)

  * Added a [`track_event()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.track_event "fiftyone.operators.operations.Operations.track_event") operator for logging plugin events in the App [#4489](https://github.com/voxel51/fiftyone/pull/4489)




Zoo

  * Added [YOLOv10 and RT-DETR models](integrations__ultralytics.md#ultralytics-object-detection) to the zoo [#4544](https://github.com/voxel51/fiftyone/pull/4544)

  * Added [YOLOv8 classification models](integrations__ultralytics.md#ultralytics-image-classification) to the zoo [#4549](https://github.com/voxel51/fiftyone/pull/4549)

  * Added support for storing object track IDs if present when running [Ultralytics models](integrations__ultralytics.md#ultralytics-integration) from the zoo [#4569](https://github.com/voxel51/fiftyone/pull/4569)

  * Added support for GPU inference when running [Hugging Face Transformers](integrations__huggingface.md#huggingface-transformers) models from the zoo [#4587](https://github.com/voxel51/fiftyone/pull/4587)

  * Extended support for group datasets, masks, heatmaps, and thumbnails when uploading FiftyOne datasets to [Hugging Face Hub](integrations__huggingface.md#huggingface-hub) [#4566](https://github.com/voxel51/fiftyone/pull/4566)

  * Allow `ragged_batches` to be configured when using Torch models with custom transforms [#4509](https://github.com/voxel51/fiftyone/pull/4509), [#4512](https://github.com/voxel51/fiftyone/pull/4512)




## FiftyOne Enterprise 1.7.1#

_Released June 11, 2024_

Includes all updates from FiftyOne 0.24.1, plus:

  * Improved stability of loading/navigating to saved views in the App

  * Fixed a notification error when deleting users from the Team Settings page

  * Improved stability of the Team Groups page after deleting users

  * Optimized export of cloud-backed 3D scenes




## FiftyOne 0.24.1#

_Released June 11, 2024_

Whatâs New

  * Added [Ultralytics YOLOv8 models](integrations__ultralytics.md#ultralytics-integration) trained on Open Images v7 to the model zoo! [#4398](https://github.com/voxel51/fiftyone/pull/4398)




App

  * Fixed a regression from FiftyOne 0.24.0 that would prevent operator outputs and error states from displaying in the App [#4445](https://github.com/voxel51/fiftyone/pull/4445)




Core

  * Optimized metadata computation for 3D scenes [#4442](https://github.com/voxel51/fiftyone/pull/4442)

  * Fixed a bug that could cause 3D assets to be omitted when exporting 3D scenes [#4442](https://github.com/voxel51/fiftyone/pull/4442)




Utils

  * The [`make_patches_dataset()`](api__fiftyone.core.patches.md#fiftyone.core.patches.make_patches_dataset "fiftyone.core.patches.make_patches_dataset"), [`make_frames_dataset()`](api__fiftyone.core.video.md#fiftyone.core.video.make_frames_dataset "fiftyone.core.video.make_frames_dataset"), and [`make_clips_dataset()`](api__fiftyone.core.clips.md#fiftyone.core.clips.make_clips_dataset "fiftyone.core.clips.make_clips_dataset") utilities can now be directly called [#4416](https://github.com/voxel51/fiftyone/pull/4416)




Annotation

  * Added support loading annotations for large CVAT tasks with many jobs [#4392](https://github.com/voxel51/fiftyone/pull/4392)




## FiftyOne Enterprise 1.7.0#

_Released May 29, 2024_

Includes all updates from FiftyOne 0.24.0, plus:

  * Added a [Roles page](enterprise__roles_and_permissions.md#enterprise-roles-page) that summarizes the actions and permissions available to each user role

  * Added support for customizing the role that a user will have when sending an invitation for a new user to access a specific dataset

  * Added the ability to configure the expiration time for signed URLs used by your FiftyOne Enterprise deployment

  * Fixed a regression from FiftyOne Enterprise 1.6 that could cause login errors when accepting invites




## FiftyOne 0.24.0#

_Released May 29, 2024_

Whatâs New

  * Added support for [3D meshes and 3D geometries](https://docs.voxel51.com/user_guide/using_datasets.html#d-datasets)! [#3985](https://github.com/voxel51/fiftyone/pull/3985)

  * Added a [quickstart-3d dataset](dataset_zoo__datasets__quickstart_3d.md#dataset-zoo-quickstart-3d) to the zoo! [#4406](https://github.com/voxel51/fiftyone/pull/4406)

  * Added support for [saving custom workspaces](user_guide__app.md#app-workspaces)! [#4205](https://github.com/voxel51/fiftyone/pull/4205), [#4211](https://github.com/voxel51/fiftyone/pull/4211)

  * You can now scroll/customize the content displayed in the [App tooltip](user_guide__app.md#app-sample-view)! [#4254](https://github.com/voxel51/fiftyone/pull/4254)

  * FiftyOne now lazily connects to the database only when needed [#4236](https://github.com/voxel51/fiftyone/pull/4236)

  * Added [Grounding DINO](integrations__huggingface.md#huggingface-transformers-zero-shot-detection) as an option for zero shot object detection [#4292](https://github.com/voxel51/fiftyone/pull/4292)

  * Added a new [anomaly detection tutorial](tutorials__anomaly_detection.md) [#4312](https://github.com/voxel51/fiftyone/pull/4312)




App

  * Added a `media_fallback` option to the [dataset App config](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-media-fields) [#4280](https://github.com/voxel51/fiftyone/pull/4280)

  * [`launch_app()`](api__fiftyone.core.session.md#fiftyone.core.session.launch_app "fiftyone.core.session.launch_app") now respects the current [`group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_slice "fiftyone.core.dataset.Dataset.group_slice") when loading grouped datasets [#4423](https://github.com/voxel51/fiftyone/pull/4423)

  * Allow sidebar changes during lightning loading states [#4319](https://github.com/voxel51/fiftyone/pull/4319)

  * Fixed overlay processing for empty label lists [#4345](https://github.com/voxel51/fiftyone/pull/4345)

  * Fixed `support` filtering in the sample modal for [`TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections") fields [#4346](https://github.com/voxel51/fiftyone/pull/4346)

  * Fixed a regression from FiftyOne 0.23.8 when viewing dynamically grouped views into group datasets [#4299](https://github.com/voxel51/fiftyone/pull/4299)




Core

  * Gracefully handle None-valued `tags` fields [#4351](https://github.com/voxel51/fiftyone/pull/4351)

  * More robust path normalization when importing [FiftyOneDataset](user_guide__import_datasets.md#fiftyonedataset-import) exports from other operating systems [#4353](https://github.com/voxel51/fiftyone/pull/4353)

  * Fixed possible concurrency bugs when updating/deleting runs [#4323](https://github.com/voxel51/fiftyone/pull/4323)

  * Fixed possible concurrency bugs when updating views, workspaces, and group slices [#4350](https://github.com/voxel51/fiftyone/pull/4350)

  * Fixed a timezone bug with [`DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField") for GMT+ users [#4371](https://github.com/voxel51/fiftyone/pull/4371)




Utils

  * Added support for non-sequential category IDs when importing/exporting data in [COCO format](user_guide__import_datasets.md#cocodetectiondataset-import) [#4354](https://github.com/voxel51/fiftyone/pull/4354), [#4309](https://github.com/voxel51/fiftyone/pull/4309)

  * Added a [`DeepSort`](api__fiftyone.utils.tracking.deepsort.md#fiftyone.utils.tracking.deepsort.DeepSort "fiftyone.utils.tracking.deepsort.DeepSort") tracking utility [#4372](https://github.com/voxel51/fiftyone/pull/4372), [#4296](https://github.com/voxel51/fiftyone/pull/4296)




Plugins

  * Added a [`DrawerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DrawerView "fiftyone.operators.types.DrawerView") option to render your operators as a side drawer in the grid/sample visualizer rather than as a modal [#4240](https://github.com/voxel51/fiftyone/pull/4240)

  * Added a [`set_spaces()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_spaces "fiftyone.operators.operations.Operations.set_spaces") method for setting the current spaces layout from operators [#4381](https://github.com/voxel51/fiftyone/pull/4381)

  * Added support for numpy dtypes when serializing operator results [#4324](https://github.com/voxel51/fiftyone/pull/4324)

  * Fixed a bug where recently used operators may not appear first in the [Operator browser](plugins__using_plugins.md#using-operators) [#4287](https://github.com/voxel51/fiftyone/pull/4287)

  * Fixed logging syntax in the builtin [`set_progress()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_progress "fiftyone.operators.operations.Operations.set_progress") operation [#4417](https://github.com/voxel51/fiftyone/pull/4417)




Zoo

  * Fixed a bug with [YOLO-NAS inference](integrations__super_gradients.md#super-gradients-integration) [#4429](https://github.com/voxel51/fiftyone/pull/4429)




## FiftyOne Enterprise 1.6.1#

_Released May 10, 2024_

Bugs

  * Fixed an issue with logging into FiftyOne Enterprise in Enterprise Proxy environments




## FiftyOne Enterprise 1.6.0#

_Released April 30, 2024_

Whatâs New

  * Added [Groups](enterprise__roles_and_permissions.md#enterprise-groups) for managing and dataset access for groups of users

  * Introduced a new [Pluggable Authentication](enterprise__pluggable_auth.md#pluggable-auth) system for customizing FiftyOne Enterprise authentication

  * Removed Auth0 as a hard dependency for Enterprise deployments with the introduction of [Internal Mode](enterprise__pluggable_auth.md#internal-mode)

  * Added support for directly authenticating with [Identity Providers](enterprise__pluggable_auth.md#identity-providers)

  * Added a [Super Admin UI](enterprise__pluggable_auth.md#super-admin-ui) for administering FiftyOne Enterprise deployments

  * Added the ability to search for users on the Users page




## FiftyOne Enterprise 1.5.10#

_Released April 18, 2024_

  * Fixed an issue where video datasets were not loading due to ffmpeg dependency




## FiftyOne Enterprise 1.5.9#

_Released April 15, 2024_

Includes all updates from FiftyOne 0.23.8, plus:

  * [Download contexts](enterprise__cloud_media.md#enterprise-cloud-media-python) now support batching based on content size

  * All builtin methods that require access to cloud media now use [download contexts](enterprise__cloud_media.md#enterprise-cloud-media-python) to download media in batches during execution rather than downloading media in a single batch up-front

  * The [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") method no longer caches all cloud media involved in the export

  * Optimized the localhost App experience when using [API connections](enterprise__api_connection.md#enterprise-api-connection)

  * Optimized performance of data-intensive API calls when using [API connections](enterprise__api_connection.md#enterprise-api-connection)




## FiftyOne 0.23.8#

_Released April 15, 2024_

News

  * Released a [Hugging Face Hub integration](integrations__huggingface.md#huggingface-hub) for programmatically publishing and downloading datasets to/from Hugging Face Hub! [#4193](https://github.com/voxel51/fiftyone/pull/4193)




App

  * [Space sizes](user_guide__app.md#app-spaces) are now persisted when the App is refreshed [#4171](https://github.com/voxel51/fiftyone/pull/4171)

  * Added support for rendering detections with empty instance masks in the App [#4227](https://github.com/voxel51/fiftyone/pull/4227)

  * Enhanced label overlay processing to support empty label lists [#4215](https://github.com/voxel51/fiftyone/pull/4215)

  * Optimized by the App server by removing unnecessary server lock-ups due to synchronous IO calls [#4180](https://github.com/voxel51/fiftyone/pull/4180)

  * Optimized sidebar performance for grouped datasets [#4182](https://github.com/voxel51/fiftyone/pull/4182)

  * Optimized dataset counting for index page queries [#4114](https://github.com/voxel51/fiftyone/pull/4114)

  * Fixed a bug where sidebar group name changes in the App were not persisted [#4241](https://github.com/voxel51/fiftyone/pull/4241)

  * Fixed a bug when applying filters to [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") fields [#4201](https://github.com/voxel51/fiftyone/pull/4201)

  * Fixed a bug where in-App tagging actions may not be restricted to the currently selected samples [#4195](https://github.com/voxel51/fiftyone/pull/4195)

  * Fixed a bug when bookmarking sidebar filters for group datasets [#4097](https://github.com/voxel51/fiftyone/pull/4097)

  * Fixed a bug where the saved view dropdown would cover the view stage popover [#4242](https://github.com/voxel51/fiftyone/pull/4242)




Core

  * All [save contexts](https://docs.voxel51.com/user_guide/using_datasets.html#save-contexts) now respect the [default batching strategy](user_guide__config.md#configuring-fiftyone) and can be configured to use content size-based batching [#4243](https://github.com/voxel51/fiftyone/pull/4243)

  * All SDK methods now use [save contexts](https://docs.voxel51.com/user_guide/using_datasets.html#save-contexts) rather than calling [`sample.save()`](api__fiftyone.core.sample.md#fiftyone.core.sample.Sample.save "fiftyone.core.sample.Sample.save") in a loop [#4243](https://github.com/voxel51/fiftyone/pull/4243)

  * Added a [`read_files()`](api__fiftyone.core.storage.md#fiftyone.core.storage.read_files "fiftyone.core.storage.read_files") utility to efficiently read from multiple files in a threadpool [#4243](https://github.com/voxel51/fiftyone/pull/4243)

  * Optimized segmentation mask conversion [#4185](https://github.com/voxel51/fiftyone/pull/4185), [#4188](https://github.com/voxel51/fiftyone/pull/4188)

  * Resolved singularity issues in [`compute_orthographic_projection_images()`](api__fiftyone.utils.utils3d.md#fiftyone.utils.utils3d.compute_orthographic_projection_images "fiftyone.utils.utils3d.compute_orthographic_projection_images") [#4206](https://github.com/voxel51/fiftyone/pull/4206)

  * Fixed matplotlib style deprecation error [#4213](https://github.com/voxel51/fiftyone/pull/4213)




Docs

  * Added a [clustering tutorial](tutorials__clustering.md) [#4245](https://github.com/voxel51/fiftyone/pull/4245)

  * Added a [small object detection tutorial](tutorials__small_object_detection.md) [#4263](https://github.com/voxel51/fiftyone/pull/4263)

  * Refreshed many popular [tutorials](https://docs.voxel51.com/tutorials/index.html#tutorials) [#4207](https://github.com/voxel51/fiftyone/pull/4207)




Annotation

  * Upgraded the [Labelbox integration](integrations__labelbox.md#labelbox-integration) to support the Export V2 API [#4260](https://github.com/voxel51/fiftyone/pull/4260)




Plugins

  * [Secrets](plugins__developing_plugins.md#operator-secrets) are now available to operators in their [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input"), [`resolve_output()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_output "fiftyone.operators.operator.Operator.resolve_output"), and [`resolve_execution_options()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_execution_options "fiftyone.operators.operator.Operator.resolve_execution_options") methods [#4169](https://github.com/voxel51/fiftyone/pull/4169)

  * `ctx.view` now reflects when the current view is saved [#4200](https://github.com/voxel51/fiftyone/pull/4200)

  * Fixed a regression in debounce behavior in operator input forms that could potentially result in degraded performance [#4199](https://github.com/voxel51/fiftyone/pull/4199)

  * Fixed a bug when using the [`set_view()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_view "fiftyone.operators.operations.Operations.set_view") method in operators [#4198](https://github.com/voxel51/fiftyone/pull/4198)




Zoo

  * Added support for loading [YOLOv8 and YOLOv9 segmentation models](integrations__ultralytics.md#ultralytics-instance-segmentation) from the Model Zoo [#4220](https://github.com/voxel51/fiftyone/pull/4220)

  * Added support for applying [YOLO oriented bounding box models](integrations__ultralytics.md#ultralytics-oriented-bounding-boxes) to FiftyOne datasets [#4230](https://github.com/voxel51/fiftyone/pull/4230), [#4238](https://github.com/voxel51/fiftyone/pull/4238)

  * Added support for applying [Segment Anything](model_zoo__models__segment_anything_vitb_torch.md#model-zoo-segment-anything-vitb-torch) models to the frames of video datasets [#4229](https://github.com/voxel51/fiftyone/pull/4229)




## FiftyOne Enterprise 1.5.8#

_Released March 21, 2024_

Includes all updates from FiftyOne 0.23.7.

## FiftyOne 0.23.7#

_Released March 21, 2024_

App

  * Updated `Have a Team?` link in the App to point to the [Book a demo](https://voxel51.com/book-a-demo/?utm_source=FiftyOneApp) page [#4127](https://github.com/voxel51/fiftyone/pull/4127)

  * Fixed indexed boolean fields in lightning mode [#4139](https://github.com/voxel51/fiftyone/pull/4139)

  * Fixed app crash when many None-valued fields exist in the sample modal [#4154](https://github.com/voxel51/fiftyone/pull/4154)




Docs

  * Added an [Albumentations integration](integrations__albumentations.md#albumentations-integration) for performing data augmentation on FiftyOne datasets [#4155](https://github.com/voxel51/fiftyone/pull/4155)

  * Added [Places2 dataset](dataset_zoo__datasets__places.md#dataset-zoo-places) to the zoo [#4130](https://github.com/voxel51/fiftyone/pull/4130)

  * Added a [zero-shot image classification tutorial](tutorials__zero_shot_classification.md) [#4133](https://github.com/voxel51/fiftyone/pull/4133)

  * [Improved documentation](enterprise__installation.md#enterprise-cloud-credentials) for configuring AWS and GCP cloud credentials [#4151](https://github.com/voxel51/fiftyone/pull/4151)

  * Added [YOLOv8, YOLOv9, and YOLO-World](integrations__ultralytics.md#ultralytics-integration) to the FiftyOne Model Zoo [#4153](https://github.com/voxel51/fiftyone/pull/4153)

  * Added `og:image` meta tag to all documentation pages for better page sharing on socials [#4173](https://github.com/voxel51/fiftyone/pull/4173)

  * Updated the lightning mode docs to clarify that wildcard indexes should not generally be used by default [#4138](https://github.com/voxel51/fiftyone/pull/4138)




Plugins and Operators

  * Added support for [executing operators programmatically](plugins__using_plugins.md#executing-operators-sdk) in notebook contexts [#4134](https://github.com/voxel51/fiftyone/pull/4134)

  * Improved execution of operators during loading of the App [#4136](https://github.com/voxel51/fiftyone/pull/4136)

  * Added a new [on_dataset_open](plugins__developing_plugins.md#operator-config) hook to auto-execute operators when datasets are opened in the App [#4137](https://github.com/voxel51/fiftyone/pull/4137)

  * Improved performance of operator type resolution by only calling [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") on demand [#4152](https://github.com/voxel51/fiftyone/pull/4152)

  * Added support for loading saved views by name or slug when using the [`set_view()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_view "fiftyone.operators.operations.Operations.set_view") operator [#4159](https://github.com/voxel51/fiftyone/pull/4159) and [#4178](https://github.com/voxel51/fiftyone/pull/4178)

  * Added ability to [trigger builtin operators](plugins__developing_plugins.md#operator-execution) during operator execution via [`ctx.ops`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.ops "fiftyone.operators.executor.ExecutionContext.ops") [#4164](https://github.com/voxel51/fiftyone/pull/4164)

  * Fixed issue where JS operator input was not validated when calling `ctx.trigger()` or `executeOperator()` directly [#4170](https://github.com/voxel51/fiftyone/pull/4170)

  * Show execution error of an operator in a notification when calling `ctx.trigger()` or `executeOperator()` directly [#4170](https://github.com/voxel51/fiftyone/pull/4170) and [#4178](https://github.com/voxel51/fiftyone/pull/4178)




Core

  * Improved [SuperGradients](integrations__super_gradients.md#super-gradients-integration) inference performance [#4149](https://github.com/voxel51/fiftyone/pull/4149)

  * Passing a [grouped collection](https://docs.voxel51.com/user_guide/groups.html#groups) to a method that was not specifically designed to handle them now raises better validation errors [#4150](https://github.com/voxel51/fiftyone/pull/4150)

  * [`MediaExporter`](api__fiftyone.utils.data.md#fiftyone.utils.data.MediaExporter "fiftyone.utils.data.MediaExporter") no longer re-exports media unnecessarily [#4143](https://github.com/voxel51/fiftyone/pull/4143)

  * Added explicit support for Python 3.11 and 3.12 [#4157](https://github.com/voxel51/fiftyone/pull/4157)

  * Added a [`perform_nms()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.perform_nms "fiftyone.utils.labels.perform_nms") utility for non-maximum suppression on object detections [#4160](https://github.com/voxel51/fiftyone/pull/4160)

  * Improved error message when the given dataset name is unavailable [#4161](https://github.com/voxel51/fiftyone/pull/4161)

  * Removed use of deprecated non-integer arguments in [`take()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.take "fiftyone.core.collections.SampleCollection.take") and [`shuffle()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.shuffle "fiftyone.core.collections.SampleCollection.shuffle") [#4052](https://github.com/voxel51/fiftyone/pull/4052)

  * Added ability to change `map_type` from the default `roadmap` ([carto-positron](https://plotly.com/python/mapbox-layers/)) to `satellite` ([public USGS map imagery](https://basemap.nationalmap.gov/)) in [`location_scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.location_scatterplot "fiftyone.core.plots.plotly.location_scatterplot") [#4075](https://github.com/voxel51/fiftyone/pull/4075)

  * Cloning a dataset or view now includes any custom MongoDB indexes [#4115](https://github.com/voxel51/fiftyone/pull/4115)




## FiftyOne Enterprise 1.5.7#

_Released March 6, 2024_

Includes all updates from FiftyOne 0.23.6, plus:

  * Improved performance of [`values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values") when using [API connections](enterprise__api_connection.md#enterprise-api-connection)

  * Improved stability of long-running operations when using [API connections](enterprise__api_connection.md#enterprise-api-connection)

  * Added support for including prefixes when providing [bucket-specific credentials](enterprise__installation.md#enterprise-cloud-storage-page)




## FiftyOne 0.23.6#

_Released March 6, 2024_

Whatâs New

  * Added a [dimensionality reduction tutorial](tutorials__dimension_reduction.md) [#4033](https://github.com/voxel51/fiftyone/pull/4033)

  * Added a [data augmentation tutorial](tutorials__data_augmentation.md) [#4109](https://github.com/voxel51/fiftyone/pull/4109)

  * Added a formal [Open CLIP integration page](integrations__openclip.md#openclip-integration) [#4049](https://github.com/voxel51/fiftyone/pull/4049)

  * Documented support for open-world object detection with [YOLO World](integrations__ultralytics.md#ultralytics-open-vocabulary-object-detection) [#4112](https://github.com/voxel51/fiftyone/pull/4112)

  * Added support for importing/exporting contours in [YOLO format](user_guide__import_datasets.md#yolov5dataset-import) [#4094](https://github.com/voxel51/fiftyone/pull/4094)

  * Added cosine metric as an option for [Milvus similarity indexes](integrations__milvus.md#milvus-integration) [#4081](https://github.com/voxel51/fiftyone/pull/4081)

  * Added support for local files when using the [Label Studio integration](integrations__labelstudio.md#label-studio-local-storage) [#3969](https://github.com/voxel51/fiftyone/pull/3969)

  * Removed App dependency on `_cls` for embedded documents [#4090](https://github.com/voxel51/fiftyone/pull/4090)




Bugs

  * Fixed issue with filter counts on video datasets in the App [#4095](https://github.com/voxel51/fiftyone/pull/4095)

  * Fixed issue with color scheme initialization in the App [#4092](https://github.com/voxel51/fiftyone/pull/4092)

  * Fixed issue when changing group slice with filters in the App [#4098](https://github.com/voxel51/fiftyone/pull/4098)

  * Fixed issue with zero-shot detection batching [#4108](https://github.com/voxel51/fiftyone/pull/4108)

  * Fixed issue with the operator target view utility when no view or sample selection is present [#4113](https://github.com/voxel51/fiftyone/pull/4113)




## FiftyOne Enterprise 1.5.6#

_Released February 14, 2024_

Includes all updates from FiftyOne 0.23.5, plus:

  * Improved dataset search user experience

  * Post login redirects will now send the user to the correct page




## FiftyOne 0.23.5#

_Released February 14, 2024_

Whatâs New

  * Added subcounts to search results in the sidebar [#3973](https://github.com/voxel51/fiftyone/pull/3973)

  * Added [`fiftyone.operators.types.ViewTargetProperty`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetProperty "fiftyone.operators.types.ViewTargetProperty") to make it simpler to add view selection to a [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") [#4076](https://github.com/voxel51/fiftyone/pull/4076)

  * Added support for apply monocular depth estimation transformers from the Hugging Face `transformers` library directly to FiftyOne datasets [#4082](https://github.com/voxel51/fiftyone/pull/4035)




Bugs

  * Fixed an issue where increments were padded improperly [#4035](https://github.com/voxel51/fiftyone/pull/4035)

  * Fixed an issue when setting `session.color_scheme` [#4060](https://github.com/voxel51/fiftyone/pull/4060)

  * Fixed sidebar groups resolution when the dataset app config setting is configured [#4064](https://github.com/voxel51/fiftyone/pull/4064)

  * Fixed issue when `SelectGroupSlices` view stage is applied with only one slice within video grouped datasets [#4066](https://github.com/voxel51/fiftyone/pull/4066)

  * Fixed non-default pcd slice rendering in the App [#4044](https://github.com/voxel51/fiftyone/pull/4044)

  * Dynamic groups configuration options are now only shown when relevant [#4068](https://github.com/voxel51/fiftyone/pull/4068)

  * Fixed issue with dynamic groups mode pagination [#4068](https://github.com/voxel51/fiftyone/pull/4068)

  * Enabled tagging in sidebar lightning mode [#4048](https://github.com/voxel51/fiftyone/pull/4048)




## FiftyOne Enterprise 1.5.5#

_Released January 25, 2024_

Includes all updates from FiftyOne 0.23.4, plus:

Bugs

  * Fixed a proxy URL bug that prevented custom JS panels from launching




## FiftyOne 0.23.4#

_Released January 25, 2024_

Core

  * Added support for passing kwargs directly when creating custom runs [#4039](https://github.com/voxel51/fiftyone/pull/4039)




Brain

  * Added support for registering [custom visualization methods](brain.md#brain-visualization-api) [#4038](https://github.com/voxel51/fiftyone/pull/4038)




## FiftyOne Enterprise 1.5.4#

_Released January 19, 2024_

Includes all updates from FiftyOne 0.23.3, plus:

General

  * Optimized [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") calls involving cloud-backed media

  * Deployments with their `FIFTYONE_API_URI` environment variable set will now display the API URI to users in the Enterprise App

  * Improved debug logs by adding the head and tail of large results

  * Updated `motor` dependency to 3.3.0




Bugs

  * Fixed a regression when exporting cloud-backed media to [CVAT](integrations__cvat.md#cvat-integration) for annotation

  * Fixed an issue where API requests were not being prefixed with the correct proxy URL

  * Fixed running [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") over API connections with the [MongoDB backend](integrations__mongodb.md#mongodb-integration)




## FiftyOne 0.23.3#

_Released January 19, 2024_

News

  * Released a [Hugging Face integration](integrations__huggingface.md#huggingface-integration) for running inference with `transformers` models on your FiftyOne datasets!

  * Released a [SuperGradients integration](integrations__super_gradients.md#super-gradients-integration) for running inference with YOLO-NAS architectures!




App

  * Primitive values in [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument") list fields are now displayed as comma-separated values (previously displayed as None) in the sample modal [#3963](https://github.com/voxel51/fiftyone/pull/3963)

  * Improved field visibilityâs show metadata toggle [#3926](https://github.com/voxel51/fiftyone/pull/3926)

  * Fixed issues for unknown operator types and defaults [#3851](https://github.com/voxel51/fiftyone/pull/3851)

  * Miscellaneous saved view improvements [#3974](https://github.com/voxel51/fiftyone/pull/3974)

  * Fixed a bug where images in the sample modal errored when frame fields were added to video slices in mixed datasets [#3966](https://github.com/voxel51/fiftyone/pull/3966)

  * Fixed in-App sort by similarity for datasets with a color scheme [#3966](https://github.com/voxel51/fiftyone/pull/3958)

  * Fixed issues where media and other URLs were constructed incorrectly [#3976](https://github.com/voxel51/fiftyone/pull/3976)

  * Fixed keyboard navigation for dropdowns throughout the App [#3965](https://github.com/voxel51/fiftyone/pull/3965)




Brain

  * Added support for passing [Hugging Face](integrations__huggingface.md#huggingface-integration), [Ultralytics](integrations__ultralytics.md#ultralytics-integration), and [SuperGradients](integrations__super_gradients.md#super-gradients-integration) models directly brain methods [#4004](https://github.com/voxel51/fiftyone/pull/4004)

  * Added support to [`register_run()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.Similarity.register_run "fiftyone.brain.similarity.Similarity.register_run") for configuring whether run cleanup happens [#3978](https://github.com/voxel51/fiftyone/pull/3978)

  * Added support for passing model kwargs to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") and [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization")

  * Fixed issues with similarity searches on views and with pre-computed embeddings using the [MongoDB backend](integrations__mongodb.md#mongodb-integration)




Core

  * Added dynamic batching to bulk writes like [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#4015](https://github.com/voxel51/fiftyone/pull/4015)

  * Added support for customizing progress bar rendering at method level [#3979](https://github.com/voxel51/fiftyone/pull/3979)

  * Include sample/frame singletons when clearing dataset cache via [`clear_cache()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clear_cache "fiftyone.core.dataset.Dataset.clear_cache") [#4016](https://github.com/voxel51/fiftyone/pull/4016)

  * Fixed issues with embedded document field schemas [#4002](https://github.com/voxel51/fiftyone/pull/4002)




Models

  * Added support for directly passing [Ultralytics models](integrations__ultralytics.md#ultralytics-integration) models to [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model")

  * Added GPU support for [OpenCLIP](model_zoo__models__open_clip_torch.md#model-zoo-open-clip-torch) models [#3986](https://github.com/voxel51/fiftyone/pull/3986)

  * Added prompt embedding capabilities to [OpenCLIP](model_zoo__models__open_clip_torch.md#model-zoo-open-clip-torch) models [#3960](https://github.com/voxel51/fiftyone/pull/3960)




Plugins

  * Added a builtin `delete_selected_labels` operator [#4001](https://github.com/voxel51/fiftyone/pull/4001)

  * Updated [`ctx.selected_labels`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.selected_labels "fiftyone.operators.executor.ExecutionContext.selected_labels") format to be consistent with other SDK methods [#3998](https://github.com/voxel51/fiftyone/pull/3998)




Tutorials

  * Added a [monocular depth estimation](tutorials__monocular_depth_estimation.md) tutorial [#3991](https://github.com/voxel51/fiftyone/pull/3991)




## FiftyOne Enterprise 1.5.3#

_Released December 21, 2023_

Includes all updates from FiftyOne 0.23.2, plus:

General

  * Improved performance of [`add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples"), [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values"), [`compute_metadata()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_metadata "fiftyone.core.collections.SampleCollection.compute_metadata"), and other large batched computations when using [API connections](enterprise__api_connection.md#enterprise-api-connection)

  * Added `label` as a searchable field for delegated operations

  * Fixed issue where invalid tokens were not causing redirects

  * Re-running a delegated operation now uses dataset ID instead of name

  * Trimmed API logging of large batch SDK operations




## FiftyOne 0.23.2#

_Released December 21, 2023_

News

  * Added [OpenCLIP](model_zoo__models__open_clip_torch.md#model-zoo-open-clip-torch) to the FiftyOne Model Zoo! [#3925](https://github.com/voxel51/fiftyone/pull/3925)




App

  * Added support for frames-as-videos in nested groups [#3935](https://github.com/voxel51/fiftyone/pull/3935)

  * Fixed an issue where embeddings legend did not display full names [#3927](https://github.com/voxel51/fiftyone/pull/3927)

  * Added a toggle to show/hide fields in the sample modal that have undefined values [#3937](https://github.com/voxel51/fiftyone/pull/3937)

  * Fixed an issue with the Lightning threshold reset button [#3933](https://github.com/voxel51/fiftyone/pull/3933)

  * Fixed an issue where similarity search only worked on the default group slice [#3912](https://github.com/voxel51/fiftyone/pull/3912)

  * Fixed issue where users could not select scalar fields in the sidebar [#3938](https://github.com/voxel51/fiftyone/pull/3938)




Core

  * Added configurable batching choices to optimize throughput for operations like [`add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples") [#3923](https://github.com/voxel51/fiftyone/pull/3923)

  * IoU computations for non-filled polylines now uses keypoint similarity [#3930](https://github.com/voxel51/fiftyone/pull/3930)

  * Optimized bulk write database operations like [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#3942](https://github.com/voxel51/fiftyone/pull/3942)

  * Added configurable batch sizes to bulk write operations [#3944](https://github.com/voxel51/fiftyone/pull/3944)

  * Added builtin support for Ubuntu 23 [#3936](https://github.com/voxel51/fiftyone/pull/3936)

  * Fixed an issue where exporting patches would have incorrect path names [#3921](https://github.com/voxel51/fiftyone/pull/3921)

  * Removed loading from mongoengine cache [#3922](https://github.com/voxel51/fiftyone/pull/3922)

  * Fixed overwriting dataset metadata with empty values during import [#3913](https://github.com/voxel51/fiftyone/pull/3913)




Annotation

  * Added support for annotating multiple label fields using the Label Studio backend [#3895](https://github.com/voxel51/fiftyone/pull/3895)




Plugins

  * Added support for [delegating function calls](plugins__using_plugins.md#delegating-function-calls) via the new [@voxel51/utils/delegate](https://github.com/voxel51/fiftyone-plugins/pull/98) operator [#3939](https://github.com/voxel51/fiftyone/pull/3939)

  * Added the ability to search multiple fields in a delegated operation list query [#3892](https://github.com/voxel51/fiftyone/pull/3892)

  * Delegated operators now reference datasets by ID rather than name for robustness to dataset name changes [#3920](https://github.com/voxel51/fiftyone/pull/3920)

  * Improved validation for the builtin `delete_selected_samples` and `clone_selected_samples` operators [#3914](https://github.com/voxel51/fiftyone/pull/3914)

  * Fixed backwards compatibility issues with `ctx.secrets` [#3908](https://github.com/voxel51/fiftyone/pull/3908)

  * Fixed issue with JS plugin App configs [#3924](https://github.com/voxel51/fiftyone/pull/3924)




## FiftyOne Enterprise 1.5.2#

_Released December 11, 2023_

Bugs

  * Avoid creating non-existent database indexes on API startup

  * Avoid errors when archiving snapshots with corrupted run results




## FiftyOne Enterprise 1.5.1#

_Released December 8, 2023_

Includes all updates from FiftyOne 0.23.1

## FiftyOne 0.23.1#

_Released December 8, 2023_

App

  * Fixed Python 3.8 installations [#3905](https://github.com/voxel51/fiftyone/pull/3905)

  * Fixed App error pages [#3903](https://github.com/voxel51/fiftyone/pull/3903)

  * Fixed `session.dataset = None` [#3890](https://github.com/voxel51/fiftyone/pull/3890)




Core

  * Fixed inferring doubly-nested dynamic list field types [#3900](https://github.com/voxel51/fiftyone/pull/3900)

  * Fixed [`compute_metadata()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_metadata "fiftyone.core.collections.SampleCollection.compute_metadata") when `Pillow<7` is installed [#3897](https://github.com/voxel51/fiftyone/pull/3897)

  * Fixed default group indexes creation when importing a [FiftyOneDataset](user_guide__import_datasets.md#fiftyonedataset-import) [#3894](https://github.com/voxel51/fiftyone/pull/3894)




## FiftyOne Enterprise 1.5.0#

_Released December 6, 2023_

Includes all updates from FiftyOne 0.23.0, plus:

Features

  * Added support for archiving older [dataset snapshots](enterprise__dataset_versioning.md#dataset-versioning-snapshot-archival) to cold storage

  * Added support for executing operators on [dataset snapshots](enterprise__dataset_versioning.md#dataset-versioning)

  * Added support for uploading [multiple sets of cloud credentials](enterprise__installation.md#enterprise-cloud-storage-page), some of which may only apply to data in certain bucket(s)

  * Added support for uploading media [to Labelbox](integrations__labelbox.md#labelbox-integration) directly from S3 buckets

  * Added support for executing the builtin `open_dataset` operator in the Enterprise UI

  * Added support for executing operators when viewing datasets with no samples, for example to add media/labels to the dataset from within the App

  * Added support for [editing the label](enterprise__plugins.md#enterprise-runs-renaming) of a delegated operation

  * Added support for manually marking delegated operations as failed

  * Added support for [monitoring the progress](enterprise__plugins.md#enterprise-runs-monitoring-progress) of delegated operations

  * Improved handling of plugin secrets

  * Added the ability to attach authorization tokens to media/asset requests

  * Added new filter options to the dataset listing page

  * Filters/searches on the dataset listing page are now persisted through URL query parameters

  * Validate regexes before searching datasets to stop hard crashes

  * Enforce exact version of `auth0` python package

  * Added debug logging on API startup




Bugs

  * Fixed an issue with the [Runs page](enterprise__plugins.md#enterprise-runs-page) when viewing delegated operations that were scheduled via the SDK

  * Users with special access to a dataset are now displayed properly

  * Fixed an issue when loading certain datasets with saved [color schemes](user_guide__app.md#app-color-schemes) in the Enterprise UI

  * Fixed an issue on the dataset listing page where the page size menu would sometimes stay open after making a selection

  * Fixed an issue when downloading plugins via the API that contain bytes data or `.pyc` files

  * Fixed an issue where certain disabled operators were not correctly appearing as disabled in the operator browser

  * Improved reliability of similarity sort actions




## FiftyOne 0.23.0#

_Released December 6, 2023_

News

  * Released a [Redis integration](integrations__redis.md#redis-integration) for native text and image searches on FiftyOne datasets!

  * Released a [MongoDB integration](integrations__mongodb.md#mongodb-integration) for native text and image searches on FiftyOne datasets!

  * Released a [V7 integration](integrations__v7.md#v7-integration) for annotating FiftyOne datasets!




App

  * Added a new Lightning mode to the App sidebar that provides an optimized filtering experience for large datasets [#3807](https://github.com/voxel51/fiftyone/pull/3807)

  * Added support for viewing image groups [as a video](user_guide__app.md#app-dynamic-groups) [#3812](https://github.com/voxel51/fiftyone/pull/3812)

  * Added support for configuring custom color schemes for [semantic segmentation](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation) labels via the [color scheme editor](user_guide__app.md#app-color-schemes) [#3727](https://github.com/voxel51/fiftyone/pull/3727)

  * Added support for configuring custom [Heatmap](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) colorscales via the [color scheme editor](user_guide__app.md#app-color-schemes) [#3804](https://github.com/voxel51/fiftyone/pull/3804)

  * Improved rendering and customizability of label tags in the [color scheme](user_guide__app.md#app-color-schemes) [#3622](https://github.com/voxel51/fiftyone/pull/3622)

  * Added an empty dataset landing page that allows for importing media and/or labels to the dataset from the App by running operators [#3766](https://github.com/voxel51/fiftyone/pull/3766)

  * Added a landing page that appears when no dataset is currently selected that allows for creating/opening datasets in the App by running operators [#3766](https://github.com/voxel51/fiftyone/pull/3766)

  * Added support for executing operators when the sample modal is open [#3747](https://github.com/voxel51/fiftyone/pull/3747)

  * Added a keyboard shortcut for batch selecting samples in grid and modal [#3718](https://github.com/voxel51/fiftyone/pull/3718)

  * Made field visibilityâs selections persistent across page refreshes [#3646](https://github.com/voxel51/fiftyone/pull/3646)

  * Introduced error alert for view bar errors in view stages [#3613](https://github.com/voxel51/fiftyone/pull/3613)

  * Ensure that the last used brain key is loaded by default in the similarity search menu [#3714](https://github.com/voxel51/fiftyone/pull/3714)

  * Added support for launching the App with a non-default browser [#3789](https://github.com/voxel51/fiftyone/pull/3789)

  * Upgraded `werkzeug` from 2.0.3 to 3.0.1 in requirements for improved compatibility [#3723](https://github.com/voxel51/fiftyone/pull/3723)




Core

  * Adding support for registering [custom evaluation methods](user_guide__evaluation.md#custom-evaluation-backends) [#3695](https://github.com/voxel51/fiftyone/pull/3695)

  * Optimized the [`compute_metadata()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_metadata "fiftyone.core.collections.SampleCollection.compute_metadata") implementation [#3801](https://github.com/voxel51/fiftyone/pull/3801)

  * Added full support for working with images that use `EXIF` tags [#3824](https://github.com/voxel51/fiftyone/pull/3824)

  * Added support for parsing and exporting visibility attribute for keypoints in [COCO format](user_guide__export_datasets.md#cocodetectiondataset-export) [#3808](https://github.com/voxel51/fiftyone/pull/3808)




Plugins

  * Added `ctx.current_sample` to operatorâs [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") to support applying operators to the current sample open in the App modal [#3792](https://github.com/voxel51/fiftyone/pull/3792)

  * Added support for configuring an operatorâs available [execution options](plugins__developing_plugins.md#operator-execution-options) in cases where immediate and/or delegated execution should be available [#3839](https://github.com/voxel51/fiftyone/pull/3839)

  * Added support for [programmatically executing](plugins__using_plugins.md#executing-operators-sdk) generator operators via the SDK [#3803](https://github.com/voxel51/fiftyone/pull/3803)

  * Added a builtin `clear_sample_field` operator for clearing sample fields [#3800](https://github.com/voxel51/fiftyone/pull/3800)

  * Loosened the [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig") constructor signature for enhanced forward/backward compatibility [#3786](https://github.com/voxel51/fiftyone/pull/3786)

  * Fixed an issue where operator form defaults were not always applied [#3777](https://github.com/voxel51/fiftyone/pull/3777)

  * Improved handling of fields in operator forms [#3728](https://github.com/voxel51/fiftyone/pull/3728)

  * Improved default value control in operator forms [#3371](https://github.com/voxel51/fiftyone/pull/3371)




Annotation

  * Updated the [Labelbox integration](integrations__labelbox.md#labelbox-integration) to support the latest version of the Labelbox API [#3781](https://github.com/voxel51/fiftyone/pull/3781)

  * Removed the need for prepending sequence numbers to filenames when uploading images to the [CVAT integration](integrations__cvat.md#cvat-integration) with sufficiently new versions of the CVAT SDK [#3823](https://github.com/voxel51/fiftyone/pull/3823)




Bugs

  * Improved the implementation of saved view loading in the App [#3788](https://github.com/voxel51/fiftyone/pull/3788)

  * Fixed an issue where typing the backtick key would close the operator palette [#3790](https://github.com/voxel51/fiftyone/pull/3790)

  * Fixed orthographic projection bug for more accurate 3D rendering [#3864](https://github.com/voxel51/fiftyone/pull/3864)

  * Addressed missing notifications when scheduling certain delegated operations from the App [#3861](https://github.com/voxel51/fiftyone/pull/3861)

  * Resolved issues with generator operators [#3861](https://github.com/voxel51/fiftyone/pull/3861)

  * Fixed operator form exception when `onChange` is missing [#3840](https://github.com/voxel51/fiftyone/pull/3840)

  * Corrected operator form crash and changed field re-render [#3833](https://github.com/voxel51/fiftyone/pull/3833)

  * Fixed select/show samples builtin operator for better sample management [#3818](https://github.com/voxel51/fiftyone/pull/3818)

  * Addressed hidden validation error bug for more accurate error handling [#3776](https://github.com/voxel51/fiftyone/pull/3776)

  * Fixed issue with custom colors when switching between name and list [#3847](https://github.com/voxel51/fiftyone/pull/3847)

  * Various improvements and fixes around color management [#3649](https://github.com/voxel51/fiftyone/pull/3649)

  * Resolved issue where tag labels in multiple samples could only tag labels in the last sample [#3858](https://github.com/voxel51/fiftyone/pull/3858)

  * Prevent operator list from rendering behind the sample modal [#3757](https://github.com/voxel51/fiftyone/pull/3757)

  * Fixed boolean not displayed in modal view sidebar entry for consistent data representation [#3713](https://github.com/voxel51/fiftyone/pull/3713)

  * Fixed random seed issue when creating [`Take`](api__fiftyone.core.stages.md#fiftyone.core.stages.Take "fiftyone.core.stages.Take") view stages in the App [#3855](https://github.com/voxel51/fiftyone/pull/3855)

  * Fixed dynamically grouped views for non-group parent media types of grouped datasets [#3798](https://github.com/voxel51/fiftyone/pull/3798)

  * Addressed media fields issues for more reliable media handling [#3722](https://github.com/voxel51/fiftyone/pull/3722)

  * Fixed an issue with selecting group slices in views that contain a [`Select`](api__fiftyone.core.stages.md#fiftyone.core.stages.Select "fiftyone.core.stages.Select") view stage [#3852](https://github.com/voxel51/fiftyone/pull/3852)

  * Fixed an issue with view reloading for datasets that have saved views [#3838](https://github.com/voxel51/fiftyone/pull/3838)

  * Fixed rendering of semantic segmentation masks within [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument") fields [#3825](https://github.com/voxel51/fiftyone/pull/3825)

  * Resolved an issue with the slice/group statistics selector where no default option is selected [#3698](https://github.com/voxel51/fiftyone/pull/3698)

  * Fixed various issues with builtin operators [#3817](https://github.com/voxel51/fiftyone/pull/3817)

  * Addressed a potential data duplication issue when merging in-memory samples into grouped datasets [#3816](https://github.com/voxel51/fiftyone/pull/3816)

  * Resolved possible malformed [FiftyOneDataset](user_guide__export_datasets.md#fiftyonedataset-export) format exports due to concurrent edits [#3726](https://github.com/voxel51/fiftyone/pull/3726)

  * Fixed the plugin cache check [#3676](https://github.com/voxel51/fiftyone/pull/3676)

  * Fixed an error when pressing the esc key in the App [#3662](https://github.com/voxel51/fiftyone/pull/3662)




## FiftyOne Enterprise 1.4.5#

_Released November 21, 2023_

General

  * Added debug log events to API server startup




## FiftyOne Enterprise 1.4.4#

_Released November 3, 2023_

Includes all updates from FiftyOne 0.22.3, plus:

General

  * Optimized iterator operations such as export

  * Improved plugin upload reliability

  * Further improved dataset listing queries




Bugs

  * Fixed clips, frames, and patches views for grouped datasets in the App

  * Fixed cloud credential initialization during deployment restarts

  * Fixed snapshot diff computation in large datasets with MongoDB < v6.0




## FiftyOne 0.22.3#

_Released November 3, 2023_

Core

  * Optimized [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") [#3733](https://github.com/voxel51/fiftyone/pull/3733)




App

  * Fixed rendering of [`BooleanFields`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField") in the sample modal [#3720](https://github.com/voxel51/fiftyone/pull/3720)

  * Optimized the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#3733](https://github.com/voxel51/fiftyone/pull/3733)

  * Fixed [media field](user_guide__app.md#app-multiple-media-fields) changes in the sample modal [#3735](https://github.com/voxel51/fiftyone/pull/3735)

  * Fixed sidebar reordering edge case [#3753](https://github.com/voxel51/fiftyone/pull/3753)

  * Fixed the [Operator browser](plugins__using_plugins.md#using-operators) in the sample modal [#3764](https://github.com/voxel51/fiftyone/pull/3764)

  * Fixed [3D detections](user_guide__app.md#app-3d-orthographic-projections) in the grid [#3761](https://github.com/voxel51/fiftyone/pull/3761)




Brain

  * Optimized similarity backends when performing KNN queries against their entire indexes

  * Fixed performing similarity queries on filtered views in the [LanceDB integration](integrations__lancedb.md#lancedb-integration)

  * Fixed calling [`remove_from_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.remove_from_index "fiftyone.brain.similarity.SimilarityIndex.remove_from_index") on an index that uses the `embeddings_field` parameter

  * Fixed [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings") when `skip_existing=True` is provided




Plugins

  * Fixed `on_startup` [Operator execution](plugins__using_plugins.md#using-operators) [#3731](https://github.com/voxel51/fiftyone/pull/3731)

  * Fixed `selected_labels` in [Operator contexts](plugins__using_plugins.md#using-operators) [#3740](https://github.com/voxel51/fiftyone/pull/3740)

  * Improved [Operator placements](plugins__using_plugins.md#using-operators) [#3742](https://github.com/voxel51/fiftyone/pull/3742)

  * Fixed `async` generator results in [delegated operations](plugins__overview.md#fiftyone-plugins) [#3754](https://github.com/voxel51/fiftyone/pull/3754)

  * Fixed `ctx.secrets` in [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") [#3759](https://github.com/voxel51/fiftyone/pull/3759)




CLI

  * Added [fiftyone delegated fail](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated-fail) and [fiftyone delegated delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated-delete) commands [#3721](https://github.com/voxel51/fiftyone/pull/3721)




## FiftyOne Enterprise 1.4.3#

_Released October 20, 2023_

Includes all updates from FiftyOne 0.22.2, plus:

General

  * Improved dataset listing queries

  * Improved error handling when listing datasets

  * Fixed issues with offline access and auth errors requiring cookies to be cleared manually

  * Reduced max export size of datasets to 100MB

  * Users will now only _see an operator_ if their role meets the required role




## FiftyOne 0.22.2#

_Released October 20, 2023_

Core

  * Added a `fiftyone_max_thread_pool_workers` option to the [FiftyOne config](user_guide__config.md#configuring-fiftyone) [#3654](https://github.com/voxel51/fiftyone/pull/3654)

  * Added a `fiftyone_max_process_pool_workers` option to the [FiftyOne config](user_guide__config.md#configuring-fiftyone) [#3654](https://github.com/voxel51/fiftyone/pull/3654)

  * Added support for directly calling [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") on [patches views](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views) to export image patches [#3651](https://github.com/voxel51/fiftyone/pull/3651)

  * Fixed an [issue](https://github.com/voxel51/fiftyone/issues/3688) where CVAT import fails when `insert_new` is `False` [#3691](https://github.com/voxel51/fiftyone/pull/3691)




App

  * Fixed dataset recreation across processes [#3655](https://github.com/voxel51/fiftyone/pull/3655)

  * Fixed the [`Session.url`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session "fiftyone.core.session.session.Session") property in Colab [#3645](https://github.com/voxel51/fiftyone/pull/3645)

  * Fixed converting to patches in [grouped datasets](https://docs.voxel51.com/user_guide/groups.html#groups) when sidebar filters are present [#3666](https://github.com/voxel51/fiftyone/pull/3666)

  * Fixed browser cache issues when upgrading [#3683](https://github.com/voxel51/fiftyone/pull/3683)




Plugins

  * Use a fallback icon when an operator cannot be executed [#3661](https://github.com/voxel51/fiftyone/pull/3661)

  * [`FileView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileView "fiftyone.operators.types.FileView") now captures content as well as filename and type of the [`UploadedFile`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile "fiftyone.operators.types.UploadedFile") [#3679](https://github.com/voxel51/fiftyone/pull/3679)

  * Fixed issue where the `fiftyone delegated launch` CLI command would print confusing errors [#3694](https://github.com/voxel51/fiftyone/pull/3694)

  * Added a [`list_operators()`](api__fiftyone.operators.md#fiftyone.operators.list_operators "fiftyone.operators.list_operators") utility for listing operators [#3694](https://github.com/voxel51/fiftyone/pull/3694)

  * Added a [`operator_exists()`](api__fiftyone.operators.md#fiftyone.operators.operator_exists "fiftyone.operators.operator_exists") utility for checking if an operator exists [#3694](https://github.com/voxel51/fiftyone/pull/3694)

  * [`Number`](api__fiftyone.operators.types.md#fiftyone.operators.types.Number "fiftyone.operators.types.Number") properties now support `min` and `max` options in various views and validation [#3684](https://github.com/voxel51/fiftyone/pull/3684)

  * Improved validation of primitive types in operators [#3685](https://github.com/voxel51/fiftyone/pull/3685)

  * Fixed issue where non-required property validated as required [#3701](https://github.com/voxel51/fiftyone/pull/3701)

  * Fixed an issue where plugin cache was not cleared when a plugin was deleted [#3700](https://github.com/voxel51/fiftyone/pull/3700)

  * [`File`](api__fiftyone.operators.types.md#fiftyone.operators.types.File "fiftyone.operators.types.File") now uses [`FileExplorerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView "fiftyone.operators.types.FileExplorerView") by default [#3656](https://github.com/voxel51/fiftyone/pull/3656)




Zoo

  * Fixed issue preventing [DINOv2](integrations__pytorch_hub.md#dinov2-example) models from being loaded [#3660](https://github.com/voxel51/fiftyone/pull/3690)




## FiftyOne Enterprise 1.4.2#

_Released October 6, 2023_

Includes all updates from FiftyOne 0.22.1, plus:

General

  * Error messages now clearly indicate when attempting to use a duplicate key on datasets a user does not have access to

  * Fixed issue with setting default access permissions for new datasets

  * Deleting a dataset now deletes all dataset-related references

  * Default fields now populate properly when creating a new dataset regardless of client

  * Improved complex/multi collection aggregations in the api client

  * Fixed issue where users could not list other users within their own org

  * Snapshots now properly include all run results

  * Fixed issue where reverting a snapshot behaved incorrectly in some cases

  * Fixed Python 3.7 support in the fiftyone-teams SDK




App

  * Searching users has been improved

  * Resolved issue with recent views not displaying properly




## FiftyOne 0.22.1#

_Released October 6, 2023_

App

  * Fixed empty detection instance masks [#3559](https://github.com/voxel51/fiftyone/pull/3559)

  * Fixed a visual issue with scrollbars [#3605](https://github.com/voxel51/fiftyone/pull/3605)

  * Fixed a bug with color by index for videos [#3606](https://github.com/voxel51/fiftyone/pull/3606)

  * Fixed an issue where [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") (and other label types) subfields were properly handling primitive types [#3577](https://github.com/voxel51/fiftyone/pull/3577)

  * Fixed an issue launching the App in Databrick notebooks [#3609](https://github.com/voxel51/fiftyone/pull/3609)




Core

  * Resolved groups aggregation issue resulting in unstable ordering of documents [#3641](https://github.com/voxel51/fiftyone/pull/3614)

  * Fixed an issue where group indexes were not created against the correct `id` property [#3627](https://github.com/voxel51/fiftyone/pull/3627)

  * Fixed issue with empty segmentation mask conversion in COCO-formatted datasets [#3595](https://github.com/voxel51/fiftyone/pull/3595/commits/ad0607aeabbd5d6dcbcfccc622ee5caf1f71f930)




Plugins

  * Added a new [`fiftyone.plugins.utils`](api__fiftyone.plugins.utils.md#module-fiftyone.plugins.utils "fiftyone.plugins.utils") module that provides common utilities for plugin development [#3612](https://github.com/voxel51/fiftyone/pull/3612)

  * Re-enabled text-only placement support when icon is not available [#3593](https://github.com/voxel51/fiftyone/pull/3593)

  * Added read-only support for [`FileExplorerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView "fiftyone.operators.types.FileExplorerView") [#3639](https://github.com/voxel51/fiftyone/pull/3597)

  * The `fiftyone delegated launch` CLI command will now only run one operation at a time [#3615](https://github.com/voxel51/fiftyone/pull/3615)

  * Fixed an issue where custom component props were not supported [#3595](https://github.com/voxel51/fiftyone/pull/3549)

  * Fixed issue where `selected_labels` were missing from the [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") during [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") and [`resolve_output()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_output "fiftyone.operators.operator.Operator.resolve_output") [#3575](https://github.com/voxel51/fiftyone/pull/3574)




## FiftyOne Enterprise 1.4.1#

_Released September 21, 2023_

Bugs

  * Patched a regression that prevented the Enterprise App from working behind proxies




## FiftyOne Enterprise 1.4.0#

_Released September 20, 2023_

Includes all updates from FiftyOne 0.22.0, plus:

News

  * Added support for [dataset versioning](enterprise__dataset_versioning.md#dataset-versioning)!

  * Added support for scheduling [delegated operations](enterprise__plugins.md#enterprise-delegated-operations) via the App




App

  * Admins can now [upload secrets](enterprise__secrets.md#enterprise-secrets) via the UI which are made available to all plugins and delegated operations at runtime

  * Optimized page load times when accessing the Team Settings page

  * Optimized page load times when opening a dataset for the first time in a new web session




## FiftyOne 0.22.0#

_Released September 20, 2023_

News

  * Added a native [Ultralytics integration](integrations__ultralytics.md#ultralytics-integration)! [#3451](https://github.com/voxel51/fiftyone/pull/3451)

  * Added support for scheduling [delegated operations](plugins__overview.md#fiftyone-plugins) from within the App! [#3312](https://github.com/voxel51/fiftyone/pull/3312)




App

  * Updated the [Histograms panel](user_guide__app.md#app-histograms-panel) to only render one field at a time to improve performance [#3419](https://github.com/voxel51/fiftyone/pull/3419)

  * Gracefully fallback to `filepath` if a datasetâs [`app_config`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.app_config "fiftyone.core.dataset.Dataset.app_config") has a custom grid media field that has been excluded from the current view [#3498](https://github.com/voxel51/fiftyone/pull/3498)

  * Improved rendering of 2D polylines [#3476](https://github.com/voxel51/fiftyone/pull/3476)

  * Prevented unnecessary page reloads when clearing selections in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#3507](https://github.com/voxel51/fiftyone/pull/3507)

  * Removed unnecessary page reloads when resetting field visibility filters [#3441](https://github.com/voxel51/fiftyone/pull/3441)

  * Fixed an off-by-one bug when paging in the sample grid [#3416](https://github.com/voxel51/fiftyone/pull/3416)

  * Fixed a bug when applying field visibility filters to fields of type [`DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField") and [`DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField") [#3418](https://github.com/voxel51/fiftyone/pull/3418)

  * Fixed a bug when changing slices for grouped datasets in the sample modal when sidebar filters have been applied [#3545](https://github.com/voxel51/fiftyone/pull/3545)

  * Fixed a bug when visualizing dynamic groupings of grouped datasets with sparse (missing) slices [#3470](https://github.com/voxel51/fiftyone/pull/3470)

  * Fixed a bug that prevented the group media visibility dropdown from opening [#3480](https://github.com/voxel51/fiftyone/pull/3480)

  * Fixed a bug where attributes of grouped samples were missing in the modal [#3436](https://github.com/voxel51/fiftyone/pull/3436)




Core

  * Added support for grouping by compound keys using [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by") [#3515](https://github.com/voxel51/fiftyone/pull/3515)

  * Added `create_index=False` options to [`sort_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by "fiftyone.core.collections.SampleCollection.sort_by") and [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by") [#3515](https://github.com/voxel51/fiftyone/pull/3515)

  * Added a new `tags` filter option to [`list_datasets()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.list_datasets "fiftyone.core.dataset.list_datasets") [#3492](https://github.com/voxel51/fiftyone/pull/3492)

  * Added a [`fiftyone.core.storage`](api__fiftyone.core.storage.md#module-fiftyone.core.storage "fiftyone.core.storage") module that provides a common interface for filesystem I/O [#3406](https://github.com/voxel51/fiftyone/pull/3406)

  * Added dataset tag and label filters when exporting datasets [via the CLI](https://docs.voxel51.com/cli/index.html#cli-fiftyone-datasets-export) [#3412](https://github.com/voxel51/fiftyone/pull/3412)

  * Added support for running FiftyOne in podman containers [#3483](https://github.com/voxel51/fiftyone/pull/3483)

  * Optimized the [`list_datasets(info=True)`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.list_datasets "fiftyone.core.dataset.list_datasets") implementation [#3528](https://github.com/voxel51/fiftyone/pull/3528)

  * Added support for providing frame sizes when constructing [rotated boxes](https://docs.voxel51.com/user_guide/using_datasets.html#rotated-bounding-boxes) and [cuboids](https://docs.voxel51.com/user_guide/using_datasets.html#cuboids) [#3409](https://github.com/voxel51/fiftyone/pull/3409)

  * Fixed a bug with automatic non-persistent dataset cleanup when running MongoDB v4.4 and later [#3486](https://github.com/voxel51/fiftyone/pull/3486)

  * Fixed a bug where default indexes for grouped datasets were not created via [`clone()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone "fiftyone.core.dataset.Dataset.clone") and [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") [#3515](https://github.com/voxel51/fiftyone/pull/3515)

  * Fixed a bug where NaNs were causing orthographic projection computations to crash [#3427](https://github.com/voxel51/fiftyone/pull/3427)

  * Fixed a bug with the [OpenLABEL importer](user_guide__import_datasets.md#openlabelimagedataset-import) when given incomplete keypoint skeletons [#3429](https://github.com/voxel51/fiftyone/pull/3429)




Plugins

  * Added a new [`FileExplorerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView "fiftyone.operators.types.FileExplorerView") type that allows for browsing file systems and selecting files or directories [#3459](https://github.com/voxel51/fiftyone/pull/3459)

  * Added `ctx.secrets` to plugins [#3453](https://github.com/voxel51/fiftyone/pull/3453)

  * Added a builtin `set_progress` operator [#3516](https://github.com/voxel51/fiftyone/pull/3516)

  * Fixed broken wiring of the [`MarkdownView`](api__fiftyone.operators.types.md#fiftyone.operators.types.MarkdownView "fiftyone.operators.types.MarkdownView"), [`SwitchView`](api__fiftyone.operators.types.md#fiftyone.operators.types.SwitchView "fiftyone.operators.types.SwitchView"), and [`Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement") components [#3537](https://github.com/voxel51/fiftyone/pull/3537)




Zoo

  * Graceful handling of empty prompts when using [Segment Anything](model_zoo__models__segment_anything_vitb_torch.md#model-zoo-segment-anything-vitb-torch) models [#3505](https://github.com/voxel51/fiftyone/pull/3505)

  * Fixed bugs where [Segment Anything](model_zoo__models__segment_anything_vitb_torch.md#model-zoo-segment-anything-vitb-torch) model weights were not loaded and auto-inference would only return one set of masks [#3465](https://github.com/voxel51/fiftyone/pull/3465)




## FiftyOne Enterprise 1.3.6#

_Released August 8, 2023_

Includes all updates from FiftyOne 0.21.6.

## FiftyOne 0.21.6#

_Released August 8, 2023_

App

  * Fixed the Embeddings panel [#3401](https://github.com/voxel51/fiftyone/pull/3401)

  * Fixed a bug when using the sidebar to filter views that have selected fields [#3405](https://github.com/voxel51/fiftyone/pull/3405)




## FiftyOne Enterprise 1.3.5#

_Released August 7, 2023_

Includes all updates from FiftyOne 0.21.5, plus:

App

  * Fixed a bug with [dataset search](enterprise__app.md#enterprise-homepage) where suggestions may not appear when matches across multiple types collide

  * Upgraded the [Plugin configuration UI](enterprise__plugins.md#enterprise-plugins) to better explain the available Operator permission configuration options




SDK

  * Significant performance optimizations by introducing cursor batching for relevant API endpoints




## FiftyOne 0.21.5#

_Released August 7, 2023_

News

  * Added [Segment Anything](https://segment-anything.com) to the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo)! [#3330](https://github.com/voxel51/fiftyone/pull/3330)

  * Added [DINOv2](https://github.com/facebookresearch/dinov2) to the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo)! [#2951](https://github.com/voxel51/fiftyone/pull/2951)

  * Added support for loading models from [PyTorch Hub](integrations__pytorch_hub.md#pytorch-hub-integration)! [#2949](https://github.com/voxel51/fiftyone/pull/2949)




App

  * Added support for controlling field visibility in the grid independent of filtering [#3248](https://github.com/voxel51/fiftyone/pull/3248)

  * Added support for filtering by label tags in individual label fields [#3287](https://github.com/voxel51/fiftyone/pull/3287)

  * Added support for specifying [custom colors](user_guide__app.md#app-color-schemes-app) for list fields [#3319](https://github.com/voxel51/fiftyone/pull/3319)

  * Added support for opening the [color panel](user_guide__app.md#app-color-schemes-app) when the sample modal is open [#3355](https://github.com/voxel51/fiftyone/pull/3355)

  * Added helper text explaining custom color options [#3383](https://github.com/voxel51/fiftyone/pull/3383)

  * Added support for viewing slices of grouped datasets in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#3351](https://github.com/voxel51/fiftyone/pull/3351)

  * Added support for coloring embeddings plots by list fields [#3326](https://github.com/voxel51/fiftyone/pull/3326)

  * Improved overflow when the actions row contains many icons [#3296](https://github.com/voxel51/fiftyone/pull/3296)

  * Added support for tagging all visible PCD slices [#3384](https://github.com/voxel51/fiftyone/pull/3384)

  * Improved handling of group datasets whose groups may contain missing samples for certain slices [#3333](https://github.com/voxel51/fiftyone/pull/3333)

  * Fixed various issues when visualizing grouped datasets [#3353](https://github.com/voxel51/fiftyone/pull/3353), [#3322](https://github.com/voxel51/fiftyone/pull/3322), [#3318](https://github.com/voxel51/fiftyone/pull/3318), [#3379](https://github.com/voxel51/fiftyone/pull/3379), [#3318](https://github.com/voxel51/fiftyone/pull/3318)

  * Added bazel support [#3338](https://github.com/voxel51/fiftyone/pull/3338)

  * Removed the maximum `starlette` version requirement [#3297](https://github.com/voxel51/fiftyone/pull/3297)




Plugins

  * Added support for accessing the currently selected labels in the App within plugin execution contexts [#3295](https://github.com/voxel51/fiftyone/pull/3295)

  * Added support for configuring custom [Operator icons](plugins__using_plugins.md#using-operators) [#3299](https://github.com/voxel51/fiftyone/pull/3299)

  * Improved Operator form validation debounce behavior [#3291](https://github.com/voxel51/fiftyone/pull/3291)

  * Fixed some bugs that prevented customer visualizer plugins from being recognized [#3357](https://github.com/voxel51/fiftyone/pull/3357)




Core

  * Improved robustness of concurrent schema updates [#3308](https://github.com/voxel51/fiftyone/pull/3308)

  * Schema changes are now maintained by the [`select_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_group_slices "fiftyone.core.collections.SampleCollection.select_group_slices") stage [#3336](https://github.com/voxel51/fiftyone/pull/3336)

  * Added support for exporting keypoints with nan-valued coordinates in [COCO format](user_guide__export_datasets.md#cocodetectiondataset-export) [#3316](https://github.com/voxel51/fiftyone/pull/3316)

  * Updated [YOLOv5 exports](user_guide__export_datasets.md#yolov5dataset-export) to use dict-style class names [#3393](https://github.com/voxel51/fiftyone/pull/3393)

  * Fixed a bug when passing an RGB hex string to [`to_segmentation()`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection.to_segmentation "fiftyone.core.labels.Detection.to_segmentation") [#3293](https://github.com/voxel51/fiftyone/pull/3293)

  * Fixed a bug where [`has_field()`](api__fiftyone.core.document.md#fiftyone.core.document.Document.has_field "fiftyone.core.document.Document.has_field") would not recognize dynamic fields [#3349](https://github.com/voxel51/fiftyone/pull/3349)

  * Fixed a bug when applying [`merge_sample()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_sample "fiftyone.core.dataset.Dataset.merge_sample") to grouped datasets [#3327](https://github.com/voxel51/fiftyone/pull/3327)




Zoo

  * Use `weights` parameter instead of deprecated `pretrained` parameter for torchvision models [#3348](https://github.com/voxel51/fiftyone/pull/3348)

  * Added support for running zoo models with the MPS backend [#2843](https://github.com/voxel51/fiftyone/pull/2843)

  * Fixed YouTube video downloading for zoo datasets like [ActivityNet](dataset_zoo__datasets__activitynet_200.md#dataset-zoo-activitynet-200) and [Kinetics](dataset_zoo__datasets__kinetics_700_2020.md#dataset-zoo-kinetics-700-2020) [#3382](https://github.com/voxel51/fiftyone/pull/3382)




Annotation

  * Upgraded the [Labelbox integration](integrations__labelbox.md#labelbox-integration) to support the latest Labelbox API version [#3323](https://github.com/voxel51/fiftyone/pull/3323)

  * Fixed text and checkbox attribute usage when using CVAT 2.5 [#3373](https://github.com/voxel51/fiftyone/pull/3373)




Brain

  * Added support for [gRPC connections](integrations__qdrant.md#qdrant-setup) when using the Qdrant similarity backend [#3296](https://github.com/voxel51/fiftyone/pull/3296)

  * Improved support for [creating similarity indexes](brain.md#brain-similarity-api) with embeddings stored in dataset fields

  * Resolved bugs with similarity queries using the sklearn backend [#3304](https://github.com/voxel51/fiftyone/issues/3304), [#3305](https://github.com/voxel51/fiftyone/issues/3305)




Docs

  * Fixed some documentation typos [#3283](https://github.com/voxel51/fiftyone/issues/3283), [#3289](https://github.com/voxel51/fiftyone/issues/3289), [#3290](https://github.com/voxel51/fiftyone/issues/3290)




## FiftyOne 0.21.4#

_Released July 14, 2023_

  * Fixed [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") event emission [#3301](https://github.com/voxel51/fiftyone/pull/3301)




## FiftyOne Enterprise 1.3.3#

_Released July 12, 2023_

Includes all updates from FiftyOne 0.21.3, plus:

SDK

  * Added a `cache=True` option to the [upload_media()](enterprise__cloud_media.md#enterprise-cloud-api-reference) utility that allows for automatically adding any uploaded files to your local cache

  * Fixed a bug when launching the App locally via API connections




## FiftyOne 0.21.3#

_Released July 12, 2023_

News

  * Released a [Milvus integration](integrations__milvus.md#milvus-integration) for native text and image searches on FiftyOne datasets!

  * Released a [LanceDB integration](integrations__lancedb.md#lancedb-integration) for native text and image searches on FiftyOne datasets!




App

  * Added support for embedded keypoint fields in [`filter_keypoints()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_keypoints "fiftyone.core.collections.SampleCollection.filter_keypoints") [#3279](https://github.com/voxel51/fiftyone/pull/3279)

  * Fixed keypoint filtering [#3270](https://github.com/voxel51/fiftyone/pull/3280)

  * Fixed a bug that caused non-matching samples to remain in the grid when applying multiple sidebar filters [#3270](https://github.com/voxel51/fiftyone/pull/3270)

  * Fixed a bug when filtering by IDs in the sidebar [#3270](https://github.com/voxel51/fiftyone/pull/3270)

  * Fixed label tags grid bubbles for filterless views [#3257](https://github.com/voxel51/fiftyone/pull/3267)




Core

  * Added a [`merge_sample()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_sample "fiftyone.core.dataset.Dataset.merge_sample") method for merging individual samples into existing datasets [#3274](https://github.com/voxel51/fiftyone/pull/3274)

  * Fixed a bug when passing dict-valued `points` to [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") [#3268](https://github.com/voxel51/fiftyone/pull/3268)

  * Fixed a bug when filtering keypoints stored in embedded documents [#3279](https://github.com/voxel51/fiftyone/pull/3279)




## FiftyOne Enterprise 1.3.2#

_Released July 5, 2023_

Includes all updates from FiftyOne 0.21.2.

## FiftyOne 0.21.2#

_Released July 3, 2023_

App

  * Fixes grid pagination results after applying sidebar filters [#3249](https://github.com/voxel51/fiftyone/pull/3249)

  * Fixes redundant sidebar groups for custom schemas [#3250](https://github.com/voxel51/fiftyone/pull/3250)




## FiftyOne Enterprise 1.3.1#

_Released June 30, 2023_

Includes all features from FiftyOne 0.21.1, plus:

General

  * App containers no longer need to be restarted in order for Azure/MinIO credentials uploaded via the Enterprise UI to be properly recognized

  * Fixed an intermittent bug when computing metadata for remote filepaths

  * Reverted a change from Enterprise 1.3.0 so that the SDK again supports the declared minimum version requirement of `pymongo==3.12`




SDK

  * Updated the order of precedence for SDK connections so that [API connections](enterprise__api_connection.md#enterprise-api-connection) take precedence over [direct database connections](user_guide__config.md#configuring-mongodb-connection)

  * Fixed a bug when connecting to Enterprise deployments with non-standard database names via API connections

  * Fixed a bug when saving run results using API connections

  * Fixed a bug when deleting datasets using API connections




Management SDK

  * Added support for [deleting user invitations](enterprise__management_sdk.md#enterprise-sdk-user-management) by email in addition to invitation ID

  * Added support for [configuring permissions](enterprise__management_sdk.md#enterprise-sdk-dataset-permissions) for invited users that have not yet logged in




## FiftyOne 0.21.1#

_Released June 30, 2023_

App

  * Sidebar filters can now [leverage indexes](user_guide__app.md#app-optimizing-query-performance) for improved performance! [#3137](https://github.com/voxel51/fiftyone/pull/3137)

  * Optimized the App gridâs loading performance, especially for datasets with large samples [#3137](https://github.com/voxel51/fiftyone/pull/3137)

  * Improved the usability of the [field visibility modal](user_guide__app.md#app-field-visibility) [#3154](https://github.com/voxel51/fiftyone/pull/3154)

  * Added support for visualizing Label fields stored within dynamic embedded documents [#3141](https://github.com/voxel51/fiftyone/pull/3141)

  * Added support for coloring embeddings plots by list fields [#3230](https://github.com/voxel51/fiftyone/pull/3230)

  * Added a `proxy_url` setting to the [App config](user_guide__config.md#configuring-fiftyone-app) that allows for overriding the server URL [#3222](https://github.com/voxel51/fiftyone/pull/3222)

  * Added support for configuring [custom colors](user_guide__app.md#app-color-schemes) for sample tags [#3171](https://github.com/voxel51/fiftyone/pull/3171)

  * Fixed a bug that caused the point cloud selector from disappearing [#3200](https://github.com/voxel51/fiftyone/pull/3200)

  * Fixed various minor bugs when viewing [dynamic groups](user_guide__app.md#app-dynamic-groups) in the App [#3172](https://github.com/voxel51/fiftyone/pull/3172)




Core

  * Methods like [`tag_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.tag_labels "fiftyone.core.collections.SampleCollection.tag_labels"), [`select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels"), [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export"), and [`draw_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.draw_labels "fiftyone.core.collections.SampleCollection.draw_labels") now automatically detect and properly handle label fields stored within embedded documents [#3152](https://github.com/voxel51/fiftyone/pull/3152)

  * All [`Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document") objects now support `doc["nested.field"]` key access [#3152](https://github.com/voxel51/fiftyone/pull/3152)

  * Dynamic field detection now automatically detects dynamic attributes of list fields with inhomogeneous values [#3152](https://github.com/voxel51/fiftyone/pull/3152)

  * Fixed a bug that would cause dynamic field schema methods to erroneously declare subfields of [`Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") points [#3152](https://github.com/voxel51/fiftyone/pull/3152)

  * Fixed a bug when applying [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") to video dataset views [#3159](https://github.com/voxel51/fiftyone/pull/3159)




Plugins

  * Added support for rendering markdown-style tables using the Operator table view type [#3162](https://github.com/voxel51/fiftyone/pull/3162)

  * Added support for multiselect to the Operator string type [#3192](https://github.com/voxel51/fiftyone/pull/3192)

  * Added `--all` flags to plugin CLI methods [#3177](https://github.com/voxel51/fiftyone/pull/3177)

  * Placements and on-startup hooks are now omitted for disabled Operators [#3175](https://github.com/voxel51/fiftyone/pull/3175)

  * Fixed a bug with `read_only=True` mode for certain Operator view types [#3225](https://github.com/voxel51/fiftyone/pull/3225)




Annotation

  * Added support for CVATâs `frame_start`, `frame_stop`, and `frame_step` options when creating annotation tasks [#3181](https://github.com/voxel51/fiftyone/pull/3181)




## FiftyOne Enterprise 1.3.0#

_Released May 31, 2023_

Includes all features from FiftyOne 0.21.0, plus:

General

  * Added a [Management SDK](enterprise__management_sdk.md#enterprise-management-sdk) subpackage for programmatically configuring user roles, dataset permissions, plugins, and more

  * Added support for authenticated [API connections](enterprise__api_connection.md#enterprise-api-connection) when using the Python SDK that respect user roles, dataset permissions, etc

  * Logins now automatically redirect back to the page you were trying to access

  * Improved non-persistent dataset cleanup behavior

  * Fixed a bug that could cause the media cache to erroneously garbage collect large files while they are downloading

  * Fixed a bug when cloning views into new datasets via the Enterprise UI




Admin

  * Added support for [uploading and managing plugins](enterprise__plugins.md#enterprise-plugins) via the Enterprise UI

  * Added support for cross account IAM roles when configuring cloud storage credentials

  * Fixed a bug that prevented Azure/MinIO credentials uploaded via the Enterprise UI from being properly recognized by the App




## FiftyOne 0.21.0#

_Released May 31, 2023_

App

  * Added support for viewing and executing operators in the App! [#2679](https://github.com/voxel51/fiftyone/pull/2679)

  * Added support for creating [dynamic groups](user_guide__app.md#app-dynamic-groups) in the App [#2934](https://github.com/voxel51/fiftyone/pull/2934)

  * Added support for overlaying multiple point cloud slices in Looker3D [#2912](https://github.com/voxel51/fiftyone/pull/2912)

  * Added support for customizing the App [color scheme](user_guide__app.md#app-color-schemes) via a new color scheme modal [#2824](https://github.com/voxel51/fiftyone/pull/2824)

  * Added support for configuring [field visibility](user_guide__app.md#app-field-visibility) in the Appâs sidebar [#2924](https://github.com/voxel51/fiftyone/pull/2924), [#3024](https://github.com/voxel51/fiftyone/pull/3024)

  * Added support for visualizing [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields stored within top-level embedded document fields [#2885](https://github.com/voxel51/fiftyone/pull/2885)

  * Optimized App loading for datasets with large sample documents [#3139](https://github.com/voxel51/fiftyone/pull/3139)

  * Optimized App routes that involve synchronous computations [#3066](https://github.com/voxel51/fiftyone/pull/3066)

  * Fixed a URL filepath bug that could cause orthographic projections to fail to render [#3122](https://github.com/voxel51/fiftyone/pull/3122)

  * Fixed a layout bug when working with long brain keys in the Embeddings panel [#3026](https://github.com/voxel51/fiftyone/pull/3026)

  * Added a welcome message that displays when the App is launched for the first time with a new FiftyOne version [#3092](https://github.com/voxel51/fiftyone/pull/3092)




Core

  * Added support for creating [dynamic grouped views](https://docs.voxel51.com/user_guide/using_views.html#view-groups) [#2475](https://github.com/voxel51/fiftyone/pull/2475)

  * Added support for storing [default color schemes](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config-color-scheme) for datasets [#2824](https://github.com/voxel51/fiftyone/pull/2824)

  * Added support for selecting/excluding fields via dynamically defined filters via [`select_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_fields "fiftyone.core.collections.SampleCollection.select_fields") and [`exclude_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_fields "fiftyone.core.collections.SampleCollection.exclude_fields") [#2898](https://github.com/voxel51/fiftyone/pull/2898)

  * Added support for [evaluating keypoints](user_guide__evaluation.md#evaluating-detections) [#2776](https://github.com/voxel51/fiftyone/pull/2776), [#2928](https://github.com/voxel51/fiftyone/pull/2928)

  * Added support for computing DICE score when evaluating segmentations [#2777](https://github.com/voxel51/fiftyone/pull/2777), [#2901](https://github.com/voxel51/fiftyone/pull/2901)

  * Added a new [`list_schema()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_schema "fiftyone.core.collections.SampleCollection.list_schema") aggregation for inferring the contents of nested list fields [#2882](https://github.com/voxel51/fiftyone/pull/2882)

  * Added support for declaring dynamic nested list fields [#2882](https://github.com/voxel51/fiftyone/pull/2882)

  * Handling missing label fields when deleting labels [#2918](https://github.com/voxel51/fiftyone/pull/2918)

  * Only match .txt files when reading YOLO labels [#3127](https://github.com/voxel51/fiftyone/pull/3127)

  * Improved behavior of [`transform_images()`](api__fiftyone.utils.image.md#fiftyone.utils.image.transform_images "fiftyone.utils.image.transform_images") and [`transform_videos()`](api__fiftyone.utils.video.md#fiftyone.utils.video.transform_videos "fiftyone.utils.video.transform_videos") utilities when processing media in-place [#2931](https://github.com/voxel51/fiftyone/pull/2931)

  * Added utils and helpful warnings that advise how to patch broken saved views and runs [#2970](https://github.com/voxel51/fiftyone/pull/2970), [#2971](https://github.com/voxel51/fiftyone/pull/2971)

  * Replaced `pkg_resources` with `importlib.metadata` [#2930](https://github.com/voxel51/fiftyone/pull/2930)




Plugins

  * Added [Operators](plugins__using_plugins.md#using-operators) to the plugin framework [#2679](https://github.com/voxel51/fiftyone/pull/2679)

  * Added CLI methods for [plugins](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins) and [operators](https://docs.voxel51.com/cli/index.html#cli-fiftyone-operators) [#3025](https://github.com/voxel51/fiftyone/pull/3025), [#3038](https://github.com/voxel51/fiftyone/pull/3038)




Annotation

  * Added support for CVAT 2.4 [#2959](https://github.com/voxel51/fiftyone/pull/2959)

  * Added support for importing/exporting instances when using the Label Studio integration [#2706](https://github.com/voxel51/fiftyone/pull/2706), [#2917](https://github.com/voxel51/fiftyone/pull/2917)

  * Added support for importing multiclass classifications from Scale [#3117](https://github.com/voxel51/fiftyone/pull/3117)

  * Updated Scale integration to assume that imported line annotations are not closed shapes [#3123](https://github.com/voxel51/fiftyone/pull/3123)

  * Fixed broken Scale docs links and unlabeled annotation task support [#2916](https://github.com/voxel51/fiftyone/pull/2916)




Zoo

  * Added the [Sama-COCO dataset](dataset_zoo__datasets__sama_coco.md#dataset-zoo-sama-coco) to the zoo! [#2904](https://github.com/voxel51/fiftyone/pull/2904)




Tutorials

  * Updated detection mistakes tutorial to avoid unnecessarily resetting the App [#3034](https://github.com/voxel51/fiftyone/pull/3034)




## FiftyOne Enterprise 1.2.1#

_Released April 5, 2023_

Includes all features from FiftyOne 0.20.1, plus:

General

  * When your session expires, you are now automatically logged out rather than being presented with a cryptic server error

  * Improved the accuracy of size estimates when exporting filepaths and/or tags from the Enterprise UI




Admin

  * Added support for uploading Azure storage credentials for your deployment via the `Settings > Cloud storage` page




SDK

  * Added support for working with media in Azure cloud storage. Refer to [this section](enterprise__installation.md#enterprise-azure) to see how to provide your storage credentials




Deployment

  * Added support for deploying into Microsoft Azure environments

  * Fixed a bug that prevented the dataset page from loading for deployments running MongoDB 4.4




## FiftyOne 0.20.1#

_Released April 5, 2023_

App

  * Added support for storing datetimes as field metadata and viewing them in the Appâs field tooltip [#2861](https://github.com/voxel51/fiftyone/pull/2861)

  * Fixed a bug when pulling color-by data for sample embeddings plots when viewing patches in the sample grid [#2846](https://github.com/voxel51/fiftyone/pull/2846)

  * Fixed a bug that prevented the sample grid from refreshing when composing multiple sidebar filters [#2849](https://github.com/voxel51/fiftyone/pull/2849)

  * Fixed a bug that prevented field-specific mask targets from being recognized when rendering segmentations in the App [#2879](https://github.com/voxel51/fiftyone/pull/2879)

  * Fixed a bug when rendering heatmaps stored as images on disk [#2872](https://github.com/voxel51/fiftyone/pull/2872), [#2880](https://github.com/voxel51/fiftyone/pull/2880)




Core

  * Added support for dynamically inferring fields on embedded lists and documents [#2863](https://github.com/voxel51/fiftyone/pull/2863), [#2882](https://github.com/voxel51/fiftyone/pull/2882)

  * Added support for listing datasets matching a glob pattern [#2868](https://github.com/voxel51/fiftyone/pull/2868)

  * Improved the robustness of [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") when cleaning up after a failed merge [#2844](https://github.com/voxel51/fiftyone/pull/2844)

  * Using new libraries for ndjson and archive extraction [#2864](https://github.com/voxel51/fiftyone/pull/2864)

  * Fixed a bug that prevented [text similarity searches](brain.md#brain-similarity-text) from succeeding when GPU is available [#2853](https://github.com/voxel51/fiftyone/pull/2853)

  * Fixed a bug where [`stats()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.stats "fiftyone.core.collections.SampleCollection.stats") would report the wrong size for dataset views that select/exclude fields on MongoDB 5.2 or later [#2840](https://github.com/voxel51/fiftyone/pull/2840)

  * Fixed a bug with dynamic schema expansion of list fields [#2855](https://github.com/voxel51/fiftyone/pull/2855)

  * Fixed a bug when merging video samples into a grouped dataset that did not previously contain videos [#2851](https://github.com/voxel51/fiftyone/pull/2851)

  * Fixed a validation bug when importing COCO datasets whose description is not a string [#2848](https://github.com/voxel51/fiftyone/pull/2848)




Documentation

  * Updated the source URLs for the [Caltech-101](dataset_zoo__datasets__caltech101.md#dataset-zoo-caltech101) and [Caltech-256](dataset_zoo__datasets__caltech256.md#dataset-zoo-caltech256) datasets [#2841](https://github.com/voxel51/fiftyone/pull/2841)

  * Fixed a typo in the [Caltech-256](dataset_zoo__datasets__caltech256.md#dataset-zoo-caltech256) dataset documentation [#2842](https://github.com/voxel51/fiftyone/pull/2842)




## FiftyOne Enterprise 1.2#

_Released March 22, 2023_

Includes all features from FiftyOne 0.20.0, plus:

Admin settings

  * Admins who use SSO to authorize new users to auto-join their FiftyOne Enterprise deployment can now configure the [default role](enterprise__roles_and_permissions.md#enterprise-roles) for those users

  * Admins can now configure the [default access level](enterprise__roles_and_permissions.md#enterprise-default-access) that Members receive on newly created datasets Dataset page




Dataset page

  * Added support for viewing [Segmentation](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation) and [Heatmap](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) data stored as images in the cloud in the App

  * Added support for exporting one or more fields of a dataset in CSV format through the Enterprise UI

  * Stack traces for unhandled errors are now presented directly in the App so that users can self-diagnose issues




Deployment

  * Added support for sharded databases




## FiftyOne 0.20.0#

_Released March 22, 2023_

News

  * Added support for querying by [arbitrary text prompts](brain.md#brain-similarity-text) in the App! [#2633](https://github.com/voxel51/fiftyone/pull/2633)

  * Released a [Qdrant integration](integrations__qdrant.md#qdrant-integration) for native text and image searches on FiftyOne datasets!

  * Released a [Pinecone integration](integrations__pinecone.md#pinecone-integration) for native text and image searches on FiftyOne datasets!




App

  * Switched the default sidebar mode to `fast` [#2714](https://github.com/voxel51/fiftyone/pull/2714)

  * Refactored sample/label tags in the App so that they are treated the same as any other list field [#2557](https://github.com/voxel51/fiftyone/pull/2557)

  * Added support for visualizing [orthographic projection images](https://docs.voxel51.com/user_guide/using_datasets.html#orthographic-projection-images) for point cloud datasets/slices [#2660](https://github.com/voxel51/fiftyone/pull/2660)

  * Added a filter/selection indicator to the title of all Panels that can be clicked to clear the Panelâs current state [#2652](https://github.com/voxel51/fiftyone/pull/2652)

  * Any selection state associated with a Panel is now automatically cleared when the Panel is closed [#2652](https://github.com/voxel51/fiftyone/pull/2652)

  * Added a button to the saved view selector for clearing the current view [#2661](https://github.com/voxel51/fiftyone/pull/2661)

  * Added support for maximizing/hiding individual panels of the grouped modal [#2688](https://github.com/voxel51/fiftyone/pull/2688)

  * Added support for switching between multiple point cloud slices [#2675](https://github.com/voxel51/fiftyone/pull/2675)

  * Added keyboard shortcuts for opening Panels directly in split mode [#2663](https://github.com/voxel51/fiftyone/pull/2663)

  * Upgraded Looker3D controls [#2753](https://github.com/voxel51/fiftyone/pull/2753)

  * Upgraded the modalâs JSON viewer [#2677](https://github.com/voxel51/fiftyone/pull/2677)

  * Selected labels are not reset after applying a [similarity search](user_guide__app.md#app-similarity) [#2820](https://github.com/voxel51/fiftyone/pull/2820)

  * Stack traces for unhandled errors are now presented directly in the App so that users can self-diagnose issues [#2795](https://github.com/voxel51/fiftyone/pull/2795), [#2797](https://github.com/voxel51/fiftyone/pull/2797)

  * Improved error handling when loading invalid/missing brain results in the [Embeddings panel](user_guide__app.md#app-embeddings-panel) [#2651](https://github.com/voxel51/fiftyone/pull/2651), [#2790](https://github.com/voxel51/fiftyone/pull/2790)

  * More intuitive behavior when combining Embedding panel selections and sidebar filters [#2741](https://github.com/voxel51/fiftyone/pull/2741)

  * Ensure that URL is updated when loading saved views via a Python session [#2740](https://github.com/voxel51/fiftyone/pull/2740)

  * Switched to wildcard-based string matching in the sidebar [#2736](https://github.com/voxel51/fiftyone/pull/2736)

  * Plugins can now load components and utilities from runtime instead of compiling their own [#2680](https://github.com/voxel51/fiftyone/pull/2680)

  * Stability improvements when loading and handling errors in plugins [#2758](https://github.com/voxel51/fiftyone/pull/2758)

  * Informative error messages are now displayed when visualization results fail to load in the Embeddings panel [#2751](https://github.com/voxel51/fiftyone/pull/2751)

  * Resolved some edge cases when loading views with different schemas via Python sessions [#2730](https://github.com/voxel51/fiftyone/pull/2730)

  * Fixed a bug that would cause saving views to intermittently fail [#2667](https://github.com/voxel51/fiftyone/pull/2667)

  * Fixed a bug when using saved views with Python <3.9 in the App [#2676](https://github.com/voxel51/fiftyone/pull/2676), [#2728](https://github.com/voxel51/fiftyone/pull/2728)

  * Fixed a bug that could cause App crashes when loading [`SelectGroupSlices`](api__fiftyone.core.stages.md#fiftyone.core.stages.SelectGroupSlices "fiftyone.core.stages.SelectGroupSlices") stages in the view bar [#2669](https://github.com/voxel51/fiftyone/pull/2669), [#2743](https://github.com/voxel51/fiftyone/pull/2743)

  * Fixed a bug that could cause App crashes when filtering keypoints [#2774](https://github.com/voxel51/fiftyone/pull/2774), [#2779](https://github.com/voxel51/fiftyone/pull/2779)

  * Fixed a bug when lassoing patch embeddings with the Map panel open [#2754](https://github.com/voxel51/fiftyone/pull/2754)

  * Fixed inconsistencies with selection, tagging, active slices, and sidebar stats in the modal for grouped datasets [#2785](https://github.com/voxel51/fiftyone/pull/2785), [#2782](https://github.com/voxel51/fiftyone/pull/2782), [#2769](https://github.com/voxel51/fiftyone/pull/2769), [#2759](https://github.com/voxel51/fiftyone/pull/2759), [#2749](https://github.com/voxel51/fiftyone/pull/2749), [#2731](https://github.com/voxel51/fiftyone/pull/2731)

  * Fixed a bug when pressing enter twice in a label tag popover [#2757](https://github.com/voxel51/fiftyone/pull/2757)

  * Fixed a bug where keyboard listeners in the modal would interfere with other input interactions [#2786](https://github.com/voxel51/fiftyone/pull/2786)

  * Fixed a bug where some users would see erroneous scrollbars [#2794](https://github.com/voxel51/fiftyone/pull/2794)

  * Fixed bugs when tagging labels in the grouped modal [#2820](https://github.com/voxel51/fiftyone/pull/2820)

  * Fixed a bug when retrieving values for filter dropdowns in the grouped modal [#2817](https://github.com/voxel51/fiftyone/pull/2817)

  * Fixed a bug that would raise an App error after deleting certain saved views [#2801](https://github.com/voxel51/fiftyone/pull/2801)

  * Fixed the formatting of the `support` field in the modal sidebar for clip views [#2800](https://github.com/voxel51/fiftyone/pull/2800)

  * Fixed a bug with URL rendering in the sidebar [#2735](https://github.com/voxel51/fiftyone/pull/2735)

  * Fixed a bug when streaming filtered frame labels [#2682](https://github.com/voxel51/fiftyone/pull/2682), [#2733](https://github.com/voxel51/fiftyone/pull/2733)

  * Fixed a bug when adding new tags to a selected sample or label [#2703](https://github.com/voxel51/fiftyone/pull/2703)

  * Fixed a bug when matching by tags that contain spaces [#2658](https://github.com/voxel51/fiftyone/pull/2658)




Core

  * Added support for querying by vectors and text prompts [#2569](https://github.com/voxel51/fiftyone/pull/2569)

  * Upgraded the [similarity index interface](brain.md#brain-similarity), including [Qdrant](integrations__qdrant.md#qdrant-integration) and [Pinecone](integrations__pinecone.md#pinecone-integration) support, and the ability to add/remove embeddings to an existing index [#2792](https://github.com/voxel51/fiftyone/pull/2792)

  * Added support for storing and visualizing cuboids and rotated bounding boxes in the App [#2296](https://github.com/voxel51/fiftyone/pull/2296)

  * Added support for [evaluating](user_guide__evaluation.md#evaluating-detections) 3D object detections [#2486](https://github.com/voxel51/fiftyone/pull/2486)

  * Added a [`to_trajectories()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_trajectories "fiftyone.core.collections.SampleCollection.to_trajectories") view stage [#1300](https://github.com/voxel51/fiftyone/pull/1300)

  * Added support for generating [orthographic projection images](https://docs.voxel51.com/user_guide/using_datasets.html#orthographic-projection-images) for point cloud datasets/slices [#2656](https://github.com/voxel51/fiftyone/pull/2656)

  * Added validation to [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#2770](https://github.com/voxel51/fiftyone/pull/2770)

  * Frame collections are now lazily created only when necessary [#2727](https://github.com/voxel51/fiftyone/pull/2727)

  * Upgraded the document save implementation to only use upsert operations when explicitly required [#2727](https://github.com/voxel51/fiftyone/pull/2727)

  * Added `_dataset_id` to all sample/frame documents in datasets [#2711](https://github.com/voxel51/fiftyone/pull/2711)

  * Added a [`save()`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults.save "fiftyone.core.runs.RunResults.save") and [`save_config()`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults.save_config "fiftyone.core.runs.RunResults.save_config") methods to [`RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults") [#2696](https://github.com/voxel51/fiftyone/pull/2696), [#2772](https://github.com/voxel51/fiftyone/pull/2772)

  * Added support for renaming existing runs via new [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run"), [`rename_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_brain_run "fiftyone.core.collections.SampleCollection.rename_brain_run"), and [`rename_evaluation()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_evaluation "fiftyone.core.collections.SampleCollection.rename_evaluation") methods [#2696](https://github.com/voxel51/fiftyone/pull/2696)

  * Added support for filtering by run type and config parameters when using [`list_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_annotation_runs "fiftyone.core.collections.SampleCollection.list_annotation_runs"), [`list_brain_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_brain_runs "fiftyone.core.collections.SampleCollection.list_brain_runs"), and [`list_evaluations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_evaluations "fiftyone.core.collections.SampleCollection.list_evaluations") [#2696](https://github.com/voxel51/fiftyone/pull/2696), [#2772](https://github.com/voxel51/fiftyone/pull/2772)

  * Added an [`add_group_slice()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_group_slice "fiftyone.core.dataset.Dataset.add_group_slice") method to declare new slices on grouped datasets [#2727](https://github.com/voxel51/fiftyone/pull/2727)

  * Added support for controlling whether saved views and runs are imported/exported in [FiftyOneDataset format](user_guide__import_datasets.md#fiftyonedataset-import) [#2806](https://github.com/voxel51/fiftyone/pull/2806)

  * Added support for negative integer mask targets [#2686](https://github.com/voxel51/fiftyone/pull/2686)

  * Downward migrations for future-but-compatible versions of FiftyOne are now skipped rather than raising an error [#2683](https://github.com/voxel51/fiftyone/pull/2683)

  * Fixed a bug when cloning datasets with run results [#2772](https://github.com/voxel51/fiftyone/pull/2772)

  * Fixed a bug with the `dynamic=True` syntax for declaring dynamic fields on list documents [#2767](https://github.com/voxel51/fiftyone/pull/2767)

  * Fixed a bug in deferred saves where filtered list updates were not being applied [#2727](https://github.com/voxel51/fiftyone/pull/2727)




Annotation

  * Added support for passing CVAT organization to annotation jobs [#2716](https://github.com/voxel51/fiftyone/pull/2716)




Docs

  * Added [documentation](https://docs.voxel51.com/user_guide/using_datasets.html#point-cloud-datasets) for working with point cloud-only datasets [#2724](https://github.com/voxel51/fiftyone/pull/2724)

  * Added [documentation](https://docs.voxel51.com/user_guide/using_datasets.html#custom-embedded-documents) for on-the-fly custom embedded document creation [#2687](https://github.com/voxel51/fiftyone/pull/2687)

  * Fixed broken torchvision dataset links in the docs [#2771](https://github.com/voxel51/fiftyone/pull/2771)




Zoo

  * Added a `tensorflow-macos` option when loading TF models from the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) [#2685](https://github.com/voxel51/fiftyone/pull/2685)




Tutorials

  * Added a [Point-E tutorial](tutorials__pointe.md) showcasing the 3D Visualizerâs capabilities in the context of building a 3D self-driving dataset [#2818](https://github.com/voxel51/fiftyone/pull/2818)

  * Added a [YOLOv8 tutorial](tutorials__yolov8.md) [#2755](https://github.com/voxel51/fiftyone/pull/2755)

  * Updated the media in the [Open Images tutorial](tutorials__open_images.md) [#2665](https://github.com/voxel51/fiftyone/pull/2665)




## FiftyOne Enterprise 1.1.1#

_Released February 14, 2023_

Includes all features from FiftyOne 0.19.1, plus:

Plugins

  * Resolved a bug that prevented Enterprise deployments from recognizing installed plugins




## FiftyOne 0.19.1#

_Released February 14, 2023_

App

  * Fixed a bug when launching the App in Python 3.8 or earlier [#2647](https://github.com/voxel51/fiftyone/pull/2647)

  * Fixed a bug that prevented launching the App in Databricks notebooks [#2647](https://github.com/voxel51/fiftyone/pull/2647)




Core

  * Fixed a bug in certain environments that prevented progress bars from rendering correctly [#2647](https://github.com/voxel51/fiftyone/pull/2647)




## FiftyOne Enterprise 1.1#

_Released February 9, 2023_

Includes all features from FiftyOne 0.19.0, plus:

User roles

  * Renamed the existing Guest role to [Collaborator](https://docs.voxel51.com/enterprise/roles_and_permissions.html#collaborator)

  * Added a new [Guest](https://docs.voxel51.com/enterprise/roles_and_permissions.html#guest) role




Homepage

  * Added a Recent views widget to the homepage that shows the most recent saved views that you have viewed in the Enterprise UI




Dataset page

  * Added support for cloning the current view (including any filters, selections, etc) into a new dataset from the UI

  * Added support for exporting the current view to local disk or a cloud bucket in various formats (filepaths only, filepaths and tags, media only, labels only, media and labels)




Deployment

  * Added support for deploying Enterprise into environments with proxy networks




## FiftyOne 0.19.0#

_Released February 9, 2023_

News

  * [FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise) documentation is now publicly available! [#2388](https://github.com/voxel51/fiftyone/pull/2388)




App

  * Added the [Spaces framework](user_guide__app.md#app-spaces) [#2524](https://github.com/voxel51/fiftyone/pull/2524)

  * Added native support for [visualizing embeddings](user_guide__app.md#app-embeddings-panel) [#2524](https://github.com/voxel51/fiftyone/pull/2524)

  * Refactored the map tab into a dedicated [map panel](user_guide__app.md#app-map-panel) [#2524](https://github.com/voxel51/fiftyone/pull/2524)

  * Refactored the histograms tab into a dedicated [histograms panel](user_guide__app.md#app-histograms-panel) [#2524](https://github.com/voxel51/fiftyone/pull/2524)

  * Added support for [loading and saving views](user_guide__app.md#app-saving-views) [#2461](https://github.com/voxel51/fiftyone/pull/2461)

  * Added support for visualizing [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") and [`Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap") masks stored on disk [#2358](https://github.com/voxel51/fiftyone/pull/2358)

  * Added support for visualizing RGB segmentations [#2483](https://github.com/voxel51/fiftyone/pull/2483)

  * Added retries for all network requests to improve stability [#2406](https://github.com/voxel51/fiftyone/pull/2406)

  * Optimized the tagging menu [#2368](https://github.com/voxel51/fiftyone/pull/2368)

  * Optimized sample tagging on video datasets [#2440](https://github.com/voxel51/fiftyone/pull/2440)

  * Donât refresh the background grid when applying tags in the modal [#2594](https://github.com/voxel51/fiftyone/pull/2594)

  * Only show supported keys in the evaluations dropdown [#2427](https://github.com/voxel51/fiftyone/pull/2427)

  * Fixed handling of None values when filtering numeric/list fields [#2422](https://github.com/voxel51/fiftyone/pull/2422), [#2412](https://github.com/voxel51/fiftyone/pull/2412), [#2403](https://github.com/voxel51/fiftyone/pull/2403)

  * Never show expanded filter list for ID fields [#2408](https://github.com/voxel51/fiftyone/pull/2408)

  * Ensure that the bookmark icon displays when extended selections exist [#2366](https://github.com/voxel51/fiftyone/pull/2366)

  * Automatically clear sample selection after [sorting by similarity](user_guide__app.md#app-similarity) [#2595](https://github.com/voxel51/fiftyone/pull/2595)

  * Use consistent loading dots throughout the App [#2321](https://github.com/voxel51/fiftyone/pull/2321)

  * Fixed a bug when filtering by custom embedded list fields [#2407](https://github.com/voxel51/fiftyone/pull/2407)

  * Fixed bugs when screenshotting the App in notebook contexts [#2398](https://github.com/voxel51/fiftyone/pull/2398)

  * Fixed bugs when launching the App in Databricks notebooks [#2397](https://github.com/voxel51/fiftyone/pull/2397)

  * Show metadata for frame-level fields in the fields tooltip [#2386](https://github.com/voxel51/fiftyone/pull/2386)

  * Fixed bugs when configuring plugin settings and modal media fields [#2383](https://github.com/voxel51/fiftyone/pull/2383)

  * Fixed bugs with multiple media fields when loading views that exclude fields [#2378](https://github.com/voxel51/fiftyone/pull/2378), [#2303](https://github.com/voxel51/fiftyone/pull/2303)




Core

  * Added support for programmatically [configuring space layouts](user_guide__app.md#app-spaces-python) [#2524](https://github.com/voxel51/fiftyone/pull/2524)

  * Added support for [loading and saving views](https://docs.voxel51.com/user_guide/using_views.html#saving-views) [#2461](https://github.com/voxel51/fiftyone/pull/2461)

  * Added support for storing [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") and [`Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap") masks on disk [#2301](https://github.com/voxel51/fiftyone/pull/2301)

  * Added support for RGB segmentations in [`evaluate_segmentations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_segmentations "fiftyone.core.collections.SampleCollection.evaluate_segmentations") [#2483](https://github.com/voxel51/fiftyone/pull/2483)

  * Added a new [`transform_segmentations()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.transform_segmentations "fiftyone.utils.labels.transform_segmentations") utility [#2483](https://github.com/voxel51/fiftyone/pull/2483)

  * Added support for declaring dynamic fields on generated views via [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#2513](https://github.com/voxel51/fiftyone/pull/2513)

  * Added support for [importing](user_guide__import_datasets.md#csvdataset-import) and [exporting](user_guide__export_datasets.md#csvdataset-export) datasets in CSV format [#2616](https://github.com/voxel51/fiftyone/pull/2616), [#2450](https://github.com/voxel51/fiftyone/pull/2450)

  * Added support for [importing](user_guide__import_datasets.md#mediadirectory-import) and [exporting](user_guide__export_datasets.md#mediadirectory-export) directories of arbitrary media files [#2605](https://github.com/voxel51/fiftyone/pull/2605)

  * Added a dedicated [`clear_cache()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clear_cache "fiftyone.core.dataset.Dataset.clear_cache") method for clearing a datasetâs run cache [#2471](https://github.com/voxel51/fiftyone/pull/2471)

  * Updated all plotting methods, eg [`scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.scatterplot "fiftyone.core.plots.base.scatterplot") to always rely on sample/label IDs when pulling data for plots [#2614](https://github.com/voxel51/fiftyone/pull/2614)

  * Updated [`compute_patch_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_patch_embeddings "fiftyone.core.collections.SampleCollection.compute_patch_embeddings") to store patch embeddings directly on [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") objects when the `embeddings_field` argument is provided [#2626](https://github.com/voxel51/fiftyone/pull/2626)

  * Added support for passing frame-level fields directly to [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") [#2418](https://github.com/voxel51/fiftyone/pull/2418)

  * Added an optional `dynamic=True` flag to [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#2372](https://github.com/voxel51/fiftyone/pull/2372)

  * Added support for declaring custom [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") attributes via [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#2372](https://github.com/voxel51/fiftyone/pull/2372)

  * Adds a new [`set_label_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_label_values "fiftyone.core.collections.SampleCollection.set_label_values") utility for setting attributes on [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances by their IDs [#2372](https://github.com/voxel51/fiftyone/pull/2372)

  * Always update datasetâs `last_loaded_at` property when they are loaded [#2375](https://github.com/voxel51/fiftyone/pull/2375)

  * Migrated runs to a separate database collection, for efficiency [#2189](https://github.com/voxel51/fiftyone/pull/2189)

  * Added an [`exact_frame_count()`](api__fiftyone.utils.video.md#fiftyone.utils.video.exact_frame_count "fiftyone.utils.video.exact_frame_count") utility for computing exact video frame counts [#2373](https://github.com/voxel51/fiftyone/pull/2373)

  * Updated the [3D visualizer](https://docs.voxel51.com/user_guide/using_datasets.html#d-detections) to use true centroid (not bottom-center) coordinates for 3D detections [#2474](https://github.com/voxel51/fiftyone/pull/2474)

  * Added support for loading specific group slice(s) when using [`iter_groups()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.iter_groups "fiftyone.core.collections.SampleCollection.iter_groups") and [`get_group()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_group "fiftyone.core.collections.SampleCollection.get_group") [#2528](https://github.com/voxel51/fiftyone/pull/2528)

  * Added an [`exclude_groups()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_groups "fiftyone.core.collections.SampleCollection.exclude_groups") view stage [#2451](https://github.com/voxel51/fiftyone/pull/2451)

  * Added support for importing annotations directly on grouped datasets [#2349](https://github.com/voxel51/fiftyone/pull/2349)

  * Added a [`group_collections()`](api__fiftyone.utils.groups.md#fiftyone.utils.groups.group_collections "fiftyone.utils.groups.group_collections") utility for merging multiple collections into a grouped dataset [#2332](https://github.com/voxel51/fiftyone/pull/2332)

  * Added support for converting an existing dataset into a grouped dataset via [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") [#2332](https://github.com/voxel51/fiftyone/pull/2332)

  * Added support for deleting grouped fields when the dataset contains only one media type [#2332](https://github.com/voxel51/fiftyone/pull/2332)

  * Updated [`Dataset.stats()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.stats "fiftyone.core.dataset.Dataset.stats") to include media from all slices of grouped datasets [#2635](https://github.com/voxel51/fiftyone/pull/2635)

  * Fixed a bug when calling [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames") on a view that filters the frames of the input dataset [#2361](https://github.com/voxel51/fiftyone/pull/2361)

  * Fixed some bugs when passing multiple aggregations with the same field name and type to [`aggregate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.aggregate "fiftyone.core.collections.SampleCollection.aggregate") [#2617](https://github.com/voxel51/fiftyone/pull/2617)

  * Fixed a bug when manually unwinding list fields in aggregations [#2608](https://github.com/voxel51/fiftyone/pull/2608)

  * Fixed a bug when loading datasets with CVAT attributes stored in [VOC format](user_guide__import_datasets.md#vocdetectiondataset-import) [#2359](https://github.com/voxel51/fiftyone/pull/2359)

  * Fixed a bug in default sidebar group expansion [#2441](https://github.com/voxel51/fiftyone/pull/2441)




Annotation

  * Added support for CVAT 2.4 [#2597](https://github.com/voxel51/fiftyone/pull/2597)

  * Added support for providing custom task names for CVAT tasks [#2353](https://github.com/voxel51/fiftyone/pull/2353)

  * Fixed a bug when checking if CVAT projects exist [#2491](https://github.com/voxel51/fiftyone/pull/2491)

  * Fixed a bug when checking if CVAT tasks exist [#2070](https://github.com/voxel51/fiftyone/pull/2070)




Zoo

  * Added [Open Images V7](dataset_zoo__datasets__open_images_v7.md#dataset-zoo-open-images-v7) to the zoo [#2446](https://github.com/voxel51/fiftyone/pull/2446)

  * Updated the [KITTI multiview](dataset_zoo__datasets__kitti_multiview.md#dataset-zoo-kitti-multiview) and [quickstart-groups](dataset_zoo__datasets__quickstart_groups.md#dataset-zoo-quickstart-groups) datasets to not use legacy 3D visualizer settings [#2474](https://github.com/voxel51/fiftyone/pull/2474)

  * Added support for filtering datasets when using [`list_zoo_datasets()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.list_zoo_datasets "fiftyone.zoo.datasets.list_zoo_datasets") [#2448](https://github.com/voxel51/fiftyone/pull/2448)




Docs

  * Added detailed [plugin documentation](plugins__overview.md#fiftyone-plugins) [#2442](https://github.com/voxel51/fiftyone/pull/2442)

  * Added [documentation](https://docs.voxel51.com/user_guide/using_datasets.html#label-conversions) for converting between common label formats [#2498](https://github.com/voxel51/fiftyone/pull/2498)

  * Added a [pandas vs FiftyOne](tutorials__pandas_comparison.md) tutorial [#2310](https://github.com/voxel51/fiftyone/pull/2310)

  * Added a [pandas vs FiftyOne](cheat_sheets__pandas_vs_fiftyone.md#pandas-cheat-sheet) cheat sheet [#2329](https://github.com/voxel51/fiftyone/pull/2329)

  * Added a [FiftyOne terminology](cheat_sheets__fiftyone_terminology.md#terminology-cheat-sheet) cheat sheet [#2484](https://github.com/voxel51/fiftyone/pull/2484)

  * Added a [view stage](cheat_sheets__views_cheat_sheet.md#views-cheat-sheet) cheat sheet [#2452](https://github.com/voxel51/fiftyone/pull/2452)

  * Added a [filtering](cheat_sheets__filtering_cheat_sheet.md#filtering-cheat-sheet) cheat sheet [#2447](https://github.com/voxel51/fiftyone/pull/2447)




## FiftyOne Enterprise 1.0#

_Released November 8, 2022_

Includes all features from FiftyOne 0.18.0, plus:

News

  * FiftyOne Enterprise is now generally available, [read more here](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise)!




## FiftyOne 0.18.0#

_Released November 8, 2022_

App

  * Significantly optimized the performance of the sidebar by lazily computing statistics only for currently visible fields [#2191](https://github.com/voxel51/fiftyone/pull/2191)

  * Added new sidebar modes with updated default behavior that further optimizes the performance of the App for large datasets [#2191](https://github.com/voxel51/fiftyone/pull/2191)

  * Added support for configuring the sidebar mode dynamically in the App and programmatically on a per-dataset basis [#2191](https://github.com/voxel51/fiftyone/pull/2191)

  * Added support for programmatically configuring [sidebar groups](user_guide__app.md#app-sidebar-groups) and default expansion states on a per-dataset basis [#2190](https://github.com/voxel51/fiftyone/pull/2190)

  * Added support for viewing field-level descriptions via a new [field tooltip](user_guide__app.md#app-fields-sidebar) [#2216](https://github.com/voxel51/fiftyone/pull/2216)

  * Added support for filtering by and viewing stats for custom embedded document attributes [#1825](https://github.com/voxel51/fiftyone/pull/1825)

  * Added a new light mode option! [#2156](https://github.com/voxel51/fiftyone/pull/2156)

  * Improved responsiveness of the sidebar when toggling fields on and off [#2247](https://github.com/voxel51/fiftyone/pull/2247)

  * Improved responsiveness and state management of the view bar [#2230](https://github.com/voxel51/fiftyone/pull/2230)

  * Restored the ability to shift-select multiple samples in the grid view [#2110](https://github.com/voxel51/fiftyone/issues/2110)

  * Fixed an issue that could cause unselected label fields to be inadvertently tagged when using the label tagging UI [#2121](https://github.com/voxel51/fiftyone/issues/2121)

  * Fixed an issue that would prevent label tags applied on patch views in the tagging UI from persisting to the underlying dataset [#2113](https://github.com/voxel51/fiftyone/issues/2113)

  * Fixed an issue that could arise when loading a group dataset with sparse alternate media fields [#2164](https://github.com/voxel51/fiftyone/issues/2164)

  * Fixed some issues with datetime rendering and timezone handling [#2111](https://github.com/voxel51/fiftyone/issues/2111), [#2112](https://github.com/voxel51/fiftyone/issues/2112)




Core

  * Added support for declaring [custom dynamic attributes](https://docs.voxel51.com/user_guide/using_datasets.html#dynamic-attributes) on datasets! [#1825](https://github.com/voxel51/fiftyone/pull/1825)

  * Added support for storing [field-level metadata](https://docs.voxel51.com/user_guide/using_datasets.html#storing-field-metadata) on datasets [#2216](https://github.com/voxel51/fiftyone/pull/2216)

  * Added native support for installing on Apple Silicon with MongoDB 6 [#2165](https://github.com/voxel51/fiftyone/pull/2165)

  * Dataset creation using default naming is now multiprocess-safe [#2097](https://github.com/voxel51/fiftyone/pull/2097)

  * Optimized the implementation of tagging samples and labels [#2203](https://github.com/voxel51/fiftyone/pull/2203), [#2208](https://github.com/voxel51/fiftyone/pull/2208)

  * Optimized the implementation of [`select()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select "fiftyone.core.collections.SampleCollection.select"), [`select_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_by "fiftyone.core.collections.SampleCollection.select_by"), and [`select_groups()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_groups "fiftyone.core.collections.SampleCollection.select_groups") when performing ordered selections [#2227](https://github.com/voxel51/fiftyone/pull/2227)

  * Updated the logic of [`exists()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exists "fiftyone.core.collections.SampleCollection.exists") to be more intuitive for frame fields [#2209](https://github.com/voxel51/fiftyone/pull/2209)

  * Upgraded server and MongoDB requirements to `pymongo>=3.11`, `motor>=2.3` and newer pinned versions of `mongoengine`, `starlette`, and `strawberry-graphql` [#2215](https://github.com/voxel51/fiftyone/pull/2215)

  * Added support for modifying the filepaths of a frame view [#2193](https://github.com/voxel51/fiftyone/pull/2193)

  * Improved the implementation of [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") and related methods to safely cleanup in case of failed merges [#2135](https://github.com/voxel51/fiftyone/pull/2135)

  * Fixed some bugs that could occur when creating frame views into grouped collections [#2144](https://github.com/voxel51/fiftyone/pull/2144)

  * Fixed a bug when using [`select_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_by "fiftyone.core.collections.SampleCollection.select_by") with `ObjectId` fields [#2140](https://github.com/voxel51/fiftyone/pull/2140)

  * Added an option to import annotation IDs when loading data stored in [COCO format](user_guide__import_datasets.md#cocodetectiondataset-import) [#2122](https://github.com/voxel51/fiftyone/pull/2122)

  * Added support for including the export directory in the `dataset.yaml` file generated by [YOLOv5 exports](user_guide__export_datasets.md#yolov5dataset-export) [#2114](https://github.com/voxel51/fiftyone/pull/2114)




Annotation

  * Updated the default CVAT endpoint to <https://app.cvat.ai> [#2228](https://github.com/voxel51/fiftyone/pull/2228)

  * Fixed a bug that would cause annotation runs involving unlabeled samples to crash when using the Label Studio backend [#2145](https://github.com/voxel51/fiftyone/pull/2145)




Zoo

  * Added support for using CUDA devices when running the [CLIP model](model_zoo__models__clip_vit_base32_torch.md#model-zoo-clip-vit-base32-torch) from the zoo [#2201](https://github.com/voxel51/fiftyone/pull/2201)




## FiftyOne 0.17.2#

_Released September 20, 2022_

App

  * Fixed a backward compatibility bug when connecting to older database versions [#2103](https://github.com/voxel51/fiftyone/pull/2103)




## FiftyOne 0.17.1#

_Released September 20, 2022_

Core

  * Removed `TypedDict` usage introduced in v0.17.0 that is not supported in Python 3.7 [#2100](https://github.com/voxel51/fiftyone/pull/2100)




## FiftyOne 0.17.0#

_Released September 19, 2022_

App

  * Added support for [visualizing grouped datasets](https://docs.voxel51.com/user_guide/groups.html#groups-app) in the App [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added support for [visualizing point cloud samples](user_guide__app.md#app-3d-visualizer) in the modal [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added support for visualizing and interacting with [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") data in a new [Map panel](user_guide__app.md#app-map-panel) [#1976](https://github.com/voxel51/fiftyone/pull/1976)

  * Added initial support for [custom App plugins](plugins__overview.md#fiftyone-plugins) [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added support for configuring [multiple media fields](user_guide__app.md#app-multiple-media-fields) [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Fixed Google Colab screenshotting and cell updates [#2069](https://github.com/voxel51/fiftyone/pull/2069)




Core

  * Added support for [grouped datasets](https://docs.voxel51.com/user_guide/groups.html#groups), e.g., multiple camera view scenes [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added support for point cloud samples in grouped datasets [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added an [`app_config`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.app_config "fiftyone.core.dataset.Dataset.app_config") property to datasets for [configuring App behavior](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config) on a per-dataset basis [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added an optional `rel_dir` parameter to [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") and [`draw_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.draw_labels "fiftyone.core.collections.SampleCollection.draw_labels") [#2060](https://github.com/voxel51/fiftyone/pull/2060)

  * Added an optional `abs_paths=True` option to [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") [#2060](https://github.com/voxel51/fiftyone/pull/2060)

  * Added an optional `use_dirs=True` parameter to [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") that causes metadata to be exported in per-sample/frame JSON files [#2028](https://github.com/voxel51/fiftyone/pull/2028)

  * Updated the [COCO importer](user_guide__import_datasets.md#cocodetectiondataset-import) to load all available label types by default [#1869](https://github.com/voxel51/fiftyone/pull/1869)

  * Fixed a bug when passing `ordered=True` to [`select_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_by "fiftyone.core.collections.SampleCollection.select_by") [#2059](https://github.com/voxel51/fiftyone/pull/2059)

  * Fixed an error that would occur when storing [custom embedded documents](https://docs.voxel51.com/user_guide/using_datasets.html#custom-embedded-documents) on dynamic label attributes [#2051](https://github.com/voxel51/fiftyone/pull/2051)

  * Fixed a [`match_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_frames "fiftyone.core.collections.SampleCollection.match_frames") bug that caused all frames to be included, even if the view filters the frames [#2029](https://github.com/voxel51/fiftyone/pull/2029)




Docs

  * Added a [tutorial](tutorials__detectron2.md) showing how to integrate FiftyOne into a Detectron2 model training pipeline [#2054](https://github.com/voxel51/fiftyone/pull/2054)




Annotation

  * Fixed a bug that occurred when checking if tasks exist on CVAT v2 servers [#2070](https://github.com/voxel51/fiftyone/pull/2070)

  * Fixed an error that occurred when deserializing Label Studio annotation results [#2074](https://github.com/voxel51/fiftyone/pull/2074)




Zoo

  * Added [clip-vit-base32-torch](model_zoo__models__clip_vit_base32_torch.md#model-zoo-clip-vit-base32-torch) to the model zoo! [#2072](https://github.com/voxel51/fiftyone/pull/2072)

  * Added the [Quickstart Groups dataset](dataset_zoo__datasets__quickstart_groups.md#dataset-zoo-quickstart-groups) to the dataset zoo! [#1765](https://github.com/voxel51/fiftyone/pull/1765)

  * Added the [KITTI Multiview dataset](dataset_zoo__datasets__kitti_multiview.md#dataset-zoo-kitti-multiview) to the dataset zoo! [#1765](https://github.com/voxel51/fiftyone/pull/1765)




## FiftyOne 0.16.6#

_Released August 25, 2022_

App

  * Fixed a bug that caused the App to break when sample tags contained `.` [#1924](https://github.com/voxel51/fiftyone/pull/1924)

  * Fixed search results alignment [#1930](https://github.com/voxel51/fiftyone/pull/1930)

  * Fixed App refreshes after view changes had occurred from the view bar [#1931](https://github.com/voxel51/fiftyone/pull/1931)

  * Fixed mask targets rendering in the tooltip [#1943](https://github.com/voxel51/fiftyone/pull/1943) [#1949](https://github.com/voxel51/fiftyone/pull/1949)

  * Fixed classification confusion matrix connections [#1967](https://github.com/voxel51/fiftyone/pull/1967)




Core

  * Added [save contexts](https://docs.voxel51.com/user_guide/using_datasets.html#save-contexts), which enable efficient batch edits of datasets and views [#1727](https://github.com/voxel51/fiftyone/pull/1727)

  * Added Plotly v5 support [#1981](https://github.com/voxel51/fiftyone/pull/1981)

  * Added a [quantiles aggregation](https://docs.voxel51.com/user_guide/using_aggregations.html#aggregations-quantiles) [#1937](https://github.com/voxel51/fiftyone/pull/1937)

  * Added support for writing transformed images/videos to new locations in the [`transform_images()`](api__fiftyone.utils.image.md#fiftyone.utils.image.transform_images "fiftyone.utils.image.transform_images") and [`transform_videos()`](api__fiftyone.utils.video.md#fiftyone.utils.video.transform_videos "fiftyone.utils.video.transform_videos") functions [#2007](https://github.com/voxel51/fiftyone/pull/2007)

  * Added support for configuring the [package-wide logging level](user_guide__config.md#configuring-fiftyone) [#2009](https://github.com/voxel51/fiftyone/pull/2009)

  * Added more full-featured support for serializing and deserializing datasets, views, and samples via `to_dict()` and `from_dict()` [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Added support for dynamic attributes when performing coerced exports [#1993](https://github.com/voxel51/fiftyone/pull/1993)

  * Introduced the notion of client compatibility versions [#2017](https://github.com/voxel51/fiftyone/pull/2017)

  * Extended [`stats()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to all sample collections [#1940](https://github.com/voxel51/fiftyone/pull/1940)

  * Added support for serializing aggregations [#1911](https://github.com/voxel51/fiftyone/pull/1911)

  * Added [`weighted_sample()`](api__fiftyone.utils.random.md#fiftyone.utils.random.weighted_sample "fiftyone.utils.random.weighted_sample") and [`balanced_sample()`](api__fiftyone.utils.random.md#fiftyone.utils.random.balanced_sample "fiftyone.utils.random.balanced_sample") utility methods [#1925](https://github.com/voxel51/fiftyone/pull/1925)

  * Added an optional `new_ids=True` option to [`Dataset.add_collection()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_collection "fiftyone.core.dataset.Dataset.add_collection") that generates new sample/frame IDs when adding the samples [#1927](https://github.com/voxel51/fiftyone/pull/1927)

  * Added support for the `path` variable in `dataset.yaml` of [YOLOv5 datasets](user_guide__import_datasets.md#yolov5dataset-import) [#1903](https://github.com/voxel51/fiftyone/issues/1903)

  * Fixed a bug that prevented using [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") to set frame-level label fields [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed automatic declaration of frame fields when computing embeddings on a frame view [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed a regression that caused label ID fields to be returned as `ObjectID` [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed a bug that allowed default frame fields to be excluded [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * [`ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView") instances will now report their `metadata` type as [`VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed [`load_evaluation_view()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.load_evaluation_view "fiftyone.core.dataset.Dataset.load_evaluation_view") when `select_fields` is `True` [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed boolean field parsing when declaring fields [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed a bug that caused nested embedded documents to corrupt datasets [#1922](https://github.com/voxel51/fiftyone/pull/1922)

  * Fixed a bug that prevented assignment of array-valued dynamic attributes to labels [#1922](https://github.com/voxel51/fiftyone/pull/1922)




Annotation

  * Added a new [Label Studio integration!](integrations__labelstudio.md#label-studio-integration) [#1848](https://github.com/voxel51/fiftyone/pull/1848)

  * Optimized loading CVAT annotations and performing operations on [`CVATAnnotationResults`](api__fiftyone.utils.cvat.md#fiftyone.utils.cvat.CVATAnnotationResults "fiftyone.utils.cvat.CVATAnnotationResults") [#1944](https://github.com/voxel51/fiftyone/pull/1944)

  * Upgraded the [`AnnotationAPI`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationAPI "fiftyone.utils.annotations.AnnotationAPI") interface [#1997](https://github.com/voxel51/fiftyone/pull/1997)

  * Fixed loading group IDs in CVAT video tasks [#1917](https://github.com/voxel51/fiftyone/pull/1917)

  * Fixed uploading to a CVAT project when no label schema is provided [#1926](https://github.com/voxel51/fiftyone/pull/1926)




## FiftyOne 0.16.5#

_Released June 24, 2022_

App

  * Fixed dataset selection searches [#1907](https://github.com/voxel51/fiftyone/pull/1907)

  * Fixed dataset results for long dataset names [#1907](https://github.com/voxel51/fiftyone/pull/1907)




## FiftyOne 0.16.4#

_Released June 21, 2022_

App

  * Fixed frame fields omission in the sidebar [#1899](https://github.com/voxel51/fiftyone/pull/1899)




## FiftyOne 0.16.3#

_Released June 20, 2022_

App

  * Added hotkey to hide overlays while pressed [#1779](https://github.com/voxel51/fiftyone/pull/1779)

  * Changed expanded view ESC sequence to reset zoom before frame scrubbing [#1810](https://github.com/voxel51/fiftyone/pull/1810)

  * Fixed the expanded view tooltip when a keypoint has `nan` point(s) [#1828](https://github.com/voxel51/fiftyone/pull/1828)

  * Fixed initial loading of keypoint skeletons [#1828](https://github.com/voxel51/fiftyone/pull/1828)

  * Fixed [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") rendering in the grid [#1828](https://github.com/voxel51/fiftyone/pull/1828)

  * Fixed App loads for environments with old (`<=v0.14.0`) datasets that have yet to be migrated [#1829](https://github.com/voxel51/fiftyone/pull/1829)

  * Fixed spurious loading states from tagging in the expanded view [#1834](https://github.com/voxel51/fiftyone/pull/1834)

  * Fixed a bug that caused frame classifications to be incorrectly rendered in the grid [#1877](https://github.com/voxel51/fiftyone/pull/1877)

  * Fixed active (checked) field persistence in the grid when changing views [#1878](https://github.com/voxel51/fiftyone/pull/1878)

  * Fixed views and actions that contain `BSON` [#1879](https://github.com/voxel51/fiftyone/pull/1879)

  * Fixed `JSON` rendering in the expanded view for nested data [#1880](https://github.com/voxel51/fiftyone/pull/1880)

  * Fixed selection and expansion for bad media files [#1882](https://github.com/voxel51/fiftyone/pull/1882)

  * Fixed `Other` plot tab `date` and `datetime` fields with `None` values [#1817](https://github.com/voxel51/fiftyone/pull/1817)

  * Increased results from 10 to 200 for search selectors [#1875](https://github.com/voxel51/fiftyone/pull/1875)

  * Fixed App issues related to dataset deletion and dataset schema changes [#1875](https://github.com/voxel51/fiftyone/pull/1875)




Core

  * Added `skeleton` and `skeleton_key` to the OpenLABEL [image](user_guide__import_datasets.md#openlabelimagedataset-import) and [video](user_guide__import_datasets.md#openlabelvideodataset-import) importers [#1812](https://github.com/voxel51/fiftyone/pull/1812)

  * Fixed a database field issue in [`clone_frame_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_frame_field "fiftyone.core.dataset.Dataset.clone_frame_field") and [`clone_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_sample_field "fiftyone.core.dataset.Dataset.clone_sample_field"), [#1824](https://github.com/voxel51/fiftyone/pull/1824)

  * Fixed using zoo models with the newest version of Torchvision [#1838](https://github.com/voxel51/fiftyone/pull/1838)

  * Added [`classifications_to_detections()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.classifications_to_detections "fiftyone.utils.labels.classifications_to_detections") for converting classifications to detections [#1842](https://github.com/voxel51/fiftyone/pull/1842)

  * Set forking as the default for macOS multiprocessing [#1844](https://github.com/voxel51/fiftyone/pull/1844)

  * Added [`dataset.tags`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.tags "fiftyone.core.dataset.Dataset.tags") for organizing datasets [#1845](https://github.com/voxel51/fiftyone/pull/1845)

  * Added functionality to explicitly define classes for evaluation methods [#1858](https://github.com/voxel51/fiftyone/pull/1858)

  * Fixed `tfrecord` shard enumeration, i.e. zero indexing [#1859](https://github.com/voxel51/fiftyone/pull/1859)

  * Added support for label field dicts when importing labeled datasets [#1864](https://github.com/voxel51/fiftyone/pull/1864)

  * Removed non-XML or non-TXT files from CVAT, KITTI, CVATVideo [#1884](https://github.com/voxel51/fiftyone/pull/1884)




Annotation

  * Updated CVAT task and project processing [#1839](https://github.com/voxel51/fiftyone/pull/1839)

  * Added the ability to upload and download group ids from CVAT [#1876](https://github.com/voxel51/fiftyone/pull/1876)




## FiftyOne 0.16.2#

_Released June 2, 2022_

App

  * Added explicit error handling when `FFmpeg` is installed so it is made clear to the user that it must be installed to use video datasets in the App [#1801](https://github.com/voxel51/fiftyone/pull/1801)

  * Fixed range requests for media files, e.g. mp4s, on the server [#1786](https://github.com/voxel51/fiftyone/pull/1786)

  * Fixed tag rendering in the grid [#1808](https://github.com/voxel51/fiftyone/pull/1808)

  * Fixed tagging selected labels in the expanded view [#1808](https://github.com/voxel51/fiftyone/pull/1808)

  * Fixed `session.view = None` [#1808](https://github.com/voxel51/fiftyone/pull/1808)

  * Fixed issues with patches views [#1808](https://github.com/voxel51/fiftyone/pull/1808)




Core

  * Fixed errors related to session-attached plots [#1808](https://github.com/voxel51/fiftyone/pull/1808)




## FiftyOne 0.16.1#

_Released May 26, 2022_

App

  * Fixed a bug that caused label rendering to be delayed until statistics were loaded [#1776](https://github.com/voxel51/fiftyone/pull/1776)

  * Fixed the `v0.16.0` migration that prevents label lists, e.g. [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") from showing their label filters when expanded in the sidebar [#1785](https://github.com/voxel51/fiftyone/pull/1785)

  * Fixed expanded samples in clips views which appeared to be empty [#1790](https://github.com/voxel51/fiftyone/pull/1790)

  * Fixed âSort by similarityâ with a `dist_field` [#1790](https://github.com/voxel51/fiftyone/pull/1790)

  * Fixed âColor byâ for simple values (classifications, tags, etc.) [#1790](https://github.com/voxel51/fiftyone/pull/1790)

  * Fixed changing datasets when sort by similarity is set [#1790](https://github.com/voxel51/fiftyone/pull/1790)

  * Fixed mask and map coloring [#1790](https://github.com/voxel51/fiftyone/pull/1790)

  * Fixed fortran array handling for masks and maps [#1790](https://github.com/voxel51/fiftyone/pull/1790)




Core

  * Fixed a formatting issue when raising an exception because unsupported plotting backend was requested [#1794](https://github.com/voxel51/fiftyone/pull/1794)




## FiftyOne 0.16.0#

_Released May 24, 2022_

App

  * Added routing, e.g. `/datasets/:dataset-name` [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Redesigned the sidebar to support custom grouping and sorting of fields and tags [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Added graceful handling of deleted datasets in the App [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Fixed epoch rendering [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Fixed empty heatmap rendering [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Added stack traces to the new error page [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Fixed `ESC` when viewing single frame clips [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Fixed handling of unsupported videos [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Added support for opening the expanded view while sample(s) are selected [#1713](https://github.com/voxel51/fiftyone/pull/1713)

  * Fixed keypoint skeleton rendering for named skeletons of frame fields [#1713](https://github.com/voxel51/fiftyone/pull/1713)




Core

  * Fixed edge cases in [`clone_frame_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_frame_field "fiftyone.core.dataset.Dataset.clone_frame_field"), [`merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples"), and [`rename_frame_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_frame_field "fiftyone.core.dataset.Dataset.rename_frame_field") [#1749](https://github.com/voxel51/fiftyone/pull/1749)

  * Fixed a bug that would cause non-persistent datasets to be prematurely deleted [#1747](https://github.com/voxel51/fiftyone/pull/1747)

  * Fixed loading relative paths in [YOLOv5](user_guide__import_datasets.md#yolov5dataset-import) format [#1721](https://github.com/voxel51/fiftyone/pull/1721)

  * Fixed image lists for the `image_path` parameter when importing [GeoTIFF datasets](user_guide__import_datasets.md#geotiffdataset-import) [#1728](https://github.com/voxel51/fiftyone/pull/1728)

  * Added a [`find_duplicates()`](api__fiftyone.utils.iou.md#fiftyone.utils.iou.find_duplicates "fiftyone.utils.iou.find_duplicates") utility to automatically find duplicate objects based on IoU [#1714](https://github.com/voxel51/fiftyone/pull/1714)




## FiftyOne 0.15.1#

_Released April 26, 2022_

App

  * Added support for rendering keypoint skeletons [#1601](https://github.com/voxel51/fiftyone/pull/1601)

  * Added support for rendering per-point confidences and other custom per-point attributes on [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects [#1601](https://github.com/voxel51/fiftyone/pull/1601)

  * Added support for rendering Fortan-ordered arrays [#1660](https://github.com/voxel51/fiftyone/pull/1660)




Core

  * Added support for [storing keypoint skeletons](https://docs.voxel51.com/user_guide/using_datasets.html#storing-keypoint-skeletons) on datasets [#1601](https://github.com/voxel51/fiftyone/pull/1601)

  * Added a [`filter_keypoints()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_keypoints "fiftyone.core.collections.SampleCollection.filter_keypoints") stage that applies per-`point` filters to [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects [#1601](https://github.com/voxel51/fiftyone/pull/1601)

  * Added support for rendering keypoints skeletons and missing keypoints to [`draw_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.draw_labels "fiftyone.core.collections.SampleCollection.draw_labels") [#1601](https://github.com/voxel51/fiftyone/pull/1601)

  * Added support for per-point confidences and other custom per-point attributes on [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects. See [this section](https://docs.voxel51.com/user_guide/using_datasets.html#keypoints) for details [#1601](https://github.com/voxel51/fiftyone/pull/1601)

  * Added a [`concat()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.concat "fiftyone.core.collections.SampleCollection.concat") view stage that allows for concatenating one collection onto another [#1662](https://github.com/voxel51/fiftyone/pull/1662)

  * Non-persistent datasets are now automatically deleted when using a custom `database_uri` [#1697](https://github.com/voxel51/fiftyone/pull/1697)

  * Added a `database_admin` config setting that can control whether database migrations are allowed. See [this page](user_guide__config.md#database-migrations) for details [#1692](https://github.com/voxel51/fiftyone/pull/1692)

  * Added a `database_name` config setting that allows for customizing the MongoDB database name [#1692](https://github.com/voxel51/fiftyone/pull/1692)

  * [`Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") attributes are now exported as tag attributes when exporting in [CVATImageDataset format](user_guide__export_datasets.md#cvatimagedataset-export) [#1686](https://github.com/voxel51/fiftyone/pull/1686)

  * The `iscrowd` attribute is now always populated when exporting in [COCO format](user_guide__export_datasets.md#cocodetectiondataset-export) [#1664](https://github.com/voxel51/fiftyone/pull/1664)

  * Fixed a `KeyError` bug when loading dataset with relative paths on Windows [#1675](https://github.com/voxel51/fiftyone/pull/1675)




Brain

  * Added `fiftyone-brain` wheels for Python 3.10

  * Added support for installing `fiftyone-brain` on Apple Silicon




Annotation

  * Fixed a `CSRF Failed` error when connecting to some CVAT servers [#1668](https://github.com/voxel51/fiftyone/pull/1668)




Integrations

  * Updated the [Lightning Flash integration](integrations__lightning_flash.md#lightning-flash) to support Flash versions 0.7.0 or later [#1671](https://github.com/voxel51/fiftyone/pull/1671)




Zoo

  * Added the [Families in the Wild dataset](dataset_zoo__datasets__fiw.md#dataset-zoo-fiw) to the FiftyOne Dataset Zoo! [#1663](https://github.com/voxel51/fiftyone/pull/1663)




## FiftyOne 0.15.0#

_Released March 23, 2022_

App

  * Fixed [`Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") rendering in the visualizer [#1604](https://github.com/voxel51/fiftyone/pull/1604)




Core

  * Added a [`Dataset.delete_frames()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_frames "fiftyone.core.dataset.Dataset.delete_frames") method that allows for deleting frames by ID [#1650](https://github.com/voxel51/fiftyone/pull/1650)

  * Added a [`keep_fields()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.keep_fields "fiftyone.core.view.DatasetView.keep_fields") method to [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") and its subclasses [#1616](https://github.com/voxel51/fiftyone/pull/1616)

  * Added a [`lines()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.lines "fiftyone.core.plots.base.lines") method that allows for plotting lines whose scatter points can be interactively selected via the typical [interactive plotting workflows](https://voxel51.com/docs/fiftyone/user_guide/plots.html) [#1614](https://github.com/voxel51/fiftyone/pull/1614)

  * Added an optional `force_rgb=True` syntax when importing/exporting/creating TF records using all relevant methods in [`fiftyone.utils.tf`](api__fiftyone.utils.tf.md#module-fiftyone.utils.tf "fiftyone.utils.tf") [#1612](https://github.com/voxel51/fiftyone/pull/1612)

  * Added support for passing additional kwargs to the `fiftyone convert` CLI command [#1612](https://github.com/voxel51/fiftyone/pull/1612)

  * Added support for annotating video-level labels when using [`draw_labeled_videos()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.draw_labeled_videos "fiftyone.utils.annotations.draw_labeled_videos") [#1619](https://github.com/voxel51/fiftyone/pull/1619)

  * Added the ability to slice using a [`ViewField`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewField "fiftyone.core.expressions.ViewField") [#1630](https://github.com/voxel51/fiftyone/pull/1630)

  * Fixed bug in [`from_images_dir()`](api__fiftyone.utils.tf.md#fiftyone.utils.tf.from_images_dir "fiftyone.utils.tf.from_images_dir") where attempting to load 4-channel images errored even if `force_rgb=True` [#1632](https://github.com/voxel51/fiftyone/pull/1632)

  * Fixed a bug that prevented frames from being attached to video collections when aggregating expressions that involve both [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")-level and [`Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame")-level fields [#1644](https://github.com/voxel51/fiftyone/pull/1644)

  * Added support for importing [image](user_guide__import_datasets.md#openlabelimagedataset-import) and [video](user_guide__import_datasets.md#openlabelvideodataset-import) datasets in [OpenLABEL format](https://www.asam.net/index.php?eID=dumpFile&t=f&f=3876&token=413e8c85031ae64cc35cf42d0768627514868b2f#_introduction) [#1609](https://github.com/voxel51/fiftyone/pull/1609)




Annotation

  * Added support for CVATv2 servers when using the CVAT backend [#1638](https://github.com/voxel51/fiftyone/pull/1638)

  * Added an `issue_tracker` argument to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") when using the CVAT backend [#1625](https://github.com/voxel51/fiftyone/pull/1625)

  * Added a `dest_field` argument to [`load_annotations()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.load_annotations "fiftyone.utils.annotations.load_annotations") which allows you to specify the name of the field to which to load annotations [#1642](https://github.com/voxel51/fiftyone/pull/1642)

  * Added a property to annotation backends that decides whether to allow annotation of video-level labels [#1655](https://github.com/voxel51/fiftyone/pull/1655)

  * Fixed a bug where views that dynamically modify label strings would result in labels not being uploaded to the annotation backend [#1647](https://github.com/voxel51/fiftyone/pull/1647)




Docs

  * Added [documentation](https://docs.voxel51.com/user_guide/using_datasets.html#custom-embedded-documents) for defining custom [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument") and [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument") classes [#1617](https://github.com/voxel51/fiftyone/pull/1617)

  * Added [documentation](https://docs.voxel51.com/user_guide/using_views.html#view-slicing) about boolean view indexing to the user guide [#1617](https://github.com/voxel51/fiftyone/pull/1617)

  * Added a [recipe](recipes__creating_views.md) for creating views and view expressions [#1641](https://github.com/voxel51/fiftyone/pull/1641)




## FiftyOne 0.14.4#

_Released February 7, 2022_

News

  * With support from the [ActivityNet team](http://activity-net.org/download.html), FiftyOne is now a recommended tool for downloading, visualizing, and evaluating on the Activitynet dataset! Check out [this guide](integrations__activitynet.md#activitynet) for more details




App

  * Fixed encoding of sample media URLs so image and video filepaths with special characters are supported

  * Fixed an error that would occur when rendering empty [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") instances




Core

  * Added an official [Dockerfile](https://github.com/voxel51/fiftyone/blob/develop/Dockerfile)

  * Changed the default implementation of [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames") to assume that the user has already sampled the frames offline and stored their locations in a `filepath` field of each [`Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") in their video dataset. See [this section](https://docs.voxel51.com/user_guide/using_views.html#frame-views) for more details

  * Updated [`DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to save changes to (only) the samples in the view to the underlying dataset

  * Added a new [`DatasetView.keep()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.keep "fiftyone.core.view.DatasetView.keep") method that deletes any samples that are not in the view from the underlying dataset

  * Added [`InteractivePlot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.save "fiftyone.core.plots.base.InteractivePlot.save") and [`ViewPlot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot "fiftyone.core.plots.base.ViewPlot") methods that can be used to save plots as static images

  * Added support for populating query distances on a dataset when using [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") to query by similarity

  * Added a [`instances_to_polylines()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.instances_to_polylines "fiftyone.utils.labels.instances_to_polylines") utility that converts instance segmentations to [`Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") format

  * Added support for frame labels to all conversion methods in the [`fiftyone.utils.labels`](api__fiftyone.utils.labels.md#module-fiftyone.utils.labels "fiftyone.utils.labels") module

  * Updated the implementation of [`Detection.to_polyline()`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection.to_polyline "fiftyone.core.labels.Detection.to_polyline") so that all attributes are included rather than just ETA-supported ones

  * Added support for including empty labels via an `include_missing` keyword argument in [`add_yolo_labels()`](api__fiftyone.utils.yolo.md#fiftyone.utils.yolo.add_yolo_labels "fiftyone.utils.yolo.add_yolo_labels")

  * Added a [`download_youtube_videos()`](api__fiftyone.utils.youtube.md#fiftyone.utils.youtube.download_youtube_videos "fiftyone.utils.youtube.download_youtube_videos") utility for efficiently and robustly downloading videos or specific segments from YouTube

  * Added a `skip_failures` flag to [`transform_images()`](api__fiftyone.utils.image.md#fiftyone.utils.image.transform_images "fiftyone.utils.image.transform_images") and [`transform_videos()`](api__fiftyone.utils.video.md#fiftyone.utils.video.transform_videos "fiftyone.utils.video.transform_videos")

  * Added `shuffle` and `seed` parameters to [`FiftyOneImageLabelsDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter "fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter") and [`FiftyOneVideoLabelsDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter "fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter")

  * Added an `include_all_data` parameter to [`YOLOv5DatasetImporter`](api__fiftyone.utils.yolo.md#fiftyone.utils.yolo.YOLOv5DatasetImporter "fiftyone.utils.yolo.YOLOv5DatasetImporter")

  * Resolved a bug that would previously cause an error when writing aggregations on video datasets that involve applying expressions directly to `"frames"`




Annotation

  * Added support for [importing](user_guide__import_datasets.md#cvatimagedataset-import) and [exporting](user_guide__export_datasets.md#cvatimagedataset-export) sample-level tags in CVAT format

  * Fixed a bug that prevented existing label fields such as [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") that can contain multiple annotation types (boxes or instances) from being specified in calls to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate")

  * CVAT login credentials are no longer included in exception messages




Zoo

  * Added [ActivityNet 100](dataset_zoo__datasets__activitynet_100.md#dataset-zoo-activitynet-100) to the dataset zoo!

  * Added [ActivityNet 200](dataset_zoo__datasets__activitynet_200.md#dataset-zoo-activitynet-200) to the dataset zoo!

  * Added [Kinetics 400](dataset_zoo__datasets__kinetics_400.md#dataset-zoo-kinetics-400) to the dataset zoo!

  * Added [Kinetics 600](dataset_zoo__datasets__kinetics_600.md#dataset-zoo-kinetics-600) to the dataset zoo!

  * Added [Kinetics 700](dataset_zoo__datasets__kinetics_700.md#dataset-zoo-kinetics-700) to the dataset zoo!

  * Added [Kinetics 700-2020](dataset_zoo__datasets__kinetics_700_2020.md#dataset-zoo-kinetics-700-2020) to the dataset zoo!




## FiftyOne 0.14.3#

_Released January 13, 2022_

Core

  * Added hollow support for 32-bit systems (a [database_uri](user_guide__config.md#configuring-mongodb-connection) must be used in such cases)

  * Added support for indexing into datasets using boolean arrays or view expressions via new `dataset[bool_array]` and `dataset[bool_expr]` syntaxes

  * Added support for registering custom [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument") classes that can be used to populate fields and embedded fields of datasets

  * Added support for importing and exporting `confidence` in YOLO formats

  * Added support for directly passing a `filename -> filepath` mapping dict to the `data_path` parameter to [dataset importers](user_guide__import_datasets.md#importing-datasets)

  * Added graceful casting of `int`-like and `float`-like values like `np.float(1.0)` to their respective Python primitives for storage in the database

  * Changed the default to `num_workers=0` when using methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") to apply Torch models on Windows, which avoids multiprocessing issues

  * Fixed a bug when calling [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") with both the `classes` and `compute_mAP=True` arguments provided

  * Fixed a bug that could arise when importing segmentation data from a COCO JSON that contains objects with `[]` segmentation data

  * Fixed a bug in expressions containing near-epoch dates

  * Added support for setting frame-level fields by passing frame number dicts to [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values")

  * Fixes a bug that prevented [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") from working as expected when `key_field="id"` argument is used

  * Fixed a bug that occurred when computing patch embeddings defined by [polylines](https://docs.voxel51.com/user_guide/using_datasets.html#polylines)

  * Added decision thresholds to the tooltips of PR/ROC curves plotted via the following methods:
    
    * [`BinaryClassificationResults.plot_pr_curve()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.plot_pr_curve "fiftyone.utils.eval.classification.BinaryClassificationResults.plot_pr_curve")

    * [`BinaryClassificationResults.plot_roc_curve()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.BinaryClassificationResults.plot_roc_curve "fiftyone.utils.eval.classification.BinaryClassificationResults.plot_roc_curve")

    * [`COCODetectionResults.plot_pr_curves()`](api__fiftyone.utils.eval.coco.md#fiftyone.utils.eval.coco.COCODetectionResults.plot_pr_curves "fiftyone.utils.eval.coco.COCODetectionResults.plot_pr_curves")

    * [`OpenImagesDetectionResults.plot_pr_curves()`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesDetectionResults.plot_pr_curves "fiftyone.utils.eval.openimages.OpenImagesDetectionResults.plot_pr_curves")




Brain

  * Graceful handling of missing/uncomputable embeddings in [`compute_uniqueness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_uniqueness "fiftyone.brain.compute_uniqueness")

  * Graceful handling of edge cases like `fraction <= 0` in [`find_duplicates()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.find_duplicates "fiftyone.brain.similarity.DuplicatesMixin.find_duplicates"),

  * Removed a spurious warning message that was previously logged when computing patch embeddings for a collection containing samples with no patches




Annotation

  * Added a new [Labelbox integration](integrations__labelbox.md#labelbox-integration)!

  * Added an [`import_annotations()`](api__fiftyone.utils.cvat.md#fiftyone.utils.cvat.import_annotations "fiftyone.utils.cvat.import_annotations") method for importing existing CVAT projects or task(s) into FiftyOne

  * Added support for [configuring the size of CVAT tasks](integrations__cvat.md#cvat-large-runs) via a new `task_size` parameter

  * Added graceful handling of deleted tasks when importing annotations from CVAT via [`load_annotations()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.load_annotations "fiftyone.core.dataset.Dataset.load_annotations")

  * Added an `unexpected` parameter that provides [a variety of options](integrations__cvat.md#cvat-unexpected-annotations) for handling unexpected annotations returned by the CVAT API

  * Added support for passing request headers to the CVAT API

  * Fixed a bug that occurred when importing single frame track segments from CVAT




Zoo

  * Fixed a regression in `fiftyone==0.14.1` that prevented [zoo datasets](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo) that use the Torch backend from being downloaded

  * Added the following TF2 models to the Model Zoo!
    
    * [centernet-hg104-1024-coco-tf2](model_zoo__models__centernet_hg104_1024_coco_tf2.md#model-zoo-centernet-hg104-1024-coco-tf2)

    * [centernet-resnet101-v1-fpn-512-coco-tf2](model_zoo__models__centernet_resnet101_v1_fpn_512_coco_tf2.md#model-zoo-centernet-resnet101-v1-fpn-512-coco-tf2)

    * [centernet-resnet50-v2-512-coco-tf2](model_zoo__models__centernet_resnet50_v2_512_coco_tf2.md#model-zoo-centernet-resnet50-v2-512-coco-tf2)

    * [centernet-mobilenet-v2-fpn-512-coco-tf2](model_zoo__models__centernet_mobilenet_v2_fpn_512_coco_tf2.md#model-zoo-centernet-mobilenet-v2-fpn-512-coco-tf2)

    * [efficientdet-d0-512-coco-tf2](model_zoo__models__efficientdet_d0_512_coco_tf2.md#model-zoo-efficientdet-d0-512-coco-tf2)

    * [efficientdet-d1-640-coco-tf2](model_zoo__models__efficientdet_d1_640_coco_tf2.md#model-zoo-efficientdet-d1-640-coco-tf2)

    * [efficientdet-d2-768-coco-tf2](model_zoo__models__efficientdet_d2_768_coco_tf2.md#model-zoo-efficientdet-d2-768-coco-tf2)

    * [efficientdet-d3-896-coco-tf2](model_zoo__models__efficientdet_d3_896_coco_tf2.md#model-zoo-efficientdet-d3-896-coco-tf2)

    * [efficientdet-d4-1024-coco-tf2](model_zoo__models__efficientdet_d4_1024_coco_tf2.md#model-zoo-efficientdet-d4-1024-coco-tf2)

    * [efficientdet-d5-1280-coco-tf2](model_zoo__models__efficientdet_d5_1280_coco_tf2.md#model-zoo-efficientdet-d5-1280-coco-tf2)

    * [efficientdet-d6-1280-coco-tf2](model_zoo__models__efficientdet_d6_1280_coco_tf2.md#model-zoo-efficientdet-d6-1280-coco-tf2)

    * [efficientdet-d7-1536-coco-tf2](model_zoo__models__efficientdet_d7_1536_coco_tf2.md#model-zoo-efficientdet-d7-1536-coco-tf2)

    * [ssd-mobilenet-v2-320-coco17](model_zoo__models__ssd_mobilenet_v2_320_coco17.md#model-zoo-ssd-mobilenet-v2-320-coco17)

    * [ssd-mobilenet-v1-fpn-640-coco17](model_zoo__models__ssd_mobilenet_v1_fpn_640_coco17.md#model-zoo-ssd-mobilenet-v1-fpn-640-coco17)




## FiftyOne 0.14.2#

_Released November 24, 2021_

App

  * Improved mask loading times for [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation"), [`Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap"), and [`Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") labels with instance masks




Core

  * Optimized image metadata calculation to read only the bare minimum byte content of each image

  * Improved handling of relative paths and user paths in config settings and environment variables

  * Optimized database I/O and improved the helpfulness of warnings/errors that are generated when applying models via [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"), and [`compute_patch_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_patch_embeddings "fiftyone.core.collections.SampleCollection.compute_patch_embeddings")

  * Resolved a [memory leak](https://github.com/voxel51/fiftyone/issues/1442) that could occur when computing predictions/embeddings for very large datasets with Torch models




Brain

  * Added the `points` keyword argument to [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") for providing your own manually computed low-dimensional representation for use with interactive embeddings plots

  * Graceful handling of missing/uncomputable embeddings in [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") and [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity")

  * Added checks that occur at the start of all methods to ensure that any required dependencies are installed prior to performing any expensive computations




Annotation

  * Changed CVAT uploads to retain original filenames

  * A helpful error is now raised when the `"frames."` prefix is omitted from label fields when requesting spatial annotations on video datasets




Zoo

  * Patched an issue that prevented downloading the [VOC-2007](dataset_zoo__datasets__voc_2007.md#dataset-zoo-voc-2007) and [VOC-2012](dataset_zoo__datasets__voc_2012.md#dataset-zoo-voc-2012) datasets from the zoo




## FiftyOne 0.14.1#

_Released November 15, 2021_

App

  * Optimized grid loading for collections that do not have metadata computed

  * Fixed filtering by label for Colab notebooks

  * Fixed a bug where the App would crash if an image or video MIME type could not be inferred from the filepath, e.g. without an extension

  * Fixed first pixel coloring for segmentations

  * Added graceful handling of nonfinites (`-inf`, `inf`, and `nan`)




Core

  * Fixed [`clone()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") for views with a parent dataset that has brain runs

  * Fixed sampling frames when using [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames")

  * Fixed importing of [`FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") with run results

  * Added a [`Regression`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Regression "fiftyone.core.labels.Regression") label type

  * Added a [`random_split()`](api__fiftyone.utils.random.md#fiftyone.utils.random.random_split "fiftyone.utils.random.random_split") method

  * Added support for negating [`match_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_labels "fiftyone.core.collections.SampleCollection.match_labels") queries

  * Added a [`MaxResize`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.MaxResize "fiftyone.utils.torch.MaxResize") transform

  * Added `image_max_size` and `image_max_dim` parameters to [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig")

  * Added support for non-sequential updates in [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values")

  * Added a `compute_max_ious()` utility

  * Added support for labels-only exports when working with [`YOLOv4Dataset`](api__fiftyone.types.md#fiftyone.types.YOLOv4Dataset "fiftyone.types.YOLOv4Dataset") and [`YOLOv5Dataset`](api__fiftyone.types.md#fiftyone.types.YOLOv5Dataset "fiftyone.types.YOLOv5Dataset") formats

  * Added `fiftyone.utils.beam` for parallel import, merge, and export operations with [Apache Beam](https://beam.apache.org)

  * Added an [`add_yolo_labels()`](api__fiftyone.utils.yolo.md#fiftyone.utils.yolo.add_yolo_labels "fiftyone.utils.yolo.add_yolo_labels") utility that provides support for adding YOLO-formatted model predictions to an existing dataset

  * Added support for importing/exporting multilabel classifications when using [FiftyOneImageClassificationDataset format](user_guide__import_datasets.md#fiftyoneimageclassificationdataset-import)

  * Fixed the `force_reencode` flag for [`reencode_videos()`](api__fiftyone.utils.video.md#fiftyone.utils.video.reencode_videos "fiftyone.utils.video.reencode_videos")

  * Converted COCO and Open Images dataset downloads to use multithreading rather than multiprocessing

  * Updated evaluation confusion matrices to always include rows and columns for missing/other




Annotation

  * Added support for annotating multiple label fields in one CVAT task

  * Added an `allow_index_edits` parameter to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") for disallowing video track index changes

  * Improved label ID tracking in CVAT by leveraging CVATâs server IDs in addition to `label_id` attributes

  * Fixed a bug when annotating videos in CVAT with `None` label fields

  * Fixed a bug when annotating new fields in CVAT

  * Fixed a bug when annotating non-continuous tracks in CVAT

  * Fixed a bug when annotating a track in CVAT that is present on the last frame of a video

  * Fixed a bug when annotating with `allow_additions=False`




Docs

  * Added a section on [adding model predictions](user_guide__import_datasets.md#adding-model-predictions) to existing datasets to the user guide

  * Added explicit examples of labels-only [imports](user_guide__import_datasets.md#importing-datasets) and [exports](user_guide__export_datasets.md#exporting-datasets) for all relevant datasets to the docs

  * Documented how class lists are computed when exporting in formats like YOLO and COCO that require explicit class lists

  * Documented the supported label types for all exporters




## FiftyOne 0.14.0#

_Released October 15, 2021_

App

  * Added support for visualizing [heatmaps](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps) using either transparency or a customizable colorscale

  * Added a label opacity slider in both the sample grid and the expanded sample view

  * Added support for visualizing [clips views](user_guide__app.md#app-video-clips)

  * Added support for rendering and filtering [`DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField") and [`DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField") data

  * Improved error handling in the grid and when streaming frames

  * Fixed a bug that caused incorrect label rendering for sparse frame labels in the video visualizer

  * Added a `default_app_address` setting to the FiftyOne config for restricting sessions to a hostname. See [this page](installation__environments.md#restricting-app-address) for more details




Core

  * Added a [Heatmap label type](https://docs.voxel51.com/user_guide/using_datasets.html#heatmaps)

  * Added support for adding [date and datetime fields](https://docs.voxel51.com/user_guide/using_datasets.html#dates-and-datetimes) to FiftyOne datasets

  * Added the [`to_clips()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_clips "fiftyone.core.collections.SampleCollection.to_clips") method for creating clips views into video datasets

  * Added clip views sections to the [App user guide page](user_guide__app.md#app-video-clips) and [dataset views user guide page](https://docs.voxel51.com/user_guide/using_views.html#clip-views)

  * Added support for [exporting video clips](user_guide__export_datasets.md#export-label-coercion) in labeled video formats

  * Added a `trajectories=True` flag to [`filter_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_labels "fiftyone.core.collections.SampleCollection.filter_labels") that allows for matching entire object trajectories for which a given filter matches the object in at least one frame of the video

  * Added set operations [`is_subset()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.is_subset "fiftyone.core.expressions.ViewExpression.is_subset"), [`set_equals()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.set_equals "fiftyone.core.expressions.ViewExpression.set_equals"), [`unique()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.unique "fiftyone.core.expressions.ViewExpression.unique"), [`union()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.union "fiftyone.core.expressions.ViewExpression.union"), [`intersection()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.intersection "fiftyone.core.expressions.ViewExpression.intersection"), [`difference()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.difference "fiftyone.core.expressions.ViewExpression.difference"), and [`contains(all=True)`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.contains "fiftyone.core.expressions.ViewExpression.contains") to the view expression API

  * Added date operations [`to_date()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.to_date "fiftyone.core.expressions.ViewExpression.to_date"), [`millisecond()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.millisecond "fiftyone.core.expressions.ViewExpression.millisecond"), [`second()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.second "fiftyone.core.expressions.ViewExpression.second"), [`minute()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.minute "fiftyone.core.expressions.ViewExpression.minute"), [`hour()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.hour "fiftyone.core.expressions.ViewExpression.hour"), [`day_of_week()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.day_of_week "fiftyone.core.expressions.ViewExpression.day_of_week"), [`day_of_month()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.day_of_month "fiftyone.core.expressions.ViewExpression.day_of_month"), [`day_of_year()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.day_of_year "fiftyone.core.expressions.ViewExpression.day_of_year"), [`month()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.month "fiftyone.core.expressions.ViewExpression.month"), and [`year()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.year "fiftyone.core.expressions.ViewExpression.year") to the view expression API

  * Missing ground truth/predictions are now included by default when viewing [confusion matrices](user_guide__plots.md#confusion-matrix-plots) for detection tasks




Annotation

  * Added support for specifying per-class attributes when [defining a label schema](integrations__annotation.md#annotation-label-schema) for an annotation task

  * Added support for specifying whether labels can be added, deleted or moved and whether certain label attributes are read-only when [configuring an annotation task](integrations__annotation.md#annotation-restricting-edits)

  * Added support for respecting keyframe information when adding or editing [video annotations](integrations__annotation.md#annotation-labeling-videos)

  * Fixed a 0-based versus 1-based frame numbering bug when [importing](user_guide__import_datasets.md#cvatvideodataset-import) and [exporting](user_guide__export_datasets.md#cvatvideodataset-export) labels in CVAT video format

  * Added support for adding/editing bounding box shapes (not tracks) if desired when annotating video frames using the [CVAT backend](integrations__cvat.md#cvat-integration)

  * Fixed a bug that prevented importing of video annotations from the CVAT backend that involved the splitting or merging of object tracks

  * Added a `project_name` parameter that allows for [creating annotation tasks](integrations__cvat.md#cvat-requesting-annotations) within a new project when using the CVAT backend

  * Added support for specifying a list of task assignees when creating video annotation tasks (which generate one task per video) using the CVAT backend

  * Fixed a bug when adding/editing boolean attributes in an annotation task using the CVAT backend

  * Added a new `occluded` attribute type option that links an attribute to the builtin occlusion icon when [annotating label attributes](integrations__cvat.md#cvat-label-attributes) using the CVAT backend




## FiftyOne 0.13.3#

_Released September 22, 2021_

App

  * Improved the efficiency of loading label graphs for fields with many distinct values

  * Fixed some audio-related bugs when viewing video samples with audio channels

  * Fixed a bug that prevented boolean App filters from working properly




Core

  * Added support for importing/exporting segmentation masks with greater than 256 classes when working with the [ImageSegmentationDirectory](user_guide__export_datasets.md#imagesegmentationdirectory-export) format

  * Added support for importing GeoTIFF images via a new [GeoTIFFDataset](user_guide__import_datasets.md#geotiffdataset-import) format

  * Added new [`split_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.split_labels "fiftyone.core.collections.SampleCollection.split_labels") and [`merge_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.merge_labels "fiftyone.core.collections.SampleCollection.merge_labels") methods that provide convenient syntaxes for moving labels between new and existing label fields of a dataset

  * Added [`ensure_frames()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.ensure_frames "fiftyone.core.dataset.Dataset.ensure_frames") and [`clear_frames()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clear_frames "fiftyone.core.dataset.Dataset.clear_frames") methods that can be used to conveniently initialize and clear the frames of video datasets, respectively

  * Added support for using a MongoDB dataset whose version is [not explicitly supported](user_guide__config.md#configuring-mongodb-connection)

  * Removed the `opencv-python-headless` maximum version requirement

  * Fixed a race condition that could prevent callbacks on [interactive plots](user_guide__plots.md#interactive-plots) from working properly on sufficiently large datasets




Annotation

  * Added support for annotating semantic segmentations and instance segmentations using the [CVAT backend](integrations__cvat.md#cvat-requesting-annotations)

  * Added support for annotating polylines using the CVAT backend

  * Added support for immutable attributes when annotating object tracks for video datasets using the CVAT backend

  * Exposed the `use_cache`, `use_zip_chunks`, and `chunk_size` parameters when uploading annotations via the CVAT backend

  * Fixed a bug that prevented multiple imports of the same annotation run from working as expected when a label is deleted but then later re-added

  * Fixed a bug that prevented annotations for new label fields of video datasets from being imported properly

  * Fixed a bug that would cause unsuppoted shapes such as polygons with less than 3 vertices to be deleted when editing existing labels with the CVAT backend




## FiftyOne 0.13.2#

_Released September 3, 2021_

App

  * Improved aggregation queries resulting in ~10x faster statistics load times and time-to-interaction in the Fields Sidebar!

  * Optimized in-App tagging actions

  * Fixed count inconsistencies for large sets of [`StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField") results in the Fields Sidebar




Core

  * Added support for providing compound sort criteria when using the [`sort_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by "fiftyone.core.collections.SampleCollection.sort_by") stage

  * Added support for configuring the wait time when using [`Session.wait()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.wait "fiftyone.core.session.Session.wait") to block execution until the App is closed, including support for serving forever

  * Fixed errors experienced by Windows users when running FiftyOne APIs that involved multiprocessing

  * Resolved errors that could occur when importing CVAT XML files with empty-valued attributes in their schema and/or individual labels

  * Added support for importing CVAT-style attributes when loading labels in COCO and VOC formats




## FiftyOne 0.13.1#

_Released August 25, 2021_

App

  * Fixed `id` rendering in the grid when the `id` checkbox is active




Annotation

  * Fixed a bug that could cause mismatches between media and their pre-existing labels when uploading data to CVAT for annotation whose source media lives in multiple directories




## FiftyOne 0.13.0#

_Released August 24, 2021_

App

  * Added support for visualizing and filtering list fields

  * Added support for visualizing segmentation masks of any integer type (uint8, uint16, etc.)

  * Improved handling of falsey field values in the fields sidebar and image vizualizer

  * Improved the JSON display format available from the expanded sample modal

  * Resolved an issue that caused some users to see duplicate App screenshots when calling [`Session.freeze()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.freeze "fiftyone.core.session.Session.freeze") in Jupyter notebooks

  * Fixed a bug that prevented users from being able to click left/right arrows to navigate between samples in the expanded sample modal when working in Jupyter notebooks

  * Fixed a bug where pressing the `ESC` key had no effect in the expanded sample modal when working with datasets with no label fields

  * Fixed a bug that prevented the desktop App from launching when using source builds




Brain

  * Added new [`find_unique()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.find_unique "fiftyone.brain.similarity.DuplicatesMixin.find_unique"), [`unique_view()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.unique_view "fiftyone.brain.similarity.DuplicatesMixin.unique_view"), and [`visualize_unique()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.visualize_unique "fiftyone.brain.similarity.DuplicatesMixin.visualize_unique") methods to the [`SimilarityIndex`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex "fiftyone.brain.similarity.SimilarityIndex") object returned by [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") that enable you to identify a maximally unique set of images or objects in a dataset

  * Added new [`find_duplicates()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.find_duplicates "fiftyone.brain.similarity.DuplicatesMixin.find_duplicates"), [`duplicates_view()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.duplicates_view "fiftyone.brain.similarity.DuplicatesMixin.duplicates_view"), and [`visualize_duplicates()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.DuplicatesMixin.visualize_duplicates "fiftyone.brain.similarity.DuplicatesMixin.visualize_duplicates") methods to the [`SimilarityIndex`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex "fiftyone.brain.similarity.SimilarityIndex") object returned by [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") that enable you to identify near-duplicate images or objects in a dataset

  * Added a new [`compute_exact_duplicates()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_exact_duplicates "fiftyone.brain.compute_exact_duplicates") method that can identify exactly duplicate media in a dataset




Core

  * Added support for pip-installing FiftyOne on Apple Silicon Macs. Note that MongoDB must be [self-installed](user_guide__config.md#configuring-mongodb-connection) in this case

  * Added support for using a [self-installed MongoDB database](user_guide__config.md#configuring-mongodb-connection)

  * Added a [`group_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.group_by "fiftyone.core.collections.SampleCollection.group_by") view stage that allows for reorganizing the samples in a collection so that they are grouped by a specified field or expression

  * Added a [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") property that enables users to change the behavior of App updates when selections are made in an interactive plot linked to labels. See [this page](user_guide__plots.md#plot-selection-modes) for details

  * Added support for [YOLOv5 YAML files](user_guide__import_datasets.md#yolov5dataset-import) with multiple directories per dataset split

  * Added support for importing/exporting confidences via the `score` field when working with [BDD format](user_guide__import_datasets.md#bdddataset-import)

  * Fixed some Windows-style path bugs




Annotation

  * Added a powerful [annotation API](integrations__annotation.md#fiftyone-annotation) that makes it easy to add or edit labels on your FiftyOne datasets or specific views into them

  * Added a native [CVAT integration](integrations__cvat.md#cvat-integration) that enables you to use the annotation API with [CVAT](https://github.com/opencv/cvat)




Docs

  * Added a [CVAT annotation tutorial](tutorials__cvat_annotation.md)

  * Added a [new example](brain.md#brain-near-duplicates) to the brain user guide that demonstrates unique and near-duplicate image workflows

  * Added an object embeddings example to the [embeddings visualization section](brain.md#brain-embeddings-visualization) of the brain user guide

  * Added a [new section](user_guide__plots.md#plot-selection-modes) to the plots user guide page explaining how to control the selection mode of interactive plots linked to labels




## FiftyOne 0.12.0#

_Released August 10, 2021_

App

  * Resolved performance issues with scrolling via grid virtualization. Toggling fields or selecting samples is no longer impacted by the amount of samples that have been loaded

  * Added the `Show label` option in the expanded sample view to toggle the label text above detections boxes

  * Added support for zooming and panning in the expanded sample view

  * Added support for cropping and zooming to content in the expanded sample view

  * Added support for visualizing multiple segmentation frame fields simultaneously

  * Added label streaming to the video visualizer

  * Added volume and playback rate settings to the video visualizer

  * Added the `Crop to content` option in patches or evaluation patches views which crops samples to only show the labels that make up the patch. Defaults to `True`

  * Added count and filtered count values to categorical filters ([`BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField") and [`StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField") fields)




Core

  * Added support for importing [DICOM datasets](user_guide__import_datasets.md#dicomdataset-import)

  * Added better default behavior for the `label_field` parameter when importing datasets using methods like [`from_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_dir "fiftyone.core.dataset.Dataset.from_dir") and exporting datasets using [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export")

  * When adding samples to datasets, `None`-valued sample fields are now gracefully ignored when expanding dataset schemas




Docs

  * Added [Using the image visualizer](user_guide__app.md#app-image-visualizer) and [Using the video visualizer](user_guide__app.md#app-video-visualizer) sections to the App user guide

  * Added sections covering [merging datasets](https://docs.voxel51.com/user_guide/using_datasets.html#merging-datasets) and [batch updates](https://docs.voxel51.com/user_guide/using_datasets.html#batch-updates) to the dataset user guide page




Zoo

  * Patched an Open Images issue where `classes` or `attrs` requirements were being ignored when loading a dataset with no `max_samples` requirement




## FiftyOne 0.11.2.1#

_Released July 31, 2021_

Zoo

  * Patched an Open Images issue where label files were not being downloaded when running a [`load_zoo_dataset()`](api__fiftyone.zoo.md#fiftyone.zoo.load_zoo_dataset "fiftyone.zoo.load_zoo_dataset") call that does not include `classes` or `attrs` options in an environment where Open Images has never been downloaded

  * Patched loading of Cityscapes datasets

  * Patched loading of COCO datasets




## FiftyOne 0.11.2#

_Released July 27, 2021_

App

  * Added support for calling [`Session.open_tab()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.open_tab "fiftyone.core.session.Session.open_tab") from [remote Jupyter notebooks](installation__environments.md#remote-notebooks)

  * Fixed a bug that could cause [`Session.wait()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.wait "fiftyone.core.session.Session.wait") to exit when the Appâs tab is refreshed in the browser




Core

  * Added a `plotly<5` requirement, which prevents an issue that may cause callbacks for selection events in [interactive plots](user_guide__plots.md#interactive-plots) to not trigger as expected when using Plotly V5

  * Added support for evaluating polygons and instance segmentations to [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections"). See [this page](user_guide__evaluation.md#evaluation-detection-types) for usage details

  * Added support for creating [patch views](https://docs.voxel51.com/user_guide/using_views.html#frame-patches-views) and [evaluation patch views](user_guide__evaluation.md#evaluating-videos) into the frames of video datasets

  * Greatly improved the efficiency of creating [evaluation patch views](user_guide__evaluation.md#evaluation-patches)

  * Added support for recursively listing data directories when loading datasets [from disk](user_guide__import_datasets.md#importing-datasets)

  * Added support for controlling whether/which object attributes are imported/exported in formats like [COCO](user_guide__import_datasets.md#cocodetectiondataset-import) that support arbitrary object attributes

  * Updated all dataset import/export routines to support/prefer custom object attributes stored directly on [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances as dynamic fields rather than in the `attributes` dict

  * The [ImageSegmentationDirectory](user_guide__export_datasets.md#imagesegmentationdirectory-export) format now supports exporting segmentations defined by [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with instance masks and [`Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * Added an [`objects_to_segmentations()`](api__fiftyone.utils.labels.md#fiftyone.utils.labels.objects_to_segmentations "fiftyone.utils.labels.objects_to_segmentations") utility for converting [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with instance fields and [`Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") to [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") format

  * Added graceful handling of edges cases like empty views and missing labels to all [evaluation routines](user_guide__evaluation.md#evaluating-models)

  * Added improved support for [`creating`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.create_index "fiftyone.core.collections.SampleCollection.create_index"), [`viewing`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_index_information "fiftyone.core.collections.SampleCollection.get_index_information"), and [`dropping`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.drop_index "fiftyone.core.collections.SampleCollection.drop_index") dropping sample- and frame-level indexes on datasets

  * Added additional indexes on patch and frames views to enable efficient ID-based queries

  * Added support for gracefully loading and deleting evaluations and brain methods executed in future versions of FiftyOne (e.g., after [downgrading](https://docs.voxel51.com/installation/index.html#downgrading-fiftyone) your FiftyOne package version)

  * Added an optional `progress` flag to [`iter_samples()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.iter_samples "fiftyone.core.collections.SampleCollection.iter_samples") that renders a progress bar tracking the progress of the iteration

  * Added support for installing FiftyOne on RHEL7 (Red Hat Enterprise Linux)

  * A helpful error message is now raised when a user tries to load a dataset from a future version of FiftyOne without following the [downgrade instructions](https://docs.voxel51.com/installation/index.html#downgrading-fiftyone)

  * Fixed a bug that prevented FiftyOne from being imported on read-only filesystems

  * Fixed a bug that prevented the proper loading of the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) dataset after partial downloads involving only a subset of the available label types




Zoo

  * Added support for importing license data when loading the [COCO-2014](dataset_zoo__datasets__coco_2014.md#dataset-zoo-coco-2014) and [COCO-2017](dataset_zoo__datasets__coco_2017.md#dataset-zoo-coco-2017) datasets from the zoo

  * The inapplicable `classes` flag will now be ignored when loading the unlabeled test split of [COCO-2014](dataset_zoo__datasets__coco_2014.md#dataset-zoo-coco-2014) and [COCO-2017](dataset_zoo__datasets__coco_2017.md#dataset-zoo-coco-2017)

  * Improved the partial download behavior of the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) dataset when the optional `classes` and `attrs` parameters are provided

  * Fixed a bug that prevented Windows users from downloading the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) dataset




## FiftyOne 0.11.1#

_Released June 29, 2021_

App

  * Updated the expired [Slack community link](https://slack.voxel51.com) in the App menu bar




## FiftyOne 0.11.0#

_Released June 29, 2021_

News

  * With support from the [COCO team](https://cocodataset.org/#download), FiftyOne is now a recommended tool for downloading, visualizing, and evaluating on the COCO dataset! Check out [this guide](integrations__coco.md#coco) for more details




App

  * Fixed a bug that prevented `sample_id` fields from appearing in the App when working with frames and patches views




Core

  * Added various new parameters to methods like [`Dataset.from_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_dir "fiftyone.core.dataset.Dataset.from_dir") and [`SampleCollection.export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export"), including `data_path`, `labels_path`, and `export_media` that allow for customizing the import and export of datasets. For example, you can now perform labels-only imports and exports

  * Added new [`Dataset.merge_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_dir "fiftyone.core.dataset.Dataset.merge_dir") and [`Dataset.merge_importer()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_importer "fiftyone.core.dataset.Dataset.merge_importer") methods for merging datasets from disk into existing FiftyOne datasets

  * Added support for [importing](user_guide__import_datasets.md#yolov5dataset-import) and [exporting](user_guide__export_datasets.md#yolov5dataset-export) datasets in [YOLOv5 format](https://github.com/ultralytics/yolov5)

  * Updated the [`GeoJSONDataset`](api__fiftyone.types.md#fiftyone.types.GeoJSONDataset "fiftyone.types.GeoJSONDataset") dataset type to support both image and video datasets

  * Added support for [`importing`](api__fiftyone.utils.coco.md#fiftyone.utils.coco.COCODetectionDatasetImporter "fiftyone.utils.coco.COCODetectionDatasetImporter") and [`exporting`](api__fiftyone.utils.coco.md#fiftyone.utils.coco.COCODetectionDatasetExporter "fiftyone.utils.coco.COCODetectionDatasetExporter") extra attributes in COCO format via a new `extra_attrs` parameter




Zoo

  * Added support for partial downloads and loading segmentations to the [COCO-2014](dataset_zoo__datasets__coco_2014.md#dataset-zoo-coco-2014) and [COCO-2017](dataset_zoo__datasets__coco_2017.md#dataset-zoo-coco-2017) datasets

  * When performing partial downloads on the [Open Images v6 Dataset](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) involving a subset of the available classes, all labels for matching samples will now be loaded by default




Docs

  * Added a [new page](integrations__coco.md#coco) demonstrating how to use FiftyOne to download, visualize, and evaluate on the COCO dataset

  * Added a [new page](integrations__open_images.md#open-images) demonstrating how to use FiftyOne to download, visualize, and evaluate on the Open Images dataset




## FiftyOne 0.10.0#

_Released June 21, 2021_

News

  * Weâve collaborated with the [PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning) team to make it easy to train [Lightning Flash](https://github.com/PyTorchLightning/lightning-flash) tasks on your FiftyOne datasets. Check out [this guide](integrations__lightning_flash.md#lightning-flash) for more details




Core

  * Updated the [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") and [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings") methods to natively support applying [Lightning Flash](https://github.com/PyTorchLightning/lightning-flash) models to FiftyOne datasets!




Docs

  * Added a [new page](integrations__lightning_flash.md#lightning-flash) demonstrating how to use the Lightning Flash integration




## FiftyOne 0.9.4#

_Released June 15, 2021_

App

  * Added support for matching samples by ID in the Filters Sidebar

  * Fixed a bug that caused the App to crash when selecting samples with the `Color by value` setting active

  * Fixed a bug that caused the App to crash on some Windows machines by ensuring the correct MIME type is set for JavaScript files




Core

  * Improved the performance of importing data into FiftyOne by 2x or more!

  * Added a [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames") view stage that enables on-the-fly conversion of video datasets into frames views

  * Added [`last()`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frames.last "fiftyone.core.frame.Frames.last"), [`head()`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frames.head "fiftyone.core.frame.Frames.head"), and [`tail()`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frames.tail "fiftyone.core.frame.Frames.tail") methods to the [`Frames`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frames "fiftyone.core.frame.Frames") class

  * Added new [`exclude_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_fields "fiftyone.core.collections.SampleCollection.exclude_fields"), [`select_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_frames "fiftyone.core.collections.SampleCollection.select_frames"), and [`match_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_frames "fiftyone.core.collections.SampleCollection.match_frames") view stages that enable selecting specific frames of video collections via IDs or filter expressions, respectively

  * Added a new [`match_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_labels "fiftyone.core.collections.SampleCollection.match_labels") view stage that enables matching samples that have specific labels without actually filtering the non-matching labels

  * Added support for exporting image patches using [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") by specifying an image classification dataset type and including a spatial `label_field` that defines the image patches to extract

  * Added support for automatically coercing single label fields like [`Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") into the corresponding multiple label field type [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") when using [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") to export in dataset formats that expect list-type fields

  * Added support for executing an aggregation on multiple fields via the abbreviated syntax `ids, filepaths = dataset.values(["id", "filepath"])`

  * Exposed the `id` field of all samples and frames in dataset schemas

  * Added support for merging the elements of list fields via [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") and [`Document.merge()`](api__fiftyone.core.document.md#fiftyone.core.document.Document.merge "fiftyone.core.document.Document.merge")

  * Added a number of useful options to [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples"), including `fields`, `omit_fields`, and `merge_lists`

  * Improved the efficiency of [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") when the `overwrite=False` option is provided

  * Added an optional `bool` flag to the [`match_tags()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_tags "fiftyone.core.collections.SampleCollection.match_tags") view stage that allows for optionally matching samples without the specified tags

  * Added support for computing filehashes via the `hashlib` module to [`compute_filehash()`](api__fiftyone.core.utils.md#fiftyone.core.utils.compute_filehash "fiftyone.core.utils.compute_filehash")

  * Updated the [`import_from_labelbox()`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.import_from_labelbox "fiftyone.utils.labelbox.import_from_labelbox") method to use the correct label ID (âDataRow IDâ, not âIDâ)

  * Added an optional `edges` argument to [`scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.scatterplot "fiftyone.core.plots.plotly.scatterplot") and [`location_scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.scatterplot "fiftyone.core.plots.plotly.scatterplot") that enables drawing undirected edges between scatterpoints

  * Fixed a bug in [`limit_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.limit_labels "fiftyone.core.collections.SampleCollection.limit_labels") that would cause views to contain empty label lists if the source dataset contains None-valued fields

  * Fixed a bug that prevented [`ViewExpression.contains()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.contains "fiftyone.core.expressions.ViewExpression.contains") from accepting [`ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") instances as arguments




Zoo

  * Fixed a string encoding issue that prevented some Windows users from loading the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) dataset

  * Updated the [vgg16-imagenet-tf1](model_zoo__models__vgg16_imagenet_tf1.md#model-zoo-vgg16-imagenet-tf1) model (formerly named `vgg16-imagenet-tf`) to reflect the fact that it only supports TensorFlow 1.X




Docs

  * Added example usages of [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames") to the [user guide](https://docs.voxel51.com/user_guide/using_views.html#frame-views)




## FiftyOne 0.9.3#

_Released May 18, 2021_

App

  * Fixed an issue that prevented some datasets and views that contain vector or array data (e.g., logits) from properly loading in the App

  * Fixed a bug that prevented loading video datasets in the App in Google Colab environments




## FiftyOne 0.9.2#

_Released May 16, 2021_

Zoo

  * Fixed a multiprocessing bug that prevented Mac users running Python 3.8 or later from loading the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) dataset




## FiftyOne 0.9.1#

_Released May 12, 2021_

App

  * Fixed a bug that caused the App to crash when choosing to `Color by value`




## FiftyOne 0.9.0#

_Released May 12, 2021_

News

  * Weâve collaborated with the [Open Images Team at Google](https://storage.googleapis.com/openimages/web/download.html) to make FiftyOne a recommended tool for downloading, visualizing, and evaluating on the Open Images Dataset! Check out [this guide](integrations__open_images.md#open-images) for more details




App

  * Added a `Patches` action for easy switching to object/evaluation patches views. See [this page](user_guide__app.md#app-object-patches) for usage details

  * Added a `Sort by similarity` action that enables sorting by similarity to the selected samples/patches. See [this page](user_guide__app.md#app-similarity) for usage details

  * Added a zoom slider in the top right of the sample grid that adjusts the tile size of the sample grid

  * Added the ability to clear filters for entire field groups, e.g. `Labels` and `Scalars`, in the Filters Sidebar

  * Added `filepath` to the `Scalars` group in the Filters Sidebar

  * Added a `Label tags` graphs tab

  * Refreshed numeric, string, and boolean filter styles with improved functionality and interaction

  * Added support for [`Session.wait()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.wait "fiftyone.core.session.Session.wait") in browser contexts




Brain

  * Added a [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") method for indexing samples and object patches by similarity. See [this page](brain.md#brain-similarity) for usage details




Core

  * Added support for Open Images-style detection evaluation when using [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections"). See [this page](user_guide__evaluation.md#evaluating-detections-open-images) for usage details

  * Added the [`to_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_patches "fiftyone.core.collections.SampleCollection.to_patches") and [`to_evaluation_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_evaluation_patches "fiftyone.core.collections.SampleCollection.to_evaluation_patches") view stages for transforming collections into flattened views with respect to labels and evaluations, respectively. See [this page](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views) for usage details

  * Added support for applying image models to the frames of video datasets when using [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"), and [`compute_patch_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_patch_embeddings "fiftyone.core.collections.SampleCollection.compute_patch_embeddings")

  * Added full support for embedded documents (e.g. labels) in [`values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values") and [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values")

  * Added support for passing expressions directly to [aggregations](https://docs.voxel51.com/user_guide/using_aggregations.html#using-aggregations)

  * Added an optional `omit_empty` flag to [`select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels") and [`exclude_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_labels "fiftyone.core.collections.SampleCollection.exclude_labels") that controls whether samples with no labels are omitted when filtering

  * Added a [`Dataset.delete_labels()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_labels "fiftyone.core.dataset.Dataset.delete_labels") method for efficiently deleting labels via a variety of natural syntaxes

  * Deprecated `Dataset.remove_sample()` and `Dataset.remove_samples()` in favor of a single [`Dataset.delete_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_samples "fiftyone.core.dataset.Dataset.delete_samples") method

  * Brain results and evaluation results that are loaded via [`load_evaluation_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_evaluation_results "fiftyone.core.collections.SampleCollection.load_evaluation_results") [`load_brain_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_brain_results "fiftyone.core.collections.SampleCollection.load_brain_results") are now cached on the [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") object in-memory so that subsequent retrievals of the results in the same session will be instant




Zoo

  * Added [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) to the dataset zoo!




Docs

  * Added a new [Open Images tutorial](tutorials__open_images.md)

  * Added [object patches](user_guide__app.md#app-object-patches) and [evaluation patches](user_guide__app.md#app-evaluation-patches) sections to the [App guide](user_guide__app.md#fiftyone-app)

  * Added a [similarity](brain.md#brain-similarity) section to the [Brain guide](brain.md#fiftyone-brain)

  * Added [Open Images evaluation](user_guide__evaluation.md#evaluating-detections-open-images) and [evaluation patches](user_guide__evaluation.md#evaluation-patches) sections to the [evaluation guide](user_guide__evaluation.md#evaluating-models)

  * Added [object patches](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views) and [evaluation patches](https://docs.voxel51.com/user_guide/using_views.html#eval-patches-views) sections to the [views guide](https://docs.voxel51.com/user_guide/using_views.html#using-views)

  * Added example uses of [`to_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_patches "fiftyone.core.collections.SampleCollection.to_patches") and [`to_evaluation_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_evaluation_patches "fiftyone.core.collections.SampleCollection.to_evaluation_patches") to the [object detection tutorial](tutorials__evaluate_detections.md)

  * Added example use of [`to_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_patches "fiftyone.core.collections.SampleCollection.to_patches") to the [detection mistakes tutorial](tutorials__detection_mistakes.md)

  * Added example use of [`to_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_patches "fiftyone.core.collections.SampleCollection.to_patches") to the [adding detections recipe](recipes__adding_detections.md)




## FiftyOne 0.8.0#

_Released April 5, 2021_

App

  * Added the ability to tag samples and labels directly from the App in both the sample grid (macro) and expanded sample view (micro) with respect to and filters or currently selected samples/labels

  * Added a `LABEL TAGS` section to the Filters Sidebar to coincide with the introduction of label tags

  * Added label tooltips that display on hover in the expanded sample view

  * Expanded actions to list of button groups in the sample grid and expanded sample view

  * Added support for rendering semantic labels in the new tooltip in the expanded sample view for [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") mask values (pixel values) using the new [`Dataset.mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.mask_targets "fiftyone.core.dataset.Dataset.mask_targets") and [`Dataset.default_mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_mask_targets "fiftyone.core.dataset.Dataset.default_mask_targets") fields

  * Fixed hiding, clearing, and only showing selected samples in the samples grid




Brain

  * Added a [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") method that uses embeddings and dimensionality reduction methods to generate interactive visualizations of the samples and/or labels in a dataset. Check out [this page](brain.md#brain-embeddings-visualization) for details. Features include:
    
    * Provide your own embeddings, or choose a model from the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo), or use the provided default model

    * Supported dimensionality reduction methods include [UMAP](https://github.com/lmcinnes/umap), [t-SNE](https://lvdmaaten.github.io/tsne), and [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

    * Use this capability in a Jupyter notebook and you can interact with the plots to select samples/labels of interest in a connected [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session")

  * Added support for saving brain method results on datasets. Previous brain results can now be loaded at any time via [`Dataset.load_brain_results()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.load_brain_results "fiftyone.core.dataset.Dataset.load_brain_results")

  * Added support for providing a custom [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") or model from the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) to [`compute_uniqueness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_uniqueness "fiftyone.brain.compute_uniqueness")




Core

  * Added a [`fiftyone.core.plots`](api__fiftyone.core.plots.md#module-fiftyone.core.plots "fiftyone.core.plots") module that provides a powerful API for visualizing datasets, including interactive plots when used in Jupyter notebooks. See [this page](user_guide__plots.md#interactive-plots) for more information. Highlights include:
    
    * [`plot_confusion_matrix()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.plot_confusion_matrix "fiftyone.core.plots.base.plot_confusion_matrix"): an interactive confusion matrix that can be attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") object to visually explore model predictions

    * [`scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.scatterplot "fiftyone.core.plots.base.scatterplot"): an interactive scatterplot of 2D or 3D points that can be attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") to explore the samples/labels in a dataset based on their locations in a low-dimensional embedding space

    * [`location_scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.location_scatterplot "fiftyone.core.plots.base.location_scatterplot"): an interactive scatterplot of a dataset via its [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") coordinates

    * Added [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") and [`GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations") label types that can be used to store arbitrary GeoJSON location data on samples

    * Added the [`GeoJSONDataset`](api__fiftyone.types.md#fiftyone.types.GeoJSONDataset "fiftyone.types.GeoJSONDataset") dataset type for importing and exporting datasets in GeoJSON format

    * Added [`SampleCollection.geo_near()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.geo_near "fiftyone.core.collections.SampleCollection.geo_near") and [`SampleCollection.geo_within()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.geo_within "fiftyone.core.collections.SampleCollection.geo_within") view stages for querying datasets with location data

  * Upgraded the implementation of the [FiftyOneDataset](user_guide__export_datasets.md#fiftyonedataset-export) format, which is now 10-100x faster at importing/exporting datasets

  * Added support for generating zip/tar/etc archives to [`SampleCollection.export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") by passing an archive path rather than a directory path

  * Added [`Dataset.from_archive()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_archive "fiftyone.core.dataset.Dataset.from_archive") and [`Dataset.add_archive()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_archive "fiftyone.core.dataset.Dataset.add_archive") factory methods for importing datasets stored in archives

  * Added support for saving evaluation results on a dataset. Results can now be loaded at any time via [`Dataset.load_evaluation_results()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.load_evaluation_results "fiftyone.core.dataset.Dataset.load_evaluation_results")

  * Added a `tags` attribute to all [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types that can store a list of string tags for the labels (analogous to the `tags` attribute of [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample"))

  * Added a number of methods for working with sample and label tags:
    
    * [`SampleCollection.tag_samples()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.tag_samples "fiftyone.core.collections.SampleCollection.tag_samples")

    * [`SampleCollection.untag_samples()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.untag_samples "fiftyone.core.collections.SampleCollection.untag_samples")

    * [`SampleCollection.count_sample_tags()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.count_sample_tags "fiftyone.core.collections.SampleCollection.count_sample_tags")

    * [`SampleCollection.tag_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.tag_labels "fiftyone.core.collections.SampleCollection.tag_labels")

    * [`SampleCollection.untag_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.untag_labels "fiftyone.core.collections.SampleCollection.untag_labels")

    * [`SampleCollection.count_label_tags()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.count_label_tags "fiftyone.core.collections.SampleCollection.count_label_tags")

  * **BREAKING CHANGE** : Renamed all applicable API components that previously referenced âobjectsâ to use the more widely applicable term âlabelsâ. Affected attributes, classes, and methods are:
    
    * [`Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels") (previously `selected_objects`)

    * [`SampleCollection.select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels") (previously `select_labels()`)

    * [`SampleCollection.select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_labels "fiftyone.core.collections.SampleCollection.exclude_labels") (previously `exclude_labels()`)

    * [`SelectLabels`](api__fiftyone.core.stages.md#fiftyone.core.stages.SelectLabels "fiftyone.core.stages.SelectLabels") (previously `SelectObjects`)

    * [`ExcludeLabels`](api__fiftyone.core.stages.md#fiftyone.core.stages.ExcludeLabels "fiftyone.core.stages.ExcludeLabels") (previously `ExcludeObjects`)

  * Added new keyword arguments `ids`, `tags`, and `fields` to [`SampleCollection.select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels") and [`SampleCollection.select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_labels "fiftyone.core.collections.SampleCollection.exclude_labels") and their corresponding view stages that enable easier-to-use selection of labels by their IDs or tags

  * Added [`Session.select_labels()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.select_labels "fiftyone.core.session.Session.select_labels") for programmatically selecting labels as well a setters for [`Session.selected`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected "fiftyone.core.session.Session.selected") and [`Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels")

  * Added [`Dataset.classes`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.classes "fiftyone.core.dataset.Dataset.classes") and [`Dataset.default_classes`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_classes "fiftyone.core.dataset.Dataset.default_classes") fields that enable storing class label lists at the dataset-level that can be automatically used by methods like [`Dataset.evaluate_classifications()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.evaluate_detections "fiftyone.core.dataset.Dataset.evaluate_detections") when knowledge of the full schema of a model is required

  * Added [`Dataset.mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.mask_targets "fiftyone.core.dataset.Dataset.mask_targets") and [`Dataset.default_mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_mask_targets "fiftyone.core.dataset.Dataset.default_mask_targets") fields for providing semantic labels for [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") mask values to be used in the Appâs expanded sample view

  * Improved the runtime of [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") by ~100x for image datasets and ~10x for video datasets

  * Added an [`Dataset.add_collection()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_collection "fiftyone.core.dataset.Dataset.add_collection") method for adding the contents of a [`SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to another [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * Added the trigonometric view expressions [`cos`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.cos "fiftyone.core.expressions.ViewExpression.cos"), [`sin`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.sin "fiftyone.core.expressions.ViewExpression.sin"), [`tan`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.tan "fiftyone.core.expressions.ViewExpression.tan"), [`cosh`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.cosh "fiftyone.core.expressions.ViewExpression.cosh") [`sinh`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.sinh "fiftyone.core.expressions.ViewExpression.sinh"), [`tanh`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.tanh "fiftyone.core.expressions.ViewExpression.tanh"), [`arccos`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.arccos "fiftyone.core.expressions.ViewExpression.arccos"), [`arcsin`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.arcsin "fiftyone.core.expressions.ViewExpression.arcsin"), [`arcan`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.arctan "fiftyone.core.expressions.ViewExpression.arctan") [`arccosh`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.arccosh "fiftyone.core.expressions.ViewExpression.arccosh"), [`arcsinh`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.arcsinh "fiftyone.core.expressions.ViewExpression.arcsinh"), and [`arctanh`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.arctanh "fiftyone.core.expressions.ViewExpression.arctanh")

  * Added a [`randn`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.randn "fiftyone.core.expressions.ViewExpression.randn") expression that can generate Gaussian random numbers

  * Fixed a bug that prevented [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") from being able to process video datasets

  * Added support for applying intensive view stages such as sorting to datasets whose database representation exceeds 100MB

  * Fixed schema errors in [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") instances that contain selected or excluded fields

  * Fixed copying of [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") instances where [`ViewField`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewField "fiftyone.core.expressions.ViewField") is used




Zoo

  * Added the [quickstart-geo](dataset_zoo__datasets__quickstart_geo.md#dataset-zoo-quickstart-geo) dataset to enable quick exploration of location-based datasets




CLI

  * Removed the `--desktop` flag from the [fiftyone app connect](https://docs.voxel51.com/cli/index.html#cli-fiftyone-app-connect) command




Docs

  * Added [a tutorial](tutorials__image_embeddings.md) demonstrating how to use [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") on image datasets

  * Added an [interactive plots](user_guide__plots.md#interactive-plots) page to the user guide

  * Added a [Tags and tagging](user_guide__app.md#app-tagging) section to the App user guide

  * Added a [visualizing embedding](brain.md#brain-embeddings-visualization) section to the Brain user guide




## FiftyOne 0.7.4#

_Released March 2, 2021_

App

  * Fixed a bug that prevented [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") updates from triggering App updates

  * Fixed hiding labels in the expanded sample view




Brain

  * Added support for tracking and cleaning up brain runs similar to how evaluations are tracked. See [`get_brain_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_brain_info "fiftyone.core.collections.SampleCollection.get_brain_info"), [`list_brain_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_brain_runs "fiftyone.core.collections.SampleCollection.list_brain_runs"), [`load_brain_view()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_brain_view "fiftyone.core.collections.SampleCollection.load_brain_view"), and [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") for details

  * Updated [`compute_mistakenness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_mistakenness "fiftyone.brain.compute_mistakenness") to use FiftyOneâs evaluation framework




Core

  * Decoupled loading video [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") and [`SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") and their frames so the samples are loaded efficiently and frames are only loaded when requested

  * Add a 90 character limit to progress bars in notebook contexts to prevent overflow issues

  * Added low-level utility methods [`list_datasets()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.list_datasets "fiftyone.core.odm.database.list_datasets") and [`delete_dataset()`](api__fiftyone.core.odm.database.md#fiftyone.core.odm.database.delete_dataset "fiftyone.core.odm.database.delete_dataset") for managing a corrupted database

  * Added automatic field generation for `labelbox_id_field` when using [`import_from_labelbox()`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.import_from_labelbox "fiftyone.utils.labelbox.import_from_labelbox")




CLI

  * Added a [dataset stats](https://docs.voxel51.com/cli/index.html#cli-fiftyone-datasets-stats) command




## FiftyOne 0.7.3#

_Released February 18, 2021_

App

  * Added filtering widgets to the Filters Sidebar for [`StringFields`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField") and [`BooleanFields`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")

  * Added histogram plots for [`StringFields`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField") and [`BooleanFields`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField") in the `Scalars` tab

  * Moved `None` selection for [`StringFields`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField") to the input format in the Filters Sidebar

  * Changed `None` options to only be present when `None` values exist for a supported [`Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") in the Filters Sidebar

  * Added `Color by label` support for [`Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification"), [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications"), [`BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField"), and [`StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")

  * Added support excluding selected values for a [`StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField") in the Fields Sidebar

  * Various style and interaction improvements in the Filters Sidebar

  * The App will no longer crash when samples whose source media is unsupported or missing are loaded




Core

  * Added [`evaluate_classifications()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_classifications "fiftyone.core.collections.SampleCollection.evaluate_classifications"), [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections"), and [`evaluate_segmentations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_segmentations "fiftyone.core.collections.SampleCollection.evaluate_segmentations") methods that provide support for evaluating various types of labels. See the new [evaluation page](user_guide__evaluation.md#evaluating-models) of the user guide for more details

  * Added [`one()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for retrieving one matched [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") from a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

  * Added support for cloning and saving views into video datasets via [`clone()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.clone "fiftyone.core.view.DatasetView.clone") and [`save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save")

  * Added support for extracting batches of frame-level and/or array fields via the [`values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values") aggregation

  * Added support for setting batches of frame-level and/or array fields via [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values")

  * Added support for accessing samples from a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") via the `dataset[filepath]` syntax

  * Added support for passing [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") and any [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") iterable, e.g. [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView"), to methods like `remove_samples()`, [`exclude()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude "fiftyone.core.collections.SampleCollection.exclude"), and [`select()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select "fiftyone.core.collections.SampleCollection.select")

  * Changed the default value for `only_matches` for `filter_classifications()`, `filter_detections()`, [`filter_field()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_field "fiftyone.core.collections.SampleCollection.filter_field"), [`filter_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_labels "fiftyone.core.collections.SampleCollection.filter_labels"), [`filter_keypoints()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_keypoints "fiftyone.core.collections.SampleCollection.filter_keypoints"), and `filter_polylines()` from `False` to `True`

  * [`compute_metadata()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_metadata "fiftyone.core.collections.SampleCollection.compute_metadata") will now gracefully skip samples for which media metadata cannot be computed

  * Added a [`stats()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.stats "fiftyone.core.dataset.Dataset.stats") method for listing helpful info about the size of various entities of a dataset




Zoo

  * Added support for storing logits for many [zoo models](https://docs.voxel51.com/model_zoo/index.html#model-zoo) when using [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model")

  * Default confidence thresholds for [zoo models](https://docs.voxel51.com/model_zoo/index.html#model-zoo) are now stored on a per-model basis rather than as a global default value in [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"). All detection models still have a default confidence threshold of 0.3, and all other model types have no default confidence threshold




CLI

  * Added a [migration API](https://docs.voxel51.com/installation/index.html#downgrading-fiftyone) to provide better support for downgrading the version of your `fiftyone` package




Docs

  * Added a new [evaluation page](user_guide__evaluation.md#evaluating-models) to the user guide that explains how to evaluate various types of models with FiftyOne

  * Removed legacy `--index` flags from the install instructions from the [troubleshooting page](installation__troubleshooting.md#troubleshooting) which prevented a valid installation




## FiftyOne 0.7.2#

_Released January 28, 2021_

App

  * Changed the Filters Sidebar label filters to only return matched samples, i.e., samples with at least one matching label with respect to a filter

  * Fixed a bug in Colab notebooks that allowed for the `.ipynb` file to grow unnecessarily large

  * Improved plotting of numeric fields in the `Scalars` tab, including `[min, max)` ranges for tooltips and integer binning when appropriate

  * Fixed a bug that prevented [`select_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_fields "fiftyone.core.collections.SampleCollection.select_fields") and [`exclude_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_fields "fiftyone.core.collections.SampleCollection.exclude_fields") from being properly respected by the Filters Sidebar

  * Fixed a bug that prevented selected samples from being cleared when modifying your view or choosing an option from the select samples dropdown

  * Added an [`AppConfig`](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") for configuring options like the color pool to use when drawing [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields. See [this page](user_guide__config.md#configuring-fiftyone-app) for more info




Core

  * Added the [`MapLabels`](api__fiftyone.core.stages.md#fiftyone.core.stages.MapLabels "fiftyone.core.stages.MapLabels") and [`SetField`](api__fiftyone.core.stages.md#fiftyone.core.stages.SetField "fiftyone.core.stages.SetField") view stages

  * Added the [`HistogramValues`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.HistogramValues "fiftyone.core.aggregations.HistogramValues") and [`Sum`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Sum "fiftyone.core.aggregations.Sum") aggregations

  * Added over a dozen new [`ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") methods including powerful transformations like [`map_values()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.map_values "fiftyone.core.expressions.ViewExpression.map_values"), [`reduce()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.reduce "fiftyone.core.expressions.ViewExpression.reduce"), and [`sort()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.sort "fiftyone.core.expressions.ViewExpression.sort")

  * Exposed all [`Aggregations`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") as single execution methods on the [`SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") interface, e.g., [`distinct()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.distinct "fiftyone.core.collections.SampleCollection.distinct")

  * Added support for all [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types in [`filter_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_labels "fiftyone.core.collections.SampleCollection.filter_labels")

  * Added support for generalized field paths (embedded fields, lists, etc) to the [`Bounds`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Bounds "fiftyone.core.aggregations.Bounds"), [`Count`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Count "fiftyone.core.aggregations.Count"), [`CountValues`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.CountValues "fiftyone.core.aggregations.CountValues"), and [`Distinct`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Distinct "fiftyone.core.aggregations.Distinct") aggregations

  * Removed the deprecated `ConfidenceBounds`, `CountLabels`, and `DistinctLabels` aggregations

  * Removed the redundant `match_tag()` stage in favor of [`match_tags()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match_tags "fiftyone.core.collections.SampleCollection.match_tags")

  * Removed `AggregationResult` classes in favor of returning [`Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") results directly as builtin types

  * Added the optional `config` keyword argument to [`launch_app()`](api__fiftyone.core.session.md#fiftyone.core.session.launch_app "fiftyone.core.session.launch_app") and [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") for overriding the default [AppConfig](user_guide__config.md#configuring-fiftyone-app).




Zoo

  * Added a default confidence threshold of `0.3` when applying models from the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) via [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), which omits spurious low quality predictions from many models




CLI

  * Added a [fiftyone app config](https://docs.voxel51.com/cli/index.html#cli-fiftyone-app-config) command for inspecting the default [App config](user_guide__config.md#configuring-fiftyone-app)

  * Improved `ctrl + c` exit handling for CLI commands




Docs

  * Added a [new section](user_guide__config.md#configuring-fiftyone-app) to the [Configuring FiftyOne guide](user_guide__config.md#configuring-fiftyone) explaining how to programmatically configure the Appâs behavior

  * Updated the [Dataset views guide](https://docs.voxel51.com/user_guide/using_views.html#using-views) to provide a thorough overview of new functionality provided by stages like [`SetField`](api__fiftyone.core.stages.md#fiftyone.core.stages.SetField "fiftyone.core.stages.SetField")

  * Updated the [Aggregations guide](https://docs.voxel51.com/user_guide/using_aggregations.html#using-aggregations) to provide a thorough overview and examples of various aggregation functionality, including advanced usage tips

  * Added an FAQ section providing instructions for working with [remote Jupyter notebooks](https://docs.voxel51.com/faq/index.html#faq-remote-notebook-support)

  * Added code examples to all [`ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") class docstrings and their corresponding sample collection methods, e.g., [`map_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.map_labels "fiftyone.core.collections.SampleCollection.map_labels")

  * Added code examples to all [`Aggregation`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Aggregation "fiftyone.core.aggregations.Aggregation") class docs and their corresponding sample collection methods, e.g., [`bounds()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.bounds "fiftyone.core.collections.SampleCollection.bounds")




## FiftyOne 0.7.1#

_Released January 8, 2021_

App

  * Added automatic screenshotting for [notebook environments](installation__environments.md#notebooks)

  * Fixed a bug where the Filters Sidebar statistics would not load for empty views

  * Fixed style inconsistencies in Firefox




Core

  * Added [`Session.freeze()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.freeze "fiftyone.core.session.Session.freeze") for manually screenshotting the active App in a notebook environment

  * Renamed `Dataset.clone_field()` to [`Dataset.clone_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_sample_field "fiftyone.core.dataset.Dataset.clone_sample_field") for consistency with other operations

  * Added a [`Dataset.clone_frame_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_frame_field "fiftyone.core.dataset.Dataset.clone_frame_field") method for cloning frame-level fields of video datasets

  * Added [`DatasetView.clone_sample_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.clone_sample_field "fiftyone.core.view.DatasetView.clone_sample_field") and [`DatasetView.clone_frame_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.clone_frame_field "fiftyone.core.view.DatasetView.clone_frame_field") methods that allow cloning views into sample fields (e.g., after filtering the labels in a list field)

  * Added a [`DatasetView.clone()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.clone "fiftyone.core.view.DatasetView.clone") method for cloning a view as a new dataset

  * Added a [`DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") method for saving a view, overwriting the contents of the underlying dataset

  * Re-implemented [`Dataset.clone_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_sample_field "fiftyone.core.dataset.Dataset.clone_sample_field") and [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") via efficient DB-only operations

  * Added the `overwrite` keyword argument to the [`Dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") constructor

  * Added a `database_dir` option to the [FiftyOne Config](user_guide__config.md#configuring-fiftyone)

  * Added a `default_app_port` option to the [FiftyOne Config](user_guide__config.md#configuring-fiftyone)




Zoo

  * Added a [CenterNet model](model_zoo__models__centernet_hg104_512_coco_tf2.md#model-zoo-centernet-hg104-512-coco-tf2) to the model zoo

  * Upgraded the [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) so that many detection models that previously required TensorFlow 1.X can now be used with TensorFlow 2.X

  * Added [Caltech-256](dataset_zoo__datasets__caltech256.md#dataset-zoo-caltech256) to the dataset zoo

  * Added [ImageNet Sample](dataset_zoo__datasets__imagenet_sample.md#dataset-zoo-imagenet-sample) to the dataset zoo

  * [Caltech-101](dataset_zoo__datasets__caltech101.md#dataset-zoo-caltech101) is now available natively in the dataset zoo without the TF backend

  * [KITTI](dataset_zoo__datasets__kitti.md#dataset-zoo-kitti) is now available natively in the dataset zoo without the TF backend

  * Fixed a bug that prevented [ImageNet 2012](dataset_zoo__datasets__imagenet_2012.md#dataset-zoo-imagenet-2012) from loading properly when using the TF backend




CLI

  * Added support for controlling the error level when [applying zoo models](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-apply)




Docs

  * Added a [Dataset Zoo listing](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo) that describes all datasets in the zoo

  * Added a [Model Zoo listing](https://docs.voxel51.com/model_zoo/index.html#model-zoo) that describes all models in the zoo




## FiftyOne 0.7.0#

_Released December 21, 2020_

App

  * Added web browser support, which is now the default setting

  * Added [IPython notebook support](installation__environments.md#notebooks), e.g. Jupyter and Google Colab

  * The desktop App can now be installed as an optional dependency

  * Fixed an issue where the App would freeze after filtering labels in the Filters Sidebar




Core

  * Added a [Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) containing over 70 pretrained detection, classification, and segmentation models that you can use to generate predictions and embeddings

  * Moved project hosting to [pypi.org](https://pypi.org/project/fiftyone/)

  * Added the [`Session.show()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.show "fiftyone.core.session.Session.show") method for displaying the App in IPython notebook cells

  * Added an in-App feedback form. We would love to hear from you!

  * Added Python 3.9 support

  * Removed Python 3.5 support




CLI

  * Added a [fiftyone zoo models](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models) command that provides access to the model zoo

  * Moved the dataset zoo commands to [fiftyone zoo datasets](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets) (previously they were at `fiftyone zoo`)

  * Added a `--desktop` flag to commands that launch the App that enables launching the App as a desktop App (rather than a web browser)




## FiftyOne 0.6.6#

_Released November 25, 2020_

App

  * Added a dropdown in the header to change datasets from the App

  * Added the ability to refresh the App by clicking the FiftyOne logo in the header

  * Fixed a bug the caused numeric (scalar field) range sliders to disappear after changing the default value

  * Fixed a bug that prevented the App state from updating appropriately after applying label filters




Brain

  * Added support for computing mistakenness for detections when using [`compute_mistakenness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_mistakenness "fiftyone.brain.compute_mistakenness")




Core

  * Fixed a bug that prevented COCO datasets from being loaded from the [Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo)




CLI

  * Added support for customizing the local port when connecting to the App via the CLI

  * Added an `--ssh-key` option to the `app connect` command




Docs

  * Added [a tutorial](tutorials__detection_mistakes.md) demonstrating how to use [`compute_mistakenness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_mistakenness "fiftyone.brain.compute_mistakenness") to detect label mistakes for detection datasets

  * Added questions to the [FAQ page](https://docs.voxel51.com/faq/index.html#faq):
    
    * [Can I launch multiple App instances on a machine?](https://docs.voxel51.com/faq/index.html#faq-multiple-apps)

    * [Can I connect multiple App instances to the same dataset?](https://docs.voxel51.com/faq/index.html#faq-multiple-sessions-same-dataset)

    * [Can I connect to multiple remote sessions?](https://docs.voxel51.com/faq/index.html#faq-connect-to-multiple-remote-sessions)

    * [Can I serve multiple remote sessions from a machine?](https://docs.voxel51.com/faq/index.html#faq-serve-multiple-remote-sessions)




## FiftyOne 0.6.5#

_Released November 16, 2020_

App

  * Added concurrency to the server which greatly improves loading speeds and time-to-interaction in the Grid, View Bar, and Filters Sidebar for larger datasets and views

  * Renamed the Display Options Sidebar to the Filters Sidebar

  * Added support for coloring by `label` value in the Filters Sidebar

  * Added support for filtering [`keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint"), [`keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), [`polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), [`polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields by `label` value in the Filters Sidebar

  * Moved plot tabs into an expandable window that can be resized and maximized. This allows for viewing distributions and the sample grid at the same time

  * Fixed video loading in the grid and modal for video samples with metadata

  * Fixed showing and hiding samples in the select sample menu

  * Fixed a memory usage bug in the sample grid




Core

  * Added [Cityscapes](https://www.cityscapes-dataset.com/) and [LFW](http://vis-www.cs.umass.edu/lfw) to the [Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo)

  * Added support for renaming and deleting embedded document fields of samples via [`Dataset.rename_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_sample_field "fiftyone.core.dataset.Dataset.rename_sample_field") and [`Dataset.delete_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_sample_field "fiftyone.core.dataset.Dataset.delete_sample_field")

  * Added support for renaming and deleting embedded document fields of frames of video samples via [`Dataset.rename_frame_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_frame_field "fiftyone.core.dataset.Dataset.rename_frame_field") and [`Dataset.delete_frame_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_frame_field "fiftyone.core.dataset.Dataset.delete_frame_field")

  * Added support for deleting fields and embedded fields of individual samples via [`Sample.clear_field()`](api__fiftyone.core.sample.md#fiftyone.core.sample.Sample.clear_field "fiftyone.core.sample.Sample.clear_field") and `del sample[field_name]`

  * Added support for deleting fields and embedded fields of frame labels via [`Frame.clear_field()`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame.clear_field "fiftyone.core.frame.Frame.clear_field") and `del frame[field_name]`

  * Added support for reading/writing video datasets in JSON format via [`Dataset.from_json()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_json "fiftyone.core.dataset.Dataset.from_json") and [`SampleCollection.write_json()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.write_json "fiftyone.core.collections.SampleCollection.write_json"), respectively

  * Added [`a module`](api__fiftyone.utils.scale.md#module-fiftyone.utils.scale "fiftyone.utils.scale") for importing and exporting annotations from [Scale AI](https://scale.com)

  * Added [`a module`](api__fiftyone.utils.labelbox.md#module-fiftyone.utils.labelbox "fiftyone.utils.labelbox") for importing and exporting annotations from [Labelbox](https://labelbox.com)

  * Fixed a bug that prevented [`Dataset.add_sample()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_sample "fiftyone.core.dataset.Dataset.add_sample") and [`Dataset.add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples") from working properly when provided samples that belong to other sample collections

  * Fixed a bug that prevented frame labels from being properly cloned when calling [`Dataset.clone()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone "fiftyone.core.dataset.Dataset.clone") on video datasets




Docs

  * Added an [Environments page](installation__environments.md#environments) that outlines how to work with local, remote, and cloud data. Includes instructions for AWS, Google Cloud, and Azure

  * Add an [FAQ page](https://docs.voxel51.com/faq/index.html#faq)




## FiftyOne 0.6.4#

_Released October 29, 2020_

App

  * Improved page load times for video datasets

  * Improved support for frame- and sample-level labels in display options for video datasets

  * Added support for all label types in the labels distributions tab

  * Added support for selecting and hiding labels in the sample modal




Brain

  * Added support for computing uniqueness within regions-of-interest specified by a set of detections/polylines when using [`compute_uniqueness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_uniqueness "fiftyone.brain.compute_uniqueness")




Core

  * Added the [`filter_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_labels "fiftyone.core.collections.SampleCollection.filter_labels") view stage, which supersedes the old dedicated per-label-type filtering stages

  * Added [`select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels") and [`exclude_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_labels "fiftyone.core.collections.SampleCollection.exclude_labels") to select or exclude labels from a dataset or view

  * Added an [`aggregations framework`](api__fiftyone.core.aggregations.md#module-fiftyone.core.aggregations "fiftyone.core.aggregations") for computing aggregate values via [`aggregate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.aggregate "fiftyone.core.collections.SampleCollection.aggregate")

  * Added the [`selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels") session attribute, which holds the currently selected labels in the App

  * Added support for [`adding`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_frame_field "fiftyone.core.dataset.Dataset.add_frame_field"), [`renaming`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_frame_field "fiftyone.core.dataset.Dataset.rename_frame_field"), and [`deleting`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_frame_field "fiftyone.core.dataset.Dataset.delete_frame_field") frame-level fields of video datasets

  * Added the [`TorchImagePatchesDataset`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImagePatchesDataset "fiftyone.utils.torch.TorchImagePatchesDataset") that emits tensors of patches extracted from images defined by sets of [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") associated with the images




## FiftyOne 0.6.3#

_Released October 20, 2020_

App

  * Added sample-level display options stats, filtering, and toggling for video datasets




Core

  * Added support for [importing](user_guide__import_datasets.md#videoclassificationdirectorytree-import) and [exporting](user_guide__export_datasets.md#videoclassificationdirectorytree-export) video classification datasets organized as directory trees on disk

  * Added [BDD100K](http://bdd-data.berkeley.edu), [HMDB51](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database), and [UCF101](https://www.crcv.ucf.edu/research/data-sets/ucf101) to the [Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo)

  * Added new versions of [COCO](https://cocodataset.org/#home) that contain instance segmentations to the [Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo)

  * Added utilities for selecting labels from datasets via the Python library

  * Added a boolean `only_matches` parameter to all filter stages that enables the user to specify that a view should only contain samples that match the given filter

  * Improved performance when ingesting video datasets with frame-level labels

  * Added a [`reencode_videos()`](api__fiftyone.utils.video.md#fiftyone.utils.video.reencode_videos "fiftyone.utils.video.reencode_videos") utility to re-encode the videos in a sample collection so that they are visualizable in the FiftyOne App




## FiftyOne 0.6.2#

_Released October 15, 2020_

App

  * Improved page and grid load times for video datasets by around 10x

  * Added filtering, toggling, and statistics for labels with respect to the frame schema in the display options sidebars for video datasets

  * Added margins to the grid view for both image and video datasets

  * Fixed list parameter input submission in the view bar

  * Fixed an issue causing some label counts to be incorrect after filters are applied

  * Added support for using the keyboard to select labels when filtering




Brain

  * [`compute_uniqueness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_uniqueness "fiftyone.brain.compute_uniqueness") and [`compute_hardness()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_hardness "fiftyone.brain.compute_hardness") now support multilabel classification tasks




Core

  * [`Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") instances can now represent labels composed of multiple shapes

  * Segmentations can now be [imported](user_guide__import_datasets.md#cocodetectiondataset-import) and [exported](user_guide__export_datasets.md#cocodetectiondataset-export) when using [COCO Object Detection Format](https://cocodataset.org/#format-data).

  * Polylines and keypoints can now be [imported](user_guide__import_datasets.md#cvatimagedataset-import) and [exported](user_guide__export_datasets.md#cvatimagedataset-export) when using [CVAT image format](https://github.com/openvinotoolkit/cvat/blob/develop/cvat/apps/documentation/xml_format.md)

  * Polylines and keypoints can now be [imported](user_guide__import_datasets.md#cvatvideodataset-import) and [exported](user_guide__export_datasets.md#cvatvideodataset-export) when using [CVAT video format](https://github.com/openvinotoolkit/cvat/blob/develop/cvat/apps/documentation/xml_format.md)

  * Added support for rendering annotated versions of video samples with their frame labels overlaid via [`draw_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.draw_labels "fiftyone.core.collections.SampleCollection.draw_labels")

  * Added support for [launching quickstarts](https://docs.voxel51.com/cli/index.html#cli-fiftyone-quickstart) as remote sessions

  * Added [`Frames.update()`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frames.update "fiftyone.core.frame.Frames.update") and [`Frames.merge()`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frames.merge "fiftyone.core.frame.Frames.merge") methods to replace and merge video frames, respectively

  * Fixed [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") to properly merge the frame-by-frame contents of video samples

  * Fixed a bug where [`sample.copy()`](api__fiftyone.core.sample.md#fiftyone.core.sample.Sample.copy "fiftyone.core.sample.Sample.copy") would not create a copy of the frames of a video sample




## FiftyOne 0.6.1#

_Released October 7, 2020_

App

  * Added support for visualizing keypoints, polylines, and segmentation masks

  * Added autocompletion when selecting `SortBy` fields in the view bar

  * Added support for viewing `index` fields of [`Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") labels in the media viewer, if present

  * Fixed counting of [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields in the expanded sample view

  * Fixed a bug that prevented label filters from fully resetting when a `reset` or `clear` button is pressed




Core

  * Added support for storing [`keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint"), [`polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), and [`segmentation masks`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") on samples

  * Added support for setting an `index` attribute on [`Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") instances that defines a unique identifier for an object (e.g., across frames of a video)

  * Added support for [importing](user_guide__import_datasets.md#yolov4dataset-import) and [exporting](user_guide__export_datasets.md#yolov4dataset-export) datasets in [YOLOv4 format](https://github.com/AlexeyAB/darknet)

  * Added support for [importing](user_guide__import_datasets.md#cvatvideodataset-import) and [exporting](user_guide__export_datasets.md#cvatvideodataset-export) datasets in [CVAT video format](https://github.com/openvinotoolkit/cvat/blob/develop/cvat/apps/documentation/xml_format.md)

  * Added support for [importing](user_guide__import_datasets.md#fiftyonedataset-import) and [exporting](user_guide__export_datasets.md#fiftyonedataset-export) video datasets in [`FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format

  * Added frame field schemas to string representations for video datasets/views




CLI

  * Added options to [fiftyone datasets delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-datasets-delete) to delete all datasets matching a pattern and all non-persistent datasets




Docs

  * Added a recipe for [merging datasets](recipes__merge_datasets.md)

  * Fixed some table widths and other display issues




## FiftyOne 0.6.0#

_Released October 1, 2020_

App

  * Added support for visualizing video datasets in the App




Core

  * Added support for [storing frame labels](https://docs.voxel51.com/user_guide/using_datasets.html#video-datasets) on video samples

  * Added support for [importing](user_guide__import_datasets.md#videodirectory-import) and [exporting](user_guide__export_datasets.md#videodirectory-export) datasets of unlabeled videos

  * Added support for [importing](user_guide__import_datasets.md#fiftyonevideolabelsdataset-import) and [exporting](user_guide__export_datasets.md#fiftyonevideolabelsdataset-export) labeled video datasets in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).

  * Added support for [importing](user_guide__import_datasets.md#writing-a-custom-dataset-importer) and [exporting](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) video datasets in custom formats

  * Improved the performance of [`Dataset.rename_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_sample_field "fiftyone.core.dataset.Dataset.rename_sample_field")

  * Added support for using disk space when running aggregation pipelines on large datasets

  * Added support for automatically creating database indexes when sorting by sample fields, for efficiency

  * Fixed issues with serializing vector fields and numpy arrays




## FiftyOne 0.5.6#

_Released September 23, 2020_

App

  * Added autocompletion to view bar stage fields that accept field names (for example, [`Exists`](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists "fiftyone.core.stages.Exists"))

  * Fixed an issue that would prevent datasets with no numeric labels or scalars from loading in the App

  * Fixed an error that could occur when a view included no samples

  * Added notifications in the App that are displayed if errors occur on the backend

  * Improved keyboard navigation between view bar stages




Core

  * Added support for loading (possibly-randomized) subsets of datasets when importing them via [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances, or via factory methods such as [`Dataset.from_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_dir "fiftyone.core.dataset.Dataset.from_dir")

  * Added support for optionally skipping unlabeled images when importing image datasets via [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") instances

  * Added a [`Dataset.merge_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.merge_samples "fiftyone.core.dataset.Dataset.merge_samples") method for merging samples in datasets via joining by `filepath`

  * Added a [`Dataset.rename_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_sample_field "fiftyone.core.dataset.Dataset.rename_sample_field") method for renaming sample fields of datasets




## FiftyOne 0.5.5#

_Released September 15, 2020_

App

  * Added support for filtering samples by numeric fields in the sidebar

  * Confidence bounds are now computed for the confidence slider in the label filter - a `[0, 1]` range is no longer assumed

  * Fixed an issue that would cause certain stages to be reevaluated when the view bar was edited

  * Improved responsiveness when adding stages in the view bar, filtering, and selecting samples

  * Simplified placeholders in the view bar

  * Added support for filtering sample JSON in the expanded sample view to match the labels displayed in the media viewer

  * Updated the instructions that appear when starting the App before connecting to a session




Core

  * Added support for [`Session.wait()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.wait "fiftyone.core.session.Session.wait") for remote sessions, to make starting a remote session from a script easier




## FiftyOne 0.5.4#

_Released September 9, 2020_

App

  * Added support for selecting/excluding samples from the current view in the App by selecting them and then choosing the appropriate option from a sample selection menu

  * Added autocomplete when creating new stages in the view bar

  * Updated the look-and-feel of the view bar to clarify when a stage and/or the entire view bar are active, and to make the bar more visually consistent with the rest of the App

  * Media viewer options are maintained while browsing between samples in expanded sample view

  * Improved the look-and-feel of confidence sliders when filtering labels

  * Limited floating point numbers to three decimals when rendering them in the media viewer

  * Fixed some bugs related to content overflow in the view bar




Core

  * Added support for exporting [`Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") labels in dataset formats that expect [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") labels

  * Added support for importing/exporting supercategories for datasets in [COCO format](user_guide__import_datasets.md#cocodetectiondataset-import)




## FiftyOne 0.5.3#

_Released September 1, 2020_

App

  * Added support for filtering labels in the expanded sample view

  * Added support for displaying detection attributes in the expanded sample view

  * Added an option to display confidence when viewing labels in the expanded sample view

  * Updated look-and-feel of display options in the expanded sample view to match the main image grid view

  * Adopting a default color palette for sample fields in the App that ensures that they are visually distinct

  * Fixed a bug that prevented the App from loading empty views

  * Fixed a bug that prevented the view bar from using default values for some stage parameters




Core

  * Added support for checking that a field _does not_ exist via a new boolean parameter of the [`exists()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exists "fiftyone.core.collections.SampleCollection.exists") view stage

  * Fixed a bug that prevented FiftyOne from starting for some Windows users

  * Fixed a bug that caused [`take()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.take "fiftyone.core.collections.SampleCollection.take") and [`shuffle()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.shuffle "fiftyone.core.collections.SampleCollection.shuffle") view stages with random seeds to be regenerated when handing off between the App and Python shell




## FiftyOne 0.5.2#

_Released August 26, 2020_

App

  * Added a label filter to the App that allows you to interactively explore your labels, investigating things like confidence thresholds, individual classes, and more, directly from the App

  * Added an App error page with support for refreshing the App if something goes wrong

  * The App can now be closed and reopened within the same session




Core

  * Added a [fiftyone quickstart](https://docs.voxel51.com/cli/index.html#cli-fiftyone-quickstart) command that downloads a small dataset, launches the App, and prints some suggestions for exploring the dataset

  * Added support for multiple simultaneous FiftyOne processes. You can now operate multiple App instances (using different ports), Python shells, and/or CLI processes.

  * Added support for automatically expanding labels from multitask formats such as [BDDDataset](user_guide__import_datasets.md#bdddataset-import) and [FiftyOneImageLabelsDataset](user_guide__import_datasets.md#fiftyoneimagelabelsdataset-import) into separate label fields when importing datasets

  * Added support for exporting multiple label fields in supported formats such as [BDDDataset](user_guide__export_datasets.md#bdddataset-export) and [FiftyOneImageLabelsDataset](user_guide__export_datasets.md#fiftyoneimagelabelsdataset-export) via the [`export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") method

  * Added support for filtering fields via the [`filter_field()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.filter_field "fiftyone.core.collections.SampleCollection.filter_field") method

  * Provided a more helpful error message when using the [Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo) with no backend ML framework installed

  * Made `pycocotools` an optional dependency to make installation on Windows easier




Docs

  * Updated the [evaluate object detections](tutorials__evaluate_detections.md) tutorial to make it more friendly for execution on CPU-only machines

  * Refreshed all App-related media in the docs to reflect the new App design introduced in v0.5.0




## FiftyOne 0.5.1#

_Released August 18, 2020_

App

  * Statistics in the display options sidebar now reflect the current [view](https://docs.voxel51.com/user_guide/using_views.html#using-views), not the entire [dataset](https://docs.voxel51.com/user_guide/using_datasets.html#using-datasets)

  * Improved image tiling algorithm that prevents single images from filling an entire grid row

  * Added support for toggling label visibility within the expanded sample modal

  * Improved display of long label and tag names throughout the app

  * Enhanced view bar functionality, including keyword arguments, type annotations, error messages, help links, and overall stability improvements

  * Added keyboard shortcuts for interacting with the view bar:
    
    * `DEL` and `BACKSPACE` delete the raised (active) stage

    * `ESC` toggles focus on the ViewBar, which activates shortcuts

    * `TAB`, `ENTER`, and `ESC` submits stage input fields

    * `LEFT` and `RIGHT ARROW` traverses view stages and add-stage buttons

    * `SHIFT + LEFT ARROW` and `SHIFT + RIGHT ARROW` traverse stages




Core

  * Greatly improved the performance of loading dataset samples from the database

  * Added support for [`renaming`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.name "fiftyone.core.dataset.Dataset.name") and [`cloning`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone "fiftyone.core.dataset.Dataset.clone") datasets

  * Added more string matching operations when [querying samples](https://docs.voxel51.com/user_guide/using_views.html#querying-samples), including [`starts_with()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.starts_with "fiftyone.core.expressions.ViewExpression.starts_with"), [`ends_with()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.ends_with "fiftyone.core.expressions.ViewExpression.ends_with"), [`contains_str()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.contains_str "fiftyone.core.expressions.ViewExpression.contains_str") and [`matches_str()`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression.matches_str "fiftyone.core.expressions.ViewExpression.matches_str")




Docs

  * Added a tutorial demonstrating performing error analysis on the [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html) powered by FiftyOne




## FiftyOne 0.5.0#

_Released August 11, 2020_

News

  * FiftyOne is now open source! Read more about this exciting development [in this press release](https://voxel51.com/press/fiftyone-open-source-launch)




App

  * Major design refresh, including a [new look-and-feel for the App](https://voxel51.com/docs/fiftyone/_static/images/release-notes/v050_release_app.png)

  * Added view bar that supports constructing dataset views directly in the App

  * Redesigned expanded sample view:
    
    * Improved look-and-feel, with modal-style form factor

    * Added support for maximizing the media player

    * Added support for maximizing the raw sample view

    * Added arrow controls to navigate between samples




Core

  * Added support for [importing](user_guide__import_datasets.md#fiftyonedataset-import) and [exporting](user_guide__export_datasets.md#fiftyonedataset-export) FiftyOne datasets via the [`FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") type

  * Added a [`Dataset.info`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.info "fiftyone.core.dataset.Dataset.info") field that can be used to store dataset-level info in FiftyOne datasets

  * Added a [`shuffle()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.shuffle "fiftyone.core.collections.SampleCollection.shuffle") view stage for randomly shuffling the samples in a dataset

  * Upgraded the [`take()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.take "fiftyone.core.collections.SampleCollection.take") view stage so that each instance of a view maintains a deterministic set of samples




## FiftyOne 0.4.1#

_Released August 4, 2020_

Core

  * Added a powerful [`fiftyone.core.expressions`](api__fiftyone.core.expressions.md#module-fiftyone.core.expressions "fiftyone.core.expressions") module for constructing complex DatasetView [`match()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.match "fiftyone.core.collections.SampleCollection.match"), [`sort_by()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by "fiftyone.core.collections.SampleCollection.sort_by"), etc. stages

  * Added an `evaluate_detections()` utility for evaluating object detections in FiftyOne datasets

  * Adding support for rendering annotated versions of sample data with their labels overlaid via a [`draw_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.draw_labels "fiftyone.core.collections.SampleCollection.draw_labels") method




Docs

  * Added [a tutorial](tutorials__evaluate_detections.md) demonstrating object detection evaluation workflows powered by FiftyOne

  * Added [full documentation](https://docs.voxel51.com/user_guide/using_views.html) for constructing DatasetViews with powerful matching, filtering, and sorting operations

  * Added [a recipe](recipes__draw_labels.md) showing how to render annotated versions of samples with label field(s) overlaid

  * Upgraded [data import docs](user_guide__import_datasets.md) to simplify the material and make it easier to find the creation strategy of interest

  * Improved layout of [tutorials](https://docs.voxel51.com/tutorials/index.html), [recipes](https://docs.voxel51.com/recipes/index.html), and [user guide](https://docs.voxel51.com/user_guide/index.html) landing pages




## FiftyOne 0.4.0#

_Released July 21, 2020_

App

  * Fixed an issue that could cause launching the App to fail on Windows under Python 3.6 and older




Core

  * Added support for importing datasets in custom formats via the [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") interface

  * Added support for exporting datasets to disk in custom formats via the [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") interface

  * Added support for parsing individual elements of samples in the [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser") interface

  * Added an option to image loaders in [`fiftyone.utils.torch`](api__fiftyone.utils.torch.md#module-fiftyone.utils.torch "fiftyone.utils.torch") to convert images to RGB

  * Fixed an issue where [`Dataset.delete_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_sample_field "fiftyone.core.dataset.Dataset.delete_sample_field") would not permanently delete fields if they were modified after deletion

  * Improved the string representation of [`ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") instances




Docs

  * Added a recipe demonstrating how to [convert datasets](recipes__convert_datasets.md) on disk between common formats

  * Added recipes demonstrating how to write your own [custom dataset importers](recipes__custom_importer.md), [custom dataset exporters](recipes__custom_exporter.md), and [custom sample parsers](recipes__custom_parser.md)

  * Added a [Configuring FiftyOne](user_guide__config.md) page to the User Guide that explains how to customize your FiftyOne Config




## FiftyOne 0.3.0#

_Released June 24, 2020_

App

  * Fixed an issue that could prevent the App from connecting to the FiftyOne backend




Core

  * Added support for importing and exporting datasets in several common formats:
    
    * COCO: [`COCODetectionDataset`](api__fiftyone.types.md#fiftyone.types.COCODetectionDataset "fiftyone.types.COCODetectionDataset")

    * VOC: [`VOCDetectionDataset`](api__fiftyone.types.md#fiftyone.types.VOCDetectionDataset "fiftyone.types.VOCDetectionDataset")

    * KITTI: [`KITTIDetectionDataset`](api__fiftyone.types.md#fiftyone.types.KITTIDetectionDataset "fiftyone.types.KITTIDetectionDataset")

    * Image classification TFRecords: [`TFImageClassificationDataset`](api__fiftyone.types.md#fiftyone.types.TFImageClassificationDataset "fiftyone.types.TFImageClassificationDataset")

    * TF Object Detection API TFRecords: [`TFObjectDetectionDataset`](api__fiftyone.types.md#fiftyone.types.TFObjectDetectionDataset "fiftyone.types.TFObjectDetectionDataset")

    * CVAT image: [`CVATImageDataset`](api__fiftyone.types.md#fiftyone.types.CVATImageDataset "fiftyone.types.CVATImageDataset")

    * Berkeley DeepDrive: [`BDDDataset`](api__fiftyone.types.md#fiftyone.types.BDDDataset "fiftyone.types.BDDDataset")

  * Added [`Dataset.add_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_dir "fiftyone.core.dataset.Dataset.add_dir") and [`Dataset.from_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_dir "fiftyone.core.dataset.Dataset.from_dir") to allow for importing datasets on disk in any supported format

  * Added a [`convert_dataset()`](api__fiftyone.utils.data.converters.md#fiftyone.utils.data.converters.convert_dataset "fiftyone.utils.data.converters.convert_dataset") method to convert between supported dataset formats

  * Added support for downloading COCO 2014/2017 through the FiftyOne Dataset Zoo via the Torch backend




CLI

  * Added `fiftyone convert` to convert datasets on disk between any supported formats

  * Added `fiftyone datasets head` and `fiftyone datasets tail` to print the head/tail of datasets

  * Added `fiftyone datasets stream` to stream the samples in a dataset to the terminal with a `less`-like interface

  * Added `fiftyone datasets export` to export datasets in any available format




## FiftyOne 0.2.1#

_Released June 19, 2020_

Core

  * Added preliminary Windows support

  * [`Dataset.add_images_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_images_dir "fiftyone.core.dataset.Dataset.add_images_dir") now skips non-images

  * Improved performance of adding samples to datasets




CLI

  * Fixed an issue that could cause port forwarding to hang when initializing a remote session




## FiftyOne 0.2.0#

_Released June 12, 2020_

App

  * Added distribution graphs for label fields

  * Fixed an issue causing cached images from previously-loaded datasets to be displayed after loading a new dataset




Core

  * Added support for persistent datasets

  * Added a class-based view stage approach via the [`ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") interface

  * Added support for serializing collections as JSON and reading datasets from JSON

  * Added support for storing numpy arrays in samples

  * Added a config option to control visibility of progress bars

  * Added progress reporting to [`Dataset.add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples")

  * Added a [`SampleCollection.compute_metadata()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_metadata "fiftyone.core.collections.SampleCollection.compute_metadata") method to enable population of the `metadata` fields of samples

  * Improved reliability of shutting down the App and database services

  * Improved string representations of [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") and [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects




CLI

  * Added support for creating datasets and launching the App




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
