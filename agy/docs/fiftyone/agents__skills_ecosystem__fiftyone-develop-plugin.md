---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-develop-plugin.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-skills/blob/main/skills/fiftyone-develop-plugin/SKILL.md)

# Develop Plugin#

Scaffold and implement custom FiftyOne plugins: operators, panels, and JavaScript components.

## Install#
    
    
    curl -sL skil.sh | sh -s -- voxel51/fiftyone-skills
    

When prompted, select **fiftyone-develop-plugin** from the menu.

## Requirements#

  * [FiftyOne](https://docs.voxel51.com/getting_started/install.html)

  * Python 3.8+




## Usage#

Ask your AI assistant:
    
    
    "Create a FiftyOne operator that filters samples by confidence score"
    "Build a panel that shows a class distribution chart"
    "Scaffold a plugin that integrates with my annotation tool"
    

The skill asks clarifying questions, presents the file structure and design for your approval, then generates the full plugin code with tests.

## Example output#
    
    
    my-plugin/
    âââ fiftyone.yml
    âââ __init__.py        # operator/panel definitions
    âââ README.md
    

Install the generated plugin:
    
    
    fiftyone plugins create my-plugin
    

## See also#

  * [Plugin development docs](https://docs.voxel51.com/plugins/developing_plugins.html)

  * [FiftyOne Plugins](https://github.com/voxel51/fiftyone-plugins)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
