---
source_url: https://docs.voxel51.com/api/fiftyone.utils.utils3d.html
---

# fiftyone.utils.utils3d#

3D utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`compute_cuboid_iou`(gt,Â pred[,Â gt_crowd]) | Computes the IoU between the given ground truth and predicted cuboids.  
---|---  
`rpy_to_rotation`(euler_rpy) | Converts Euler angles in roll-pitch-yaw order to a scipy.spatial.transform Rotation.  
`multiple_coordinate_transform`(points,Â ...[,Â ...]) | Applies a sequence of 3D coordinate frame transformations to a point and its orientation.  
`single_coordinate_transform`(points,Â rot,Â ...) | Applies a single 3D coordinate frame transformation to a point and its orientation.  
`corners_from_euler`(location,Â rotation,Â dimension) | Computes the 3D corners of a cuboid given its location, rotation, and dimensions.  
`pinhole_projector`(points,Â cam_params[,Â ...]) | Projects 3D detection points to 2D using the given camera intrinsics assuming a pinhole camera.  
`point_in_front_of_camera`(corners_img,Â ...[,Â ...]) | Checks if the input corners are visible in the image and in front of the camera.  
`get_scene_asset_paths`(scene_paths[,Â ...]) | Extracts all asset paths for the specified 3D scenes.  
`compute_orthographic_projection_images`(...) | Computes orthographic projection images for the point clouds in the given collection.  
`compute_orthographic_projection_image`(...[,Â ...]) | Generates an orthographic projection image for the given PCD file onto the specified plane (default xy plane).  
`pcd_to_3d`(dataset[,Â slices,Â output_dir,Â ...]) | Converts the point cloud samples in the given dataset to 3D samples.  
  
**Classes:**

`OrthographicProjectionMetadata`(*args,Â **kwargs) | Class for storing metadata about orthographic projections.  
---|---  
  
fiftyone.utils.utils3d.compute_cuboid_iou(_gt_ , _pred_ , _gt_crowd =False_)#
    

Computes the IoU between the given ground truth and predicted cuboids.

Parameters:
    

  * **gt** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **pred** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **gt_crowd** (_False_) â whether the ground truth cuboid is a crowd



Returns:
    

the IoU, in `[0, 1]`

fiftyone.utils.utils3d.rpy_to_rotation(_euler_rpy : List[float]_)#
    

Converts Euler angles in roll-pitch-yaw order to a scipy.spatial.transform Rotation.

Parameters:
    

**euler_rpy** â a list of Euler angles in roll-pitch-yaw order

Returns:
    

A scipy.spatial.transform Rotation.

fiftyone.utils.utils3d.multiple_coordinate_transform(_points : List[float]_, _euler_rpy : List[float]_, _transformation_sequence : List[Tuple[[list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[float] | [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)"), [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[[list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[float]] | [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")]]_, _forward_transform_flags : List[[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")] = None_) → Tuple[List[float], List[float]]#
    

Applies a sequence of 3D coordinate frame transformations to a point and its orientation. Each transformation consists of a translation vector and a rotation matrix, applied in the order provided. The orientation is updated at each step using quaternion multiplication.

Parameters:
    

  * **points** â A 3-element list/array representing the (x, y, z) coordinates of the point

  * **euler_rpy** â A 3-element list of Euler angles [roll, pitch, yaw] in radians

  * **transformation_sequence** â A list of (translation, rotation) tuples: \- translation: 3-element vector (tx, ty, tz) \- rotation: (3, 3) rotation matrix

  * **forward_transform_flags** (_None_) â One per transformation True means apply the transform source â target False means apply the inverse (target â source). Defaults to all True



Returns:
    

  * Transformed 3D point [x, y, z].

  * Updated orientation as Euler angles [roll, pitch, yaw] in radians.




fiftyone.utils.utils3d.single_coordinate_transform(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _rot : Any_, _transformation : Tuple[[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)"), [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")]_, _forward_transform : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Tuple[[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)"), Any]#
    

Applies a single 3D coordinate frame transformation to a point and its orientation.

The transformation consists of a translation vector and a rotation matrix. The orientation is updated using quaternion multiplication.

Parameters:
    

  * **points** â A 3-element np.ndarray representing the (x, y, z) coordinates of the point

  * **rot** â A scipy.spatial.transform.Rotation representing the current orientation

  * **transformation** â A tuple containing: \- translation: 3-element array (tx, ty, tz) \- rotation_matrix: (3, 3) rotation matrix

  * **forward_transform** (_True_) â If True, applies the forward transform. If False, applies the inverse transform



Returns:
    

  * Transformed 3D point [x, y, z]

  * Updated orientation




fiftyone.utils.utils3d.corners_from_euler(_location : List[float]_, _rotation : List[float]_, _dimension : List[float]_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Computes the 3D corners of a cuboid given its location, rotation, and dimensions.

Parameters:
    

  * **location** â a 3-element list or np.ndarray representing the (x, y, z) location of the cuboid

  * **rotation** â a 3-element list or np.ndarray representing the (roll, pitch, yaw) rotation in radians

  * **dimension** â a 3-element list or np.ndarray representing the (length, width, height) of the cuboid



Returns:
    

A 3x8 np.ndarray containing the 3D coordinates of the cuboidâs corners.

fiftyone.utils.utils3d.pinhole_projector(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _cam_params : Dict_, _normalize =True_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Projects 3D detection points to 2D using the given camera intrinsics assuming a pinhole camera.

The following orientation is assumed- x axis points to the right in the image plane, y axis points down in the image plane and z axis points forward from the camera.

Parameters:
    

  * **points** â a 3xN np.ndarray containing the 3D coordinates of the points

  * **cam_params** â a dict containing the key âintrinsicsâ that maps to a 3x3 or 4x4 np.ndarray representing the camera intrinsics matrix

  * **normalize** (_True_) â whether to normalize the projected points by their z-coordinate



Returns:
    

A 2xN np.ndarray containing the projected 2D coordinates of the points. If normalize is True, the points are normalized by their z-coordinate.

fiftyone.utils.utils3d.point_in_front_of_camera(_corners_img : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _corners_3d : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _imsize : Tuple[int, int]_, _distance_threshold : float = 0.1_, _safety_threshold : float = 0.1_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Checks if the input corners are visible in the image and in front of the camera.

Parameters:
    

  * **corners_img** â a 2x8 np.ndarray containing the projected 2D coordinates of a cuboidâs corners

  * **corners_3d** â a 3x8 np.ndarray containing the 3D coordinates of the cuboidâs corners

  * **imsize** â a tuple (width, height) of the image dimensions

  * **distance_threshold** (_0.1_) â a float representing the minimum distance in meters for a corner to be considered in front of the camera

  * **safety_threshold** (_0.1_) â a float representing the minimum safety distance in meters for a corner to be considered safe



Returns:
    

True if all corners are visible in the image and all corners are in front of the camera, False otherwise.

class fiftyone.utils.utils3d.OrthographicProjectionMetadata(_* args_, _** kwargs_)#
    

Bases: [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument"), `_HasMedia`

Class for storing metadata about orthographic projections.

Parameters:
    

  * **filepath** (_None_) â the path to the orthographic projection on disk

  * **min_bound** (_None_) â the `[xmin, ymin]` of the image in the projection plane

  * **max_bound** (_None_) â the `[xmax, ymax]` of the image in the projection plane

  * **normal** (_None_) â the normal vector of the plane onto which the projection was performed. If not specified, `[0, 0, 1]` is assumed

  * **width** â the width of the image, in pixels

  * **height** â the height of the image, in pixels




**Attributes:**

`filepath` | A unicode string field.  
---|---  
`min_bound` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`max_bound` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`normal` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`width` | A 32 bit integer field.  
`height` | A 32 bit integer field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
filepath#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




min_bound#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




max_bound#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




normal#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




width#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




height#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

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

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

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

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

fiftyone.utils.utils3d.get_scene_asset_paths(_scene_paths_ , _abs_paths =False_, _skip_failures =True_, _progress =None_)#
    

Extracts all asset paths for the specified 3D scenes.

Parameters:
    

  * **scene_paths** â an iterable of `.fo3d` paths

  * **abs_paths** (_False_) â whether to return absolute paths

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if metadata cannot be computed for a file

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a dict mapping scene paths to lists of asset paths

fiftyone.utils.utils3d.compute_orthographic_projection_images(_samples_ , _size_ , _output_dir_ , _rel_dir =None_, _in_group_slice =None_, _out_group_slice =None_, _metadata_field ='orthographic_projection_metadata'_, _shading_mode =None_, _colormap =None_, _subsampling_rate =None_, _projection_normal =None_, _bounds =None_, _padding =None_, _overwrite =False_, _skip_failures =False_, _progress =None_)#
    

Computes orthographic projection images for the point clouds in the given collection.

This operation will populate `OrthographicProjectionMetadata` instances for each projection in the `metadata_field` of each sample.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.utils.utils3d as fou3d
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-groups")
    view = dataset.select_group_slices("pcd")
    
    fou3d.compute_orthographic_projection_images(view, (-1, 512), "/tmp/proj")
    
    session = fo.launch_app(view)
    

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **size** â the desired `(width, height)` for the generated maps. Either dimension can be None or negative, in which case the appropriate aspect-preserving value is used

  * **output_dir** â an output directory in which to store the images/maps

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths

  * **in_group_slice** (_None_) â the name of the group slice containing the point cloud data. Only applicable if `samples` is a grouped collection. If `samples` is a grouped collection and this parameter is not provided, the first point cloud slice will be used

  * **out_group_slice** (_None_) â the name of a group slice to which to add new samples containing the feature images/maps. Only applicable if `samples` is a grouped collection

  * **metadata_field** (_"orthographic_projection_metadata"_) â the name of the field in which to store `OrthographicProjectionMetadata` instances for each projection

  * **shading_mode** (_None_) â an optional shading algorithm for the points. Supported values are `("intensity", "rgb", or "height")`. The `"intensity"` and `"rgb"` options are only valid if the PCDâs header contains the `"rgb"` flag. By default, all points are shaded white

  * **colormap** (_None_) â 

an optional colormap to use when shading gradients, formatted as either:

    * a dict mapping values in `[0, 1]` to `(R, G, B)` tuples in `[0, 255]`

    * a list of `(R, G, B)` tuples in `[0, 255]` that cover `[0, 1]` linearly spaced

  * **subsampling_rate** (_None_) â an optional unsigned int that, if provided, defines a uniform subsampling rate. The selected point indices are [0, k, 2k, â¦], where `k = subsampling_rate`

  * **projection_normal** (_None_) â the normal vector of the plane onto which to perform the projection. By default, `(0, 0, 1)` is used

  * **bounds** (_None_) â an optional `((xmin, ymin, zmin), (xmax, ymax, zmax))` tuple defining the field of view in the projected plane for which to generate each map. Either element of the tuple or any/all of its values can be None, in which case a tight crop of the point cloud along the missing dimension(s) are used

  * **padding** (_None_) â a relative padding(s) in `[0, 1]]` to apply to the field of view bounds prior to projection. Can either be a single value to apply in all directions or a `[padx, pady, padz]`. For example, pass `padding=0.25` with no `bounds` to project onto a tight crop of each point cloud with 25% padding around it

  * **overwrite** (_False_) â whether to overwrite existing images

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if a projection fails

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.utils3d.compute_orthographic_projection_image(_filepath_ , _size_ , _shading_mode =None_, _colormap =None_, _subsampling_rate =None_, _projection_normal =None_, _bounds =None_, _padding =None_)#
    

Generates an orthographic projection image for the given PCD file onto the specified plane (default xy plane).

The returned image is a three-channel array encoding the intensity, height, and density of the point cloud.

Parameters:
    

  * **filepath** â the path to the `.pcd` file

  * **size** â the desired `(width, height)` for the generated maps. Either dimension can be None or negative, in which case the appropriate aspect-preserving value is used

  * **shading_mode** (_None_) â an optional shading algorithm for the points. Supported values are `("intensity", "rgb", or "height")`. The `"intensity"` and `"rgb"` options are only valid if the PCDâs header contains the `"rgb"` flag. By default, all points are shaded white

  * **colormap** (_None_) â 

an optional colormap to use when shading gradients, formatted as either:

    * a dict mapping values in `[0, 1]` to `(R, G, B)` tuples in `[0, 255]`

    * a list of `(R, G, B)` tuples in `[0, 255]` that cover `[0, 1]` linearly spaced

  * **subsampling_rate** (_None_) â an unsigned `int` that, if defined, defines a uniform subsampling rate. The selected point indices are [0, k, 2k, â¦], where `k = subsampling_rate`

  * **projection_normal** (_None_) â the normal vector of the plane onto which to perform the projection. By default, `(0, 0, 1)` is used

  * **bounds** (_None_) â an optional `((xmin, ymin, zmin), (xmax, ymax, zmax))` tuple defining the field of view for which to generate each map in the projected plane. Either element of the tuple or any/all of its values can be None, in which case a tight crop of the point cloud along the missing dimension(s) are used

  * **padding** (_None_) â a relative padding(s) in `[0, 1]]` to apply to the field of view bounds prior to projection. Can either be a single value to apply in all directions or a `[padx, pady, padz]`. For example, pass `padding=0.25` with no `bounds` to project onto a tight crop of the point cloud with 25% padding around it



Returns:
    

a tuple of

  * the orthographic projection image

  * an `OrthographicProjectionMetadata` instance




fiftyone.utils.utils3d.pcd_to_3d(_dataset_ , _slices =None_, _output_dir =None_, _assets_dir =None_, _rel_dir =None_, _abs_paths =False_, _progress =None_)#
    

Converts the point cloud samples in the given dataset to 3D samples.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") containing point clouds

  * **slices** (_None_) â 

point cloud slice(s) to convert. Only applicable when the dataset is grouped, in which case you can provide:

    * a slice or iterable of point cloud slices to convert in-place

    * a dict mapping point cloud slices to desired 3D slice names

    * None (default): all point cloud slices are converted in-place

  * **output_dir** (_None_) â an optional output directory for the `.fo3d` files

  * **assets_dir** (_None_) â an optional directory to copy the `.pcd` files into. Can be either an absolute directory, a subdirectory of `output_dir`, or None if you do not wish to copy point clouds

  * **rel_dir** (_None_) â an optional relative directory to strip from each point cloud path to generate a unique identifier for each scene, which is joined with `output_dir` to generate an output path for each `.fo3d` file. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the point cloud files in the exported `.fo3d` files

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
