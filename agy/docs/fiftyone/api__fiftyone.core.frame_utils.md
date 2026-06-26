---
source_url: https://docs.voxel51.com/api/fiftyone.core.frame_utils.html
---

# fiftyone.core.frame_utils#

Frame utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`is_frame_number`(value) | Determines whether the provided value is a frame number.  
---|---  
`validate_frame_number`(value) | Validates that the provided value is a frame number.  
  
**Exceptions:**

`FrameError` | Exception raised when an invalid frame number is encountered.  
---|---  
  
fiftyone.core.frame_utils.is_frame_number(_value_)#
    

Determines whether the provided value is a frame number.

Frame numbers are strictly positive integers.

Parameters:
    

**value** â a value

Returns:
    

True/False

Raises:
    

**FrameError** â if `value` is an integer but is not strictly positive

fiftyone.core.frame_utils.validate_frame_number(_value_)#
    

Validates that the provided value is a frame number.

Frame numbers are strictly positive integers.

Parameters:
    

**value** â a value

Raises:
    

**FrameError** â if `value` is not a frame number

exception fiftyone.core.frame_utils.FrameError#
    

Bases: `ValueError`

Exception raised when an invalid frame number is encountered.

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
