---
source_url: https://docs.voxel51.com/enterprise/data_quality.html
---

# Data Quality#

The Data Quality panel is a builtin feature of the [FiftyOne Enterprise App](enterprise__app.md#enterprise-app) that automatically scans your dataset for common quality issues and helps you explore and take action to resolve them.

## Data Quality panel#

You can open the Data Quality panel by clicking the â+â icon next to the Samples tab.

The panelâs home page shows a list of the available issue types and their current analysis/review status:

  * **Brightness** : scans for images that are unusually bright or dim

  * **Blurriness** : scans for images that are abnormally blurry or sharp

  * **Aspect Ratio** : scans for images that have extreme aspect ratios

  * **Entropy** : scans for images that have unusually small or large entropy

  * **Near Duplicates** : leverages embeddings to scan for [near-duplicate samples](brain.md#brain-near-duplicates) in your dataset

  * **Exact Duplicates** : uses filehashes to scan your dataset for duplicate data with either the same or different filenames




Click on the right arrow of an issue typeâs card to open its expanded view.

![data-quality-home](../_images/data_quality_home.png)

## Scanning for issues#

If you have not yet scanned a dataset for a given issue type, youâll see a landing page like this:

![data-quality-brightness-scan](../_images/data_quality_brightness_scan.png)

Clicking the âScan Datasetâ button presents two choices for execution:

![data-quality-brightness-scan-options](../_images/data_quality_brightness_scan_options.png)

Note

The âExecuteâ option is **only for testing**. In this mode, computation is performed synchronously and will timeout if it does not complete within a few minutes.

Choose âScheduleâ for all production data, which schedules the scan for [delegated execution](enterprise__plugins.md#enterprise-delegated-operations) on your compute cluster.

While a scan is in-progress, youâll see a status page like this:

![data-quality-brightness-scheduled](../_images/data_quality_brightness_scheduled.png)

Click the link in the notification to navigate to the datasetâs [Runs page](enterprise__plugins.md#enterprise-managing-delegated-operations) where you can monitor the status of the task.

## Analyzing scan results#

Once an issue scan is complete, its card will update to display an interactive histogram that you can use to analyze the findings:

![data-quality-brightness-analysis](../_images/data_quality_brightness_analysis.png)

Note

When analyzing issue scan results, we recommend using the split screen icon to the right of the Samples panel tab to arrange the Samples panel and Data Quality panel side-by-side, as shown above.

Each issue typeâs results are stored under a dedicated field of the dataset, from which the displayed histograms are generated:

  * **Brightness** : the brightness of each image is stored in a `brightness` field of the sample

  * **Blurriness** : the blurriness of each image is stored in a `blurriness` field of the sample

  * **Aspect Ratio** : the aspect ratio of each image is stored in an `aspect_ratio` field of the sample

  * **Entropy** : the entropy of each image is stored in an `entropy` field of the sample

  * **Near Duplicates** : the nearest neighbor distance of each sample is stored in a `nearest_neighbor` field of the sample

  * **Exact Duplicates** : the filehash of each image is stored in a `filehash` field of the sample




Each issue type comes with a default threshold range that highlights potential issues in your dataset. If issues are identified, the number of potential issues will be displayed in the top-left corner of the Data Quality panel and the Samples panel will automatically update to show the corresponding samples in the grid.

You can also use the threshold slider to manually explore different threshold ranges. When you release the slider, the Samples panel will automatically update to show the corresponding samples:

![data-quality-brightness-slider](../_images/data_quality_brightness_slider.gif)

If you find a better threshold for a dataset, you can save it via the âSave Thresholdâ option under the settings menu. You can use âReset Thresholdâ to the revert to the default threshold at any time.

Once youâve reviewed the potential issues in the grid, you can use the âAdd Tagsâ button to take action on them. Clicking the button will display a modal like this:

![data-quality-brightness-tag](../_images/data_quality_brightness_tag.png)

Note

If youâve selected samples in the grid, only those samples will be tagged. Otherwise, tags will be added to all samples in your current view (i.e., all potential issues).

You can use the âsample tagsâ filter in the [Appâs sidebar](user_guide__app.md#app-fields-sidebar) to retrieve, review, and act on all samples that youâve previously tagged.

The review status indicator in the top-right corner of the panel indicates whether an issue type is currently âIn Reviewâ or âReviewedâ. You can click on it at any time to toggle the review status.

If you navigate away from an issue type that is currently âIn Reviewâ, youâll be prompted to indicate whether or not youâd like to mark the issue type as âReviewedâ:

![data-quality-brightness-mark-as-reviewed](../_images/data_quality_brightness_mark_as_reviewed.png)

## Updating a scan#

The Data Quality panel gracefully adapts to changes in your datasets after scans have been performed.

If you delete samples from a dataset, the histograms of any existing scans will automatically be updated to reflect the new distribution.

If you add new samples to a dataset or clear some existing field values associated with a scan (e.g., `brightness` field values for brightness scans), the panel will automatically detect the presence of unscanned samples and will display contextual information from the home page and analysis page:

![data-quality-new-samples-home](../_images/data_quality_new_samples_home.png)

To update an existing scan, open the issue type and click the âScan New Samplesâ button in the bottom-right corner of the analysis page. This will open a modal that provides additional context and prompts you to initiate the new samples scan:

![data-quality-new-samples-modal](../_images/data_quality_new_samples_modal.png)

## Deleting a scan#

You can delete an issue scan by simply deleting the corresponding field from the dataset (e.g., `brightness` for brightness scans).

Note

Did you know? You can delete sample fields from the App using the `delete_sample_field` operator available via the [Operator browser](plugins__using_plugins.md#using-operators).

IN THIS ARTICLE 
