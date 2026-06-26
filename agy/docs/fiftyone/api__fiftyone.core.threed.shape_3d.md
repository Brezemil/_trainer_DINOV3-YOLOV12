---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.shape_3d.html
---

# fiftyone.core.threed.shape_3d#

Mesh definitions for 3D visualization.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Shape3D`(name[,Â material,Â visible,Â position,Â ...]) | Represents an abstract 3D shape.  
---|---  
`BoxGeometry`(name[,Â width,Â height,Â depth,Â ...]) | Represents a 3D box.  
`CylinderGeometry`(name[,Â radius_top,Â ...]) | Represents a 3D cylinder.  
`SphereGeometry`(name[,Â radius,Â ...]) | Represents a 3D sphere.  
`PlaneGeometry`(name[,Â width,Â height,Â ...]) | Represents a 3D plane.  
  
class fiftyone.core.threed.shape_3d.Shape3D(_name : str_, _material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents an abstract 3D shape.

Parameters:
    

  * **name** â the name of the mesh

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the shape mesh. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial") if not provided

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`set_default_material`(material) | Sets the material of the mesh.  
`traverse`([include_self]) | Traverse the scene graph.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
add(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Add one or more objects as children of this one.

as_dict()#
    

Converts the object to a dict.

clear() → None#
    

Remove all children from this object.

find_and_execute(_node : [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_, _predicate_ , _on_match_ , _stop_on_first_match : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Recursively search the scene graph and execute an action on matching nodes.

This is a generic method for traversing the scene graph and performing operations on nodes that match a given predicate. It can be used for finding and removing nodes, collecting nodes, updating nodes, etc.

The traversal continues into the subtrees of both matching and non-matching nodes. For matching nodes, the subtree is traversed when on_match returns True and stop_on_first_match is False.

Parameters:
    

  * **node** â the node to start searching from

  * **predicate** â a function that takes a child Object3D and returns

  * **criteria** (_True if it matches the search_)

  * **on_match** â a function called when a match is found, takes

  * **(****parent**

  * **searching** ([_child_](api__fiftyone.core.odm.md#fiftyone.core.odm.WorkspaceDocument.child "fiftyone.core.odm.WorkspaceDocument.child") _)__and returns True to continue_)

  * **to** (_False_)

  * **stop**

  * **stop_on_first_match** â if True, stop searching after first match

  * **processed** (_is_)



Returns:
    

True if a match was found and we should stop, False otherwise

Example

# Find all nodes with a specific name and collect them matches = [] def predicate(child):

> return child.name == âtargetâ

def on_match(parent, child):
    

matches.append(child) return True # continue searching

scene.find_and_execute(scene, predicate, on_match)

property local_transform_matrix#
    

The local transform matrix of the object.

Setting this property also decomposes the matrix into its constituent position, quaternion, and scale components. However, decomposition of matrices with skew / shear components (non-uniform scaling) might have unexpected results.

property position#
    

The position of the object in object space.

property quaternion#
    

The quaternion of the object in object space.

remove(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Remove one or more objects from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes any matching objects from their parentâs children list.

Parameters:
    

***objs** â one or more Object3D instances to remove

Raises:
    

  * **ValueError** â if any of the objects to remove is this object itself

  * **ValueError** â if any of the objects is not found in the scene graph




remove_by_name(_name : str_) → None#
    

Remove all objects with the given name from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes all objects matching the given name from their parentâs children lists.

Parameters:
    

**name** â the name of the objects to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by name

  * **ValueError** â if no objects with the given name are found




remove_by_uuid(_target_uuid : str_) → None#
    

Remove the object with the given UUID from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes the object matching the given UUID from its parentâs children list. UUIDs should be unique, so only one match is expected.

Parameters:
    

**target_uuid** â the UUID of the object to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by UUID

  * **ValueError** â if no object with the given UUID is found




property rotation#
    

The rotation of the object in object space.

property scale#
    

The scale of the object in object space.

set_default_material(_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")_)#
    

Sets the material of the mesh.

Parameters:
    

**material** ([_MeshMaterial_](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")) â the material to set as the default

traverse(_include_self =True_)#
    

Traverse the scene graph.

property uuid#
    

The unique ID of the object.

class fiftyone.core.threed.shape_3d.BoxGeometry(_name : str_, _width : float = 1_, _height : float = 1_, _depth : float = 1_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Shape3D`

Represents a 3D box.

Parameters:
    

  * **name** (_str_) â name of the box

  * **width** (_float_) â the width of the box. Defaults to 1

  * **height** (_float_) â the height of the box. Defaults to 1

  * **depth** (_float_) â the depth of the box. Defaults to 1

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the box. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`set_default_material`(material) | Sets the material of the mesh.  
`traverse`([include_self]) | Traverse the scene graph.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
add(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Add one or more objects as children of this one.

as_dict()#
    

Converts the object to a dict.

clear() → None#
    

Remove all children from this object.

find_and_execute(_node : [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_, _predicate_ , _on_match_ , _stop_on_first_match : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Recursively search the scene graph and execute an action on matching nodes.

This is a generic method for traversing the scene graph and performing operations on nodes that match a given predicate. It can be used for finding and removing nodes, collecting nodes, updating nodes, etc.

The traversal continues into the subtrees of both matching and non-matching nodes. For matching nodes, the subtree is traversed when on_match returns True and stop_on_first_match is False.

Parameters:
    

  * **node** â the node to start searching from

  * **predicate** â a function that takes a child Object3D and returns

  * **criteria** (_True if it matches the search_)

  * **on_match** â a function called when a match is found, takes

  * **(****parent**

  * **searching** ([_child_](api__fiftyone.core.odm.md#fiftyone.core.odm.WorkspaceDocument.child "fiftyone.core.odm.WorkspaceDocument.child") _)__and returns True to continue_)

  * **to** (_False_)

  * **stop**

  * **stop_on_first_match** â if True, stop searching after first match

  * **processed** (_is_)



Returns:
    

True if a match was found and we should stop, False otherwise

Example

# Find all nodes with a specific name and collect them matches = [] def predicate(child):

> return child.name == âtargetâ

def on_match(parent, child):
    

matches.append(child) return True # continue searching

scene.find_and_execute(scene, predicate, on_match)

property local_transform_matrix#
    

The local transform matrix of the object.

Setting this property also decomposes the matrix into its constituent position, quaternion, and scale components. However, decomposition of matrices with skew / shear components (non-uniform scaling) might have unexpected results.

property position#
    

The position of the object in object space.

property quaternion#
    

The quaternion of the object in object space.

remove(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Remove one or more objects from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes any matching objects from their parentâs children list.

Parameters:
    

***objs** â one or more Object3D instances to remove

Raises:
    

  * **ValueError** â if any of the objects to remove is this object itself

  * **ValueError** â if any of the objects is not found in the scene graph




remove_by_name(_name : str_) → None#
    

Remove all objects with the given name from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes all objects matching the given name from their parentâs children lists.

Parameters:
    

**name** â the name of the objects to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by name

  * **ValueError** â if no objects with the given name are found




remove_by_uuid(_target_uuid : str_) → None#
    

Remove the object with the given UUID from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes the object matching the given UUID from its parentâs children list. UUIDs should be unique, so only one match is expected.

Parameters:
    

**target_uuid** â the UUID of the object to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by UUID

  * **ValueError** â if no object with the given UUID is found




property rotation#
    

The rotation of the object in object space.

property scale#
    

The scale of the object in object space.

set_default_material(_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")_)#
    

Sets the material of the mesh.

Parameters:
    

**material** ([_MeshMaterial_](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")) â the material to set as the default

traverse(_include_self =True_)#
    

Traverse the scene graph.

property uuid#
    

The unique ID of the object.

class fiftyone.core.threed.shape_3d.CylinderGeometry(_name : str_, _radius_top : float = 1_, _radius_bottom : float = 1_, _height : float = 1_, _radial_segments : int = 32_, _height_segments : int = 1_, _open_ended : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _theta_start : float = 0_, _theta_length : float = 6.283185307179586_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Shape3D`

Represents a 3D cylinder.

Parameters:
    

  * **name** (_str_) â name of the cylinder

  * **radius_top** (_float_) â the radius of the top of the cylinder. Defaults to 1

  * **radius_bottom** (_float_) â the radius of the bottom of the cylinder. Defaults to 1

  * **height** (_float_) â the height of the cylinder. Defaults to 1

  * **radial_segments** (_int_) â number of segmented faces around the circumference of the cylinder. Defaults to 32

  * **height_segments** (_int_) â number of rows of faces around the circumference of the cylinder. Defaults to 1

  * **open_ended** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the cylinder is open-ended. Defaults to `False`

  * **theta_start** (_float_) â the start angle for the vertical sweep. Defaults to 0

  * **theta_length** (_float_) â the angle for the vertical sweep. Defaults to 2*Math.PI, which makes for a complete cylinder

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the cylinder. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`set_default_material`(material) | Sets the material of the mesh.  
`traverse`([include_self]) | Traverse the scene graph.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
add(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Add one or more objects as children of this one.

as_dict()#
    

Converts the object to a dict.

clear() → None#
    

Remove all children from this object.

find_and_execute(_node : [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_, _predicate_ , _on_match_ , _stop_on_first_match : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Recursively search the scene graph and execute an action on matching nodes.

This is a generic method for traversing the scene graph and performing operations on nodes that match a given predicate. It can be used for finding and removing nodes, collecting nodes, updating nodes, etc.

The traversal continues into the subtrees of both matching and non-matching nodes. For matching nodes, the subtree is traversed when on_match returns True and stop_on_first_match is False.

Parameters:
    

  * **node** â the node to start searching from

  * **predicate** â a function that takes a child Object3D and returns

  * **criteria** (_True if it matches the search_)

  * **on_match** â a function called when a match is found, takes

  * **(****parent**

  * **searching** ([_child_](api__fiftyone.core.odm.md#fiftyone.core.odm.WorkspaceDocument.child "fiftyone.core.odm.WorkspaceDocument.child") _)__and returns True to continue_)

  * **to** (_False_)

  * **stop**

  * **stop_on_first_match** â if True, stop searching after first match

  * **processed** (_is_)



Returns:
    

True if a match was found and we should stop, False otherwise

Example

# Find all nodes with a specific name and collect them matches = [] def predicate(child):

> return child.name == âtargetâ

def on_match(parent, child):
    

matches.append(child) return True # continue searching

scene.find_and_execute(scene, predicate, on_match)

property local_transform_matrix#
    

The local transform matrix of the object.

Setting this property also decomposes the matrix into its constituent position, quaternion, and scale components. However, decomposition of matrices with skew / shear components (non-uniform scaling) might have unexpected results.

property position#
    

The position of the object in object space.

property quaternion#
    

The quaternion of the object in object space.

remove(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Remove one or more objects from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes any matching objects from their parentâs children list.

Parameters:
    

***objs** â one or more Object3D instances to remove

Raises:
    

  * **ValueError** â if any of the objects to remove is this object itself

  * **ValueError** â if any of the objects is not found in the scene graph




remove_by_name(_name : str_) → None#
    

Remove all objects with the given name from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes all objects matching the given name from their parentâs children lists.

Parameters:
    

**name** â the name of the objects to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by name

  * **ValueError** â if no objects with the given name are found




remove_by_uuid(_target_uuid : str_) → None#
    

Remove the object with the given UUID from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes the object matching the given UUID from its parentâs children list. UUIDs should be unique, so only one match is expected.

Parameters:
    

**target_uuid** â the UUID of the object to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by UUID

  * **ValueError** â if no object with the given UUID is found




property rotation#
    

The rotation of the object in object space.

property scale#
    

The scale of the object in object space.

set_default_material(_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")_)#
    

Sets the material of the mesh.

Parameters:
    

**material** ([_MeshMaterial_](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")) â the material to set as the default

traverse(_include_self =True_)#
    

Traverse the scene graph.

property uuid#
    

The unique ID of the object.

class fiftyone.core.threed.shape_3d.SphereGeometry(_name : str_, _radius : float = 1_, _width_segments : int = 32_, _height_segments : int = 16_, _phi_start : float = 0_, _phi_length : float = 6.283185307179586_, _theta_start : float = 0_, _theta_length : float = 3.141592653589793_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Shape3D`

Represents a 3D sphere.

Parameters:
    

  * **name** (_str_) â the name of the sphere

  * **radius** (_float_) â the radius of the sphere. Defaults to 1

  * **width_segments** (_int_) â the number of segmented faces around the circumference of the sphere. Defaults to 32

  * **height_segments** (_int_) â the number of rows of faces around the circumference of the sphere. Defaults to 16

  * **phi_start** (_float_) â the start angle for the horizontal sweep. Defaults to 0

  * **phi_length** (_float_) â the angle for the horizontal sweep. Defaults to `2*math.pi`, which makes for a complete sphere

  * **theta_start** (_float_) â the start angle for the vertical sweep. Defaults to 0

  * **theta_length** (_float_) â the angle for the vertical sweep. Defaults to `math.pi`, which makes for a complete sphere

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the sphere. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`set_default_material`(material) | Sets the material of the mesh.  
`traverse`([include_self]) | Traverse the scene graph.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
add(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Add one or more objects as children of this one.

as_dict()#
    

Converts the object to a dict.

clear() → None#
    

Remove all children from this object.

find_and_execute(_node : [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_, _predicate_ , _on_match_ , _stop_on_first_match : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Recursively search the scene graph and execute an action on matching nodes.

This is a generic method for traversing the scene graph and performing operations on nodes that match a given predicate. It can be used for finding and removing nodes, collecting nodes, updating nodes, etc.

The traversal continues into the subtrees of both matching and non-matching nodes. For matching nodes, the subtree is traversed when on_match returns True and stop_on_first_match is False.

Parameters:
    

  * **node** â the node to start searching from

  * **predicate** â a function that takes a child Object3D and returns

  * **criteria** (_True if it matches the search_)

  * **on_match** â a function called when a match is found, takes

  * **(****parent**

  * **searching** ([_child_](api__fiftyone.core.odm.md#fiftyone.core.odm.WorkspaceDocument.child "fiftyone.core.odm.WorkspaceDocument.child") _)__and returns True to continue_)

  * **to** (_False_)

  * **stop**

  * **stop_on_first_match** â if True, stop searching after first match

  * **processed** (_is_)



Returns:
    

True if a match was found and we should stop, False otherwise

Example

# Find all nodes with a specific name and collect them matches = [] def predicate(child):

> return child.name == âtargetâ

def on_match(parent, child):
    

matches.append(child) return True # continue searching

scene.find_and_execute(scene, predicate, on_match)

property local_transform_matrix#
    

The local transform matrix of the object.

Setting this property also decomposes the matrix into its constituent position, quaternion, and scale components. However, decomposition of matrices with skew / shear components (non-uniform scaling) might have unexpected results.

property position#
    

The position of the object in object space.

property quaternion#
    

The quaternion of the object in object space.

remove(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Remove one or more objects from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes any matching objects from their parentâs children list.

Parameters:
    

***objs** â one or more Object3D instances to remove

Raises:
    

  * **ValueError** â if any of the objects to remove is this object itself

  * **ValueError** â if any of the objects is not found in the scene graph




remove_by_name(_name : str_) → None#
    

Remove all objects with the given name from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes all objects matching the given name from their parentâs children lists.

Parameters:
    

**name** â the name of the objects to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by name

  * **ValueError** â if no objects with the given name are found




remove_by_uuid(_target_uuid : str_) → None#
    

Remove the object with the given UUID from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes the object matching the given UUID from its parentâs children list. UUIDs should be unique, so only one match is expected.

Parameters:
    

**target_uuid** â the UUID of the object to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by UUID

  * **ValueError** â if no object with the given UUID is found




property rotation#
    

The rotation of the object in object space.

property scale#
    

The scale of the object in object space.

set_default_material(_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")_)#
    

Sets the material of the mesh.

Parameters:
    

**material** ([_MeshMaterial_](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")) â the material to set as the default

traverse(_include_self =True_)#
    

Traverse the scene graph.

property uuid#
    

The unique ID of the object.

class fiftyone.core.threed.shape_3d.PlaneGeometry(_name : str_, _width : float = 1_, _height : float = 1_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Shape3D`

Represents a 3D plane.

Parameters:
    

  * **name** (_str_) â name of the plane

  * **width** (_float_) â the width of the plane. Defaults to 1

  * **height** (_float_) â the height of the plane. Defaults to 1

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the plane. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`set_default_material`(material) | Sets the material of the mesh.  
`traverse`([include_self]) | Traverse the scene graph.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
add(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Add one or more objects as children of this one.

as_dict()#
    

Converts the object to a dict.

clear() → None#
    

Remove all children from this object.

find_and_execute(_node : [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_, _predicate_ , _on_match_ , _stop_on_first_match : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Recursively search the scene graph and execute an action on matching nodes.

This is a generic method for traversing the scene graph and performing operations on nodes that match a given predicate. It can be used for finding and removing nodes, collecting nodes, updating nodes, etc.

The traversal continues into the subtrees of both matching and non-matching nodes. For matching nodes, the subtree is traversed when on_match returns True and stop_on_first_match is False.

Parameters:
    

  * **node** â the node to start searching from

  * **predicate** â a function that takes a child Object3D and returns

  * **criteria** (_True if it matches the search_)

  * **on_match** â a function called when a match is found, takes

  * **(****parent**

  * **searching** ([_child_](api__fiftyone.core.odm.md#fiftyone.core.odm.WorkspaceDocument.child "fiftyone.core.odm.WorkspaceDocument.child") _)__and returns True to continue_)

  * **to** (_False_)

  * **stop**

  * **stop_on_first_match** â if True, stop searching after first match

  * **processed** (_is_)



Returns:
    

True if a match was found and we should stop, False otherwise

Example

# Find all nodes with a specific name and collect them matches = [] def predicate(child):

> return child.name == âtargetâ

def on_match(parent, child):
    

matches.append(child) return True # continue searching

scene.find_and_execute(scene, predicate, on_match)

property local_transform_matrix#
    

The local transform matrix of the object.

Setting this property also decomposes the matrix into its constituent position, quaternion, and scale components. However, decomposition of matrices with skew / shear components (non-uniform scaling) might have unexpected results.

property position#
    

The position of the object in object space.

property quaternion#
    

The quaternion of the object in object space.

remove(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Remove one or more objects from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes any matching objects from their parentâs children list.

Parameters:
    

***objs** â one or more Object3D instances to remove

Raises:
    

  * **ValueError** â if any of the objects to remove is this object itself

  * **ValueError** â if any of the objects is not found in the scene graph




remove_by_name(_name : str_) → None#
    

Remove all objects with the given name from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes all objects matching the given name from their parentâs children lists.

Parameters:
    

**name** â the name of the objects to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by name

  * **ValueError** â if no objects with the given name are found




remove_by_uuid(_target_uuid : str_) → None#
    

Remove the object with the given UUID from the scene graph recursively.

This method searches recursively through the entire scene graph starting from this object and removes the object matching the given UUID from its parentâs children list. UUIDs should be unique, so only one match is expected.

Parameters:
    

**target_uuid** â the UUID of the object to remove

Raises:
    

  * **ValueError** â if attempting to remove this object itself by UUID

  * **ValueError** â if no object with the given UUID is found




property rotation#
    

The rotation of the object in object space.

property scale#
    

The scale of the object in object space.

set_default_material(_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")_)#
    

Sets the material of the mesh.

Parameters:
    

**material** ([_MeshMaterial_](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")) â the material to set as the default

traverse(_include_self =True_)#
    

Traverse the scene graph.

property uuid#
    

The unique ID of the object.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
