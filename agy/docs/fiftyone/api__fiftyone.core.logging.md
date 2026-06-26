---
source_url: https://docs.voxel51.com/api/fiftyone.core.logging.html
---

# fiftyone.core.logging#

Logging utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`JsonFormatter`([fmt,Â datefmt,Â style,Â ...]) | Custom JSON formatting  
---|---  
  
**Functions:**

`add_handlers`(log_level) | Adds the default logging handlers to FiftyOne's package-wide loggers.  
---|---  
`init_logging`() | Initializes FiftyOne's package-wide logging.  
`get_logging_level`() | Gets FiftyOne's package-wide logging level.  
`set_logging_level`(level) | Sets FiftyOne's package-wide logging level.  
  
class fiftyone.core.logging.JsonFormatter(_fmt =None_, _datefmt =None_, _style ='%'_, _validate =True_, _*_ , _defaults =None_)#
    

Bases: `Formatter`

Custom JSON formatting

**Methods:**

`converter` | gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,  
---|---  
`format`(record) | Format the specified record as text.  
`formatException`(ei) | Format and return the specified exception information as a string.  
`formatMessage`(record) |   
`formatStack`(stack_info) | This method is provided as an extension point for specialized formatting of stack information.  
`formatTime`(record[,Â datefmt]) | Return the creation time of the specified LogRecord as formatted text.  
`usesTime`() | Check if the format uses the creation time of the record.  
  
**Attributes:**

`default_msec_format` |   
---|---  
`default_time_format` |   
  
converter()#
    

gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
    

tm_sec, tm_wday, tm_yday, tm_isdst)

Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a. GMT). When âsecondsâ is not passed in, convert the current time instead.

If the platform supports the tm_gmtoff and tm_zone, they are available as attributes only.

format(_record_)#
    

Format the specified record as text.

The recordâs attribute dictionary is used as the operand to a string formatting operation which yields the returned string. Before formatting the dictionary, a couple of preparatory steps are carried out. The message attribute of the record is computed using LogRecord.getMessage(). If the formatting string uses the time (as determined by a call to usesTime(), formatTime() is called to format the event time. If there is exception information, it is formatted using formatException() and appended to the message.

default_msec_format = '%s,%03d'#
    

default_time_format = '%Y-%m-%d %H:%M:%S'#
    

formatException(_ei_)#
    

Format and return the specified exception information as a string.

This default implementation just uses traceback.print_exception()

formatMessage(_record_)#
    

formatStack(_stack_info_)#
    

This method is provided as an extension point for specialized formatting of stack information.

The input data is a string as returned from a call to `traceback.print_stack()`, but with the last trailing newline removed.

The base implementation just returns the value passed in.

formatTime(_record_ , _datefmt =None_)#
    

Return the creation time of the specified LogRecord as formatted text.

This method should be called from format() by a formatter which wants to make use of a formatted time. This method can be overridden in formatters to provide for any specific requirement, but the basic behaviour is as follows: if datefmt (a string) is specified, it is used with time.strftime() to format the creation time of the record. Otherwise, an ISO8601-like (or RFC 3339-like) format is used. The resulting string is returned. This function uses a user-configurable function to convert the creation time to a tuple. By default, time.localtime() is used; to change this for a particular formatter instance, set the âconverterâ attribute to a function with the same signature as time.localtime() or time.gmtime(). To change it for all formatters, for example if you want all logging times to be shown in GMT, set the âconverterâ attribute in the Formatter class.

usesTime()#
    

Check if the format uses the creation time of the record.

fiftyone.core.logging.add_handlers(_log_level_)#
    

Adds the default logging handlers to FiftyOneâs package-wide loggers.

Parameters:
    

**log_level** â a `logging` level used to configure the loggers

fiftyone.core.logging.init_logging()#
    

Initializes FiftyOneâs package-wide logging.

The logging level is set to `fo.config.logging_level`.

fiftyone.core.logging.get_logging_level()#
    

Gets FiftyOneâs package-wide logging level.

Returns:
    

a `logging` level, such as `logging.INFO`

fiftyone.core.logging.set_logging_level(_level_)#
    

Sets FiftyOneâs package-wide logging level.

Parameters:
    

**level** â a `logging` level, such as `logging.INFO`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
