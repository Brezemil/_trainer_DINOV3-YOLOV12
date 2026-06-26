---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.lights.html
---

# fiftyone.core.threed.lights#

Lights definition for 3D visualization.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Light`([name,Â color,Â intensity,Â visible,Â ...]) | Base class for 3D lights.  
---|---  
`AmbientLight`([name,Â intensity,Â color,Â ...]) | Represents an ambient light.  
`DirectionalLight`([name,Â target,Â color,Â ...]) | Represents a directional light.  
`PointLight`([name,Â distance,Â decay,Â color,Â ...]) | Represents a point light.  
`SpotLight`([name,Â target,Â distance,Â decay,Â ...]) | Represents a spot light.  
  
class fiftyone.core.threed.lights.Light(_name : str | None = None_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Object3D`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")

Base class for 3D lights.

Parameters:
    

  * **color** (_"#ffffff"_) â the color of the light

  * **intensity** (_1.0_) â the intensity of the light in the range `[0, 1]`

  * **visible** (_True_) â default visibility of the object in the scene

  * **position** (_None_) â the position of the light in object space

  * **quaternion** (_None_) â the quaternion of the light in object space

  * **scale** (_None_) â the scale of the light in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
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

class fiftyone.core.threed.lights.AmbientLight(_name : str = 'AmbientLight'_, _intensity : float = 0.1_, _color : str = '#ffffff'_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Light`

Represents an ambient light.

This light globally illuminates all objects in the scene equally.

Parameters:
    

  * **name** (_"AmbientLight"_) â the name of the light

  * **intensity** (_0.1_) â the intensity of the light in the range `[0, 1]`

  * **color** (_"#ffffff"_) â the color of the light

  * **visible** (_True_) â default visibility of the object in the scene

  * **position** (_None_) â the position of the light in object space

  * **quaternion** (_None_) â the quaternion of the light in object space

  * **scale** (_None_) â the scale of the light in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
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

class fiftyone.core.threed.lights.DirectionalLight(_name : str = 'DirectionalLight'_, _target : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array = Vector3(x=0.0, y=0.0, z=0.0)_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Light`

Represents a directional light.

A light that gets emitted in a specific direction. This light will behave as though it is infinitely far away and the rays produced from it are all parallel.

Parameters:
    

  * **name** (_"DirectionalLight"_) â the name of the light

  * **target** (_[__0_ _,__0_ _,__0_ _]_) â the target of the light

  * **color** (_"#ffffff"_) â the color of the light

  * **intensity** (_1.0_) â the intensity of the light in the range `[0, 1]`

  * **visible** (_True_) â default visibility of the object in the scene

  * **position** (_None_) â the position of the light in object space

  * **quaternion** (_None_) â the quaternion of the light in object space

  * **scale** (_None_) â the scale of the light in object space




**Attributes:**

`target` |   
---|---  
`local_transform_matrix` | The local transform matrix of the object.  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`traverse`([include_self]) | Traverse the scene graph.  
  
target: [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array = Vector3(x=0.0, y=0.0, z=0.0)#
    

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

class fiftyone.core.threed.lights.PointLight(_name : str = 'PointLight'_, _distance : float = 0.0_, _decay : float = 2.0_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Light`

Represents a point light.

Parameters:
    

  * **name** (_"PointLight"_) â the name of the light

  * **distance** (_0.0_) â the distance at which the lightâs intensity is zero

  * **decay** (_2.0_) â the amount the light dims along the distance of the light

  * **color** (_"#ffffff"_) â the color of the light

  * **intensity** (_1.0_) â the intensity of the light in the range `[0, 1]`

  * **visible** (_True_) â default visibility of the object in the scene

  * **position** (_None_) â the position of the light in object space

  * **quaternion** (_None_) â the quaternion of the light in object space

  * **scale** (_None_) â the scale of the light in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
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

class fiftyone.core.threed.lights.SpotLight(_name : str = 'SpotLight'_, _target : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array = None_, _distance : float = 0.0_, _decay : float = 2.0_, _angle : float = 1.0471975511965976_, _penumbra : float = 0.0_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `Light`

Represents a spot light.

Parameters:
    

  * **name** (_"SpotLight"_) â the name of the light

  * **target** (_[__0_ _,__0_ _,__0_ _]_) â the target of the light

  * **distance** (_0.0_) â the distance at which the lightâs intensity is zero

  * **decay** (_2.0_) â the amount the light dims along the distance of the light

  * **angle** (_PI / 3_) â the angle of the lightâs spotlight, in radians

  * **penumbra** (_0.0_) â the angle of the penumbra of the lightâs spotlight, in radians

  * **color** (_"#ffffff"_) â the color of the light

  * **intensity** (_1.0_) â the intensity of the light in the range `[0, 1]`

  * **visible** (_True_) â default visibility of the object in the scene

  * **position** (_None_) â the position of the light in object space

  * **quaternion** (_None_) â the quaternion of the light in object space

  * **scale** (_None_) â the scale of the light in object space




**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
