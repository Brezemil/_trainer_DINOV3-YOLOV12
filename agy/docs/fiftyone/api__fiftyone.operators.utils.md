---
source_url: https://docs.voxel51.com/api/fiftyone.operators.utils.html
---

# fiftyone.operators.utils#

FiftyOne operator utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ProgressHandler`(ctx[,Â logger,Â level]) | A logging handler that reports all logging messages issued while the handler's context manager is active to the provided execution context's [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") method.  
---|---  
  
**Functions:**

`is_method_overridden`(base_class,Â ...) | Returns whether a method is overridden in a subclass.  
---|---  
`is_new`(release_date[,Â days]) | Determines if a feature is considered "new" based on its release date.  
`create_operator_response`(result) | Creates a `starlette.responses.JSONResponse` from the given [`fiftyone.operators.executor.ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") or returns a server error `starlette.responses.JSONResponse` if serialization fails.  
  
class fiftyone.operators.utils.ProgressHandler(_ctx_ , _logger =None_, _level =None_)#
    

Bases: `Handler`

A logging handler that reports all logging messages issued while the handlerâs context manager is active to the provided execution contextâs [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") method.

Parameters:
    

  * **ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **logger** (_None_) â a specific `logging.Logger` for which to report records. By default, the root logger is used

  * **level** (_None_) â an optional logging level above which to report records. By default, the loggerâs effective level is used




**Methods:**

`emit`(record) | Do whatever it takes to actually log the specified logging record.  
---|---  
`acquire`() | Acquire the I/O thread lock.  
`addFilter`(filter) | Add the specified filter to this handler.  
`close`() | Tidy up any resources used by the handler.  
`createLock`() | Acquire a thread lock for serializing access to the underlying I/O.  
`filter`(record) | Determine if a record is loggable by consulting all the filters.  
`flush`() | Ensure all logging output has been flushed.  
`format`(record) | Format the specified record.  
`get_name`() |   
`handle`(record) | Conditionally emit the specified logging record.  
`handleError`(record) | Handle errors which occur during an emit() call.  
`release`() | Release the I/O thread lock.  
`removeFilter`(filter) | Remove the specified filter from this handler.  
`setFormatter`(fmt) | Set the formatter for this handler.  
`setLevel`(level) | Set the logging level of this handler.  
`set_name`(name) |   
  
**Attributes:**

`name` |   
---|---  
  
emit(_record_)#
    

Do whatever it takes to actually log the specified logging record.

This version is intended to be implemented by subclasses and so raises a NotImplementedError.

acquire()#
    

Acquire the I/O thread lock.

addFilter(_filter_)#
    

Add the specified filter to this handler.

close()#
    

Tidy up any resources used by the handler.

This version removes the handler from an internal map of handlers, _handlers, which is used for handler lookup by name. Subclasses should ensure that this gets called from overridden close() methods.

createLock()#
    

Acquire a thread lock for serializing access to the underlying I/O.

filter(_record_)#
    

Determine if a record is loggable by consulting all the filters.

The default is to allow the record to be logged; any filter can veto this and the record is then dropped. Returns a zero value if a record is to be dropped, else non-zero.

Changed in version 3.2: Allow filters to be just callables.

flush()#
    

Ensure all logging output has been flushed.

This version does nothing and is intended to be implemented by subclasses.

format(_record_)#
    

Format the specified record.

If a formatter is set, use it. Otherwise, use the default formatter for the module.

get_name()#
    

handle(_record_)#
    

Conditionally emit the specified logging record.

Emission depends on filters which may have been added to the handler. Wrap the actual emission of the record with acquisition/release of the I/O thread lock. Returns whether the filter passed the record for emission.

handleError(_record_)#
    

Handle errors which occur during an emit() call.

This method should be called from handlers when an exception is encountered during an emit() call. If raiseExceptions is false, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors. You could, however, replace this with a custom handler if you wish. The record which was being processed is passed in to this method.

property name#
    

release()#
    

Release the I/O thread lock.

removeFilter(_filter_)#
    

Remove the specified filter from this handler.

setFormatter(_fmt_)#
    

Set the formatter for this handler.

setLevel(_level_)#
    

Set the logging level of this handler. level must be an int or a str.

set_name(_name_)#
    

fiftyone.operators.utils.is_method_overridden(_base_class_ , _sub_class_instance_ , _method_name_)#
    

Returns whether a method is overridden in a subclass.

Parameters:
    

  * **base_class** â the base class

  * **sub_class_instance** â an instance of the subclass

  * **method_name** â the name of the method



Returns:
    

True/False

fiftyone.operators.utils.is_new(_release_date_ , _days =30_)#
    

Determines if a feature is considered ânewâ based on its release date.

A feature is considered new if its release date is within the specified number of days.

Examples:
    
    
    is_new("2024-11-09")
    # True if today's date is within 30 days after 2024-11-09
    
    is_new(datetime(2024, 11, 9), days=15)
    # True if today's date is within 15 days after November 9, 2024
    
    is_new("2024-10-01", days=45)
    # False if today's date is more than 45 days after October 1, 2024
    

Parameters:
    

  * **release_date** â 

the release date of the feature, in one of the following formats:

    * a string in the format `"%Y-%m-%d"`, e.g., `"2024-11-09"`

    * a datetime instance

  * **days** (_30_) â the number of days for which the feature is considered new



Returns:
    

True/False whether the release date is within the specified number of days

async fiftyone.operators.utils.create_operator_response(_result : [ExecutionResult](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult")_) → Response | JSONResponse#
    

Creates a `starlette.responses.JSONResponse` from the given [`fiftyone.operators.executor.ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") or returns a server error `starlette.responses.JSONResponse` if serialization fails.

Parameters:
    

**result** â the operator execution result

Returns:
    

`starlette.responses.Response` or `starlette.responses.JSONResponse`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
