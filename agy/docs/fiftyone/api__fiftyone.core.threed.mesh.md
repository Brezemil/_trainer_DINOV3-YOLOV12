---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.mesh.html
---

# fiftyone.core.threed.mesh#

Mesh definitions for 3D visualization.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Mesh`(name[,Â material,Â visible,Â position,Â ...]) | Represents an abstract 3D mesh.  
---|---  
`ObjMesh`(name,Â obj_path[,Â mtl_path,Â ...]) | Represents an OBJ mesh.  
`FbxMesh`(name,Â fbx_path[,Â default_material,Â ...]) | Represents an FBX mesh.  
`GltfMesh`(name,Â gltf_path[,Â ...]) | Represents a gLTF mesh.  
`PlyMesh`(name,Â ply_path[,Â is_point_cloud,Â ...]) | Represents a PLY mesh.  
`StlMesh`(name,Â stl_path[,Â default_material,Â ...]) | Represents an STL mesh.  
  
class fiftyone.core.threed.mesh.Mesh(_name : str_, _material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Object3D`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")

Represents an abstract 3D mesh.

Parameters:
    

  * **name** â the name of the mesh

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial") if not provided

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space




**Methods:**

`set_default_material`(material) | Sets the material of the mesh.  
---|---  
`add`(*objs) | Add one or more objects as children of this one.  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`traverse`([include_self]) | Traverse the scene graph.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
set_default_material(_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")_)#
    

Sets the material of the mesh.

Parameters:
    

**material** ([_MeshMaterial_](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")) â the material to set as the default

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

traverse(_include_self =True_)#
    

Traverse the scene graph.

property uuid#
    

The unique ID of the object.

class fiftyone.core.threed.mesh.ObjMesh(_name : str_, _obj_path : str_, _mtl_path : str | None = None_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Mesh`

Represents an OBJ mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **obj_path** (_str_) â the path to the `.obj` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **mtl_path** (_str_ _,__optional_) â the path to the `.mtl` file. Defaults to `None`. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh if `mtl_path` is not provided or if material in `mtl_path` is not found. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space



Raises:
    

  * **ValueError** â if `obj_path` does not end with `.obj`

  * **ValueError** â if `mtl_path` does not end with `.mtl`




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

class fiftyone.core.threed.mesh.FbxMesh(_name : str_, _fbx_path : str_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Mesh`

Represents an FBX mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **fbx_path** (_str_) â the path to the `.fbx` file. Path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh if FBX file does not contain material information. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space



Raises:
    

**ValueError** â If `fbx_path` does not end with `.fbx`

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

class fiftyone.core.threed.mesh.GltfMesh(_name : str_, _gltf_path : str_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Mesh`

Represents a gLTF mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **gltf_path** (_str_) â the path to the `.gltf` or `.glb` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh if gLTF file does not contain material information. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space



Raises:
    

**ValueError** â if `gltf_path` does not end with â.gltfâ or `.glb`

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

class fiftyone.core.threed.mesh.PlyMesh(_name : str_, _ply_path : str_, _is_point_cloud : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _center_geometry : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Mesh`

Represents a PLY mesh. A PLY mesh can be a point cloud or a mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **ply_path** (_str_) â the path to the `.ply` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **is_point_cloud** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the PLY file is a point cloud. Defaults to `False`

  * **center_geometry** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to center the geometry. Defaults to `True`

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the mesh if PLY file does not contain vertex colors. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial"). If the PLY file contains vertex colors, the material is ignored and vertex colors are used

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space



Raises:
    

**ValueError** â if `ply_path` does not end with `.ply`

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

class fiftyone.core.threed.mesh.StlMesh(_name : str_, _stl_path : str_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Mesh`

Represents an STL mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **stl_path** (_str_) â the path to the `.stl` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the mesh. Defaults to [`fiftyone.core.threed.MeshStandardMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.MeshStandardMaterial "fiftyone.core.threed.MeshStandardMaterial")

  * **visible** (_True_) â default visibility of the mesh in the scene

  * **position** (_None_) â the position of the mesh in object space

  * **quaternion** (_None_) â the quaternion of the mesh in object space

  * **scale** (_None_) â the scale of the mesh in object space



Raises:
    

**ValueError** â if `stl_path` does not end with `.stl`

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
