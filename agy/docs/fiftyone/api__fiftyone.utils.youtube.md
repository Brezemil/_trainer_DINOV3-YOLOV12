---
source_url: https://docs.voxel51.com/api/fiftyone.utils.youtube.html
---

# fiftyone.utils.youtube#

Utilities for working with YouTube <https://youtube.com>.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_youtube_videos`(urls[,Â ...]) | Downloads a list of YouTube videos.  
---|---  
  
fiftyone.utils.youtube.download_youtube_videos(_urls_ , _download_dir =None_, _video_paths =None_, _clip_segments =None_, _ext ='.mp4'_, _only_progressive =True_, _resolution ='highest'_, _max_videos =None_, _num_workers =None_, _skip_failures =True_, _quiet =False_)#
    

Downloads a list of YouTube videos.

The `urls` argument accepts a list of YouTube âwatchâ URLs:
    
    
    urls = [
        "https://www.youtube.com/watch?v=-0URMJE8_PB",
        ...,
    ]
    

Use either the `download_dir` or `video_paths` argument to specify where to download each video.

You can use the optional `clip_segments` argument to specify a specific segment, in seconds, of each video to download:
    
    
    clip_segments = [
        (10, 25),
        (11.1, 20.2),
        None,               # entire video
        (None, 8.0),        # through beginning of video
        (8.0, None),        # through end of video
        ...
    ]
    

You can also use the optional `ext` and `resolution` arguments to specify a desired video codec and resolution to download, if possible.

YouTube videos are regularly taken down. Therefore, this method provides an optional `max_videos` argument that you can use in conjunction with `skip_failures=True` and a large list of possibly non-existent videos in `urls` in cases where you need a certain number of videos to be successfully downloaded but are willing to tolerate failures.

Parameters:
    

  * **urls** â a list of YouTube URLs to download

  * **download_dir** (_None_) â a directory in which to store the downloaded videos

  * **video_paths** (_None_) â a list of paths to which to download the videos. When downloading entire videos, a stream matching the video format implied by each fileâs extension is downloaded, if available, or else the extension of the video path is **changed** to match the available streamâs format

  * **clip_segments** (_None_) â a list of `(first, last)` tuples defining a specific segment of each video to download

  * **ext** (_".mp4"_) â a video format to download for each video, if possible. Only applicable when a `download_dir` is used. This format will be respected if such a stream exists, otherwise the format of the best available stream is used. Set this value to `None` if you want to download the stream with the best match for `resolution` and `progressive` regardless of format

  * **only_progressive** (_True_) â whether to only download progressive streams, if possible. Progressive streams contain both audio and video tracks and are typically only available at <= 720p resolution

  * **resolution** (_"highest"_) â 

a desired stream resolution to download. This filter is applied after respecting the desired video format and `only_progressive` restriction, if applicable. The supported values are:

    * `"highest"` (default): download the highest resolution stream

    * `"lowest"`: download the lowest resolution stream

    * A target resolution like `"1080p"`. In this case, the stream whose resolution is closest to this target value is downloaded

  * **max_videos** (_None_) â the maximum number of videos to successfully download. By default, all videos are downloaded

  * **num_workers** (_None_) â a suggested number of threads/processes to use when downloading videos

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if a video cannot be downloaded

  * **quiet** (_False_) â whether to suppress logging, except for a progress bar



Returns:
    

a tuple of

  * **downloaded** : a dict mapping integer indexes into `urls` to paths of successfully downloaded videos

  * **errors** : a dict mapping integer indexes into `urls` to error messages for videos that were attempted to be downloaded, but failed




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
