---
source_url: https://docs.voxel51.com/getting_started/auto_labeling/05_finalize.html
---

# Step 5: Finalize Your Auto Labeling Workflow#

Youâve analyzed, approved, and tagged predictions. Now itâs time to finalize the workflow, integrating approved labels into your dataset while discarding problematic predictions.

## Pre-Finalization Checklist#

Before finalizing, verify:

Item | Status  
---|---  
Reviewed approval queue for correctness | â   
Tagged all problematic samples | â   
Spot-checked random approved samples | â   
Documented confidence thresholds used | â   
Noted any systematic model issues (or hypothesized issues) you may have observed | â   
  
## Final Review of Approval Queue#

Navigate back to the **Auto Labeling** panel, and then to the **Approval** tab. Before finalizing the approval, take one more opportunity to add any other labels youâd like to the approval queue.

[![VAL review interface](https://cdn.voxel51.com/getting_started_val/notebook5/val_approval_queue.webp) ](https://cdn.voxel51.com/getting_started_val/notebook5/val_approval_queue.webp)

After reviewing your labels ready for approval, click **Approve labels** at the bottom of the panel

You will be prompted once more with a note that approving these labels will delete all the other **yolow_detections-in-review** labels (i.e., the labels left unapproved). Click **Approve labels**

[![VAL review interface](https://cdn.voxel51.com/getting_started_val/notebook5/val_approval_confirmation.webp) ](https://cdn.voxel51.com/getting_started_val/notebook5/val_approval_confirmation.webp)

Once approved, the status of the panel changes to **Approved** status.

[![VAL review interface](https://cdn.voxel51.com/getting_started_val/notebook5/val_status_approved.webp) ](https://cdn.voxel51.com/getting_started_val/notebook5/val_status_approved.webp)

Now your approved **yolow_detections** labels have been added as a permanent field to your dataset, with corresponding class labels and confidence filtering. You can slice and filter this field just like any other.

[![VAL review interface](https://cdn.voxel51.com/getting_started_val/notebook5/val_labels_applied.webp) ](https://cdn.voxel51.com/getting_started_val/notebook5/val_labels_applied.webp)

## You Did It!#

**Congratulations!**

Youâve completed your first Auto Labeling workflow, transforming raw predictions into high-quality, verified dataset labels.

**Next** : Review the [Guide Summary](getting_started__auto_labeling__summary.md#val-guide-summary) for key takeaways and next steps.

Tip

**Save this workflow!** The process youâve learned is broadly applicable to any labeling task. With practice, youâll develop intuition for confidence thresholds, model selection, and review strategies tailored to your specific use cases.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
