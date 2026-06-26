---
source_url: https://docs.voxel51.com/api/fiftyone.core.odm.ontology.html
---

# fiftyone.core.odm.ontology#

Ontology documents.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`OntologyType`(value) | Allowed values for `OntologyDocument.type` in storage and APIs.  
---|---  
`OntologyDocument`(**kwargs) | Backing document for ontologies.  
  
class fiftyone.core.odm.ontology.OntologyType(_value_)#
    

Bases: `str`, `Enum`

Allowed values for `OntologyDocument.type` in storage and APIs.

`TAXONOMY` â a reusable hierarchical class tree. Multiple annotation ontologies can reference the same taxonomy by name.

`ANNOTATION_ONTOLOGY` â a container that defines classes, attributes (with optional conditional display logic), and references to taxonomies. This is the document that gets connected to a label schema on a field.

**Attributes:**

`TAXONOMY` |   
---|---  
`ANNOTATION_ONTOLOGY` |   
  
**Methods:**

`encode`([encoding,Â errors]) | Encode the string using the codec registered for encoding.  
---|---  
`replace`(old,Â new[,Â count]) | Return a copy with all occurrences of substring old replaced by new.  
`split`([sep,Â maxsplit]) | Return a list of the substrings in the string, using sep as the separator string.  
`rsplit`([sep,Â maxsplit]) | Return a list of the substrings in the string, using sep as the separator string.  
`join`(iterable,Â /) | Concatenate any number of strings.  
`capitalize`() | Return a capitalized version of the string.  
`casefold`() | Return a version of the string suitable for caseless comparisons.  
`title`() | Return a version of the string where each word is titlecased.  
`center`(width[,Â fillchar]) | Return a centered string of length width.  
`count`(sub[,Â start[,Â end]]) | Return the number of non-overlapping occurrences of substring sub in string S[start:end].  
`expandtabs`([tabsize]) | Return a copy where all tab characters are expanded using spaces.  
`find`(sub[,Â start[,Â end]]) | Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
`partition`(sep,Â /) | Partition the string into three parts using the given separator.  
`index`(sub[,Â start[,Â end]]) | Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
`ljust`(width[,Â fillchar]) | Return a left-justified string of length width.  
`lower`() | Return a copy of the string converted to lowercase.  
`lstrip`([chars]) | Return a copy of the string with leading whitespace removed.  
`rfind`(sub[,Â start[,Â end]]) | Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  
`rindex`(sub[,Â start[,Â end]]) | Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  
`rjust`(width[,Â fillchar]) | Return a right-justified string of length width.  
`rstrip`([chars]) | Return a copy of the string with trailing whitespace removed.  
`rpartition`(sep,Â /) | Partition the string into three parts using the given separator.  
`splitlines`([keepends]) | Return a list of the lines in the string, breaking at line boundaries.  
`strip`([chars]) | Return a copy of the string with leading and trailing whitespace removed.  
`swapcase`() | Convert uppercase characters to lowercase and lowercase characters to uppercase.  
`translate`(table,Â /) | Replace each character in the string using the given translation table.  
`upper`() | Return a copy of the string converted to uppercase.  
`startswith`(prefix[,Â start[,Â end]]) | Return True if S starts with the specified prefix, False otherwise.  
`endswith`(suffix[,Â start[,Â end]]) | Return True if S ends with the specified suffix, False otherwise.  
`removeprefix`(prefix,Â /) | Return a str with the given prefix string removed if present.  
`removesuffix`(suffix,Â /) | Return a str with the given suffix string removed if present.  
`isascii`() | Return True if all characters in the string are ASCII, False otherwise.  
`islower`() | Return True if the string is a lowercase string, False otherwise.  
`isupper`() | Return True if the string is an uppercase string, False otherwise.  
`istitle`() | Return True if the string is a title-cased string, False otherwise.  
`isspace`() | Return True if the string is a whitespace string, False otherwise.  
`isdecimal`() | Return True if the string is a decimal string, False otherwise.  
`isdigit`() | Return True if the string is a digit string, False otherwise.  
`isnumeric`() | Return True if the string is a numeric string, False otherwise.  
`isalpha`() | Return True if the string is an alphabetic string, False otherwise.  
`isalnum`() | Return True if the string is an alpha-numeric string, False otherwise.  
`isidentifier`() | Return True if the string is a valid Python identifier, False otherwise.  
`isprintable`() | Return True if the string is printable, False otherwise.  
`zfill`(width,Â /) | Pad a numeric string with zeros on the left, to fill a field of the given width.  
`format`(*args,Â **kwargs) | Return a formatted version of S, using substitutions from args and kwargs.  
`format_map`(mapping) | Return a formatted version of S, using substitutions from mapping.  
`maketrans` | Return a translation table usable for str.translate().  
  
TAXONOMY = 'taxonomy'#
    

ANNOTATION_ONTOLOGY = 'annotation_ontology'#
    

encode(_encoding ='utf-8'_, _errors ='strict'_)#
    

Encode the string using the codec registered for encoding.

encoding
    

The encoding in which to encode the string.

errors
    

The error handling scheme to use for encoding errors. The default is âstrictâ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are âignoreâ, âreplaceâ and âxmlcharrefreplaceâ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

replace(_old_ , _new_ , _count =-1_, _/_)#
    

Return a copy with all occurrences of substring old replaced by new.

> count
>     
> 
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

split(_sep =None_, _maxsplit =-1_)#
    

Return a list of the substrings in the string, using sep as the separator string.

> sep
>     
> 
> The separator used to split the string.
> 
> When set to None (the default value), will split on any whitespace character (including n r t f and spaces) and will discard empty strings from the result.
> 
> maxsplit
>     
> 
> Maximum number of splits. -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

rsplit(_sep =None_, _maxsplit =-1_)#
    

Return a list of the substrings in the string, using sep as the separator string.

> sep
>     
> 
> The separator used to split the string.
> 
> When set to None (the default value), will split on any whitespace character (including n r t f and spaces) and will discard empty strings from the result.
> 
> maxsplit
>     
> 
> Maximum number of splits. -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

join(_iterable_ , _/_)#
    

Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: â.â.join([âabâ, âpqâ, ârsâ]) -> âab.pq.rsâ

capitalize()#
    

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()#
    

Return a version of the string suitable for caseless comparisons.

title()#
    

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

center(_width_ , _fillchar =' '_, _/_)#
    

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(_sub_[, _start_[, _end_]]) → int#
    

Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

expandtabs(_tabsize =8_)#
    

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(_sub_[, _start_[, _end_]]) → int#
    

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

partition(_sep_ , _/_)#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

index(_sub_[, _start_[, _end_]]) → int#
    

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

ljust(_width_ , _fillchar =' '_, _/_)#
    

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#
    

Return a copy of the string converted to lowercase.

lstrip(_chars =None_, _/_)#
    

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

rfind(_sub_[, _start_[, _end_]]) → int#
    

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(_sub_[, _start_[, _end_]]) → int#
    

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(_width_ , _fillchar =' '_, _/_)#
    

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rstrip(_chars =None_, _/_)#
    

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

rpartition(_sep_ , _/_)#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

splitlines(_keepends =False_)#
    

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

strip(_chars =None_, _/_)#
    

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#
    

Convert uppercase characters to lowercase and lowercase characters to uppercase.

translate(_table_ , _/_)#
    

Replace each character in the string using the given translation table.

> table
>     
> 
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()#
    

Return a copy of the string converted to uppercase.

startswith(_prefix_[, _start_[, _end_]]) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

endswith(_suffix_[, _start_[, _end_]]) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

removeprefix(_prefix_ , _/_)#
    

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

removesuffix(_suffix_ , _/_)#
    

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

isascii()#
    

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

islower()#
    

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isupper()#
    

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

istitle()#
    

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isspace()#
    

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

isdecimal()#
    

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()#
    

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isnumeric()#
    

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isalpha()#
    

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isalnum()#
    

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isidentifier()#
    

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as âdefâ or âclassâ.

isprintable()#
    

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

zfill(_width_ , _/_)#
    

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

format(_* args_, _** kwargs_) → str#
    

Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (â{â and â}â).

format_map(_mapping_) → str#
    

Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (â{â and â}â).

static maketrans()#
    

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

class fiftyone.core.odm.ontology.OntologyDocument(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

Backing document for ontologies.

Ontologies are global resources not scoped to any single dataset. Multiple datasets can reference the same ontology by name. Each save creates a new versioned document; `(slug, version)` is unique, so names differing only in case or punctuation collide on save.

`schema_version` records the internal layout version of the row at write time. Bump `CURRENT_SCHEMA_VERSION` and add a migration when changing the persisted structure (especially `root`).

**Attributes:**

`name` | A unicode string field.  
---|---  
`slug` | A unicode string field.  
`version` | A 32 bit integer field.  
`schema_version` | A 32 bit integer field.  
`type` | A unicode string field.  
`description` | A unicode string field.  
`root` | A dictionary field that wraps a standard Python dictionary.  
`created_at` | A datetime field.  
`last_modified_at` | A datetime field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | A field wrapper around MongoDB's ObjectIds.  
`in_db` | Whether the document has been inserted into the database.  
`pk` | Get the primary key.  
  
**Methods:**

`save`(*args,Â **kwargs) | Saves the document to the database.  
---|---  
`cascade_save`(**kwargs) | Recursively save any references and generic references on the document.  
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
  
**Miscellaneous:**

`DoesNotExist` |   
---|---  
`MultipleObjectsReturned` |   
  
**Classes:**

`my_metaclass` |   
---|---  
  
name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




slug#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




version#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




schema_version#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




type#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




description#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




root#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




created_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




last_modified_at#
    

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




save(_* args: Any_, _** kwargs: Any_) → OntologyDocument#
    

Saves the document to the database.

If the document already exists, it will be updated, otherwise it will be created.

Parameters:
    

  * **upsert** (_False_) â whether to insert the document if it has an `id` populated but no document with that ID exists in the database

  * **validate** (_True_) â whether to validate the document

  * **safe** (_False_) â whether to `reload()` the document before raising any errors



Returns:
    

self

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
