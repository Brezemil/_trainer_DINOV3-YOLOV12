---
source_url: https://docs.voxel51.com/getting_started/depth_estimation/summary.html
---

# Summary: What Youâve Learned#

Congratulations! Youâve completed the Depth Estimation Guide. Letâs recap what youâve accomplished and explore where you can go next.

## Step-by-Step Recap#

**Step 1: Loading Depth Data** You learned how to load depth estimation datasets in FiftyOne, working with both NumPy-based depth maps (DIODE dataset) and image-based depth maps (NYU Depth V2). This included understanding depth validity masks, computing appropriate visualization ranges, and using `group_by()` to create video-like visualizations from sequential frame data. **Step 2: Using Depth Estimation Models** You explored multiple approaches to running depth estimation models including FiftyOneâs Model Zoo integration, manual Hugging Face integration, community plugins like DepthPro, and the Diffusers library. You learned how to store predictions as Heatmaps and compare multiple model outputs.

## Suggested Exercises#

  1. **Multi-Model Comparison** : Run different depth estimation models on the same dataset and compare their predictions. Which model performs best for indoor vs outdoor scenes?
  2. **Custom Dataset Loading** : Load your own depth dataset into FiftyOne and structure it with appropriate metadata.
  3. **Validity Mask Analysis** : For datasets with validity masks, analyze what percentage of pixels have valid depth measurements.
  4. **Sequential Grouping** : Experiment with different grouping strategies for datasets with sequential frames.
  5. **Dataset Curation** : Use FiftyOneâs filtering capabilities to curate training datasets by scene type, depth range, or quality characteristics.



## Resources and Further Reading#

  * [FiftyOne Documentation](https://docs.voxel51.com/)
  * [FiftyOne Depth Estimation Tutorial](https://docs.voxel51.com/tutorials/monocular_depth_estimation.html)
  * [Heatmap API Reference](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap)
  * [DIODE Dataset](https://diode-dataset.org/)
  * [NYU Depth Dataset V2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html)
  * [Hugging Face Depth Estimation Models](https://huggingface.co/models?pipeline_tag=depth-estimation)
  * [Depth-Anything V2](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf)
  * [Marigold Depth](https://huggingface.co/prs-eth/marigold-depth-v1-0)
  * [Intel DPT Models](https://huggingface.co/Intel/dpt-large)
  * [Monocular Depth Estimation Overview](https://huggingface.co/docs/transformers/tasks/monocular_depth_estimation)



## What to Do Next#

Now that youâve mastered depth estimation with FiftyOne, here are some suggested next steps:

  * **Explore Model Evaluation** \- Learn how to evaluate depth estimation models by comparing predictions against ground truth and identifying failure cases
  * **Try Out FiftyOne Brain** \- Use similarity analysis to find images with similar depth characteristics or identify outliers in your dataset
  * **Build Custom Workflows** \- Create domain-specific workflows for your depth estimation use case (robotics, AR/VR, autonomous vehicles, 3D reconstruction, etc.)
  * **Join the Community** \- Connect with other FiftyOne users to share insights and learn advanced depth estimation techniques
  * **Apply to Real Projects** \- Use these skills on your production depth estimation datasets to improve data quality and model performance



## Weâd Love Your Feedback#

Your feedback helps us improve FiftyOne and create better learning experiences. Please let us know:

  * What aspects of this depth estimation guide were most helpful?
  * What could be improved or clarified?
  * What depth estimation-specific topics would you like to see covered in future guides?
  * Any issues or bugs you encountered?

You can reach us at `support@voxel51.com` or join our [Discord community](https://community.voxel51.com). Thank you for completing the Depth Estimation Guide! We hope youâre excited to apply these skills to build better depth estimation systems. IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
