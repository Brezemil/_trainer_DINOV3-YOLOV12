---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.scene_3d.html
---

# fiftyone.core.threed.scene_3d#

3D scene definitions.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SceneBackground`([color,Â image,Â cube,Â intensity]) | Represents the background of the scene.  
---|---  
`Scene`([camera,Â lights,Â background]) | Represents a scene graph which contains a hierarchy of 3D objects.  
  
class fiftyone.core.threed.scene_3d.SceneBackground(_color : str | None = None_, _image : str | None = None_, _cube : List[str] | None = None_, _intensity : float | None = 1.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents the background of the scene.

Parameters:
    

  * **color** (_str_ _,__optional_) â the background color of the scene

  * **image** (_str_ _,__optional_) â the path to the background image. Defaults to None. This takes precedence over color if provided

  * **cube** ([_list_](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list") _,__optional_) â the paths to the six faces of the background. The order of the faces is: +X, -X, +Y, -Y, +Z, -Z. Defaults to `None`. This takes precedence over the image and color if provided. This can be used to build a skybox

  * **intensity** (_float_ _,__optional_) â the intensity of the background. Defaults to `1.0`. This only applies for `image` and `cube` backgrounds




**Attributes:**

`color` |   
---|---  
`image` |   
`cube` |   
`intensity` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property color: str | None#
    

property image: str | None#
    

property cube: List[str] | None#
    

property intensity: float | None#
    

as_dict() → dict#
    

class fiftyone.core.threed.scene_3d.Scene(_camera : [PerspectiveCamera](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera "fiftyone.core.threed.camera.PerspectiveCamera") | None = None_, _lights : List[[Light](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light "fiftyone.core.threed.lights.Light")] | None = None_, _background : SceneBackground | None = None_)#
    

Bases: [`Object3D`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")

Represents a scene graph which contains a hierarchy of 3D objects.

Example usage:
    
    
    import fiftyone as fo
    
    scene = fo.Scene()
    
    obj_mesh = fo.ObjMesh(
        "obj_mesh_name", "/path/to/mesh.obj", mtl_path="/path/to/mesh.mtl"
    )
    gltf_mesh = fo.GltfMesh("gltf_mesh_name", "/path/to/mesh.gltf")
    pcd = fo.PointCloud("pcd_name", "/path/to/points.pcd")
    
    scene.add(obj_mesh)
    scene.add(gltf_mesh)
    scene.add(pcd)
    
    scene.write("/path/to/scene.fo3d")
    
    sample = fo.Sample("/path/to/scene.fo3d")
    
    dataset = fo.Dataset()
    dataset.add_sample(sample)
    

Parameters:
    

  * **camera** (_None_) â the default camera of the scene. If `None`, a default [`fiftyone.core.threed.PerspectiveCamera`](api__fiftyone.core.threed.md#fiftyone.core.threed.PerspectiveCamera "fiftyone.core.threed.PerspectiveCamera") is created with reasonable defaults

  * **lights** (_None_) â a list of lights in the scene. If``None``, a default set of lights is used, which includes an ambient light and six directional lights placed at different angles around the scene

  * **background** (_None_) â the background for the scene. May be a color, image, or a skybox




**Methods:**

`copy`() | Returns a deep copy of the scene.  
---|---  
`write`(fo3d_path[,Â resolve_relative_paths,Â ...]) | Export the scene to a `.fo3d` file.  
`add`(*objs) | Add one or more objects as children of this one.  
`as_dict`() | Converts the object to a dict.  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`traverse`([include_self]) | Traverse the scene graph.  
`update_asset_paths`(asset_rewrite_paths) | Update asset paths in this scene according to an input dict mapping.  
`get_scene_summary`() | Returns a summary of the scene.  
`get_asset_paths`() | Returns a list of all asset paths in the scene.  
`from_fo3d`(path) | Loads a scene from an FO3D file.  
  
**Attributes:**

`local_transform_matrix` | The local transform matrix of the object.  
---|---  
`position` | The position of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`rotation` | The rotation of the object in object space.  
`scale` | The scale of the object in object space.  
`uuid` | The unique ID of the object.  
  
copy()#
    

Returns a deep copy of the scene.

write(_fo3d_path : str_, _resolve_relative_paths =False_, _pprint =False_)#
    

Export the scene to a `.fo3d` file.

Parameters:
    

  * **fo3d_path** â the path to write the scene to

  * **resolve_relative_paths** â whether to resolve relative paths in the scene to absolute paths. If `True`, all asset paths in the scene are resolved to absolute paths. If `False`, asset paths are left as-is. Defaults to `False`.

  * **pprint** â whether to pretty-print the JSON output. Defaults to `False`.




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

traverse(_include_self =False_)#
    

Traverse the scene graph.

Parameters:
    

**include_self** â whether to include the current node in the traversal

Returns:
    

a generator that yields `Object3D` instances

property uuid#
    

The unique ID of the object.

update_asset_paths(_asset_rewrite_paths : dict_)#
    

Update asset paths in this scene according to an input dict mapping.

Asset path is unchanged if it does not exist in `asset_rewrite_paths`

Parameters:
    

**asset_rewrite_paths** â `dict` mapping asset path to new asset path

Returns:
    

`True` if the scene was modified.

get_scene_summary()#
    

Returns a summary of the scene.

get_asset_paths()#
    

Returns a list of all asset paths in the scene.

Note that any relative asset paths are not resolved to absolute paths.

Returns:
    

a list of asset paths

static from_fo3d(_path : str_)#
    

Loads a scene from an FO3D file.

Parameters:
    

**path** â the path to an `.fo3d` file

Returns:
    

a `Scene`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
