---
source_url: https://docs.voxel51.com/api/fiftyone.core.storage.html
---

# fiftyone.core.storage#

File storage utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`FileSystem`(value) | Enumeration of the available file systems.  
---|---  
`TempDir`([basedir]) | Context manager that creates and destroys a temporary directory.  
`FileCollection`([iterable]) | A list of open file-like objects with a closing context manager  
  
**Functions:**

`get_file_system`(path) | Returns the file system enum for the given path.  
---|---  
`split_prefix`(path) | Splits the file system prefix from the given path.  
`get_bucket_name`(path) | Gets the bucket name from the given path.  
`is_local`(path) | Determines whether the given path is local.  
`ensure_local`(path) | Ensures that the given path is local.  
`normalize_path`(path) | Normalizes the given path by converting it to an absolute path and expanding the user directory, if necessary.  
`make_temp_dir`([basedir]) | Makes a temporary directory.  
`open_file`(path[,Â mode]) | Opens the given file for reading or writing.  
`open_files`(paths[,Â mode,Â skip_failures,Â ...]) | Opens the given files for reading or writing.  
`read_file`(path[,Â binary]) | Reads the file.  
`read_files`(paths[,Â binary,Â skip_failures,Â ...]) | Reads the specified files into memory.  
`write_file`(str_or_bytes,Â path) | Writes the given string/bytes to a file.  
`sep`(path) | Returns the path separator for the given path.  
`join`(a,Â *p) | Joins the given path components into a single path.  
`realpath`(path) | Converts the given path to absolute, resolving symlinks and relative path indicators such as `.` and `..`.  
`isabs`(path) | Determines whether the given path is absolute.  
`abspath`(path) | Converts the given path to an absolute path, resolving relative path indicators such as `.` and `..`.  
`normpath`(path) | Normalizes the given path by converting all slashes to forward slashes on Unix and backslashes on Windows and removing duplicate slashes.  
`exists`(path) | Determines whether the given file or directory exists.  
`isfile`(path) | Determines whether the given file exists.  
`isdir`(dirpath) | Determines whether the given directory exists.  
`make_archive`(dirpath,Â archive_path[,Â cleanup]) | Makes an archive containing the given directory.  
`extract_archive`(archive_path[,Â outdir,Â cleanup]) | Extracts the contents of an archive.  
`ensure_empty_dir`(dirpath[,Â cleanup]) | Ensures that the given directory exists and is empty.  
`ensure_basedir`(path) | Makes the base directory of the given path, if necessary.  
`ensure_dir`(dirpath) | Makes the given directory, if necessary.  
`load_json`(path_or_str) | Loads JSON from the input argument.  
`read_json`(path) | Reads a JSON file.  
`write_json`(d,Â path[,Â pretty_print]) | Writes JSON object to file.  
`load_ndjson`(path_or_str) | Loads NDJSON from the input argument.  
`read_ndjson`(path) | Reads an NDJSON file.  
`write_ndjson`(obj,Â path) | Writes the list of JSON dicts in NDJSON format.  
`read_yaml`(path) | Reads a YAML file.  
`write_yaml`(obj,Â path,Â **kwargs) | Writes the object to a YAML file.  
`list_files`(dirpath[,Â abs_paths,Â recursive,Â ...]) | Lists the files in the given directory.  
`list_subdirs`(dirpath[,Â abs_paths,Â recursive]) | Lists the subdirectories in the given directory, sorted alphabetically and excluding hidden directories.  
`list_buckets`(fs[,Â abs_paths]) | Lists the available buckets in the given file system.  
`list_available_file_systems`() | Lists the file systems that are currently available for use with methods like `list_files()` and `list_buckets()`.  
`get_glob_matches`(glob_patt) | Returns a list of file paths matching the given glob pattern.  
`get_glob_root`(glob_patt) | Finds the root directory of the given glob pattern, i.e., the deepest subdirectory that contains no glob characters.  
`copy_file`(inpath,Â outpath) | Copies the input file to the output location.  
`copy_files`(inpaths,Â outpaths[,Â ...]) | Copies the files to the given locations.  
`copy_dir`(indir,Â outdir[,Â overwrite,Â ...]) | Copies the input directory to the output directory.  
`move_file`(inpath,Â outpath) | Moves the given file to a new location.  
`move_files`(inpaths,Â outpaths[,Â ...]) | Moves the files to the given locations.  
`move_dir`(indir,Â outdir[,Â overwrite,Â ...]) | Moves the contents of the given directory into the given output directory.  
`delete_file`(path) | Deletes the file at the given path.  
`delete_files`(paths[,Â skip_failures,Â progress]) | Deletes the files from the given locations.  
`delete_dir`(dirpath) | Deletes the given directory and recursively deletes any empty directories from the resulting directory tree.  
`run`(fcn,Â tasks[,Â return_results,Â ...]) | Applies the given function to each element of the given tasks.  
  
class fiftyone.core.storage.FileSystem(_value_)#
    

Bases: `Enum`

Enumeration of the available file systems.

**Attributes:**

`LOCAL` |   
---|---  
  
LOCAL = 'local'#
    

fiftyone.core.storage.get_file_system(_path_)#
    

Returns the file system enum for the given path.

Parameters:
    

**path** â a path

Returns:
    

a `FileSystem` value

fiftyone.core.storage.split_prefix(_path_)#
    

Splits the file system prefix from the given path.

The prefix for local paths is `""`.

Example usages:
    
    
    import fiftyone.core.storage as fos
    
    fos.split_prefix("/path/to/file")       # ('', '/path/to/file')
    fos.split_prefix("a/file")              # ('', 'a/file')
    

Parameters:
    

**path** â a path

Returns:
    

a `(prefix, path)` tuple

fiftyone.core.storage.get_bucket_name(_path_)#
    

Gets the bucket name from the given path.

The bucket name for local paths is `""`.

Example usages:
    
    
    import fiftyone.core.storage as fos
    
    fos.get_bucket_name("/path/to/file")       # ''
    fos.get_bucket_name("a/file")              # ''
    

Parameters:
    

**path** â a path

Returns:
    

the bucket name string

fiftyone.core.storage.is_local(_path_)#
    

Determines whether the given path is local.

Parameters:
    

**path** â a path

Returns:
    

True/False

fiftyone.core.storage.ensure_local(_path_)#
    

Ensures that the given path is local.

Parameters:
    

**path** â a path

fiftyone.core.storage.normalize_path(_path_)#
    

Normalizes the given path by converting it to an absolute path and expanding the user directory, if necessary.

Parameters:
    

**path** â a path

Returns:
    

the normalized path

fiftyone.core.storage.make_temp_dir(_basedir =None_)#
    

Makes a temporary directory.

Parameters:
    

**basedir** (_None_) â an optional directory in which to create the new directory. The default is `fiftyone.config.default_dataset_dir`

Returns:
    

the temporary directory path

class fiftyone.core.storage.TempDir(_basedir =None_)#
    

Bases: `object`

Context manager that creates and destroys a temporary directory.

Parameters:
    

**basedir** (_None_) â an optional directory in which to create the new directory. The default is `fiftyone.config.default_dataset_dir`

fiftyone.core.storage.open_file(_path_ , _mode ='r'_)#
    

Opens the given file for reading or writing.

Example usage:
    
    
    import fiftyone.core.storage as fos
    
    with fos.open_file("/tmp/file.txt", "w") as f:
        f.write("Hello, world!")
    
    with fos.open_file("/tmp/file.txt", "r") as f:
        print(f.read())
    

Parameters:
    

  * **path** â the path

  * **mode** (_"r"_) â the mode. Supported values are `("r", "rb", "w", "wb")`



Returns:
    

an open file-like object

class fiftyone.core.storage.FileCollection(_iterable =()_, _/_)#
    

Bases: `list`

A list of open file-like objects with a closing context manager

**Methods:**

`append`(object,Â /) | Append object to the end of the list.  
---|---  
`clear`() | Remove all items from list.  
`copy`() | Return a shallow copy of the list.  
`count`(value,Â /) | Return number of occurrences of value.  
`extend`(iterable,Â /) | Extend list by appending elements from the iterable.  
`index`(value[,Â start,Â stop]) | Return first index of value.  
`insert`(index,Â object,Â /) | Insert object before index.  
`pop`([index]) | Remove and return item at index (default last).  
`remove`(value,Â /) | Remove first occurrence of value.  
`reverse`() | Reverse _IN PLACE_.  
`sort`(*[,Â key,Â reverse]) | Sort the list in ascending order and return None.  
  
append(_object_ , _/_)#
    

Append object to the end of the list.

clear()#
    

Remove all items from list.

copy()#
    

Return a shallow copy of the list.

count(_value_ , _/_)#
    

Return number of occurrences of value.

extend(_iterable_ , _/_)#
    

Extend list by appending elements from the iterable.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

insert(_index_ , _object_ , _/_)#
    

Insert object before index.

pop(_index =-1_, _/_)#
    

Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

remove(_value_ , _/_)#
    

Remove first occurrence of value.

Raises ValueError if the value is not present.

reverse()#
    

Reverse _IN PLACE_.

sort(_*_ , _key =None_, _reverse =False_)#
    

Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

fiftyone.core.storage.open_files(_paths_ , _mode ='r'_, _skip_failures =False_, _progress =None_)#
    

Opens the given files for reading or writing.

Note: when `skip_failures` is True, entries corresponding to failed opens
    

are `None`

Parameters:
    

  * **paths** â a list of paths

  * **mode** (_"r"_) â the mode. Supported values are `("r", "rb", "w", "wb")`

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a `FileCollection` (list) of open file-like objects

fiftyone.core.storage.read_file(_path_ , _binary =False_)#
    

Reads the file.

Parameters:
    

  * **path** â the filepath

  * **binary** (_False_) â whether to read the file in binary mode



Returns:
    

the file contents

fiftyone.core.storage.read_files(_paths_ , _binary =False_, _skip_failures =False_, _progress =None_)#
    

Reads the specified files into memory.

Parameters:
    

  * **paths** â a list of filepaths

  * **binary** (_False_) â whether to read the files in binary mode

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of file contents

fiftyone.core.storage.write_file(_str_or_bytes_ , _path_)#
    

Writes the given string/bytes to a file.

If a string is provided, it is encoded via `.encode()`.

Parameters:
    

  * **str_or_bytes** â the string or bytes

  * **path** â the filepath




fiftyone.core.storage.sep(_path_)#
    

Returns the path separator for the given path.

Parameters:
    

**path** â the filepath

Returns:
    

the path separator

fiftyone.core.storage.join(_a_ , _* p_)#
    

Joins the given path components into a single path.

Parameters:
    

  * **a** â the root

  * ***p** â additional path components



Returns:
    

the joined path

fiftyone.core.storage.realpath(_path_)#
    

Converts the given path to absolute, resolving symlinks and relative path indicators such as `.` and `..`.

Parameters:
    

**path** â the filepath

Returns:
    

the resolved path

fiftyone.core.storage.isabs(_path_)#
    

Determines whether the given path is absolute.

Parameters:
    

**path** â the filepath

Returns:
    

True/False

fiftyone.core.storage.abspath(_path_)#
    

Converts the given path to an absolute path, resolving relative path indicators such as `.` and `..`.

Parameters:
    

**path** â the filepath

Returns:
    

the absolute path

fiftyone.core.storage.normpath(_path_)#
    

Normalizes the given path by converting all slashes to forward slashes on Unix and backslashes on Windows and removing duplicate slashes.

Use this function when you need a version of `os.path.normpath` that converts `\` to `/` on Unix.

Parameters:
    

**path** â a path

Returns:
    

the normalized path

fiftyone.core.storage.exists(_path_)#
    

Determines whether the given file or directory exists.

Parameters:
    

**path** â the file or directory path

Returns:
    

True/False

fiftyone.core.storage.isfile(_path_)#
    

Determines whether the given file exists.

Parameters:
    

**path** â the filepath

Returns:
    

True/False

fiftyone.core.storage.isdir(_dirpath_)#
    

Determines whether the given directory exists.

Cloud âfoldersâ are deemed to exist only if they are non-empty.

Parameters:
    

**dirpath** â the directory path

Returns:
    

True/False

fiftyone.core.storage.make_archive(_dirpath_ , _archive_path_ , _cleanup =False_)#
    

Makes an archive containing the given directory.

Supported formats include `.zip`, `.tar`, `.tar.gz`, `.tgz`, `.tar.bz` and `.tbz`.

Parameters:
    

  * **dirpath** â the directory to archive

  * **archive_path** â the archive path to write

  * **cleanup** (_False_) â whether to delete the directory after archiving it




fiftyone.core.storage.extract_archive(_archive_path_ , _outdir =None_, _cleanup =False_)#
    

Extracts the contents of an archive.

The following formats are guaranteed to work: `.zip`, `.tar`, `.tar.gz`, `.tgz`, `.tar.bz`, `.tbz`.

If an archive _not_ in the above list is found, extraction will be attempted via the `patool` package, which supports many formats but may require that additional system packages be installed.

Parameters:
    

  * **archive_path** â the archive path

  * **outdir** (_None_) â the directory into which to extract the archive. By default, the directory containing the archive is used

  * **cleanup** (_False_) â whether to delete the archive after extraction




fiftyone.core.storage.ensure_empty_dir(_dirpath_ , _cleanup =False_)#
    

Ensures that the given directory exists and is empty.

Parameters:
    

  * **dirpath** â the directory path

  * **cleanup** (_False_) â whether to delete any existing directory contents



Raises:
    

**ValueError** â if the directory is not empty and `cleanup` is False

fiftyone.core.storage.ensure_basedir(_path_)#
    

Makes the base directory of the given path, if necessary.

Parameters:
    

**path** â the filepath

fiftyone.core.storage.ensure_dir(_dirpath_)#
    

Makes the given directory, if necessary.

Parameters:
    

**dirpath** â the directory path

fiftyone.core.storage.load_json(_path_or_str_)#
    

Loads JSON from the input argument.

Parameters:
    

**path_or_str** â the filepath or JSON string

Returns:
    

the loaded JSON

fiftyone.core.storage.read_json(_path_)#
    

Reads a JSON file.

Parameters:
    

**path** â the filepath

Returns:
    

the JSON data

fiftyone.core.storage.write_json(_d_ , _path_ , _pretty_print =False_)#
    

Writes JSON object to file.

Parameters:
    

  * **d** â JSON data

  * **path** â the filepath

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




fiftyone.core.storage.load_ndjson(_path_or_str_)#
    

Loads NDJSON from the input argument.

Parameters:
    

**path_or_str** â the filepath or NDJSON string

Returns:
    

a list of JSON dicts

fiftyone.core.storage.read_ndjson(_path_)#
    

Reads an NDJSON file.

Parameters:
    

**path** â the filepath

Returns:
    

a list of JSON dicts

fiftyone.core.storage.write_ndjson(_obj_ , _path_)#
    

Writes the list of JSON dicts in NDJSON format.

Parameters:
    

  * **obj** â a list of JSON dicts

  * **path** â the filepath




fiftyone.core.storage.read_yaml(_path_)#
    

Reads a YAML file.

Parameters:
    

**path** â the filepath

Returns:
    

a list of JSON dicts

fiftyone.core.storage.write_yaml(_obj_ , _path_ , _** kwargs_)#
    

Writes the object to a YAML file.

Parameters:
    

  * **obj** â a Python object

  * **path** â the filepath

  * ****kwargs** â optional arguments for `yaml.dump(..., **kwargs)`




fiftyone.core.storage.list_files(_dirpath_ , _abs_paths =False_, _recursive =False_, _include_hidden_files =False_, _return_metadata =False_, _sort =True_)#
    

Lists the files in the given directory.

If the directory does not exist, an empty list is returned.

Parameters:
    

  * **dirpath** â the path to the directory to list

  * **abs_paths** (_False_) â whether to return the absolute paths to the files

  * **recursive** (_False_) â whether to recursively traverse subdirectories

  * **include_hidden_files** (_False_) â whether to include dot files

  * **return_metadata** (_False_) â whether to return metadata dicts for each file instead of filepaths

  * **sort** (_True_) â whether to sort the list of files



Returns:
    

a list of filepaths or metadata dicts

fiftyone.core.storage.list_subdirs(_dirpath_ , _abs_paths =False_, _recursive =False_)#
    

Lists the subdirectories in the given directory, sorted alphabetically and excluding hidden directories.

Parameters:
    

  * **dirpath** â the path to the directory to list

  * **abs_paths** (_False_) â whether to return absolute paths

  * **recursive** (_False_) â whether to recursively traverse subdirectories



Returns:
    

a list of subdirectories

fiftyone.core.storage.list_buckets(_fs_ , _abs_paths =False_)#
    

Lists the available buckets in the given file system.

This method returns subdirectories of `/` (or the current drive on Windows).

Parameters:
    

  * **fs** â a `FileSystem` value

  * **abs_paths** (_False_) â whether to return absolute paths



Returns:
    

a list of buckets

fiftyone.core.storage.list_available_file_systems()#
    

Lists the file systems that are currently available for use with methods like `list_files()` and `list_buckets()`.

Returns:
    

a list of `FileSystem` values

fiftyone.core.storage.get_glob_matches(_glob_patt_)#
    

Returns a list of file paths matching the given glob pattern.

The matches are returned in sorted order.

Parameters:
    

**glob_patt** â a glob pattern like `/path/to/files-*.jpg`

Returns:
    

a list of file paths

fiftyone.core.storage.get_glob_root(_glob_patt_)#
    

Finds the root directory of the given glob pattern, i.e., the deepest subdirectory that contains no glob characters.

Parameters:
    

**glob_patt** â a glob pattern like `/path/to/files-*.jpg`

Returns:
    

  * the root

  * True/False whether the pattern contains any special characters




Return type:
    

a tuple of

fiftyone.core.storage.copy_file(_inpath_ , _outpath_)#
    

Copies the input file to the output location.

Parameters:
    

  * **inpath** â the input path

  * **outpath** â the output path




fiftyone.core.storage.copy_files(_inpaths_ , _outpaths_ , _skip_failures =False_, _progress =None_)#
    

Copies the files to the given locations.

Parameters:
    

  * **inpaths** â a list of input paths

  * **outpaths** â a list of output paths

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.storage.copy_dir(_indir_ , _outdir_ , _overwrite =True_, _skip_failures =False_, _progress =None_)#
    

Copies the input directory to the output directory.

Parameters:
    

  * **indir** â the input directory

  * **outdir** â the output directory

  * **overwrite** (_True_) â whether to delete an existing output directory (True) or merge its contents (False)

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.storage.move_file(_inpath_ , _outpath_)#
    

Moves the given file to a new location.

Parameters:
    

  * **inpath** â the input path

  * **outpath** â the output path




fiftyone.core.storage.move_files(_inpaths_ , _outpaths_ , _skip_failures =False_, _progress =None_)#
    

Moves the files to the given locations.

Parameters:
    

  * **inpaths** â a list of input paths

  * **outpaths** â a list of output paths

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.storage.move_dir(_indir_ , _outdir_ , _overwrite =True_, _skip_failures =False_, _progress =None_)#
    

Moves the contents of the given directory into the given output directory.

Parameters:
    

  * **indir** â the input directory

  * **outdir** â the output directory

  * **overwrite** (_True_) â whether to delete an existing output directory (True) or merge its contents (False)

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.storage.delete_file(_path_)#
    

Deletes the file at the given path.

Any empty directories are also recursively deleted from the resulting directory tree.

Parameters:
    

**path** â the filepath

fiftyone.core.storage.delete_files(_paths_ , _skip_failures =False_, _progress =None_)#
    

Deletes the files from the given locations.

Any empty directories are also recursively deleted from the resulting directory tree.

Parameters:
    

  * **paths** â a list of paths

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if an operation fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.storage.delete_dir(_dirpath_)#
    

Deletes the given directory and recursively deletes any empty directories from the resulting directory tree.

Parameters:
    

**dirpath** â the directory path

fiftyone.core.storage.run(_fcn_ , _tasks_ , _return_results =True_, _num_workers =None_, _progress =None_)#
    

Applies the given function to each element of the given tasks.

Parameters:
    

  * **fcn** â a function that accepts a single argument

  * **tasks** â an iterable of function arguments

  * **return_results** (_True_) â whether to return the function results

  * **num_workers** (_None_) â a suggested number of threads to use

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

the list of function outputs, or None if `return_results == False`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
