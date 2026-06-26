---
source_url: https://docs.voxel51.com/api/fiftyone.utils.image.html
---

# fiftyone.utils.image#

Image utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`read`(path_or_url[,Â include_alpha,Â flag]) | Reads the image from the given path as a numpy array.  
---|---  
`write`(img,Â path) | Writes image to file.  
`reencode_images`(sample_collection[,Â ext,Â ...]) | Re-encodes the images in the sample collection to the given format.  
`transform_images`(sample_collection[,Â size,Â ...]) | Transforms the images in the sample collection according to the provided parameters.  
`reencode_image`(input_path,Â output_path) | Re-encodes the image to the format specified by the given output path.  
`transform_image`(input_path,Â output_path[,Â ...]) | Transforms the image according to the provided parameters.  
  
fiftyone.utils.image.read(_path_or_url_ , _include_alpha =False_, _flag =None_)#
    

Reads the image from the given path as a numpy array.

Color images are returned as RGB arrays.

Parameters:
    

  * **path** â the filepath or URL of the image

  * **include_alpha** (_False_) â whether to include the alpha channel of the image, if present, in the returned array

  * **flag** (_None_) â an optional OpenCV image format flag to use. If provided, this flag takes precedence over `include_alpha`



Returns:
    

a uint8 numpy array containing the image

fiftyone.utils.image.write(_img_ , _path_)#
    

Writes image to file.

Parameters:
    

  * **img** â a numpy array

  * **path** â the output path




fiftyone.utils.image.reencode_images(_sample_collection_ , _ext ='.png'_, _force_reencode =True_, _media_field ='filepath'_, _output_field =None_, _output_dir =None_, _rel_dir =None_, _update_filepaths =True_, _delete_originals =False_, _num_workers =None_, _skip_failures =False_, _progress =None_)#
    

Re-encodes the images in the sample collection to the given format.

If no `output_dir` is specified and `delete_originals` is False, then if a transformation would result in overwriting an existing file with the same filename, the original file is renamed to `<name>-original.<ext>`.

Note

This method will not update the `metadata` field of the collection after transforming. You can repopulate the `metadata` field if needed by calling:
    
    
    sample_collection.compute_metadata(overwrite=True)
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **ext** (_".png"_) â the image format to use (e.g., â.pngâ or â.jpgâ)

  * **force_reencode** (_True_) â whether to re-encode images whose extension already matches `ext`

  * **media_field** (_"filepath"_) â the input field containing the image paths to transform

  * **output_field** (_None_) â an optional field in which to store the paths to the transformed images. By default, `media_field` is updated in-place

  * **output_dir** (_None_) â an optional output directory in which to write the transformed images. If none is provided, the images are updated in-place

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths

  * **update_filepaths** (_True_) â whether to store the output paths on the sample collection

  * **delete_originals** (_False_) â whether to delete the original images after re-encoding

  * **num_workers** (_None_) â a suggested number of worker processes to use

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an image cannot be re-encoded

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.image.transform_images(_sample_collection_ , _size =None_, _min_size =None_, _max_size =None_, _interpolation =None_, _ext =None_, _force_reencode =False_, _media_field ='filepath'_, _output_field =None_, _output_dir =None_, _rel_dir =None_, _update_filepaths =True_, _delete_originals =False_, _num_workers =None_, _skip_failures =False_, _progress =None_)#
    

Transforms the images in the sample collection according to the provided parameters.

If no `output_dir` is specified and `delete_originals` is False, then if a transformation would result in overwriting an existing file with the same filename, the original file is renamed to `<name>-original.<ext>`.

Note

This method will not update the `metadata` field of the collection after transforming. You can repopulate the `metadata` field if needed by calling:
    
    
    sample_collection.compute_metadata(overwrite=True)
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **size** (_None_) â an optional `(width, height)` for each image. One dimension can be -1, in which case the aspect ratio is preserved

  * **min_size** (_None_) â an optional minimum `(width, height)` for each image. A dimension can be -1 if no constraint should be applied. The images are resized (aspect-preserving) if necessary to meet this constraint

  * **max_size** (_None_) â an optional maximum `(width, height)` for each image. A dimension can be -1 if no constraint should be applied. The images are resized (aspect-preserving) if necessary to meet this constraint

  * **interpolation** (_None_) â an optional `interpolation` argument for `cv2.resize()`

  * **ext** (_None_) â an optional image format to re-encode the source images into (e.g., â.pngâ or â.jpgâ)

  * **force_reencode** (_False_) â whether to re-encode images whose parameters already match the specified values

  * **media_field** (_"filepath"_) â the input field containing the image paths to transform

  * **output_field** (_None_) â an optional field in which to store the paths to the transformed images. By default, `media_field` is updated in-place

  * **output_dir** (_None_) â an optional output directory in which to write the transformed images. If none is provided, the images are updated in-place

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths

  * **update_filepaths** (_True_) â whether to store the output paths on the sample collection

  * **delete_originals** (_False_) â whether to delete the original images if any transformation was applied

  * **num_workers** (_None_) â a suggested number of worker processes to use

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an image cannot be transformed

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.image.reencode_image(_input_path_ , _output_path_)#
    

Re-encodes the image to the format specified by the given output path.

Parameters:
    

  * **input_path** â the path to the input image

  * **output_path** â the path to write the output image




fiftyone.utils.image.transform_image(_input_path_ , _output_path_ , _size =None_, _min_size =None_, _max_size =None_, _interpolation =None_)#
    

Transforms the image according to the provided parameters.

Parameters:
    

  * **input_path** â the path to the input image

  * **output_path** â the path to write the output image

  * **size** (_None_) â an optional `(width, height)` for the image. One dimension can be -1, in which case the aspect ratio is preserved

  * **min_size** (_None_) â an optional minimum `(width, height)` for the image. A dimension can be -1 if no constraint should be applied. The image is resized (aspect-preserving) if necessary to meet this constraint

  * **max_size** (_None_) â an optional maximum `(width, height)` for the image. A dimension can be -1 if no constraint should be applied. The image is resized (aspect-preserving) if necessary to meet this constraint

  * **interpolation** (_None_) â an optional `interpolation` argument for `cv2.resize()`




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
