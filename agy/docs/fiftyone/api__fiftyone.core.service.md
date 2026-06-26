---
source_url: https://docs.voxel51.com/api/fiftyone.core.service.html
---

# fiftyone.core.service#

FiftyOne Services.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Exceptions:**

`ServiceException` | Base class for service-related exceptions.  
---|---  
`ServiceListenTimeout`(name[,Â port]) | Exception raised when a network-bound service fails to bind to a port.  
`ServiceExecutableNotFound` | Exception raised when the service executable is not found on disk.  
  
**Classes:**

`Service`() | Interface for FiftyOne services.  
---|---  
`MultiClientService`() | Base class for services that support multiple clients.  
`DatabaseService`() | Service that controls the underlying MongoDB database.  
`ServerService`(port[,Â address,Â do_not_track]) | Service that controls the FiftyOne web server.  
  
exception fiftyone.core.service.ServiceException#
    

Bases: `Exception`

Base class for service-related exceptions.

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

exception fiftyone.core.service.ServiceListenTimeout(_name_ , _port =None_)#
    

Bases: `ServiceException`

Exception raised when a network-bound service fails to bind to a port.

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

exception fiftyone.core.service.ServiceExecutableNotFound#
    

Bases: `ServiceException`

Exception raised when the service executable is not found on disk.

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

class fiftyone.core.service.Service#
    

Bases: `object`

Interface for FiftyOne services.

All services must define a `command` property.

Services are run in an isolated Python subprocess (see `service/main.py`) to ensure that they are shut down when the main Python process exits. The `command` and `working_dir` properties control the execution of the service in the subprocess.

**Attributes:**

`service_name` |   
---|---  
`working_dir` |   
`allow_headless` |   
`command` |   
`env` |   
  
**Methods:**

`start`() | Starts the service.  
---|---  
`stop`() | Stops the service.  
`wait`() | Waits for the service to exit and returns its exit code.  
  
service_name = None#
    

working_dir = '.'#
    

allow_headless = False#
    

property command#
    

property env#
    

start()#
    

Starts the service.

stop()#
    

Stops the service.

wait()#
    

Waits for the service to exit and returns its exit code.

class fiftyone.core.service.MultiClientService#
    

Bases: `Service`

Base class for services that support multiple clients.

**Attributes:**

`attached` |   
---|---  
`allow_headless` |   
`command` |   
`env` |   
`service_name` |   
`working_dir` |   
  
**Methods:**

`start`() | Searches for a running instance of this service, or starts one if no instance is found.  
---|---  
`stop`() | Disconnects from the service without actually stopping it.  
`wait`() | Waits for the service to exit and returns its exit code.  
  
attached = False#
    

start()#
    

Searches for a running instance of this service, or starts one if no instance is found.

stop()#
    

Disconnects from the service without actually stopping it.

allow_headless = False#
    

property command#
    

property env#
    

service_name = None#
    

wait()#
    

Waits for the service to exit and returns its exit code.

working_dir = '.'#
    

class fiftyone.core.service.DatabaseService#
    

Bases: `MultiClientService`

Service that controls the underlying MongoDB database.

**Attributes:**

`service_name` |   
---|---  
`allow_headless` |   
`MONGOD_EXE_NAME` |   
`command` |   
`port` |   
`attached` |   
`env` |   
`working_dir` |   
  
**Methods:**

`find_mongod`() | Returns the path to the mongod executable.  
---|---  
`start`() | Searches for a running instance of this service, or starts one if no instance is found.  
`stop`() | Disconnects from the service without actually stopping it.  
`wait`() | Waits for the service to exit and returns its exit code.  
  
service_name = 'db'#
    

allow_headless = True#
    

MONGOD_EXE_NAME = 'mongod'#
    

property command#
    

property port#
    

static find_mongod()#
    

Returns the path to the mongod executable.

attached = False#
    

property env#
    

start()#
    

Searches for a running instance of this service, or starts one if no instance is found.

stop()#
    

Disconnects from the service without actually stopping it.

wait()#
    

Waits for the service to exit and returns its exit code.

working_dir = '.'#
    

class fiftyone.core.service.ServerService(_port_ , _address =None_, _do_not_track =False_)#
    

Bases: `Service`

Service that controls the FiftyOne web server.

**Attributes:**

`service_name` |   
---|---  
`working_dir` |   
`allow_headless` |   
`command` |   
`port` |   
`address` |   
`env` |   
  
**Methods:**

`start`() | Starts the service.  
---|---  
`stop`() | Stops the service.  
`wait`() | Waits for the service to exit and returns its exit code.  
  
service_name = 'server'#
    

working_dir = '/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/fiftyone/server'#
    

allow_headless = True#
    

start()#
    

Starts the service.

property command#
    

property port#
    

property address#
    

property env#
    

stop()#
    

Stops the service.

wait()#
    

Waits for the service to exit and returns its exit code.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
