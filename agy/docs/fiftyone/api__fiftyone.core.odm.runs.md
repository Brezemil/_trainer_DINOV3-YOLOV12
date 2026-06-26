---
source_url: https://docs.voxel51.com/api/fiftyone.core.odm.runs.html
---

# fiftyone.core.odm.runs#

Dataset run documents.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`RunDocument`(**kwargs) | Backing document for dataset runs.  
---|---  
  
class fiftyone.core.odm.runs.RunDocument(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Backing document for dataset runs.

**Attributes:**

`dataset_id` | An Object ID field.  
---|---  
`key` | A unicode string field.  
`version` | A unicode string field.  
`timestamp` | A datetime field.  
`config` | A dictionary field that wraps a standard Python dictionary.  
`view_stages` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`results` | A GridFS storage field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Methods:**

`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
---|---  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`compare_indexes`() | Compares the indexes defined in MongoEngine with the ones existing in the database.  
`copy`([new_id]) | Returns a deep copy of the document.  
`copy_with_new_id`() |   
`create_index`(keys[,Â background]) | Creates the given indexes if required.  
`delete`([signal_kwargs]) | Delete the `Document` from the database.  
`drop_collection`() | Drops the entire collection associated with this `Document` type from the database.  
`ensure_indexes`() | Checks the document meta data and ensures all the indexes exist.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`list_indexes`() | Lists all indexes that should be created for the Document collection.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`modify`([query]) | Perform an atomic update of the document in the database and reload the document object using updated version.  
`register_delete_rule`(document_cls,Â ...) | This method registers the delete rules to apply when removing this object.  
`reload`(*fields,Â **kwargs) | Reloads the document from the database.  
`save`([upsert,Â validate,Â safe]) | Saves the document to the database.  
`select_related`([max_depth]) | Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`switch_collection`(collection_name[,Â ...]) | Temporarily switch the collection for a document instance.  
`switch_db`(db_alias[,Â keep_created]) | Temporarily switch the database for a document instance.  
`to_dbref`() | Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`update`(**kwargs) | Performs an update on the `Document` A convenience wrapper to `update()`.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
dataset_id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




key#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




version#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




timestamp#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




config#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




view_stages#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




results#
    

A GridFS storage field.

exception DoesNotExist#
    

Bases: `DoesNotExist`

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

exception MultipleObjectsReturned#
    

Bases: `MultipleObjectsReturned`

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

STRICT = False#
    

cascade_save(_** kwargs_)#
    

Recursively save any references and generic references on the document.

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

classmethod compare_indexes()#
    

Compares the indexes defined in MongoEngine with the ones existing in the database. Returns any missing/extra indexes.

copy(_new_id =False_)#
    

Returns a deep copy of the document.

Parameters:
    

**new_id** (_False_) â whether to generate a new ID for the copied document. By default, the ID is left as `None` and will be automatically populated when the document is added to the database

copy_with_new_id()#
    

classmethod create_index(_keys_ , _background =False_, _** kwargs_)#
    

Creates the given indexes if required.

Parameters:
    

  * **keys** â a single index key or a list of index keys (to construct a multi-field index); keys may be prefixed with a **+** or a **-** to determine the index ordering

  * **background** â Allows index creation in the background




delete(_signal_kwargs =None_, _** write_concern_)#
    

Delete the `Document` from the database. This will only take effect if the document has been previously saved.

Parameters:
    

  * **signal_kwargs** â (optional) kwargs dictionary to be passed to the signal calls.

  * **write_concern** â Extra keyword arguments are passed down which will be used as options for the resultant `getLastError` command. For example, `save(..., w: 2, fsync: True)` will wait until at least two servers have recorded the write and will force an fsync on the primary server.




classmethod drop_collection()#
    

Drops the entire collection associated with this `Document` type from the database.

Raises `OperationError` if the document has no collection set (i.g. if it is abstract)

classmethod ensure_indexes()#
    

Checks the document meta data and ensures all the indexes exist.

Global defaults can be set in the meta - see guide/defining-documents

By default, this will get called automatically upon first interaction with the Document collection (query, save, etc) so unless you disabled auto_create_index, you shouldnât have to call this manually.

This also gets called upon every call to Document.save if auto_create_index_on_save is set to True

If called multiple times, MongoDB will not re-recreate indexes if they exist already

Note

You can disable automatic index creation by setting auto_create_index to False in the documents meta data

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

A field wrapper around MongoDBâs ObjectIds.

property in_db#
    

Whether the document has been inserted into the database.

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

classmethod list_indexes()#
    

Lists all indexes that should be created for the Document collection. It includes all the indexes from super- and sub-classes.

Note that it will only return the indexesâ fields, not the indexesâ options

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




modify(_query =None_, _** update_)#
    

Perform an atomic update of the document in the database and reload the document object using updated version.

Returns True if the document has been updated or False if the document in the database doesnât match the query.

Note

All unsaved changes that have been made to the document are rejected if the method returns True.

Parameters:
    

  * **query** â the update will be performed only if the document in the database matches the query

  * **update** â Django-style update keyword arguments




my_metaclass#
    

alias of `TopLevelDocumentMetaclass`

property pk#
    

Get the primary key.

classmethod register_delete_rule(_document_cls_ , _field_name_ , _rule_)#
    

This method registers the delete rules to apply when removing this object.

reload(_* fields_, _** kwargs_)#
    

Reloads the document from the database.

Parameters:
    

***fields** â an optional args list of specific fields to reload

save(_upsert =False_, _validate =True_, _safe =False_, _** kwargs_)#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

select_related(_max_depth =1_)#
    

Handles dereferencing of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") objects to a maximum depth in order to cut down the number queries to mongodb.

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

switch_collection(_collection_name_ , _keep_created =True_)#
    

Temporarily switch the collection for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_collection('old-users')
    user.save()
    

Parameters:
    

  * **collection_name** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching collection, else is reset to True




See also

Use `switch_db` if you need to read from another database

switch_db(_db_alias_ , _keep_created =True_)#
    

Temporarily switch the database for a document instance.

Only really useful for archiving off data and calling save():
    
    
    user = User.objects.get(id=user_id)
    user.switch_db('archive-db')
    user.save()
    

Parameters:
    

  * **db_alias** (_str_) â The database alias to use for saving the document

  * **keep_created** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â keep self._created value after switching db, else is reset to True




See also

Use `switch_collection` if you need to read from another collection

to_dbref()#
    

Returns an instance of [`DBRef`](https://pymongo.readthedocs.io/en/stable/api/bson/dbref.html#bson.dbref.DBRef "\(in PyMongo v4.17.0\)") useful in __raw__ queries.

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

update(_** kwargs_)#
    

Performs an update on the `Document` A convenience wrapper to `update()`.

Raises `OperationError` if called on an object that has not yet been saved.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
