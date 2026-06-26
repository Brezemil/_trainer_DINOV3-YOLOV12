---
source_url: https://docs.voxel51.com/api/fiftyone.core.annotation.validate_label_schemas.html
---

# fiftyone.core.annotation.validate_label_schemas#

Annotation label schema validation

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Exceptions:**

`ValidationErrors` | Validation errors for label schemas  
---|---  
  
**Functions:**

`validate_label_schemas`(sample_collection,Â ...) | Validates label schemas for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
---|---  
  
exception fiftyone.core.annotation.validate_label_schemas.ValidationErrors#
    

Bases: `ExceptionGroup`

Validation errors for label schemas

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`derive` |   
`split` |   
`subgroup` |   
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
`exceptions` | nested exceptions  
`message` | exception message  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

derive()#
    

exceptions#
    

nested exceptions

message#
    

exception message

split()#
    

subgroup()#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

fiftyone.core.annotation.validate_label_schemas.validate_label_schemas(_sample_collection_ , _label_schema_ , _allow_new_attrs =False_, _allow_new_fields =False_, _fields =None_, __allow_default =False_)#
    

Validates label schemas for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"). See `generate_label_schemas()` for acceptable label schema specifications

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_schema** â a label schemas `dict` or an individual fieldâs label schema `dict` if only one field is provided

  * **allow_new_attrs** (_False_) â whether to allow label attributes that do not yet exist on the [field schema](https://docs.voxel51.com/user_guide/using_datasets.html#field-schemas)

  * **allow_new_fields** (_False_) â whether to allow label schemas for fields that do not yet exist on the [field schema](https://docs.voxel51.com/user_guide/using_datasets.html#field-schemas)

  * **fields** (_None_) â a field name, `embedded.field.name` or iterable of such values



Raises:
    

**ValidationErrors** â if the label schema(s) are invalid

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
