---
source_url: https://docs.voxel51.com/api/fiftyone.utils.transforms.html
---

# fiftyone.utils.transforms#

Pure mathematical 3D transformation utilities.

This module provides stateless functions for 3D transformations including:

  * Quaternion operations (conversion, multiplication, inversion)

  * Transform matrix construction and decomposition

  * Coordinate system conversions (OpenCV, OpenGL, ROS, etc.)

  * Point transformation utilities




All functions use numpy arrays and follow consistent conventions:

  * Quaternions use [qx, qy, qz, qw] (scalar-last) format

  * Rotation matrices are 3x3 numpy arrays

  * Transform matrices are 4x4 homogeneous matrices

  * Points are Nx3 numpy arrays




For high-level camera and transform data models that persist to the database, see [`fiftyone.core.camera`](api__fiftyone.core.camera.md#module-fiftyone.core.camera "fiftyone.core.camera").

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Data:**

`AXIS_FLIP_OPENCV_TO_OPENGL` | 3x3 matrix to convert from OpenCV (RDF) to OpenGL (RUB) camera convention.  
---|---  
`AXIS_FLIP_OPENGL_TO_OPENCV` | 3x3 matrix to convert from OpenGL (RUB) to OpenCV (RDF) camera convention.  
  
**Functions:**

`quaternion_to_rotation_matrix`(q) | Convert a quaternion to a 3x3 rotation matrix.  
---|---  
`rotation_matrix_to_quaternion`(R) | Convert a 3x3 rotation matrix to a quaternion.  
`quaternion_multiply`(q1,Â q2) | Multiply two quaternions using Hamilton product.  
`quaternion_inverse`(q) | Compute the inverse of a unit quaternion.  
`quaternion_from_euler`(angles[,Â seq]) | Convert Euler angles to quaternion.  
`euler_from_quaternion`(q[,Â seq]) | Convert quaternion to Euler angles.  
`make_transform_matrix`(R,Â t) | Construct a 4x4 homogeneous transformation matrix from rotation and translation.  
`decompose_transform_matrix`(T) | Extract rotation and translation from a 4x4 transformation matrix.  
`invert_transform_matrix`(T) | Efficiently invert a rigid transformation matrix.  
`compose_transforms`(T1,Â T2) | Compose two transformation matrices.  
`axis_flip_matrix`(from_conv,Â to_conv) | Get the 3x3 rotation matrix to convert between coordinate conventions.  
`opencv_to_opengl_points`(pts) | Convert points from OpenCV to OpenGL camera convention.  
`opengl_to_opencv_points`(pts) | Convert points from OpenGL to OpenCV camera convention.  
`transform_points_by_convention`(pts,Â ...) | Transform points between coordinate conventions.  
`transform_points`(pts,Â T) | Apply a 4x4 transformation matrix to 3D points.  
`rotate_points`(pts,Â R) | Apply a 3x3 rotation matrix to 3D points.  
`translate_points`(pts,Â t) | Translate 3D points by a vector.  
  
fiftyone.utils.transforms.AXIS_FLIP_OPENCV_TO_OPENGL = array([[ 1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]])#
    

3x3 matrix to convert from OpenCV (RDF) to OpenGL (RUB) camera convention.

fiftyone.utils.transforms.AXIS_FLIP_OPENGL_TO_OPENCV = array([[ 1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]])#
    

3x3 matrix to convert from OpenGL (RUB) to OpenCV (RDF) camera convention.

fiftyone.utils.transforms.quaternion_to_rotation_matrix(_q_)#
    

Convert a quaternion to a 3x3 rotation matrix.

Parameters:
    

**q** â quaternion as [qx, qy, qz, qw] (scalar-last convention)

Returns:
    

a (3, 3) numpy array representing the rotation matrix

fiftyone.utils.transforms.rotation_matrix_to_quaternion(_R_)#
    

Convert a 3x3 rotation matrix to a quaternion.

Parameters:
    

**R** â a (3, 3) rotation matrix

Returns:
    

quaternion as [qx, qy, qz, qw] (scalar-last convention)

fiftyone.utils.transforms.quaternion_multiply(_q1_ , _q2_)#
    

Multiply two quaternions using Hamilton product.

The result represents the composition of rotations: first q1, then q2.

Parameters:
    

  * **q1** â first quaternion as [qx, qy, qz, qw]

  * **q2** â second quaternion as [qx, qy, qz, qw]



Returns:
    

product quaternion as [qx, qy, qz, qw]

fiftyone.utils.transforms.quaternion_inverse(_q_)#
    

Compute the inverse of a unit quaternion.

For unit quaternions, the inverse equals the conjugate: q^(-1) = [-qx, -qy, -qz, qw]

Parameters:
    

**q** â unit quaternion as [qx, qy, qz, qw]

Returns:
    

inverse quaternion as [qx, qy, qz, qw]

fiftyone.utils.transforms.quaternion_from_euler(_angles_ , _seq ='xyz'_)#
    

Convert Euler angles to quaternion.

Parameters:
    

  * **angles** â Euler angles in radians as [angle1, angle2, angle3]

  * **seq** â rotation sequence, e.g., âxyzâ, âzyxâ, âZYXâ (default âxyzâ). Lowercase letters represent rotations about axes of the rotated frame (intrinsic), uppercase about the fixed frame (extrinsic).



Returns:
    

quaternion as [qx, qy, qz, qw]

fiftyone.utils.transforms.euler_from_quaternion(_q_ , _seq ='xyz'_)#
    

Convert quaternion to Euler angles.

Parameters:
    

  * **q** â quaternion as [qx, qy, qz, qw]

  * **seq** â rotation sequence, e.g., âxyzâ, âzyxâ, âZYXâ (default âxyzâ). Lowercase letters represent rotations about axes of the rotated frame (intrinsic), uppercase about the fixed frame (extrinsic).



Returns:
    

Euler angles in radians as [angle1, angle2, angle3]

fiftyone.utils.transforms.make_transform_matrix(_R_ , _t_)#
    

Construct a 4x4 homogeneous transformation matrix from rotation and translation.

The resulting matrix has the form:
    
    
    [[R, t],
     [0, 1]]
    

Parameters:
    

  * **R** â a (3, 3) rotation matrix

  * **t** â a (3,) translation vector



Returns:
    

a (4, 4) homogeneous transformation matrix

fiftyone.utils.transforms.decompose_transform_matrix(_T_)#
    

Extract rotation and translation from a 4x4 transformation matrix.

Parameters:
    

**T** â a (4, 4) or (3, 4) homogeneous transformation matrix

Returns:
    

tuple of (R, t) where R is a (3, 3) rotation matrix and t is a (3,) translation vector

fiftyone.utils.transforms.invert_transform_matrix(_T_)#
    

Efficiently invert a rigid transformation matrix.

For a rigid transform [R|t], the inverse is [R^T | -R^T @ t]. This is more numerically stable and efficient than general matrix inversion.

Parameters:
    

**T** â a (4, 4) homogeneous transformation matrix

Returns:
    

a (4, 4) inverse transformation matrix

fiftyone.utils.transforms.compose_transforms(_T1_ , _T2_)#
    

Compose two transformation matrices.

If T1 represents A->B and T2 represents B->C, the result is A->C.

Mathematically: T_result = T2 @ T1

Parameters:
    

  * **T1** â first transformation matrix (4, 4) representing A->B

  * **T2** â second transformation matrix (4, 4) representing B->C



Returns:
    

composed transformation matrix (4, 4) representing A->C

fiftyone.utils.transforms.axis_flip_matrix(_from_conv_ , _to_conv_)#
    

Get the 3x3 rotation matrix to convert between coordinate conventions.

Supported conventions:
    

  * Camera: âopencvâ (RDF), âopenglâ (RUB)

  * Robotics: ârosâ/âfluâ (Forward-Left-Up), âfruâ (Forward-Right-Up)

  * Aviation/Geo: ânedâ (North-East-Down), âenuâ (East-North-Up)




Parameters:
    

  * **from_conv** â source coordinate convention

  * **to_conv** â target coordinate convention



Returns:
    

a (3, 3) rotation matrix that transforms points from the source convention to the target convention

fiftyone.utils.transforms.opencv_to_opengl_points(_pts_)#
    

Convert points from OpenCV to OpenGL camera convention.

OpenCV: X-right, Y-down, Z-forward (RDF) OpenGL: X-right, Y-up, Z-backward (RUB)

This flips Y and Z axes: (x, y, z) -> (x, -y, -z)

Parameters:
    

**pts** â (N, 3) array of points in OpenCV convention

Returns:
    

(N, 3) array of points in OpenGL convention

fiftyone.utils.transforms.opengl_to_opencv_points(_pts_)#
    

Convert points from OpenGL to OpenCV camera convention.

OpenGL: X-right, Y-up, Z-backward (RUB) OpenCV: X-right, Y-down, Z-forward (RDF)

This flips Y and Z axes: (x, y, z) -> (x, -y, -z)

Parameters:
    

**pts** â (N, 3) array of points in OpenGL convention

Returns:
    

(N, 3) array of points in OpenCV convention

fiftyone.utils.transforms.transform_points_by_convention(_pts_ , _from_conv_ , _to_conv_)#
    

Transform points between coordinate conventions.

Parameters:
    

  * **pts** â (N, 3) array of points

  * **from_conv** â source coordinate convention

  * **to_conv** â target coordinate convention



Returns:
    

(N, 3) array of transformed points

fiftyone.utils.transforms.transform_points(_pts_ , _T_)#
    

Apply a 4x4 transformation matrix to 3D points.

Parameters:
    

  * **pts** â (N, 3) array of 3D points

  * **T** â (4, 4) homogeneous transformation matrix



Returns:
    

(N, 3) array of transformed points

fiftyone.utils.transforms.rotate_points(_pts_ , _R_)#
    

Apply a 3x3 rotation matrix to 3D points.

Parameters:
    

  * **pts** â (N, 3) array of 3D points

  * **R** â (3, 3) rotation matrix



Returns:
    

(N, 3) array of rotated points

fiftyone.utils.transforms.translate_points(_pts_ , _t_)#
    

Translate 3D points by a vector.

Parameters:
    

  * **pts** â (N, 3) array of 3D points

  * **t** â (3,) translation vector



Returns:
    

(N, 3) array of translated points

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
