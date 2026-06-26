---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-data-enrichment.html
---

![Enterprise Skill](https://img.shields.io/badge/Enterprise-Skill-orange)

# Data Enrichment#

Take a raw dataset with no metadata or labels and enrich it with image properties, CLIP embeddings, and a UMAP visualization â ready for semantic search, duplicate detection, and downstream labeling workflows.

![Data Enrichment](https://cdn.voxel51.com/fiftyone-internal-skills/data_enrichment.webp)

## Requirements#

[FiftyOne Enterprise](https://voxel51.com/fiftyone-teams)

[FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

## Usage#

Ask your AI assistant:
    
    
    "Enrich my dataset"
    "Compute embeddings for my images"
    "Set up my dataset for semantic search"
    "I have raw images with no metadata, where do I start?"
    

The skill audits existing fields first and skips any step already done. It then computes image metadata, CLIP embeddings, and a UMAP visualization as sequential delegated background jobs â each step waits for the previous one to finish before starting.

## See also#

[FiftyOne Enterprise docs](https://docs.voxel51.com/enterprise/index.html)

[FiftyOne Brain](https://docs.voxel51.com/brain.html)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
