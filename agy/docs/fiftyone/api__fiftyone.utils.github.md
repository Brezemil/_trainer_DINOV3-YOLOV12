---
source_url: https://docs.voxel51.com/api/fiftyone.utils.github.html
---

# fiftyone.utils.github#

GitHub utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`GitHubRepository`(repo[,Â safe]) | Class for interacting with a GitHub repository.  
---|---  
  
class fiftyone.utils.github.GitHubRepository(_repo_ , _safe =False_)#
    

Bases: `object`

Class for interacting with a GitHub repository.

Note

To interact with private GitHub repositories that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Parameters:
    

  * **repo** â 

the GitHub repository or identifier, which can be:

    * a GitHub repo URL like `https://github.com/<user>/<repo>`

    * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

    * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * **safe** (_False_) â whether to allow `repo` to contain a tree path like `https://github.com/<user>/<repo>/tree/<branch>/<path>`. If `safe=True` and a `<path>` is found, it is extracted and stored in the `safe_path()` property




**Attributes:**

`user` | The username of the repo.  
---|---  
`repo` | The name of the repo.  
`ref` | The ref (e.g. branch, tag, commit hash), if any.  
`safe_path` | The path that was extracted from the provided ref, if any.  
`identifier` | The repository identifier string.  
  
**Methods:**

`get_repo_info`() | Returns a dict of info about the repository.  
---|---  
`get_file`(path[,Â outpath]) | Downloads the file at the given path.  
`list_path_contents`([path]) | Returns the contents of the repo rooted at the given path.  
`list_repo_contents`([recursive]) | Returns a flat list of the repository's contents.  
`download`(outdir) | Downloads the repository to the specified root directory.  
`parse_url`(url) |   
`parse_identifier`(identifier) |   
  
property user#
    

The username of the repo.

property repo#
    

The name of the repo.

property ref#
    

The ref (e.g. branch, tag, commit hash), if any.

property safe_path#
    

The path that was extracted from the provided ref, if any.

property identifier#
    

The repository identifier string.

get_repo_info()#
    

Returns a dict of info about the repository.

Returns:
    

an info dict

get_file(_path_ , _outpath =None_)#
    

Downloads the file at the given path.

Parameters:
    

  * **path** â the filepath in the repository

  * **outpath** (_None_) â a path on disk to write the file



Returns:
    

the file bytes, if no `outpath` is provided

list_path_contents(_path =None_)#
    

Returns the contents of the repo rooted at the given path.

Note

This method has a limit of 1,000 files. [Documentation](https://docs.github.com/en/rest/repos/contents).

Parameters:
    

**path** (_None_) â an optional root path to start the search from

Returns:
    

a list of file info dicts

list_repo_contents(_recursive =True_)#
    

Returns a flat list of the repositoryâs contents.

Note

This method has a limit of 100,000 entries and 7MB response size. [Documentation](https://docs.github.com/en/rest/git/trees).

Parameters:
    

**recursive** (_True_) â whether to recursively traverse subdirectories

Returns:
    

a list of file info dicts

download(_outdir_)#
    

Downloads the repository to the specified root directory.

Parameters:
    

**outdir** â the output directory

static parse_url(_url_)#
    

static parse_identifier(_identifier_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
