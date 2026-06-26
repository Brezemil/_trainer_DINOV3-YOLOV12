---
source_url: https://docs.voxel51.com/api/fiftyone.utils.video.html
---

# fiftyone.utils.video#

Video utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`extract_clip`(video_path,Â output_path[,Â ...]) | Extracts the specified clip from the video.  
---|---  
`reencode_videos`(sample_collection[,Â ...]) | Re-encodes the videos in the sample collection as H.264 MP4s that can be visualized in the FiftyOne App.  
`transform_videos`(sample_collection[,Â fps,Â ...]) | Transforms the videos in the sample collection according to the provided parameters using `ffmpeg`.  
`sample_videos`(sample_collection[,Â ...]) | Samples the videos in the sample collection into directories of per-frame images according to the provided parameters using `ffmpeg`.  
`reencode_video`(input_path,Â output_path[,Â ...]) | Re-encodes the video using the H.264 codec.  
`transform_video`(input_path,Â output_path[,Â ...]) | Transforms the video according to the provided parameters using `ffmpeg`.  
`sample_video`(input_path,Â output_patt[,Â ...]) | Samples the video into a directory of per-frame images according to the provided parameters using `ffmpeg`.  
`sample_frames_uniform`(frame_rate[,Â ...]) | Returns a list of frame numbers sampled uniformly according to the provided parameters.  
`concat_videos`(input_paths,Â output_path[,Â ...]) | Concatenates the given list of videos, in order, into a single video.  
`exact_frame_count`(input_path) | Returns the exact number of frames in the video.  
  
fiftyone.utils.video.extract_clip(_video_path_ , _output_path_ , _support =None_, _timestamps =None_, _metadata =None_, _fast =False_)#
    

Extracts the specified clip from the video.

Provide either `support` or `timestamps` to this method.

When fast=False, the following ffmpeg command is used:
    
    
    # Slower, more accurate option
    ffmpeg -ss <start_time> -i <video_path> -t <duration> <output_path>
    

When fast is True, the following two-step ffmpeg process is used:
    
    
    # Faster, less accurate option
    ffmpeg -ss <start_time> -i <video_path> -t <duration> -c copy <tmp_path>
    ffmpeg -i <tmp_path> <output_path>
    

Parameters:
    

  * **video_path** â the path to the video

  * **output_path** â the path to write the extracted clip

  * **support** (_None_) â the `[first, last]` frame number range to clip

  * **timestamps** (_None_) â the `[start, stop]` timestamps to clip, in seconds

  * **metadata** (_None_) â the [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") for the video

  * **fast** (_False_) â whether to use a faster-but-potentially-less-accurate strategy to extract the clip




fiftyone.utils.video.reencode_videos(_sample_collection_ , _force_reencode =True_, _media_field ='filepath'_, _output_field =None_, _output_dir =None_, _rel_dir =None_, _update_filepaths =True_, _delete_originals =False_, _skip_failures =False_, _verbose =False_, _progress =None_, _** kwargs_)#
    

Re-encodes the videos in the sample collection as H.264 MP4s that can be visualized in the FiftyOne App.

If no `output_dir` is specified and `delete_originals` is False, then if a transformation would result in overwriting an existing file with the same filename, the original file is renamed to `<name>-original.<ext>`.

By default, the re-encoding is performed via the following `ffmpeg` command:
    
    
    ffmpeg \
        -loglevel error -vsync 0 -i $INPUT_PATH \
        -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -vsync 0 -an \
        $OUTPUT_PATH
    

You can configure parameters of the re-encoding such as codec and compression by passing keyword arguments for `eta.core.video.FFmpeg(**kwargs)` to this function.

Note

This method will not update the `metadata` field of the collection after transforming. You can repopulate the `metadata` field if needed by calling:
    
    
    sample_collection.compute_metadata(overwrite=True)
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **force_reencode** (_True_) â whether to re-encode videos that are already MP4s

  * **media_field** (_"filepath"_) â the input field containing the video paths to transform

  * **output_field** (_None_) â an optional field in which to store the paths to the transformed videos. By default, `media_field` is updated in-place

  * **output_dir** (_None_) â an optional output directory in which to write the transformed videos. If none is provided, the videos are updated in-place

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each video. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths

  * **update_filepaths** (_True_) â whether to store the output paths on the sample collection

  * **delete_originals** (_False_) â whether to delete the original videos after re-encoding

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if a video cannot be re-encoded

  * **verbose** (_False_) â whether to log the `ffmpeg` commands that are executed

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â keyword arguments for `eta.core.video.FFmpeg(**kwargs)`




fiftyone.utils.video.transform_videos(_sample_collection_ , _fps =None_, _min_fps =None_, _max_fps =None_, _size =None_, _min_size =None_, _max_size =None_, _reencode =False_, _force_reencode =False_, _media_field ='filepath'_, _output_field =None_, _output_dir =None_, _rel_dir =None_, _update_filepaths =True_, _delete_originals =False_, _skip_failures =False_, _verbose =False_, _progress =None_, _** kwargs_)#
    

Transforms the videos in the sample collection according to the provided parameters using `ffmpeg`.

If no `output_dir` is specified and `delete_originals` is False, then if a transformation would result in overwriting an existing file with the same filename, the original file is renamed to `<name>-original.<ext>`.

In addition to the size and frame rate parameters, if `reencode == True`, the following basic `ffmpeg` command structure is used to re-encode the videos as H.264 MP4s:
    
    
    ffmpeg \
        -loglevel error -vsync 0 -i $INPUT_PATH \
        -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -vsync 0 -an \
        $OUTPUT_PATH
    

Note

This method will not update the `metadata` field of the collection after transforming. You can repopulate the `metadata` field if needed by calling:
    
    
    sample_collection.compute_metadata(overwrite=True)
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **fps** (_None_) â an optional frame rate at which to resample the videos

  * **min_fps** (_None_) â an optional minimum frame rate. Videos with frame rate below this value are upsampled

  * **max_fps** (_None_) â an optional maximum frame rate. Videos with frame rate exceeding this value are downsampled

  * **size** (_None_) â an optional `(width, height)` for each frame. One dimension can be -1, in which case the aspect ratio is preserved

  * **min_size** (_None_) â an optional minimum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **max_size** (_None_) â an optional maximum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **reencode** (_False_) â whether to re-encode the videos as H.264 MP4s

  * **force_reencode** (_False_) â whether to re-encode videos whose parameters already satisfy the specified values

  * **media_field** (_"filepath"_) â the input field containing the video paths to transform

  * **output_field** (_None_) â an optional field in which to store the paths to the transformed videos. By default, `media_field` is updated in-place

  * **output_dir** (_None_) â an optional output directory in which to write the transformed videos. If none is provided, the videos are updated in-place

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each video. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths

  * **update_filepaths** (_True_) â whether to store the output paths on the sample collection

  * **delete_originals** (_False_) â whether to delete the original videos after re-encoding

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if a video cannot be transformed

  * **verbose** (_False_) â whether to log the `ffmpeg` commands that are executed

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â keyword arguments for `eta.core.video.FFmpeg(**kwargs)`




fiftyone.utils.video.sample_videos(_sample_collection_ , _frames_patt =None_, _frames =None_, _fps =None_, _max_fps =None_, _size =None_, _min_size =None_, _max_size =None_, _original_frame_numbers =True_, _force_sample =False_, _media_field ='filepath'_, _output_field =None_, _output_dir =None_, _rel_dir =None_, _save_filepaths =False_, _delete_originals =False_, _skip_failures =False_, _verbose =False_, _progress =None_, _** kwargs_)#
    

Samples the videos in the sample collection into directories of per-frame images according to the provided parameters using `ffmpeg`.

By default, each folder of images is written using the same basename as the input video. For example, if `frames_patt = "%%06d.jpg"`, then videos with the following paths:
    
    
    /path/to/video1.mp4
    /path/to/video2.mp4
    ...
    

would be sampled as follows:
    
    
    /path/to/video1/
        000001.jpg
        000002.jpg
        ...
    /path/to/video2/
        000001.jpg
        000002.jpg
        ...
    

However, you can use the optional `output_dir` and `rel_dir` parameters to customize the location and shape of the sampled frame folders. For example, if `output_dir = "/tmp"` and `rel_dir = "/path/to"`, then videos with the following paths:
    
    
    /path/to/folderA/video1.mp4
    /path/to/folderA/video2.mp4
    /path/to/folderB/video3.mp4
    ...
    

would be sampled as follows:
    
    
    /tmp/folderA/
        video1/
            000001.jpg
            000002.jpg
            ...
        video2/
            000001.jpg
            000002.jpg
            ...
    /tmp/folderB/
        video3/
            000001.jpg
            000002.jpg
            ...
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **frames_patt** (_None_) â a pattern specifying the filename/format to use to store the sampled frames, e.g., `"%%06d.jpg"`. The default value is `fiftyone.config.default_sequence_idx + fiftyone.config.default_image_ext`

  * **frames** (_None_) â an optional list of lists defining specific frames to sample from each video. Entries can also be None, in which case all frames will be sampled. If provided, `fps` and `max_fps` are ignored

  * **fps** (_None_) â an optional frame rate at which to sample frames

  * **max_fps** (_None_) â an optional maximum frame rate. Videos with frame rate exceeding this value are downsampled

  * **size** (_None_) â an optional `(width, height)` for each frame. One dimension can be -1, in which case the aspect ratio is preserved

  * **min_size** (_None_) â an optional minimum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **max_size** (_None_) â an optional maximum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **original_frame_numbers** (_True_) â whether to use the original frame numbers when writing the output frames (True) or to instead reindex the frames as 1, 2, â¦ (False)

  * **force_sample** (_False_) â whether to resample videos whose sampled frames already exist

  * **media_field** (_"filepath"_) â the input field containing the video paths to sample

  * **output_field** (_None_) â an optional frame field in which to store the paths to the sampled frames. By default, `media_field` is used

  * **output_dir** (_None_) â an optional output directory in which to write the sampled frames. By default, the frames are written in folders with the same basename of each video

  * **rel_dir** (_None_) â a relative directory to remove from the filepath of each video, if possible. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path"). This argument can be used in conjunction with `output_dir` to cause the sampled frames to be written in a nested directory structure within `output_dir` matching the shape of the input videoâs folder structure

  * **save_filepaths** (_False_) â whether to save the sampled frame paths in the `output_field` field of each frame of the input collection

  * **delete_originals** (_False_) â whether to delete the original videos after sampling

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if a video cannot be sampled

  * **verbose** (_False_) â whether to log the `ffmpeg` commands that are executed

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â keyword arguments for `eta.core.video.FFmpeg(**kwargs)`




fiftyone.utils.video.reencode_video(_input_path_ , _output_path_ , _verbose =False_, _** kwargs_)#
    

Re-encodes the video using the H.264 codec.

By default, the re-encoding is performed via the following `ffmpeg` command:
    
    
    ffmpeg \
        -loglevel error -vsync 0 -i $INPUT_PATH \
        -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -vsync 0 -an \
        $OUTPUT_PATH
    

You can configure parameters of the re-encoding such as codec and compression by passing keyword arguments for `eta.core.video.FFmpeg(**kwargs)` to this function.

Parameters:
    

  * **input_path** â the path to the input video

  * **output_path** â the path to write the output video

  * **verbose** (_False_) â whether to log the `ffmpeg` command that is executed

  * ****kwargs** â keyword arguments for `eta.core.video.FFmpeg(**kwargs)`




fiftyone.utils.video.transform_video(_input_path_ , _output_path_ , _fps =None_, _min_fps =None_, _max_fps =None_, _size =None_, _min_size =None_, _max_size =None_, _reencode =False_, _verbose =False_, _** kwargs_)#
    

Transforms the video according to the provided parameters using `ffmpeg`.

In addition to the size and frame rate parameters, if `reencode == True`, the following basic `ffmpeg` command structure is used to re-encode the video as an H.264 MP4:
    
    
    ffmpeg \
        -loglevel error -vsync 0 -i $INPUT_PATH \
        -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -vsync 0 -an \
        $OUTPUT_PATH
    

Parameters:
    

  * **input_path** â the path to the input video

  * **output_path** â the path to write the output video

  * **fps** (_None_) â an optional frame rate at which to resample the videos

  * **min_fps** (_None_) â an optional minimum frame rate. Videos with frame rate below this value are upsampled

  * **max_fps** (_None_) â an optional maximum frame rate. Videos with frame rate exceeding this value are downsampled

  * **size** (_None_) â an optional `(width, height)` for each frame. One dimension can be -1, in which case the aspect ratio is preserved

  * **min_size** (_None_) â an optional minimum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **max_size** (_None_) â an optional maximum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **reencode** (_False_) â whether to reencode the video (see main description)

  * **verbose** (_False_) â whether to log the `ffmpeg` command that is executed

  * ****kwargs** â keyword arguments for `eta.core.video.FFmpeg(**kwargs)`




fiftyone.utils.video.sample_video(_input_path_ , _output_patt_ , _frames =None_, _fps =None_, _max_fps =None_, _size =None_, _min_size =None_, _max_size =None_, _original_frame_numbers =True_, _verbose =False_, _** kwargs_)#
    

Samples the video into a directory of per-frame images according to the provided parameters using `ffmpeg`.

Parameters:
    

  * **input_path** â the path to the input video

  * **output_patt** â a pattern like `/path/to/images/%%06d.jpg` specifying the filename/format to write the sampled frames

  * **frames** (_None_) â an iterable of frame numbers to sample. If provided, `fps` and `max_fps` are ignored

  * **fps** (_None_) â an optional frame rate at which to sample the frames

  * **max_fps** (_None_) â an optional maximum frame rate. Videos with frame rate exceeding this value are downsampled

  * **size** (_None_) â an optional `(width, height)` for each frame. One dimension can be -1, in which case the aspect ratio is preserved

  * **min_size** (_None_) â an optional minimum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **max_size** (_None_) â an optional maximum `(width, height)` for each frame. A dimension can be -1 if no constraint should be applied. The frames are resized (aspect-preserving) if necessary to meet this constraint

  * **original_frame_numbers** (_True_) â whether to use the original frame numbers when writing the output frames (True) or to instead reindex the frames as 1, 2, â¦ (False)

  * **verbose** (_False_) â whether to log the `ffmpeg` command that is executed

  * ****kwargs** â keyword arguments for `eta.core.video.FFmpeg(**kwargs)`




fiftyone.utils.video.sample_frames_uniform(_frame_rate_ , _total_frame_count =None_, _support =None_, _fps =None_, _max_fps =None_, _always_sample_last =False_)#
    

Returns a list of frame numbers sampled uniformly according to the provided parameters.

Parameters:
    

  * **frame_rate** â the video frame rate

  * **total_frame_count** (_None_) â the total number of frames in the video

  * **support** (_None_) â a `[first, last]` frame range from which to sample

  * **fps** (_None_) â a frame rate at which to sample frames

  * **max_fps** (_None_) â a maximum frame rate at which to sample frames

  * **always_sample_last** (_False_) â whether to always sample the last frame



Returns:
    

a list of frame numbers, or None if all frames should be sampled

fiftyone.utils.video.concat_videos(_input_paths_ , _output_path_ , _verbose =False_)#
    

Concatenates the given list of videos, in order, into a single video.

Parameters:
    

  * **input_paths** â a list of video paths

  * **output_path** â the path to write the output video

  * **verbose** (_False_) â whether to log the `ffmpeg` command that is executed




fiftyone.utils.video.exact_frame_count(_input_path_)#
    

Returns the exact number of frames in the video.

Warning

This method uses the `-count_frames` argument of `ffprobe`, which requires decoding the video and can be very slow.

Parameters:
    

**input_path** â the path to the video

Returns:
    

the number of frames in the video

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
