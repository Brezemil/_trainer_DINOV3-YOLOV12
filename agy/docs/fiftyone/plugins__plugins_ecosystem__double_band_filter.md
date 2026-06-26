---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/double_band_filter.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/jacobmarks/double-band-filter-plugin)

# Double Band Filter Plugin#

![match_either_band](https://github.com/jacobmarks/double-band-filter-plugin/assets/12500356/5e51740b-f528-40ea-acb1-f66358b69aaa)

This plugin provides an operator to filter a float-valued field on two ranges simultaneously.

Choose a field from the drop-down, and then specify two ranges. The operator will return all samples where the field value is in the first range or the second range. Behind the scenes, this is implemented using FiftyOne ViewExpressions and the `match()` method.

# Installation#
    
    
    fiftyone plugins download https://github.com/jacobmarks/double-band-filter-plugin/
    

# Operators#

## `match_either_band`#

Filter a float-valued field on two ranges simultaneously. The operator will return all samples where the field value is in the first range or the second range.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
