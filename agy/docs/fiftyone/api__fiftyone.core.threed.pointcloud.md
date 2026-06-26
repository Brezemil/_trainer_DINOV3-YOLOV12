---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.pointcloud.html
---

# fiftyone.core.threed.pointcloud#

PointCloud definition for 3D visualization.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PointCloud`(name,Â pcd_path[,Â material,Â ...]) | Represents a point cloud.  
---|---  
  
class fiftyone.core.threed.pointcloud.PointCloud(_name : str_, _pcd_path : str_, _material : [PointCloudMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial "fiftyone.core.threed.material_3d.PointCloudMaterial") | None = None_, _center_geometry : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _flag_for_projection : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Object3D`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")

Represents a point cloud.

Parameters:
    

  * **name** (_str_) â the name of the point cloud

  * **pcd_path** (_str_) â the path to the `.pcd` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** ([`fiftyone.core.threed.PointCloudMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.PointCloudMaterial "fiftyone.core.threed.PointCloudMaterial"), optional) â the material of the point cloud. If not specified, defaults to a new instance of [`fiftyone.core.threed.PointCloudMaterial`](api__fiftyone.core.threed.md#fiftyone.core.threed.PointCloudMaterial "fiftyone.core.threed.PointCloudMaterial") with its default parameters

  * **center_geometry** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to center the geometry of the point cloud. Defaults to `False`

  * **flag_for_projection** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to flag the point cloud for usage in orthographic projection. Each [`fiftyone.core.threed.Scene`](api__fiftyone.core.threed.md#fiftyone.core.threed.Scene "fiftyone.core.threed.Scene") can have at most one asset flagged for orthographic projection. Defaults to `False`. If multiple assets are flagged, the first one will be chosen

  * **visible** (_True_) â default visibility of the point cloud in the scene

  * **position** (_None_) â the position of the object in point cloud space

  * **quaternion** (_None_) â the quaternion of the point cloud in object space

  * **scale** (_None_) â the scale of the point cloud in object space



Raises:
    

**ValueError** â if `pcd_path` does not end with `.pcd`

**Methods:**

`set_default_material`(material) | Sets the material of the point cloud.  
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
  
set_default_material(_material : [PointCloudMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial "fiftyone.core.threed.material_3d.PointCloudMaterial")_)#
    

Sets the material of the point cloud.

Parameters:
    

**material** ([_PointCloudMaterial_](api__fiftyone.core.threed.md#fiftyone.core.threed.PointCloudMaterial "fiftyone.core.threed.PointCloudMaterial")) â The material to set as the default

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
