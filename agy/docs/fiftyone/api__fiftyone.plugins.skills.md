---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.skills.html
---

# fiftyone.plugins.skills#

FiftyOne plugin skills.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SkillDefinition`(path,Â metadata,Â plugin_name) | A skill definition.  
---|---  
  
**Functions:**

`list_skills`([enabled,Â plugin,Â category]) | Lists available skills from installed plugins.  
---|---  
  
class fiftyone.plugins.skills.SkillDefinition(_path_ , _metadata_ , _plugin_name_)#
    

Bases: `object`

A skill definition.

Parameters:
    

  * **path** â the absolute path to the skillâs Markdown file

  * **metadata** â a skill metadata dict parsed from the fileâs YAML frontmatter

  * **plugin_name** â the name of the plugin that provides this skill




**Attributes:**

`name` | The name of the skill.  
---|---  
`description` | The description of the skill.  
`category` | The category of the skill.  
`path` | The absolute path to the skill file.  
`plugin_name` | The name of the plugin that provides this skill.  
`content` | The full raw content of the skill file.  
  
**Methods:**

`to_dict`() | Returns a JSON dict representation of the skill.  
---|---  
  
property name#
    

The name of the skill.

property description#
    

The description of the skill.

property category#
    

The category of the skill.

property path#
    

The absolute path to the skill file.

property plugin_name#
    

The name of the plugin that provides this skill.

property content#
    

The full raw content of the skill file.

to_dict()#
    

Returns a JSON dict representation of the skill.

Returns:
    

a JSON dict

fiftyone.plugins.skills.list_skills(_enabled =True_, _plugin =None_, _category =None_)#
    

Lists available skills from installed plugins.

Parameters:
    

  * **enabled** (_True_) â whether to include only enabled plugins (True), only disabled plugins (False), or all plugins (`"all"`)

  * **plugin** (_None_) â a plugin name or list of plugin names to include. By default, skills from all plugins are included

  * **category** (_None_) â a category or list of categories to filter by. By default, skills of all categories are included



Returns:
    

a list of `SkillDefinition` instances

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
