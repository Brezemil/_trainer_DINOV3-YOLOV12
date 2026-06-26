---
source_url: https://docs.voxel51.com/getting_started/auto_labeling/summary.html
---

# Summary: What Youâve Learned#

Congratulations! Youâve completed the Auto Labeling Guide. Letâs recap what youâve accomplished and explore where you can go next.

## Step-by-Step Recap#

**Step 1: Prepare Your Dataset and Delegated Operators**

You learned how to set up the foundation for Auto Labeling by preparing your dataset in FiftyOne Enterprise and configuring GPU-enabled delegated operators. This included understanding the infrastructure requirements and ensuring your environment is ready for auto labeling workflows.

**Step 2: Configure Your Auto Labeling Run**

You mastered the configuration process for an auto label run, including sample selection, model selection, class configuration, target label fields, and confidence thresholds. This step showed you how to customize the auto-labeling process to match your specific annotation needs.

**Step 3: Analyze and Approve Predictions**

You explored FiftyOneâs review interface for systematically assessing auto-generated labels. This included using the Review and Approval tabs to batch select correct predictions and mark them for approval.

**Step 4: Assess Labels with Embeddings**

You used FiftyOneâs patch embeddings visualization to identify outliers, false positives, and false negatives that are difficult to spot through manual review. You then tagged problematic predictions for relabeling or removal.

**Step 5: Finalize Your Auto Labeling Workflow**

You learned how to complete the VAL workflow by integrating approved labels into your dataset, discarding the rest.

## Suggested Exercises#

  1. **Custom Confidence Thresholds** : Experiment with different confidence thresholds for different classes. Which threshold values optimize the balance between automation and accuracy for your use case?

  2. **Iterative Refinement** : Run multiple VAL cycles on the same dataset, using insights from embeddings to improve each iteration. Track how prediction quality improves over successive runs.

  3. **Team Collaboration** : Set up a workflow where different team members review and approve labels for different object classes. How does VAL facilitate distributed annotation workflows?

  4. **Integration with Training Pipelines** : Use approved VAL labels to train or fine-tune your models. Measure the impact of high-quality auto-labeled data on model performance.




## Resources and Further Reading#

  * [FiftyOne Enterprise Documentation](https://docs.voxel51.com/enterprise/index.html#)

  * [Delegated Operations Guide](https://docs.voxel51.com/enterprise/plugins.html#enterprise-delegated-operations)

  * [FiftyOne Embeddings Tutorial](tutorials__image_embeddings.md)

  * [Model Evaluation Guide](https://docs.voxel51.com/getting_started/model_evaluation/index.html)

  * [FiftyOne Dataset Zoo](https://docs.voxel51.com/user_guide/dataset_zoo/index.html)




## What to Do Next#

Now that youâve mastered Auto Labeling with FiftyOne, here are some suggested next steps:

  * **Explore Segmentation with Auto Labeling** \- Apply auto label workflows to instance and semantic segmentation tasks

  * **Build Custom Models** \- Integrate your own detection or classification models into the Auto Labeling pipeline

  * **Scale Your Annotation** \- Use Auto Labeilng to accelerate annotation on large-scale datasets with thousands of images

  * **Join the Community** \- Connect with other FiftyOne Enterprise users to share Auto Labeling best practices and advanced techniques

  * **Apply to Production** \- Implement Auto Labeling in your production annotation pipelines to reduce manual labeling costs and improve data quality




## Weâd Love Your Feedback#

Your feedback helps us improve FiftyOne and create better learning experiences. Please let us know:

  * What aspects of this Auto Labeling guide were most helpful?

  * What could be improved or clarified?

  * What auto labeling-specific topics would you like to see covered in future guides?

  * Any issues or bugs you encountered?




You can reach us at `support@voxel51.com` or join our [Discord community](https://community.voxel51.com).

Thank you for completing the Auto Labeling Guide! We hope youâre excited to apply these skills to accelerate your annotation workflows and improve your dataset quality.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
