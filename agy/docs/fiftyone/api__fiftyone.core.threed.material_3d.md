---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.material_3d.html
---

# fiftyone.core.threed.material_3d#

Material definition for 3D visualization.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Material3D`([opacity]) | Base class for 3D materials.  
---|---  
`PointCloudMaterial`([shading_mode,Â ...]) | Represents a point cloud material.  
`MeshMaterial`([wireframe,Â opacity]) | Represents a mesh material.  
`MeshBasicMaterial`([color,Â wireframe,Â opacity]) | Represents a basic mesh material.  
`MeshStandardMaterial`([color,Â ...]) | Represents a standard mesh material.  
`MeshLambertMaterial`([color,Â emissive_color,Â ...]) | Represents a Lambert mesh material.  
`MeshPhongMaterial`([shininess,Â ...]) | Represents a Phong mesh material.  
`MeshDepthMaterial`([wireframe,Â opacity]) | Represents a depth mesh material.  
  
class fiftyone.core.threed.material_3d.Material3D(_opacity : float = 1.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Base class for 3D materials.

Parameters:
    

**opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`

**Attributes:**

`opacity` |   
---|---  
  
**Methods:**

`as_dict`() |   
---|---  
  
property opacity: float#
    

as_dict()#
    

class fiftyone.core.threed.material_3d.PointCloudMaterial(_shading_mode : Literal['height', 'intensity', 'rgb', 'custom'] = 'height'_, _custom_color : str = '#ffffff'_, _point_size : float = 1.0_, _attenuate_by_distance : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `Material3D`

Represents a point cloud material.

Parameters:
    

  * **shading_mode** (_"height"_) â the shading mode to use. Supported values are âheightâ, âintensityâ, ârgbâ, and âcustomâ

  * **custom_color** (_"#ffffff"_) â a custom color to use for the point cloud. This is only used when shading_mode is âcustomâ

  * **point_size** (_1.0_) â the size of the points in the point cloud

  * **attenuate_by_distance** (_False_) â whether to attenuate the point size based on distance from the camera

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Attributes:**

`shading_mode` |   
---|---  
`custom_color` |   
`point_size` |   
`attenuate_by_distance` |   
`opacity` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property shading_mode: Literal['height', 'intensity', 'rgb', 'custom']#
    

property custom_color: str#
    

property point_size: float#
    

property attenuate_by_distance: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

as_dict()#
    

property opacity: float#
    

class fiftyone.core.threed.material_3d.MeshMaterial(_wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `Material3D`

Represents a mesh material.

Parameters:
    

  * **wireframe** (_False_) â whether to render the mesh as a wireframe

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Attributes:**

`wireframe` |   
---|---  
`opacity` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property wireframe: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

as_dict()#
    

property opacity: float#
    

class fiftyone.core.threed.material_3d.MeshBasicMaterial(_color : str = '#808080'_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `MeshMaterial`

Represents a basic mesh material.

This material is not affected by lights, and is rendered as a solid color.

Parameters:
    

  * **color** (_"#808080"_) â the color of the material

  * **wireframe** (_False_) â whether to render the mesh as a wireframe

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Attributes:**

`color` |   
---|---  
`opacity` |   
`wireframe` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property color: str#
    

as_dict()#
    

property opacity: float#
    

property wireframe: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

class fiftyone.core.threed.material_3d.MeshStandardMaterial(_color : str = '#808080'_, _emissive_color : str = '#000000'_, _emissive_intensity : float = 0.0_, _metalness : float = 0.0_, _roughness : float = 1.0_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `MeshMaterial`

Represents a standard mesh material.

This material is a standard physically-based rendering (PBR) material. This material is ideal for most use cases.

Parameters:
    

  * **color** (_"#808080"_) â the color of the material

  * **emissive_color** (_"#000000"_) â the emissive color of the material. This is the color emitted by the material itself independent of the light

  * **emissive_intensity** (_0.0_) â the intensity of the emissive color

  * **metalness** (_0.0_) â the metalness of the material

  * **roughness** (_1.0_) â the roughness of the material

  * **wireframe** (_False_) â whether to render the mesh as a wireframe

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Attributes:**

`color` |   
---|---  
`opacity` |   
`wireframe` |   
`emissive_color` |   
`emissive_intensity` |   
`metalness` |   
`roughness` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property color: str#
    

property opacity: float#
    

property wireframe: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

property emissive_color: str#
    

property emissive_intensity: float#
    

property metalness: float#
    

property roughness: float#
    

as_dict()#
    

class fiftyone.core.threed.material_3d.MeshLambertMaterial(_color : str = '#808080'_, _emissive_color : str = '#000000'_, _emissive_intensity : float = 0.0_, _reflectivity : float = 1.0_, _refraction_ratio : float = 0.98_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `MeshMaterial`

Represents a Lambert mesh material.

This material only takes into account diffuse reflections, and ignores specular reflection. This is ideal for materials that reflect light evenly without a glossy or shiny appearance, such as unpolished surfaces.

Parameters:
    

  * **color** (_"#808080"_) â the color of the material

  * **emissive_color** (_"#000000"_) â the emissive color of the material. This is the color emitted by the material itself independent of the light

  * **emissive_intensity** (_0.0_) â the intensity of the emissive color

  * **reflectivity** (_1.0_) â the reflectivity of the material

  * **refraction_ratio** (_0.98_) â the refraction ratio (IOR) of the material

  * **wireframe** (_False_) â whether to render the mesh as a wireframe

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Attributes:**

`opacity` |   
---|---  
`wireframe` |   
`color` |   
`emissive_color` |   
`emissive_intensity` |   
`reflectivity` |   
`refraction_ratio` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property opacity: float#
    

property wireframe: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

property color: str#
    

property emissive_color: str#
    

property emissive_intensity: float#
    

property reflectivity: float#
    

property refraction_ratio: float#
    

as_dict()#
    

class fiftyone.core.threed.material_3d.MeshPhongMaterial(_shininess : float = 30.0_, _specular_color : str = '#111111'_, _color : str = '#808080'_, _emissive_color : str = '#000000'_, _emissive_intensity : float = 0.0_, _reflectivity : float = 1.0_, _refraction_ratio : float = 0.98_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `MeshLambertMaterial`

Represents a Phong mesh material.

This material takes into account specular reflection. This is ideal for materials that reflect light with a glossy or shiny appearance, such as polished surfaces.

Parameters:
    

  * **shininess** (_30.0_) â the shininess of the material

  * **specular_color** (_"#111111"_) â the specular color of the material

  * **color** (_"#808080"_) â the color of the material

  * **emissive_color** (_"#000000"_) â the emissive color of the material. This is the color emitted by the material itself independent of the light

  * **emissive_intensity** (_0.0_) â the intensity of the emissive color

  * **reflectivity** (_1.0_) â the reflectivity of the material

  * **refraction_ratio** (_0.98_) â the refraction ratio (IOR) of the material

  * **wireframe** (_False_) â whether to render the mesh as a wireframe

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Attributes:**

`color` |   
---|---  
`emissive_color` |   
`emissive_intensity` |   
`opacity` |   
`reflectivity` |   
`refraction_ratio` |   
`wireframe` |   
`shininess` |   
`specular_color` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property color: str#
    

property emissive_color: str#
    

property emissive_intensity: float#
    

property opacity: float#
    

property reflectivity: float#
    

property refraction_ratio: float#
    

property wireframe: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

property shininess: float#
    

property specular_color: str#
    

as_dict()#
    

class fiftyone.core.threed.material_3d.MeshDepthMaterial(_wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: `MeshMaterial`

Represents a depth mesh material.

This material is used for drawing geometry by depth, where depth is based off of the camera near and far plane. White is nearest, black is farthest.

Parameters:
    

  * **wireframe** (_False_) â whether to render the mesh as a wireframe

  * **opacity** (_1.0_) â the opacity of the material, in the range `[0, 1]`




**Methods:**

`as_dict`() |   
---|---  
  
**Attributes:**

`opacity` |   
---|---  
`wireframe` |   
  
as_dict()#
    

property opacity: float#
    

property wireframe: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
