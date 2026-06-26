---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.utils.html
---

# fiftyone.plugins.utils#

FiftyOne plugin utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`list_zoo_plugins`([info]) | Returns a list of available plugins registered in the [FiftyOne Plugins repository](https://github.com/voxel51/fiftyone-plugins) README.  
---|---  
`find_plugins`(gh_repo[,Â path,Â info]) | Returns the paths to the fiftyone YAML files for all plugins found in the given GitHub repository.  
`get_plugin_info`(gh_repo[,Â path]) | Returns a dict of plugin info for a FiftyOne plugin hosted in GitHub.  
  
fiftyone.plugins.utils.list_zoo_plugins(_info =False_)#
    

Returns a list of available plugins registered in the [FiftyOne Plugins repository](https://github.com/voxel51/fiftyone-plugins) README.

Example usage:
    
    
    import fiftyone.plugins.utils as fopu
    
    plugins = fopu.list_zoo_plugins()
    print(plugins)
    
    plugins = fopu.list_zoo_plugins(info=True)
    print(plugins)
    

Parameters:
    

**info** (_False_) â whether to retrieve full plugin info for each plugin (True) or just return the available info from the README (False)

Returns:
    

a list of dicts describing the plugins

fiftyone.plugins.utils.find_plugins(_gh_repo_ , _path =None_, _info =False_)#
    

Returns the paths to the fiftyone YAML files for all plugins found in the given GitHub repository.

Example usage:
    
    
    import fiftyone.plugins.utils as fopu
    
    # Search the entire repository
    plugins = fopu.find_plugins("https://github.com/voxel51/fiftyone-plugins")
    print(plugins)
    
    # Search a specific tree root
    plugins = fopu.find_plugins(
        "https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation"
    )
    print(plugins)
    
    # Search a specific branch + subdirectory
    plugins = fopu.find_plugins(
        "https://github.com/voxel51/fiftyone-plugins/tree/main",
        path="plugins/annotation",
    )
    print(plugins)
    

Parameters:
    

  * **gh_repo** â 

the GitHub repository, identifier, or tree path, which can be:

    * a GitHub repo URL like `https://github.com/<user>/<repo>`

    * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

    * a GitHub ref string like `<user>/<repo>[/<ref>]`

    * a GitHub tree path like `https://github.com/<user>/<repo>/tree/<branch>/<path>`

  * **path** (_None_) â an optional subdirectory of the repository to which to restrict the search. If `gh_repo` also contains a `<path>`, it is prepended to this value

  * **info** (_False_) â whether to retrieve full plugin info for each plugin (True) or just return paths to the fiftyone YAML files (False)



Returns:
    

a list of paths to fiftyone YAML files or plugin info dicts

fiftyone.plugins.utils.get_plugin_info(_gh_repo_ , _path =None_)#
    

Returns a dict of plugin info for a FiftyOne plugin hosted in GitHub.

Example usage:
    
    
    import fiftyone.plugins.utils as fopu
    
    # A repository with a top-level fiftyone YAML file
    info = fopu.get_plugin_info("https://github.com/voxel51/voxelgpt")
    print(info)
    
    # A plugin that lives in a subdirectory
    # Manually specify the branch to use
    info = fopu.get_plugin_info(
        "https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation"
    )
    print(info)
    
    # Directly link to a fiftyone YAML file
    info = fopu.get_plugin_info(
        "https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/annotation/fiftyone.yml"
    )
    print(info)
    
    # Provide subdirectory separately
    info = fopu.get_plugin_info(
        "voxel51/fiftyone-plugins",
        path="plugins/annotation",
    )
    print(info)
    
    # Provide fiftyone YAML file path separately
    info = fopu.get_plugin_info(
        "voxel51/fiftyone-plugins",
        path="plugins/annotation/fiftyone.yml",
    )
    print(info)
    

Parameters:
    

  * **gh_repo** â 

the GitHub repository, identifier, tree path, or blob path, which can be:

    * a GitHub repo URL like `https://github.com/<user>/<repo>`

    * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

    * a GitHub ref string like `<user>/<repo>[/<ref>]`

    * a GitHub tree path like `https://github.com/<user>/<repo>/tree/<branch>/<path>`

    * a GitHub blob path like `https://github.com/<user>/<repo>/blob/<branch>/<path>`

  * **path** (_None_) â the path to a fiftyone YAML file or the directory that contains it. This is only necessary if the fiftyone YAML file is not at the root of the repository and you have not implicitly included this path in `gh_repo` by providing a tree or blob path



Returns:
    

a dict or list of dicts of plugin info

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
