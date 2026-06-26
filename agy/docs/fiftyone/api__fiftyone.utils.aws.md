---
source_url: https://docs.voxel51.com/api/fiftyone.utils.aws.html
---

# fiftyone.utils.aws#

Utilities for working with Amazon Web Services <https://aws.amazon.com>.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_public_s3_files`(urls[,Â ...]) | Download files from a public AWS S3 bucket using unsigned URLs.  
---|---  
  
fiftyone.utils.aws.download_public_s3_files(_urls_ , _download_dir =None_, _num_workers =None_, _overwrite =True_)#
    

Download files from a public AWS S3 bucket using unsigned URLs.

The url argument either accepts:

>   * A list of paths to objects in the s3 bucket:
>         
>         urls = ["s3://bucket_name/dir1/file1.ext", ...]
>         
> 
> When urls is a list, then the download_dir argument is required and all objects will be downloaded into that directory
> 
>   * A dictionary mapping the paths of objects to files on disk to store each object:
>         
>         urls = {
>             "s3://bucket_name/dir1/file1.ext": "/path/to/local/file1.ext",
>             ...
>         }
>         
> 
> 


Parameters:
    

  * **urls** â either a list of URLs to objects in an s3 bucket, or a dict mapping these URLs to locations on disk. If urls is a list, then the download_dir argument is required

  * **download_dir** (_None_) â the directory to store all downloaded objects. This is only used if urls is a list

  * **num_workers** (_None_) â a suggested number of threads to use when downloading files

  * **overwrite** (_True_) â whether to overwrite existing files




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
