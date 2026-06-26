---
source_url: https://docs.voxel51.com/labs/labs_ecosystem/labs_panel.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-labs/tree/main/plugins/labs_panel)

# Labs Panel#

Labs Panel offers a convenient way to see the available Labs features, their installation status and versions, and an easy interface to manage these features.

## Usage#

### Via FiftyOne App#
    
    
    import fiftyone.zoo as foz
    import fiftyone as fo
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    

![Panel dropdown](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/labs_panel/assets/open_labs_panel.png)

_Select FiftyOne Labs panel_

![Apply model parameters](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/labs_panel/assets/labs_panel.png)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
