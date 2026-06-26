---
source_url: https://docs.voxel51.com/api/fiftyone.core.context.html
---

# fiftyone.core.context#

Context utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`init_context`() | Initializes context settings.  
---|---  
`is_notebook_context`() | Determines whether this process is running in a notebook context, either Jupyter or Google Colab.  
`is_jupyter_context`() | Determines whether this process is running in a Jupyter notebook.  
`is_colab_context`() | Determines whether this process is running in Google Colab.  
`is_databricks_context`() | Determines whether this process is running in Databricks.  
`get_url`(address,Â port[,Â proxy_url]) |   
  
**Exceptions:**

`ContextError` | Exception raised when an action is taken in an unsupported context.  
---|---  
  
fiftyone.core.context.init_context()#
    

Initializes context settings.

fiftyone.core.context.is_notebook_context()#
    

Determines whether this process is running in a notebook context, either Jupyter or Google Colab.

Returns:
    

True/False

fiftyone.core.context.is_jupyter_context()#
    

Determines whether this process is running in a Jupyter notebook.

Returns:
    

True/False

fiftyone.core.context.is_colab_context()#
    

Determines whether this process is running in Google Colab.

Returns:
    

True/False

fiftyone.core.context.is_databricks_context()#
    

Determines whether this process is running in Databricks.

Returns:
    

True/False

fiftyone.core.context.get_url(_address : str_, _port : int_, _proxy_url : str = None_, _** kwargs: Dict[str, str]_) → str#
    

exception fiftyone.core.context.ContextError#
    

Bases: `OSError`

Exception raised when an action is taken in an unsupported context.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
`characters_written` |   
`errno` | POSIX exception code  
`filename` | exception filename  
`filename2` | second exception filename  
`strerror` | exception strerror  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

characters_written#
    

errno#
    

POSIX exception code

filename#
    

exception filename

filename2#
    

second exception filename

strerror#
    

exception strerror

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
