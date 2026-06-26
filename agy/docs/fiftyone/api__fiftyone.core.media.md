---
source_url: https://docs.voxel51.com/api/fiftyone.core.media.html
---

# fiftyone.core.media#

Sample media utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_media_type`(filepath) | Gets the media type for the given filepath.  
---|---  
  
**Exceptions:**

`MediaTypeError` | Exception raised when a problem with media types is encountered.  
---|---  
`SelectGroupSlicesError`([supported_media_types]) | Exception raised when a grouped collection is passed to a method that expects a primitive media type to be selected.  
  
fiftyone.core.media.get_media_type(_filepath_)#
    

Gets the media type for the given filepath.

Parameters:
    

**filepath** â a filepath

Returns:
    

the media type

exception fiftyone.core.media.MediaTypeError#
    

Bases: `TypeError`

Exception raised when a problem with media types is encountered.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

exception fiftyone.core.media.SelectGroupSlicesError(_supported_media_types =None_)#
    

Bases: `ValueError`

Exception raised when a grouped collection is passed to a method that expects a primitive media type to be selected.

Parameters:
    

**supported_media_types** (_None_) â an optional media type or iterable of media types that are supported

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
