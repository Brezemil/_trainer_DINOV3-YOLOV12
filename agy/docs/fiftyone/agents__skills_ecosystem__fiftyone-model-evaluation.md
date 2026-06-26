---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-model-evaluation.html
---

![Enterprise Skill](https://img.shields.io/badge/Enterprise-Skill-orange)

# Model Evaluation#

Evaluate a model against ground truth, surface mAP and per-class metrics, and explore failure modes interactively in the Model Evaluation panel â all from a single natural language prompt.

![Model Evaluation](https://cdn.voxel51.com/fiftyone-internal-skills/model_evaluation.webp)

## Requirements#

[FiftyOne Enterprise](https://voxel51.com/fiftyone-teams)

[FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

## Usage#

Ask your AI assistant:
    
    
    "Evaluate my model using ground_truth as ground truth and predictions as predictions"
    "Show me where the model fails on the person class"
    "Find high-confidence false positives"
    "Compare my two model evaluations side by side"
    "How does the model perform on small objects?"
    

The skill checks for existing evaluation results first and skips computation if already done. For new evaluations it runs a delegated background job, then opens the Model Evaluation panel and navigates directly to the results. For failure mode analysis it discovers the dataset structure dynamically â label field names, eval result fields, and class labels â before applying any filters.

## See also#

[FiftyOne Enterprise docs](https://docs.voxel51.com/teams/index.html)

[FiftyOne Model Evaluation panel](https://docs.voxel51.com/enterprise/model_evaluation.html)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
