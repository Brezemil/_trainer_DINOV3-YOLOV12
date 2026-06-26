---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-data-distribution.html
---

![Enterprise Skill](https://img.shields.io/badge/Enterprise-Skill-orange)

# Data Distribution#

Scan a FiftyOne Enterprise dataset and generate histogram plots and distribution summaries for class labels, image dimensions, file sizes, tags, and numeric metadata fields.

![Data Distribution](https://cdn.voxel51.com/fiftyone-internal-skills/distribution.webp)

## Requirements#

[FiftyOne Enterprise](https://voxel51.com/fiftyone-teams)

[FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

## Usage#

Ask your AI assistant:
    
    
    "What does my data look like? Give me a breakdown of all the fields"
    "Are my train/val/test splits balanced?"
    "Show me the class distribution for ground_truth"
    "What are the image dimensions in this dataset?"
    

The skill discovers all interesting fields automatically, presents distribution summaries as tables, flags imbalances and outliers, and opens the Histograms panel in the App to show visual distributions.

## See also#

[FiftyOne Enterprise docs](https://docs.voxel51.com/teams/index.html)

[FiftyOne Histograms panel](https://docs.voxel51.com/user_guide/app.html#histograms)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
