---
source_url: https://docs.voxel51.com/api/fiftyone.utils.geojson.html
---

# fiftyone.utils.geojson#

GeoJSON utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`load_location_data`(samples,Â geojson_or_path) | Loads geolocation data for the given samples from the given GeoJSON data.  
---|---  
`to_geo_json_geometry`(label) | Returns a GeoJSON `geometry` dict representation for the given location.  
`parse_point`(arg) | Parses the point into GeoJSON dict representation.  
`parse_polygon`(arg) | Parses the polygon or multi-polygon into GeoJSON dict representation.  
`geo_within`(location_field,Â boundary[,Â strict]) | Creates a MongoDB query expression that tests whether the given location field is contained within the specified boundary shape.  
`extract_coordinates`(d) | Extracts the coordinates from all geometries in the GeoJSON dictionary.  
  
**Classes:**

`GeoJSONDatasetImporter`([dataset_dir,Â ...]) | Importer for image or video datasets whose location data and labels are stored in GeoJSON format.  
---|---  
`GeoJSONDatasetExporter`([export_dir,Â ...]) | Exporter for image or video datasets whose location data and labels are stored in GeoJSON format.  
  
fiftyone.utils.geojson.load_location_data(_samples_ , _geojson_or_path_ , _location_field =None_, _skip_missing =True_, _progress =None_)#
    

Loads geolocation data for the given samples from the given GeoJSON data.

The GeoJSON data must be a `FeatureCollection` whose features have their `filename` properties populated, which are used to match the provided samples.

Example GeoJSON data:
    
    
    {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        -73.99496451958454,
                        40.66338032487842
                    ]
                },
                "properties": {
                    "filename": "b1c66a42-6f7d68ca.jpg"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [
                            -73.80992143421788,
                            40.65611832778962
                        ],
                        [
                            -74.02930609818584,
                            40.60505054722865
                        ]
                    ]
                },
                "properties": {
                    "filename": "/path/to/b1c81faa-3df17267.jpg"
                }
            },
        ]
    }
    

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **geojson_or_path** â a GeoJSON `FeatureCollection` dict or the path to one on disk

  * **location_field** (_None_) â the name of the location field in which to store the location data, which can be either a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") or [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations") field. If not specified, then, if there is an existing [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field, that field is used, else a new âlocationâ field is created

  * **skip_missing** (_True_) â whether to skip GeoJSON features with no `filename` properties (True) or raise an error (False)

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.geojson.to_geo_json_geometry(_label_)#
    

Returns a GeoJSON `geometry` dict representation for the given location.

Parameters:
    

**label** â a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") o [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations") instance

Returns:
    

a GeoJSON dict

fiftyone.utils.geojson.parse_point(_arg_)#
    

Parses the point into GeoJSON dict representation.

Parameters:
    

**point** â 

a point specified in any of the following formats:

  * A `[longitude, latitude]` list

  * A GeoJSON dict with `Point` type

  * A [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") instance whose `point` attribute contains the point




Returns:
    

a GeoJSON dict of type `Point`

fiftyone.utils.geojson.parse_polygon(_arg_)#
    

Parses the polygon or multi-polygon into GeoJSON dict representation.

Parameters:
    

**arg** â a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation"), [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations"), GeoJSON dict, or list of coordinates that define a `Polygon` or `MultiPolygon` to search within

Returns:
    

a GeoJSON dict of type `Polygon` or `MultiPolygon`

fiftyone.utils.geojson.geo_within(_location_field_ , _boundary_ , _strict =True_)#
    

Creates a MongoDB query expression that tests whether the given location field is contained within the specified boundary shape.

Parameters:
    

  * **location_field** â the embedded field containing GeoJSON data

  * **boundary** â a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation"), [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations"), GeoJSON dict, or list of coordinates that define a `Polygon` or `MultiPolygon` to search within

  * **strict** (_True_) â whether documents must exist entirely within (True) or intersect (False) the boundary



Returns:
    

a MongoDB query dict

fiftyone.utils.geojson.extract_coordinates(_d_)#
    

Extracts the coordinates from all geometries in the GeoJSON dictionary.

The dict can have any `type` supported by the GeoJSON spec, including `Feature`, `FeatureCollection`, `GeometryCollection`, and primitive geometries `Point`, `LineString`, `Polygon`, `MultiPoint`, `MultiLineString`, or `MultiPolygon`.

Parameters:
    

**d** â a GeoJSON dict

Returns:
    

a tuple of

  * points: a list of `Point` coordinates

  * lines: a list of `LineString` coordinates

  * points: a list of `Polygon` coordinates




class fiftyone.utils.geojson.GeoJSONDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _location_field ='location'_, _multi_location =False_, _property_parsers =None_, _skip_missing_media =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`GenericSampleDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter "fiftyone.utils.data.importers.GenericSampleDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for image or video datasets whose location data and labels are stored in GeoJSON format.

See [this page](user_guide__import_datasets.md#geojsondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping filenames to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels.json`

  * **location_field** (_"location"_) â the name of the field in which to store the location data

  * **multi_location** (_False_) â whether this GeoJSON may contain multiple shapes for each sample and thus its location data should be stored in a [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations") field rather than the default [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field

  * **property_parsers** (_None_) â an optional dict mapping property names to functions that parse the property values (e.g., into the appropriate) [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types). By default, all properties are stored as primitive field values

  * **skip_missing_media** (_False_) â whether to skip (True) or raise an error (False) when features with no `filename` property are encountered

  * **include_all_data** (_False_) â whether to generate samples for all media in the data directory (True) rather than only creating samples for media with label entries (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_sample_field_schema` | Whether this importer produces a sample field schema.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
  
property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

class fiftyone.utils.geojson.GeoJSONDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _image_format =None_, _location_field =None_, _property_makers =None_, _omit_none_fields =True_, _pretty_print =False_)#
    

Bases: [`GenericSampleDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter "fiftyone.utils.data.exporters.GenericSampleDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter for image or video datasets whose location data and labels are stored in GeoJSON format.

See [this page](user_guide__export_datasets.md#geojsondataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. This has no effect if `data_path` and `labels_path` are absolute paths

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the media

    * an absolute directory path in which to export the media. In this case, the `export_dir` has no effect on the location of the data

    * a JSON filename like `"data.json"` specifying the filename of the manifest file in `export_dir` generated when `export_media` is `"manifest"`

    * an absolute filepath specifying the location to write the JSON manifest file when `export_media` is `"manifest"`. In this case, `export_dir` has no effect on the location of the data

If None, the default value of this parameter will be chosen based on the value of the `export_media` parameter

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location in `export_dir` in which to export the labels

    * an absolute filepath to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be exported into `export_dir` using the default filename

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the images in the exported labels

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **location_field** (_None_) â 

the name of the field containing the location data for each sample. Can be any of the following:

    * The name of a `fiftyone.core.fields.GeoLocation` field

    * The name of a `fiftyone.core.fields.GeoLocations` field

    * `None`, in which case there must be a single `fiftyone.core.fields.GeoLocation` field on the samples, which is used by default

  * **property_makers** (_None_) â an optional dict mapping sample field names to functions that convert the field values to property values to be stored in the `properties` field of the GeoJSON `Feature` for the sample. By default, no properties are written

  * **omit_none_fields** (_True_) â whether to omit `None`-valued Sample fields from the output properties

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(sample) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_sample_)#
    

Exports the given sample to the dataset.

Parameters:
    

**sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
