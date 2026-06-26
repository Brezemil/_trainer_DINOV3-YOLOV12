---
source_url: https://docs.voxel51.com/api/fiftyone.core.camera.html
---

# fiftyone.core.camera#

Camera calibration data model for multi-sensor geometry workflows.

This module provides first-class data models for camera intrinsics and static transforms (poses), enabling 3D-to-2D projection, 2D-to-3D unprojection, and multi-sensor fusion workflows.

Key classes:

  * `CameraIntrinsics`: Base class for camera intrinsic parameters

  * `PinholeCameraIntrinsics`: Pinhole model (no distortion)

  * `OpenCVCameraIntrinsics`: OpenCV model with radial/tangential distortion

  * `OpenCVFisheyeCameraIntrinsics`: Fisheye model with equidistant projection

  * `StaticTransform`: Rigid 6-DOF transformation (rotation + translation)

  * `CameraProjector`: Utility for projecting/unprojecting points




For low-level transformation utilities (quaternion math, coordinate system conversions, matrix operations), see [`fiftyone.utils.transforms`](api__fiftyone.utils.transforms.md#module-fiftyone.utils.transforms "fiftyone.utils.transforms").

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Data:**

`CAMERA_CONVENTION_OPENCV` | Supported 3D camera axis conventions  
---|---  
`DEFAULT_TRANSFORM_TARGET_FRAME` | Default target frame for static transforms  
  
**Classes:**

`ProjectionModel`() | Abstract base class for camera projection models.  
---|---  
`OpenCVProjectionModel`() | Standard OpenCV camera model with radial and tangential distortion.  
`FisheyeProjectionModel`() | OpenCV fisheye camera model with equidistant projection.  
`CameraIntrinsics`(*args,Â **kwargs) | Base class for camera intrinsics.  
`PinholeCameraIntrinsics`(*args,Â **kwargs) | Pinhole camera model with no distortion.  
`OpenCVCameraIntrinsics`(*args,Â **kwargs) | OpenCV Brown-Conrady camera model with radial and tangential distortion.  
`OpenCVFisheyeCameraIntrinsics`(*args,Â **kwargs) | OpenCV fisheye camera model with equidistant projection.  
`StaticTransform`(*args,Â **kwargs) | Represents a rigid 3D transformation (6-DOF pose).  
`CameraIntrinsicsRef`(*args,Â **kwargs) | Reference to dataset-level camera intrinsics.  
`StaticTransformRef`(*args,Â **kwargs) | Reference to dataset-level static transform.  
`CameraProjector`(intrinsics[,Â ...]) | Utility class for projecting points between 3D and 2D.  
  
fiftyone.core.camera.CAMERA_CONVENTION_OPENCV = 'opencv'#
    

Supported 3D camera axis conventions

fiftyone.core.camera.DEFAULT_TRANSFORM_TARGET_FRAME = 'world'#
    

Default target frame for static transforms

class fiftyone.core.camera.ProjectionModel#
    

Bases: `ABC`

Abstract base class for camera projection models.

Encapsulates projection and undistortion operations for different camera models.

**Methods:**

`project`(points,Â K,Â distortion) | Project 3D points to 2D image coordinates.  
---|---  
`undistort`(points,Â K,Â distortion) | Undistort 2D image points, returning normalized coordinates.  
`undistort_image`(image,Â K,Â distortion[,Â ...]) | Undistort an image using this projection model.  
  
abstractmethod project(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Project 3D points to 2D image coordinates.

Parameters:
    

  * **points** â (N, 3) array of 3D points in camera frame

  * **K** â (3, 3) intrinsic matrix

  * **distortion** â distortion coefficients, or None



Returns:
    

(N, 2) array of 2D pixel coordinates

abstractmethod undistort(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort 2D image points, returning normalized coordinates.

Parameters:
    

  * **points** â (N, 2) array of 2D pixel coordinates

  * **K** â (3, 3) intrinsic matrix

  * **distortion** â distortion coefficients, or None



Returns:
    

(N, 2) array of normalized coordinates (z=1 plane in camera frame)

abstractmethod undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this projection model.

class fiftyone.core.camera.OpenCVProjectionModel#
    

Bases: `ProjectionModel`

Standard OpenCV camera model with radial and tangential distortion.

**Methods:**

`project`(points,Â K,Â distortion) | Project points using OpenCV's standard camera model.  
---|---  
`undistort`(points,Â K,Â distortion) | Undistort points using OpenCV's standard camera model.  
`undistort_image`(image,Â K,Â distortion[,Â ...]) | Undistort an image using this projection model.  
  
project(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Project points using OpenCVâs standard camera model.

undistort(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort points using OpenCVâs standard camera model.

Returns normalized (x, y) coordinates (z=1 plane in camera frame).

undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this projection model.

class fiftyone.core.camera.FisheyeProjectionModel#
    

Bases: `ProjectionModel`

OpenCV fisheye camera model with equidistant projection.

**Methods:**

`project`(points,Â K,Â distortion) | Project points using OpenCV's fisheye camera model.  
---|---  
`undistort`(points,Â K,Â distortion) | Undistort points using OpenCV's fisheye camera model.  
`undistort_image`(image,Â K,Â distortion[,Â ...]) | Undistort an image using this projection model.  
  
project(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Project points using OpenCVâs fisheye camera model.

undistort(_points : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort points using OpenCVâs fisheye camera model.

Returns normalized (x, y) coordinates (z=1 plane in camera frame).

undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _K : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _distortion : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this projection model.

class fiftyone.core.camera.CameraIntrinsics(_* args_, _** kwargs_)#
    

Bases: [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument")

Base class for camera intrinsics.

All camera intrinsics models share the following parameters:

Parameters:
    

  * **fx** â focal length in pixels (x-axis)

  * **fy** â focal length in pixels (y-axis)

  * **cx** â principal point x-coordinate in pixels

  * **cy** â principal point y-coordinate in pixels

  * **skew** (_0.0_) â skew coefficient (typically 0 for modern cameras)




intrinsic_matrix#
    

the 3x3 intrinsic matrix K

Example:
    
    
    import fiftyone as fo
    
    intrinsics = fo.PinholeCameraIntrinsics(
        fx=1000.0,
        fy=1000.0,
        cx=960.0,
        cy=540.0,
    )
    
    # Access the 3x3 intrinsic matrix
    K = intrinsics.intrinsic_matrix
    

**Attributes:**

`fx` | A floating point number field.  
---|---  
`fy` | A floating point number field.  
`cx` | A floating point number field.  
`cy` | A floating point number field.  
`skew` | A floating point number field.  
`intrinsic_matrix` | Returns the 3x3 intrinsic matrix K.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`from_matrix`(matrix,Â **kwargs) | Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.  
---|---  
`get_distortion_coeffs`() | Returns the distortion coefficients for this camera model.  
`get_projection_model`() | Returns the ProjectionModel instance for this camera model.  
`camera_matrix_3x4`([transform]) | Returns the 3x4 camera projection matrix P = K @ [R|t].  
`undistort_image`(image[,Â alpha,Â new_size]) | Undistort an image using this camera's intrinsics and distortion.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
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
  
fx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




fy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




cx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




cy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




skew#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property intrinsic_matrix: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x3 intrinsic matrix K.

The matrix has the form:
    
    
    [[fx,  s, cx],
     [ 0, fy, cy],
     [ 0,  0,  1]]
    

Returns:
    

a (3, 3) numpy array

classmethod from_matrix(_matrix : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _** kwargs_) → CameraIntrinsics#
    

Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.

Parameters:
    

  * **matrix** â a (3, 3) intrinsic matrix K

  * ****kwargs** â additional fields to set on the instance



Returns:
    

a `CameraIntrinsics` instance

get_distortion_coeffs() → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None#
    

Returns the distortion coefficients for this camera model.

Returns:
    

a numpy array of distortion coefficients, or None if no distortion

get_projection_model() → ProjectionModel#
    

Returns the ProjectionModel instance for this camera model.

Returns:
    

a `ProjectionModel` instance

camera_matrix_3x4(_transform : StaticTransform | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x4 camera projection matrix P = K @ [R|t].

Note: This matrix is only valid when distortion is zero or has been pre-corrected in the image.

Parameters:
    

**transform** â optional transform defining the world-to-camera transformation (i.e., source_frame=world, target_frame=camera). If your transform is camera-to-world, call `transform.inverse()` first.

Returns:
    

a (3, 4) numpy array

undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this cameraâs intrinsics and distortion.

Removes lens distortion from an image, producing a rectified image that follows the pinhole camera model.

Parameters:
    

  * **image** â input distorted image as a numpy array with shape (H, W) for grayscale or (H, W, C) for color images

  * **alpha** â 

free scaling parameter between 0 and 1:

    * 0: returns undistorted image with all pixels valid (cropped to remove black borders)

    * 1: retains all source image pixels (may have black borders where no source data exists)

Intermediate values blend between the two extremes

  * **new_size** â optional output image size as (width, height). If None, uses the input image size



Returns:
    

undistorted image as a numpy array with the same dtype as input

Example:
    
    
    import fiftyone as fo
    import cv2
    
    intrinsics = fo.OpenCVCameraIntrinsics(
        fx=1000.0, fy=1000.0, cx=960.0, cy=540.0,
        k1=-0.1, k2=0.05,
    )
    
    distorted = cv2.imread("distorted.jpg")
    rectified = intrinsics.undistort_image(distorted)
    
    # Keep all pixels (with black borders)
    rectified_full = intrinsics.undistort_image(distorted, alpha=1.0)
    

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

class fiftyone.core.camera.PinholeCameraIntrinsics(_* args_, _** kwargs_)#
    

Bases: `CameraIntrinsics`

Pinhole camera model with no distortion.

Parameters:
    

  * **fx** â focal length in pixels (x-axis)

  * **fy** â focal length in pixels (y-axis)

  * **cx** â principal point x-coordinate in pixels

  * **cy** â principal point y-coordinate in pixels

  * **skew** (_0.0_) â skew coefficient (typically 0 for modern cameras)




Example:
    
    
    import fiftyone as fo
    
    intrinsics = fo.PinholeCameraIntrinsics(
        fx=1000.0,
        fy=1000.0,
        cx=960.0,
        cy=540.0,
    )
    

**Attributes:**

`STRICT` |   
---|---  
`cx` | A floating point number field.  
`cy` | A floating point number field.  
`field_names` | An ordered tuple of the public fields of this document.  
`fx` | A floating point number field.  
`fy` | A floating point number field.  
`intrinsic_matrix` | Returns the 3x3 intrinsic matrix K.  
`skew` | A floating point number field.  
  
**Methods:**

`camera_matrix_3x4`([transform]) | Returns the 3x4 camera projection matrix P = K @ [R|t].  
---|---  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`from_matrix`(matrix,Â **kwargs) | Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.  
`get_distortion_coeffs`() | Returns the distortion coefficients for this camera model.  
`get_field`(field_name) | Gets the field of the document.  
`get_projection_model`() | Returns the ProjectionModel instance for this camera model.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`undistort_image`(image[,Â alpha,Â new_size]) | Undistort an image using this camera's intrinsics and distortion.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
STRICT = False#
    

camera_matrix_3x4(_transform : StaticTransform | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x4 camera projection matrix P = K @ [R|t].

Note: This matrix is only valid when distortion is zero or has been pre-corrected in the image.

Parameters:
    

**transform** â optional transform defining the world-to-camera transformation (i.e., source_frame=world, target_frame=camera). If your transform is camera-to-world, call `transform.inverse()` first.

Returns:
    

a (3, 4) numpy array

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

cx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




cy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

classmethod from_matrix(_matrix : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _** kwargs_) → CameraIntrinsics#
    

Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.

Parameters:
    

  * **matrix** â a (3, 3) intrinsic matrix K

  * ****kwargs** â additional fields to set on the instance



Returns:
    

a `CameraIntrinsics` instance

fx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




fy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




get_distortion_coeffs() → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") | None#
    

Returns the distortion coefficients for this camera model.

Returns:
    

a numpy array of distortion coefficients, or None if no distortion

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_projection_model() → ProjectionModel#
    

Returns the ProjectionModel instance for this camera model.

Returns:
    

a `ProjectionModel` instance

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property intrinsic_matrix: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x3 intrinsic matrix K.

The matrix has the form:
    
    
    [[fx,  s, cx],
     [ 0, fy, cy],
     [ 0,  0,  1]]
    

Returns:
    

a (3, 3) numpy array

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

skew#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this cameraâs intrinsics and distortion.

Removes lens distortion from an image, producing a rectified image that follows the pinhole camera model.

Parameters:
    

  * **image** â input distorted image as a numpy array with shape (H, W) for grayscale or (H, W, C) for color images

  * **alpha** â 

free scaling parameter between 0 and 1:

    * 0: returns undistorted image with all pixels valid (cropped to remove black borders)

    * 1: retains all source image pixels (may have black borders where no source data exists)

Intermediate values blend between the two extremes

  * **new_size** â optional output image size as (width, height). If None, uses the input image size



Returns:
    

undistorted image as a numpy array with the same dtype as input

Example:
    
    
    import fiftyone as fo
    import cv2
    
    intrinsics = fo.OpenCVCameraIntrinsics(
        fx=1000.0, fy=1000.0, cx=960.0, cy=540.0,
        k1=-0.1, k2=0.05,
    )
    
    distorted = cv2.imread("distorted.jpg")
    rectified = intrinsics.undistort_image(distorted)
    
    # Keep all pixels (with black borders)
    rectified_full = intrinsics.undistort_image(distorted, alpha=1.0)
    

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.camera.OpenCVCameraIntrinsics(_* args_, _** kwargs_)#
    

Bases: `CameraIntrinsics`

OpenCV Brown-Conrady camera model with radial and tangential distortion.

Distortion coefficients follow the OpenCV ordering: (k1, k2, p1, p2, k3, k4, k5, k6).

The radial distortion model is:
    
    
    x_distorted = x * (1 + k1*r^2 + k2*r^4 + k3*r^6) /
                      (1 + k4*r^2 + k5*r^4 + k6*r^6)
    

The tangential distortion model is:
    
    
    x_distorted += 2*p1*x*y + p2*(r^2 + 2*x^2)
    y_distorted += p1*(r^2 + 2*y^2) + 2*p2*x*y
    

Parameters:
    

  * **fx** â focal length in pixels (x-axis)

  * **fy** â focal length in pixels (y-axis)

  * **cx** â principal point x-coordinate in pixels

  * **cy** â principal point y-coordinate in pixels

  * **skew** (_0.0_) â skew coefficient

  * **k1** (_0.0_) â radial distortion coefficient

  * **k2** (_0.0_) â radial distortion coefficient

  * **p1** (_0.0_) â tangential distortion coefficient

  * **p2** (_0.0_) â tangential distortion coefficient

  * **k3** (_0.0_) â radial distortion coefficient

  * **k4** (_0.0_) â radial distortion coefficient (rational model)

  * **k5** (_0.0_) â radial distortion coefficient (rational model)

  * **k6** (_0.0_) â radial distortion coefficient (rational model)




Example:
    
    
    import fiftyone as fo
    
    intrinsics = fo.OpenCVCameraIntrinsics(
        fx=1000.0,
        fy=1000.0,
        cx=960.0,
        cy=540.0,
        k1=-0.1,
        k2=0.05,
        p1=0.001,
        p2=-0.001,
    )
    

**Attributes:**

`k1` | A floating point number field.  
---|---  
`k2` | A floating point number field.  
`p1` | A floating point number field.  
`p2` | A floating point number field.  
`k3` | A floating point number field.  
`k4` | A floating point number field.  
`k5` | A floating point number field.  
`k6` | A floating point number field.  
`STRICT` |   
`cx` | A floating point number field.  
`cy` | A floating point number field.  
`field_names` | An ordered tuple of the public fields of this document.  
`fx` | A floating point number field.  
`fy` | A floating point number field.  
`intrinsic_matrix` | Returns the 3x3 intrinsic matrix K.  
`skew` | A floating point number field.  
  
**Methods:**

`get_distortion_coeffs`() | Returns the OpenCV distortion coefficients.  
---|---  
`camera_matrix_3x4`([transform]) | Returns the 3x4 camera projection matrix P = K @ [R|t].  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`from_matrix`(matrix,Â **kwargs) | Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.  
`get_field`(field_name) | Gets the field of the document.  
`get_projection_model`() | Returns the ProjectionModel instance for this camera model.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`undistort_image`(image[,Â alpha,Â new_size]) | Undistort an image using this camera's intrinsics and distortion.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
k1#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k2#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




p1#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




p2#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k3#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k4#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k5#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k6#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




get_distortion_coeffs() → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the OpenCV distortion coefficients.

Returns:
    

a (8,) numpy array with coefficients (k1, k2, p1, p2, k3, k4, k5, k6)

STRICT = False#
    

camera_matrix_3x4(_transform : StaticTransform | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x4 camera projection matrix P = K @ [R|t].

Note: This matrix is only valid when distortion is zero or has been pre-corrected in the image.

Parameters:
    

**transform** â optional transform defining the world-to-camera transformation (i.e., source_frame=world, target_frame=camera). If your transform is camera-to-world, call `transform.inverse()` first.

Returns:
    

a (3, 4) numpy array

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

cx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




cy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

classmethod from_matrix(_matrix : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _** kwargs_) → CameraIntrinsics#
    

Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.

Parameters:
    

  * **matrix** â a (3, 3) intrinsic matrix K

  * ****kwargs** â additional fields to set on the instance



Returns:
    

a `CameraIntrinsics` instance

fx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




fy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_projection_model() → ProjectionModel#
    

Returns the ProjectionModel instance for this camera model.

Returns:
    

a `ProjectionModel` instance

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property intrinsic_matrix: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x3 intrinsic matrix K.

The matrix has the form:
    
    
    [[fx,  s, cx],
     [ 0, fy, cy],
     [ 0,  0,  1]]
    

Returns:
    

a (3, 3) numpy array

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

skew#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this cameraâs intrinsics and distortion.

Removes lens distortion from an image, producing a rectified image that follows the pinhole camera model.

Parameters:
    

  * **image** â input distorted image as a numpy array with shape (H, W) for grayscale or (H, W, C) for color images

  * **alpha** â 

free scaling parameter between 0 and 1:

    * 0: returns undistorted image with all pixels valid (cropped to remove black borders)

    * 1: retains all source image pixels (may have black borders where no source data exists)

Intermediate values blend between the two extremes

  * **new_size** â optional output image size as (width, height). If None, uses the input image size



Returns:
    

undistorted image as a numpy array with the same dtype as input

Example:
    
    
    import fiftyone as fo
    import cv2
    
    intrinsics = fo.OpenCVCameraIntrinsics(
        fx=1000.0, fy=1000.0, cx=960.0, cy=540.0,
        k1=-0.1, k2=0.05,
    )
    
    distorted = cv2.imread("distorted.jpg")
    rectified = intrinsics.undistort_image(distorted)
    
    # Keep all pixels (with black borders)
    rectified_full = intrinsics.undistort_image(distorted, alpha=1.0)
    

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.camera.OpenCVFisheyeCameraIntrinsics(_* args_, _** kwargs_)#
    

Bases: `CameraIntrinsics`

OpenCV fisheye camera model with equidistant projection.

Uses 4 distortion coefficients (k1, k2, k3, k4) for the fisheye model.

Parameters:
    

  * **fx** â focal length in pixels (x-axis)

  * **fy** â focal length in pixels (y-axis)

  * **cx** â principal point x-coordinate in pixels

  * **cy** â principal point y-coordinate in pixels

  * **skew** (_0.0_) â skew coefficient

  * **k1** (_0.0_) â fisheye distortion coefficient

  * **k2** (_0.0_) â fisheye distortion coefficient

  * **k3** (_0.0_) â fisheye distortion coefficient

  * **k4** (_0.0_) â fisheye distortion coefficient




Example:
    
    
    import fiftyone as fo
    
    intrinsics = fo.OpenCVFisheyeCameraIntrinsics(
        fx=500.0,
        fy=500.0,
        cx=640.0,
        cy=480.0,
        k1=0.1,
        k2=-0.05,
    )
    

**Attributes:**

`k1` | A floating point number field.  
---|---  
`k2` | A floating point number field.  
`k3` | A floating point number field.  
`k4` | A floating point number field.  
`STRICT` |   
`cx` | A floating point number field.  
`cy` | A floating point number field.  
`field_names` | An ordered tuple of the public fields of this document.  
`fx` | A floating point number field.  
`fy` | A floating point number field.  
`intrinsic_matrix` | Returns the 3x3 intrinsic matrix K.  
`skew` | A floating point number field.  
  
**Methods:**

`get_distortion_coeffs`() | Returns the fisheye distortion coefficients.  
---|---  
`get_projection_model`() | Returns the ProjectionModel instance for fisheye distortion.  
`camera_matrix_3x4`([transform]) | Returns the 3x4 camera projection matrix P = K @ [R|t].  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`from_matrix`(matrix,Â **kwargs) | Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`undistort_image`(image[,Â alpha,Â new_size]) | Undistort an image using this camera's intrinsics and distortion.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
k1#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k2#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k3#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




k4#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




get_distortion_coeffs() → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the fisheye distortion coefficients.

Returns:
    

a (4,) numpy array with coefficients (k1, k2, k3, k4)

get_projection_model() → ProjectionModel#
    

Returns the ProjectionModel instance for fisheye distortion.

Returns:
    

a `FisheyeProjectionModel` instance

STRICT = False#
    

camera_matrix_3x4(_transform : StaticTransform | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x4 camera projection matrix P = K @ [R|t].

Note: This matrix is only valid when distortion is zero or has been pre-corrected in the image.

Parameters:
    

**transform** â optional transform defining the world-to-camera transformation (i.e., source_frame=world, target_frame=camera). If your transform is camera-to-world, call `transform.inverse()` first.

Returns:
    

a (3, 4) numpy array

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

cx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




cy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

classmethod from_matrix(_matrix : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _** kwargs_) → CameraIntrinsics#
    

Creates a CameraIntrinsics instance from a 3x3 intrinsic matrix.

Parameters:
    

  * **matrix** â a (3, 3) intrinsic matrix K

  * ****kwargs** â additional fields to set on the instance



Returns:
    

a `CameraIntrinsics` instance

fx#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




fy#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

property intrinsic_matrix: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x3 intrinsic matrix K.

The matrix has the form:
    
    
    [[fx,  s, cx],
     [ 0, fy, cy],
     [ 0,  0,  1]]
    

Returns:
    

a (3, 3) numpy array

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

skew#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

undistort_image(_image : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _alpha : float = 0.0_, _new_size : Tuple[int, int] | None = None_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Undistort an image using this cameraâs intrinsics and distortion.

Removes lens distortion from an image, producing a rectified image that follows the pinhole camera model.

Parameters:
    

  * **image** â input distorted image as a numpy array with shape (H, W) for grayscale or (H, W, C) for color images

  * **alpha** â 

free scaling parameter between 0 and 1:

    * 0: returns undistorted image with all pixels valid (cropped to remove black borders)

    * 1: retains all source image pixels (may have black borders where no source data exists)

Intermediate values blend between the two extremes

  * **new_size** â optional output image size as (width, height). If None, uses the input image size



Returns:
    

undistorted image as a numpy array with the same dtype as input

Example:
    
    
    import fiftyone as fo
    import cv2
    
    intrinsics = fo.OpenCVCameraIntrinsics(
        fx=1000.0, fy=1000.0, cx=960.0, cy=540.0,
        k1=-0.1, k2=0.05,
    )
    
    distorted = cv2.imread("distorted.jpg")
    rectified = intrinsics.undistort_image(distorted)
    
    # Keep all pixels (with black borders)
    rectified_full = intrinsics.undistort_image(distorted, alpha=1.0)
    

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

class fiftyone.core.camera.StaticTransform(_* args_, _** kwargs_)#
    

Bases: [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument")

Represents a rigid 3D transformation (6-DOF pose).

Stored as translation + quaternion for efficiency. Defines transformation from `source_frame` to `target_frame`:
    
    
    X_target = R @ X_source + t
    

The quaternion uses scalar-last convention [qx, qy, qz, qw], matching scipy and ROS conventions.

Parameters:
    

  * **source_frame** â name of source coordinate frame (e.g., âcamera_frontâ). This is a required argument.

  * **translation** (_[__0_ _,__0_ _,__0_ _]_) â 3-element list [tx, ty, tz] (position in target frame)

  * **quaternion** (_[__0_ _,__0_ _,__0_ _,__1_ _]_) â unit quaternion [qx, qy, qz, qw] (scalar-last convention, defaults to identity rotation)

  * **target_frame** (_None_) â name of target coordinate frame (e.g., âegoâ, âworldâ)

  * **timestamp** (_None_) â optional timestamp in nanoseconds for interpolation

  * **covariance** (_None_) â optional 6-element diagonal pose uncertainty [Ïx, Ïy, Ïz, Ïroll, Ïpitch, Ïyaw] where translations are in metric and rotations are in radians




rotation_matrix#
    

the 3x3 rotation matrix R

transform_matrix#
    

the 4x4 homogeneous transformation matrix

Example:
    
    
    import fiftyone as fo
    
    # Camera to ego transformation
    transform = fo.StaticTransform(
        translation=[1.5, 0.0, 1.2],
        # identity rotation
        quaternion=[0.0, 0.0, 0.0, 1.0],
        source_frame="camera_front",
        target_frame="ego",
    )
    
    # Access the 4x4 transformation matrix
    T = transform.transform_matrix
    

**Attributes:**

`translation` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`quaternion` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`source_frame` | A unicode string field.  
`target_frame` | A unicode string field.  
`timestamp` | A 32 bit integer field.  
`covariance` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`rotation_matrix` | Returns the 3x3 rotation matrix R.  
`transform_matrix` | Returns the 4x4 homogeneous transformation matrix.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`validate`([clean]) | Validates the transform data.  
---|---  
`from_matrix`(matrix[,Â source_frame,Â target_frame]) | Creates a StaticTransform instance from a 3x4 or 4x4 matrix.  
`inverse`() | Returns the inverse transformation.  
`compose`(other) | Composes this transform with another.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
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
  
**Classes:**

`my_metaclass` |   
---|---  
  
translation#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




quaternion#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




source_frame#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




target_frame#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




timestamp#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




covariance#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




validate(_clean =True_)#
    

Validates the transform data.

This method is called by mongoengine during save/validation.

property rotation_matrix: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 3x3 rotation matrix R.

Returns:
    

a (3, 3) numpy array

property transform_matrix: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Returns the 4x4 homogeneous transformation matrix.

The matrix has the form:
    
    
    [[R, t],
     [0, 1]]
    

where R is the 3x3 rotation and t is the 3x1 translation.

Returns:
    

a (4, 4) numpy array

classmethod from_matrix(_matrix : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _source_frame : str | None = None_, _target_frame : str | None = None_, _** kwargs_) → StaticTransform#
    

Creates a StaticTransform instance from a 3x4 or 4x4 matrix.

Parameters:
    

  * **matrix** â a (3, 4) or (4, 4) transformation matrix [R|t]

  * **source_frame** â name of source coordinate frame

  * **target_frame** â name of target coordinate frame

  * ****kwargs** â additional fields to set on the instance



Returns:
    

a `StaticTransform` instance

inverse() → StaticTransform#
    

Returns the inverse transformation.

If this transform is source_frame -> target_frame, the inverse is target_frame -> source_frame.

Returns:
    

a `StaticTransform` representing the inverse transform

compose(_other : StaticTransform_) → StaticTransform#
    

Composes this transform with another.

If self is A->B and other is B->C, the result is A->C.

Mathematically:
    

X_C = T_BC @ X_B = T_BC @ (T_AB @ X_A) So T_AC = T_BC @ T_AB (other @ self)

Parameters:
    

**other** â another `StaticTransform` to compose with. The source_frame of `other` should match target_frame of `self` for the frames to chain correctly.

Returns:
    

a `StaticTransform` representing the composed transform

Raises:
    

**ValueError** â if the frames donât chain (self.target_frame != other.source_frame when both are specified)

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

class fiftyone.core.camera.CameraIntrinsicsRef(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Reference to dataset-level camera intrinsics.

Use this to reference intrinsics stored at the dataset level rather than embedding the full intrinsics data in each sample.

Parameters:
    

**ref** â the sensor/camera name key in `dataset.camera_intrinsics`

Example:
    
    
    import fiftyone as fo
    
    # Reference dataset-level intrinsics (field name can be anything)
    sample["intrinsics"] = fo.CameraIntrinsicsRef(ref="camera_front")
    

**Attributes:**

`ref` | A unicode string field.  
---|---  
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
  
ref#
    

A unicode string field.

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

class fiftyone.core.camera.StaticTransformRef(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

Reference to dataset-level static transform.

Use this to reference transforms stored at the dataset level rather than embedding the full transform data in each sample.

Parameters:
    

**ref** â the key in `dataset.static_transforms`, either âsource_frame::target_frameâ or just âsource_frameâ (implies target is âworldâ)

Example:
    
    
    import fiftyone as fo
    
    # Reference dataset-level transform (field name can be anything)
    sample["transform"] = [
        fo.StaticTransformRef(ref="camera_front::ego"),
    ]
    

**Attributes:**

`ref` | A unicode string field.  
---|---  
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
  
ref#
    

A unicode string field.

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

class fiftyone.core.camera.CameraProjector(_intrinsics : CameraIntrinsics_, _camera_to_reference : StaticTransform | None = None_, _camera_convention : str = 'opencv'_)#
    

Bases: `object`

Utility class for projecting points between 3D and 2D.

Combines camera intrinsics and optional transforms to perform projection and unprojection operations.

Parameters:
    

  * **intrinsics** â a `CameraIntrinsics` instance

  * **camera_to_reference** (_None_) â 

optional `StaticTransform` defining the **camera-to-reference** transformation (i.e., the cameraâs pose in the reference frame). If provided, 3D points passed to `project()` are assumed to be in the reference frame (`camera_to_reference.target_frame`) and will be transformed to camera frame before projection.

The transform should have:

    * `source_frame`: the camera/sensor name (e.g., âcam_frontâ)

    * `target_frame`: the reference frame (e.g., âworldâ, âegoâ)

  * **camera_convention** (_"opencv"_) â 3D camera axis convention, either âopencvâ (z-forward, x-right, y-down) or âopenglâ (z-backward, x-right, y-up). Note: This only affects the 3D coordinate axes. Pixel coordinates always follow image-space convention with +x right, +y down, origin at top-left




Important

**Transform direction** : This class expects **camera-to-reference** transforms, NOT reference-to-camera. If you have a reference-to-camera transform (e.g., world-to-camera), invert it first:
    
    
    projector = fo.CameraProjector(intrinsics, world_to_cam.inverse())
    

Or use the `from_reference_to_camera()` constructor.

Example:
    
    
    import fiftyone as fo
    import numpy as np
    
    intrinsics = fo.PinholeCameraIntrinsics(
        fx=1000.0, fy=1000.0, cx=960.0, cy=540.0
    )
    
    # Project points already in camera frame
    projector = fo.CameraProjector(intrinsics)
    points_3d = np.array([[0, 0, 10], [1, 2, 10]])
    points_2d = projector.project(points_3d, in_camera_frame=True)
    
    # Project world points using camera-to-world transform
    cam_to_world = fo.StaticTransform(
        translation=[0.0, 0.0, 0.0],
        quaternion=[0.0, 0.0, 0.0, 1.0],
        source_frame="camera",
        target_frame="world",
    )
    projector = fo.CameraProjector(intrinsics, cam_to_world)
    world_points = np.array([[0, 0, 10]])
    pixels = projector.project(world_points, in_camera_frame=False)
    

**Methods:**

`from_reference_to_camera`(intrinsics,Â ...[,Â ...]) | Creates a CameraProjector from reference-to-camera transform.  
---|---  
`project`(points_3d[,Â in_camera_frame]) | Projects 3D points to 2D image coordinates.  
`unproject`(points_2d,Â depth[,Â in_camera_frame]) | Unprojects 2D image points to 3D given depth.  
  
classmethod from_reference_to_camera(_intrinsics : CameraIntrinsics_, _reference_to_camera : StaticTransform_, _camera_convention : str = 'opencv'_) → CameraProjector#
    

Creates a CameraProjector from reference-to-camera transform.

Use this constructor if your transform converts points FROM the reference frame TO the camera frame (e.g., world-to-camera). This is common when loading from some datasets or calibration tools.

This method automatically inverts the transform to the expected camera-to-reference format.

Parameters:
    

  * **intrinsics** â a `CameraIntrinsics` instance

  * **reference_to_camera** â a `StaticTransform` that transforms points from the reference frame to the camera frame

  * **camera_convention** â âopencvâ or âopenglâ



Returns:
    

a `CameraProjector` instance

Example:
    
    
    # If you have world-to-camera transform:
    world_to_cam = fo.StaticTransform(
        translation=[...],
        quaternion=[...],
        source_frame="world",
        target_frame="camera",
    )
    projector = fo.CameraProjector.from_reference_to_camera(
        intrinsics, world_to_cam
    )
    

project(_points_3d : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _in_camera_frame : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Projects 3D points to 2D image coordinates.

Parameters:
    

  * **points_3d** â (N, 3) array of 3D points

  * **in_camera_frame** â if True, points are already in camera frame; if False and camera_to_reference is provided, points are transformed from the reference frame to camera frame



Returns:
    

(N, 2) array of 2D pixel coordinates

unproject(_points_2d : [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _depth : float | [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")_, _in_camera_frame : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")#
    

Unprojects 2D image points to 3D given depth.

Note: For monocular cameras, depth must be provided from an external source (e.g., stereo, LiDAR, depth sensor, or depth estimation).

The depth is interpreted as z-depth in the camera coordinate frame (not Euclidean distance from camera center).

Parameters:
    

  * **points_2d** â (N, 2) array of 2D pixel coordinates

  * **depth** â scalar or (N,) array of z-depth values in camera frame

  * **in_camera_frame** â if True, returns points in camera frame; if False and camera_to_reference is provided, transforms to the reference frame



Returns:
    

(N, 3) array of 3D points

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
