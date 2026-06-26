---
source_url: https://docs.voxel51.com/plugins/api/plugins.panels.similarity_search.constants.html
---

# plugins.panels.similarity_search.constants#

Similarity search panel constants.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`RunStatus`(value) | Statuses a similarity search run can be in.  
---|---  
`QueryType`(value) | Types of similarity queries.  
  
class plugins.panels.similarity_search.constants.RunStatus(_value_)#
    

Bases: `str`, `Enum`

Statuses a similarity search run can be in.

**Attributes:**

`PENDING` |   
---|---  
`RUNNING` |   
`COMPLETED` |   
`FAILED` |   
  
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
  
PENDING = 'pending'#
    

RUNNING = 'running'#
    

COMPLETED = 'completed'#
    

FAILED = 'failed'#
    

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

class plugins.panels.similarity_search.constants.QueryType(_value_)#
    

Bases: `str`, `Enum`

Types of similarity queries.

**Attributes:**

`TEXT` |   
---|---  
`IMAGE` |   
`UPLOAD` |   
  
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
  
TEXT = 'text'#
    

IMAGE = 'image'#
    

UPLOAD = 'upload'#
    

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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
