---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.html
---

# fiftyone.core.threed#

  * [fiftyone.core.threed.camera](api__fiftyone.core.threed.camera.md)
    * [`PerspectiveCamera`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera)
      * [`PerspectiveCamera.position`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.position)
      * [`PerspectiveCamera.look_at`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.look_at)
      * [`PerspectiveCamera.up`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.up)
      * [`PerspectiveCamera.aspect`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.aspect)
      * [`PerspectiveCamera.fov`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.fov)
      * [`PerspectiveCamera.near`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.near)
      * [`PerspectiveCamera.far`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.far)
      * [`PerspectiveCamera.as_dict()`](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera.as_dict)
  * [fiftyone.core.threed.lights](api__fiftyone.core.threed.lights.md)
    * [`Light`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light)
      * [`Light.add()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.add)
      * [`Light.as_dict()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.as_dict)
      * [`Light.clear()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.clear)
      * [`Light.find_and_execute()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.find_and_execute)
      * [`Light.local_transform_matrix`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.local_transform_matrix)
      * [`Light.position`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.position)
      * [`Light.quaternion`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.quaternion)
      * [`Light.remove()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.remove)
      * [`Light.remove_by_name()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.remove_by_name)
      * [`Light.remove_by_uuid()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.remove_by_uuid)
      * [`Light.rotation`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.rotation)
      * [`Light.scale`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.scale)
      * [`Light.traverse()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.traverse)
      * [`Light.uuid`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light.uuid)
    * [`AmbientLight`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight)
      * [`AmbientLight.add()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.add)
      * [`AmbientLight.as_dict()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.as_dict)
      * [`AmbientLight.clear()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.clear)
      * [`AmbientLight.find_and_execute()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.find_and_execute)
      * [`AmbientLight.local_transform_matrix`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.local_transform_matrix)
      * [`AmbientLight.position`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.position)
      * [`AmbientLight.quaternion`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.quaternion)
      * [`AmbientLight.remove()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.remove)
      * [`AmbientLight.remove_by_name()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.remove_by_name)
      * [`AmbientLight.remove_by_uuid()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.remove_by_uuid)
      * [`AmbientLight.rotation`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.rotation)
      * [`AmbientLight.scale`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.scale)
      * [`AmbientLight.traverse()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.traverse)
      * [`AmbientLight.uuid`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.AmbientLight.uuid)
    * [`DirectionalLight`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight)
      * [`DirectionalLight.target`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.target)
      * [`DirectionalLight.add()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.add)
      * [`DirectionalLight.as_dict()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.as_dict)
      * [`DirectionalLight.clear()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.clear)
      * [`DirectionalLight.find_and_execute()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.find_and_execute)
      * [`DirectionalLight.local_transform_matrix`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.local_transform_matrix)
      * [`DirectionalLight.position`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.position)
      * [`DirectionalLight.quaternion`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.quaternion)
      * [`DirectionalLight.remove()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.remove)
      * [`DirectionalLight.remove_by_name()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.remove_by_name)
      * [`DirectionalLight.remove_by_uuid()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.remove_by_uuid)
      * [`DirectionalLight.rotation`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.rotation)
      * [`DirectionalLight.scale`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.scale)
      * [`DirectionalLight.traverse()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.traverse)
      * [`DirectionalLight.uuid`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.DirectionalLight.uuid)
    * [`PointLight`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight)
      * [`PointLight.add()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.add)
      * [`PointLight.as_dict()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.as_dict)
      * [`PointLight.clear()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.clear)
      * [`PointLight.find_and_execute()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.find_and_execute)
      * [`PointLight.local_transform_matrix`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.local_transform_matrix)
      * [`PointLight.position`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.position)
      * [`PointLight.quaternion`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.quaternion)
      * [`PointLight.remove()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.remove)
      * [`PointLight.remove_by_name()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.remove_by_name)
      * [`PointLight.remove_by_uuid()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.remove_by_uuid)
      * [`PointLight.rotation`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.rotation)
      * [`PointLight.scale`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.scale)
      * [`PointLight.traverse()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.traverse)
      * [`PointLight.uuid`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.PointLight.uuid)
    * [`SpotLight`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight)
      * [`SpotLight.add()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.add)
      * [`SpotLight.as_dict()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.as_dict)
      * [`SpotLight.clear()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.clear)
      * [`SpotLight.find_and_execute()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.find_and_execute)
      * [`SpotLight.local_transform_matrix`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.local_transform_matrix)
      * [`SpotLight.position`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.position)
      * [`SpotLight.quaternion`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.quaternion)
      * [`SpotLight.remove()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.remove)
      * [`SpotLight.remove_by_name()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.remove_by_name)
      * [`SpotLight.remove_by_uuid()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.remove_by_uuid)
      * [`SpotLight.rotation`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.rotation)
      * [`SpotLight.scale`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.scale)
      * [`SpotLight.traverse()`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.traverse)
      * [`SpotLight.uuid`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.SpotLight.uuid)
  * [fiftyone.core.threed.material_3d](api__fiftyone.core.threed.material_3d.md)
    * [`Material3D`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.Material3D)
      * [`Material3D.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.Material3D.opacity)
      * [`Material3D.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.Material3D.as_dict)
    * [`PointCloudMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial)
      * [`PointCloudMaterial.shading_mode`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial.shading_mode)
      * [`PointCloudMaterial.custom_color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial.custom_color)
      * [`PointCloudMaterial.point_size`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial.point_size)
      * [`PointCloudMaterial.attenuate_by_distance`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial.attenuate_by_distance)
      * [`PointCloudMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial.as_dict)
      * [`PointCloudMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial.opacity)
    * [`MeshMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial)
      * [`MeshMaterial.wireframe`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial.wireframe)
      * [`MeshMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial.as_dict)
      * [`MeshMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial.opacity)
    * [`MeshBasicMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshBasicMaterial)
      * [`MeshBasicMaterial.color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshBasicMaterial.color)
      * [`MeshBasicMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshBasicMaterial.as_dict)
      * [`MeshBasicMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshBasicMaterial.opacity)
      * [`MeshBasicMaterial.wireframe`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshBasicMaterial.wireframe)
    * [`MeshStandardMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial)
      * [`MeshStandardMaterial.color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.color)
      * [`MeshStandardMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.opacity)
      * [`MeshStandardMaterial.wireframe`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.wireframe)
      * [`MeshStandardMaterial.emissive_color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.emissive_color)
      * [`MeshStandardMaterial.emissive_intensity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.emissive_intensity)
      * [`MeshStandardMaterial.metalness`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.metalness)
      * [`MeshStandardMaterial.roughness`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.roughness)
      * [`MeshStandardMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshStandardMaterial.as_dict)
    * [`MeshLambertMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial)
      * [`MeshLambertMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.opacity)
      * [`MeshLambertMaterial.wireframe`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.wireframe)
      * [`MeshLambertMaterial.color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.color)
      * [`MeshLambertMaterial.emissive_color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.emissive_color)
      * [`MeshLambertMaterial.emissive_intensity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.emissive_intensity)
      * [`MeshLambertMaterial.reflectivity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.reflectivity)
      * [`MeshLambertMaterial.refraction_ratio`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.refraction_ratio)
      * [`MeshLambertMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial.as_dict)
    * [`MeshPhongMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial)
      * [`MeshPhongMaterial.color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.color)
      * [`MeshPhongMaterial.emissive_color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.emissive_color)
      * [`MeshPhongMaterial.emissive_intensity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.emissive_intensity)
      * [`MeshPhongMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.opacity)
      * [`MeshPhongMaterial.reflectivity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.reflectivity)
      * [`MeshPhongMaterial.refraction_ratio`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.refraction_ratio)
      * [`MeshPhongMaterial.wireframe`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.wireframe)
      * [`MeshPhongMaterial.shininess`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.shininess)
      * [`MeshPhongMaterial.specular_color`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.specular_color)
      * [`MeshPhongMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshPhongMaterial.as_dict)
    * [`MeshDepthMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshDepthMaterial)
      * [`MeshDepthMaterial.as_dict()`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshDepthMaterial.as_dict)
      * [`MeshDepthMaterial.opacity`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshDepthMaterial.opacity)
      * [`MeshDepthMaterial.wireframe`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshDepthMaterial.wireframe)
  * [fiftyone.core.threed.mesh](api__fiftyone.core.threed.mesh.md)
    * [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh)
      * [`Mesh.set_default_material()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.set_default_material)
      * [`Mesh.add()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.add)
      * [`Mesh.as_dict()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.as_dict)
      * [`Mesh.clear()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.clear)
      * [`Mesh.find_and_execute()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.find_and_execute)
      * [`Mesh.local_transform_matrix`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.local_transform_matrix)
      * [`Mesh.position`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.position)
      * [`Mesh.quaternion`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.quaternion)
      * [`Mesh.remove()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.remove)
      * [`Mesh.remove_by_name()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.remove_by_name)
      * [`Mesh.remove_by_uuid()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.remove_by_uuid)
      * [`Mesh.rotation`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.rotation)
      * [`Mesh.scale`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.scale)
      * [`Mesh.traverse()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.traverse)
      * [`Mesh.uuid`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh.uuid)
    * [`ObjMesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh)
      * [`ObjMesh.add()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.add)
      * [`ObjMesh.as_dict()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.as_dict)
      * [`ObjMesh.clear()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.clear)
      * [`ObjMesh.find_and_execute()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.find_and_execute)
      * [`ObjMesh.local_transform_matrix`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.local_transform_matrix)
      * [`ObjMesh.position`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.position)
      * [`ObjMesh.quaternion`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.quaternion)
      * [`ObjMesh.remove()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.remove)
      * [`ObjMesh.remove_by_name()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.remove_by_name)
      * [`ObjMesh.remove_by_uuid()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.remove_by_uuid)
      * [`ObjMesh.rotation`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.rotation)
      * [`ObjMesh.scale`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.scale)
      * [`ObjMesh.set_default_material()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.set_default_material)
      * [`ObjMesh.traverse()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.traverse)
      * [`ObjMesh.uuid`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.ObjMesh.uuid)
    * [`FbxMesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh)
      * [`FbxMesh.add()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.add)
      * [`FbxMesh.as_dict()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.as_dict)
      * [`FbxMesh.clear()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.clear)
      * [`FbxMesh.find_and_execute()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.find_and_execute)
      * [`FbxMesh.local_transform_matrix`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.local_transform_matrix)
      * [`FbxMesh.position`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.position)
      * [`FbxMesh.quaternion`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.quaternion)
      * [`FbxMesh.remove()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.remove)
      * [`FbxMesh.remove_by_name()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.remove_by_name)
      * [`FbxMesh.remove_by_uuid()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.remove_by_uuid)
      * [`FbxMesh.rotation`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.rotation)
      * [`FbxMesh.scale`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.scale)
      * [`FbxMesh.set_default_material()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.set_default_material)
      * [`FbxMesh.traverse()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.traverse)
      * [`FbxMesh.uuid`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.FbxMesh.uuid)
    * [`GltfMesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh)
      * [`GltfMesh.add()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.add)
      * [`GltfMesh.as_dict()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.as_dict)
      * [`GltfMesh.clear()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.clear)
      * [`GltfMesh.find_and_execute()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.find_and_execute)
      * [`GltfMesh.local_transform_matrix`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.local_transform_matrix)
      * [`GltfMesh.position`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.position)
      * [`GltfMesh.quaternion`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.quaternion)
      * [`GltfMesh.remove()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.remove)
      * [`GltfMesh.remove_by_name()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.remove_by_name)
      * [`GltfMesh.remove_by_uuid()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.remove_by_uuid)
      * [`GltfMesh.rotation`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.rotation)
      * [`GltfMesh.scale`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.scale)
      * [`GltfMesh.set_default_material()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.set_default_material)
      * [`GltfMesh.traverse()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.traverse)
      * [`GltfMesh.uuid`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.GltfMesh.uuid)
    * [`PlyMesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh)
      * [`PlyMesh.add()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.add)
      * [`PlyMesh.as_dict()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.as_dict)
      * [`PlyMesh.clear()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.clear)
      * [`PlyMesh.find_and_execute()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.find_and_execute)
      * [`PlyMesh.local_transform_matrix`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.local_transform_matrix)
      * [`PlyMesh.position`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.position)
      * [`PlyMesh.quaternion`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.quaternion)
      * [`PlyMesh.remove()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.remove)
      * [`PlyMesh.remove_by_name()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.remove_by_name)
      * [`PlyMesh.remove_by_uuid()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.remove_by_uuid)
      * [`PlyMesh.rotation`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.rotation)
      * [`PlyMesh.scale`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.scale)
      * [`PlyMesh.set_default_material()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.set_default_material)
      * [`PlyMesh.traverse()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.traverse)
      * [`PlyMesh.uuid`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.PlyMesh.uuid)
    * [`StlMesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh)
      * [`StlMesh.add()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.add)
      * [`StlMesh.as_dict()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.as_dict)
      * [`StlMesh.clear()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.clear)
      * [`StlMesh.find_and_execute()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.find_and_execute)
      * [`StlMesh.local_transform_matrix`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.local_transform_matrix)
      * [`StlMesh.position`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.position)
      * [`StlMesh.quaternion`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.quaternion)
      * [`StlMesh.remove()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.remove)
      * [`StlMesh.remove_by_name()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.remove_by_name)
      * [`StlMesh.remove_by_uuid()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.remove_by_uuid)
      * [`StlMesh.rotation`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.rotation)
      * [`StlMesh.scale`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.scale)
      * [`StlMesh.set_default_material()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.set_default_material)
      * [`StlMesh.traverse()`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.traverse)
      * [`StlMesh.uuid`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.StlMesh.uuid)
  * [fiftyone.core.threed.object_3d](api__fiftyone.core.threed.object_3d.md)
    * [`Object3D`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D)
      * [`Object3D.uuid`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.uuid)
      * [`Object3D.position`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.position)
      * [`Object3D.rotation`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.rotation)
      * [`Object3D.quaternion`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.quaternion)
      * [`Object3D.scale`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.scale)
      * [`Object3D.local_transform_matrix`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.local_transform_matrix)
      * [`Object3D.add()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.add)
      * [`Object3D.clear()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.clear)
      * [`Object3D.find_and_execute()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.find_and_execute)
      * [`Object3D.remove()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.remove)
      * [`Object3D.remove_by_name()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.remove_by_name)
      * [`Object3D.remove_by_uuid()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.remove_by_uuid)
      * [`Object3D.traverse()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.traverse)
      * [`Object3D.as_dict()`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D.as_dict)
  * [fiftyone.core.threed.pointcloud](api__fiftyone.core.threed.pointcloud.md)
    * [`PointCloud`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud)
      * [`PointCloud.set_default_material()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.set_default_material)
      * [`PointCloud.add()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.add)
      * [`PointCloud.as_dict()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.as_dict)
      * [`PointCloud.clear()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.clear)
      * [`PointCloud.find_and_execute()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.find_and_execute)
      * [`PointCloud.local_transform_matrix`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.local_transform_matrix)
      * [`PointCloud.position`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.position)
      * [`PointCloud.quaternion`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.quaternion)
      * [`PointCloud.remove()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.remove)
      * [`PointCloud.remove_by_name()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.remove_by_name)
      * [`PointCloud.remove_by_uuid()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.remove_by_uuid)
      * [`PointCloud.rotation`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.rotation)
      * [`PointCloud.scale`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.scale)
      * [`PointCloud.traverse()`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.traverse)
      * [`PointCloud.uuid`](api__fiftyone.core.threed.pointcloud.md#fiftyone.core.threed.pointcloud.PointCloud.uuid)
  * [fiftyone.core.threed.scene_3d](api__fiftyone.core.threed.scene_3d.md)
    * [`SceneBackground`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground)
      * [`SceneBackground.color`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground.color)
      * [`SceneBackground.image`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground.image)
      * [`SceneBackground.cube`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground.cube)
      * [`SceneBackground.intensity`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground.intensity)
      * [`SceneBackground.as_dict()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground.as_dict)
    * [`Scene`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene)
      * [`Scene.copy()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.copy)
      * [`Scene.write()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.write)
      * [`Scene.add()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.add)
      * [`Scene.as_dict()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.as_dict)
      * [`Scene.clear()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.clear)
      * [`Scene.find_and_execute()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.find_and_execute)
      * [`Scene.local_transform_matrix`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.local_transform_matrix)
      * [`Scene.position`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.position)
      * [`Scene.quaternion`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.quaternion)
      * [`Scene.remove()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.remove)
      * [`Scene.remove_by_name()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.remove_by_name)
      * [`Scene.remove_by_uuid()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.remove_by_uuid)
      * [`Scene.rotation`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.rotation)
      * [`Scene.scale`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.scale)
      * [`Scene.traverse()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.traverse)
      * [`Scene.uuid`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.uuid)
      * [`Scene.update_asset_paths()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.update_asset_paths)
      * [`Scene.get_scene_summary()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.get_scene_summary)
      * [`Scene.get_asset_paths()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.get_asset_paths)
      * [`Scene.from_fo3d()`](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.Scene.from_fo3d)
  * [fiftyone.core.threed.shape_3d](api__fiftyone.core.threed.shape_3d.md)
    * [`Shape3D`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D)
      * [`Shape3D.add()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.add)
      * [`Shape3D.as_dict()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.as_dict)
      * [`Shape3D.clear()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.clear)
      * [`Shape3D.find_and_execute()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.find_and_execute)
      * [`Shape3D.local_transform_matrix`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.local_transform_matrix)
      * [`Shape3D.position`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.position)
      * [`Shape3D.quaternion`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.quaternion)
      * [`Shape3D.remove()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.remove)
      * [`Shape3D.remove_by_name()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.remove_by_name)
      * [`Shape3D.remove_by_uuid()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.remove_by_uuid)
      * [`Shape3D.rotation`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.rotation)
      * [`Shape3D.scale`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.scale)
      * [`Shape3D.set_default_material()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.set_default_material)
      * [`Shape3D.traverse()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.traverse)
      * [`Shape3D.uuid`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D.uuid)
    * [`BoxGeometry`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry)
      * [`BoxGeometry.add()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.add)
      * [`BoxGeometry.as_dict()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.as_dict)
      * [`BoxGeometry.clear()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.clear)
      * [`BoxGeometry.find_and_execute()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.find_and_execute)
      * [`BoxGeometry.local_transform_matrix`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.local_transform_matrix)
      * [`BoxGeometry.position`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.position)
      * [`BoxGeometry.quaternion`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.quaternion)
      * [`BoxGeometry.remove()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.remove)
      * [`BoxGeometry.remove_by_name()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.remove_by_name)
      * [`BoxGeometry.remove_by_uuid()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.remove_by_uuid)
      * [`BoxGeometry.rotation`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.rotation)
      * [`BoxGeometry.scale`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.scale)
      * [`BoxGeometry.set_default_material()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.set_default_material)
      * [`BoxGeometry.traverse()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.traverse)
      * [`BoxGeometry.uuid`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.BoxGeometry.uuid)
    * [`CylinderGeometry`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry)
      * [`CylinderGeometry.add()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.add)
      * [`CylinderGeometry.as_dict()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.as_dict)
      * [`CylinderGeometry.clear()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.clear)
      * [`CylinderGeometry.find_and_execute()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.find_and_execute)
      * [`CylinderGeometry.local_transform_matrix`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.local_transform_matrix)
      * [`CylinderGeometry.position`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.position)
      * [`CylinderGeometry.quaternion`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.quaternion)
      * [`CylinderGeometry.remove()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.remove)
      * [`CylinderGeometry.remove_by_name()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.remove_by_name)
      * [`CylinderGeometry.remove_by_uuid()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.remove_by_uuid)
      * [`CylinderGeometry.rotation`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.rotation)
      * [`CylinderGeometry.scale`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.scale)
      * [`CylinderGeometry.set_default_material()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.set_default_material)
      * [`CylinderGeometry.traverse()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.traverse)
      * [`CylinderGeometry.uuid`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.CylinderGeometry.uuid)
    * [`SphereGeometry`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry)
      * [`SphereGeometry.add()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.add)
      * [`SphereGeometry.as_dict()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.as_dict)
      * [`SphereGeometry.clear()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.clear)
      * [`SphereGeometry.find_and_execute()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.find_and_execute)
      * [`SphereGeometry.local_transform_matrix`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.local_transform_matrix)
      * [`SphereGeometry.position`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.position)
      * [`SphereGeometry.quaternion`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.quaternion)
      * [`SphereGeometry.remove()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.remove)
      * [`SphereGeometry.remove_by_name()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.remove_by_name)
      * [`SphereGeometry.remove_by_uuid()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.remove_by_uuid)
      * [`SphereGeometry.rotation`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.rotation)
      * [`SphereGeometry.scale`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.scale)
      * [`SphereGeometry.set_default_material()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.set_default_material)
      * [`SphereGeometry.traverse()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.traverse)
      * [`SphereGeometry.uuid`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.SphereGeometry.uuid)
    * [`PlaneGeometry`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry)
      * [`PlaneGeometry.add()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.add)
      * [`PlaneGeometry.as_dict()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.as_dict)
      * [`PlaneGeometry.clear()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.clear)
      * [`PlaneGeometry.find_and_execute()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.find_and_execute)
      * [`PlaneGeometry.local_transform_matrix`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.local_transform_matrix)
      * [`PlaneGeometry.position`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.position)
      * [`PlaneGeometry.quaternion`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.quaternion)
      * [`PlaneGeometry.remove()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.remove)
      * [`PlaneGeometry.remove_by_name()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.remove_by_name)
      * [`PlaneGeometry.remove_by_uuid()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.remove_by_uuid)
      * [`PlaneGeometry.rotation`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.rotation)
      * [`PlaneGeometry.scale`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.scale)
      * [`PlaneGeometry.set_default_material()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.set_default_material)
      * [`PlaneGeometry.traverse()`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.traverse)
      * [`PlaneGeometry.uuid`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.PlaneGeometry.uuid)
  * [fiftyone.core.threed.transformation](api__fiftyone.core.threed.transformation.md)
    * [`Vector3`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3)
      * [`Vector3.x`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3.x)
      * [`Vector3.y`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3.y)
      * [`Vector3.z`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3.z)
      * [`Vector3.to_arr()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3.to_arr)
    * [`Euler`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler)
      * [`Euler.degrees`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.degrees)
      * [`Euler.sequence`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.sequence)
      * [`Euler.to_quaternion()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.to_quaternion)
      * [`Euler.to_arr()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.to_arr)
      * [`Euler.x`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.x)
      * [`Euler.y`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.y)
      * [`Euler.z`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Euler.z)
    * [`Quaternion`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion)
      * [`Quaternion.x`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion.x)
      * [`Quaternion.y`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion.y)
      * [`Quaternion.z`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion.z)
      * [`Quaternion.w`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion.w)
      * [`Quaternion.to_euler()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion.to_euler)
      * [`Quaternion.to_arr()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion.to_arr)
    * [`normalize_to_vec3()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.normalize_to_vec3)
    * [`coerce_to_vec3()`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.coerce_to_vec3)
  * [fiftyone.core.threed.utils](api__fiftyone.core.threed.utils.md)
    * [`camel_to_snake()`](api__fiftyone.core.threed.utils.md#fiftyone.core.threed.utils.camel_to_snake)
    * [`convert_keys_to_snake_case()`](api__fiftyone.core.threed.utils.md#fiftyone.core.threed.utils.convert_keys_to_snake_case)
  * [fiftyone.core.threed.validators](api__fiftyone.core.threed.validators.md)
    * [`validate_bool()`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.validate_bool)
    * [`validate_choice()`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.validate_choice)
    * [`validate_color()`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.validate_color)
    * [`validate_float()`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.validate_float)
    * [`validate_list()`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.validate_list)
    * [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass)



## Module contents#

3D definitions for FiftyOne.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`AmbientLight`([name,Â intensity,Â color,Â ...]) | Represents an ambient light.  
---|---  
`DirectionalLight`([name,Â target,Â color,Â ...]) | Represents a directional light.  
`PointLight`([name,Â distance,Â decay,Â color,Â ...]) | Represents a point light.  
`SpotLight`([name,Â target,Â distance,Â decay,Â ...]) | Represents a spot light.  
`MeshBasicMaterial`([color,Â wireframe,Â opacity]) | Represents a basic mesh material.  
`MeshDepthMaterial`([wireframe,Â opacity]) | Represents a depth mesh material.  
`MeshLambertMaterial`([color,Â emissive_color,Â ...]) | Represents a Lambert mesh material.  
`MeshStandardMaterial`([color,Â ...]) | Represents a standard mesh material.  
`MeshPhongMaterial`([shininess,Â ...]) | Represents a Phong mesh material.  
`PointCloudMaterial`([shading_mode,Â ...]) | Represents a point cloud material.  
`FbxMesh`(name,Â fbx_path[,Â default_material,Â ...]) | Represents an FBX mesh.  
`GltfMesh`(name,Â gltf_path[,Â ...]) | Represents a gLTF mesh.  
`ObjMesh`(name,Â obj_path[,Â mtl_path,Â ...]) | Represents an OBJ mesh.  
`PlyMesh`(name,Â ply_path[,Â is_point_cloud,Â ...]) | Represents a PLY mesh.  
`StlMesh`(name,Â stl_path[,Â default_material,Â ...]) | Represents an STL mesh.  
`Object3D`(name[,Â visible,Â position,Â scale,Â ...]) | The base class for all 3D objects in the scene.  
`Quaternion`([x,Â y,Â z,Â w]) | Represents a quaternion.  
`PointCloud`(name,Â pcd_path[,Â material,Â ...]) | Represents a point cloud.  
`Counter`([iterable]) | Dict subclass for counting hashable items.  
`PerspectiveCamera`([position,Â look_at,Â up,Â ...]) | Represents the configuration of a 3D perspective camera.  
`Light`([name,Â color,Â intensity,Â visible,Â ...]) | Base class for 3D lights.  
`Shape3D`(name[,Â material,Â visible,Â position,Â ...]) | Represents an abstract 3D shape.  
`BaseValidatedDataClass`() |   
`SceneBackground`([color,Â image,Â cube,Â intensity]) | Represents the background of the scene.  
`Scene`([camera,Â lights,Â background]) | Represents a scene graph which contains a hierarchy of 3D objects.  
`BoxGeometry`(name[,Â width,Â height,Â depth,Â ...]) | Represents a 3D box.  
`PlaneGeometry`(name[,Â width,Â height,Â ...]) | Represents a 3D plane.  
`SphereGeometry`(name[,Â radius,Â ...]) | Represents a 3D sphere.  
`CylinderGeometry`(name[,Â radius_top,Â ...]) | Represents a 3D cylinder.  
`Euler`([x,Â y,Â z,Â degrees,Â sequence]) | Represents intrinsic rotations about the object's own principal axes.  
`Vector3`([x,Â y,Â z]) | Represents a three-dimensional vector.  
  
**Functions:**

`convert_keys_to_snake_case`(d) | Convert all keys in a dictionary from camelCase to snake_case.  
---|---  
`validate_color`(v[,Â nullable]) |   
`validate_list`(v[,Â length,Â nullable]) |   
  
class fiftyone.core.threed.AmbientLight(_name : str = 'AmbientLight'_, _intensity : float = 0.1_, _color : str = '#ffffff'_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Light`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light "fiftyone.core.threed.lights.Light")

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

class fiftyone.core.threed.DirectionalLight(_name : str = 'DirectionalLight'_, _target : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array = Vector3(x=0.0, y=0.0, z=0.0)_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Light`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light "fiftyone.core.threed.lights.Light")

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

class fiftyone.core.threed.PointLight(_name : str = 'PointLight'_, _distance : float = 0.0_, _decay : float = 2.0_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Light`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light "fiftyone.core.threed.lights.Light")

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

class fiftyone.core.threed.SpotLight(_name : str = 'SpotLight'_, _target : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array = None_, _distance : float = 0.0_, _decay : float = 2.0_, _angle : float = 1.0471975511965976_, _penumbra : float = 0.0_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Light`](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light "fiftyone.core.threed.lights.Light")

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

class fiftyone.core.threed.MeshBasicMaterial(_color : str = '#808080'_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: [`MeshMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")

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
    

class fiftyone.core.threed.MeshDepthMaterial(_wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: [`MeshMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")

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
    

class fiftyone.core.threed.MeshLambertMaterial(_color : str = '#808080'_, _emissive_color : str = '#000000'_, _emissive_intensity : float = 0.0_, _reflectivity : float = 1.0_, _refraction_ratio : float = 0.98_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: [`MeshMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")

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
    

class fiftyone.core.threed.MeshStandardMaterial(_color : str = '#808080'_, _emissive_color : str = '#000000'_, _emissive_intensity : float = 0.0_, _metalness : float = 0.0_, _roughness : float = 1.0_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: [`MeshMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial")

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
    

class fiftyone.core.threed.MeshPhongMaterial(_shininess : float = 30.0_, _specular_color : str = '#111111'_, _color : str = '#808080'_, _emissive_color : str = '#000000'_, _emissive_intensity : float = 0.0_, _reflectivity : float = 1.0_, _refraction_ratio : float = 0.98_, _wireframe : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: [`MeshLambertMaterial`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshLambertMaterial "fiftyone.core.threed.material_3d.MeshLambertMaterial")

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
    

class fiftyone.core.threed.PointCloudMaterial(_shading_mode : Literal['height', 'intensity', 'rgb', 'custom'] = 'height'_, _custom_color : str = '#ffffff'_, _point_size : float = 1.0_, _attenuate_by_distance : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _opacity : float = 1.0_)#
    

Bases: [`Material3D`](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.Material3D "fiftyone.core.threed.material_3d.Material3D")

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
    

class fiftyone.core.threed.FbxMesh(_name : str_, _fbx_path : str_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents an FBX mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **fbx_path** (_str_) â the path to the `.fbx` file. Path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh if FBX file does not contain material information. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.GltfMesh(_name : str_, _gltf_path : str_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents a gLTF mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **gltf_path** (_str_) â the path to the `.gltf` or `.glb` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh if gLTF file does not contain material information. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.ObjMesh(_name : str_, _obj_path : str_, _mtl_path : str | None = None_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents an OBJ mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **obj_path** (_str_) â the path to the `.obj` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **mtl_path** (_str_ _,__optional_) â the path to the `.mtl` file. Defaults to `None`. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the mesh if `mtl_path` is not provided or if material in `mtl_path` is not found. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.PlyMesh(_name : str_, _ply_path : str_, _is_point_cloud : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _center_geometry : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents a PLY mesh. A PLY mesh can be a point cloud or a mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **ply_path** (_str_) â the path to the `.ply` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **is_point_cloud** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the PLY file is a point cloud. Defaults to `False`

  * **center_geometry** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to center the geometry. Defaults to `True`

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the mesh if PLY file does not contain vertex colors. Defaults to `fiftyone.core.threed.MeshStandardMaterial`. If the PLY file contains vertex colors, the material is ignored and vertex colors are used

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

class fiftyone.core.threed.StlMesh(_name : str_, _stl_path : str_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents an STL mesh.

Parameters:
    

  * **name** (_str_) â the name of the mesh

  * **stl_path** (_str_) â the path to the `.stl` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the mesh. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.Object3D(_name : str_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: `object`

The base class for all 3D objects in the scene.

Parameters:
    

  * **name** â the name of the object

  * **visible** (_True_) â default visibility of the object in the scene

  * **position** (_None_) â the position of the object in object space

  * **quaternion** (_None_) â the quaternion of the object in object space

  * **scale** (_None_) â the scale of the object in object space




**Attributes:**

`uuid` | The unique ID of the object.  
---|---  
`position` | The position of the object in object space.  
`rotation` | The rotation of the object in object space.  
`quaternion` | The quaternion of the object in object space.  
`scale` | The scale of the object in object space.  
`local_transform_matrix` | The local transform matrix of the object.  
  
**Methods:**

`add`(*objs) | Add one or more objects as children of this one.  
---|---  
`clear`() | Remove all children from this object.  
`find_and_execute`(node,Â predicate,Â on_match) | Recursively search the scene graph and execute an action on matching nodes.  
`remove`(*objs) | Remove one or more objects from the scene graph recursively.  
`remove_by_name`(name) | Remove all objects with the given name from the scene graph recursively.  
`remove_by_uuid`(target_uuid) | Remove the object with the given UUID from the scene graph recursively.  
`traverse`([include_self]) | Traverse the scene graph.  
`as_dict`() | Converts the object to a dict.  
  
property uuid#
    

The unique ID of the object.

property position#
    

The position of the object in object space.

property rotation#
    

The rotation of the object in object space.

property quaternion#
    

The quaternion of the object in object space.

property scale#
    

The scale of the object in object space.

property local_transform_matrix#
    

The local transform matrix of the object.

Setting this property also decomposes the matrix into its constituent position, quaternion, and scale components. However, decomposition of matrices with skew / shear components (non-uniform scaling) might have unexpected results.

add(_* objs: [Object3D](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")_) → None#
    

Add one or more objects as children of this one.

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




traverse(_include_self =True_)#
    

Traverse the scene graph.

as_dict()#
    

Converts the object to a dict.

class fiftyone.core.threed.Quaternion(_x : float = 0.0_, _y : float = 0.0_, _z : float = 0.0_, _w : float = 1.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents a quaternion.

**Attributes:**

`x` |   
---|---  
`y` |   
`z` |   
`w` |   
  
**Methods:**

`to_euler`([degrees,Â sequence]) | Converts the quaternion into euler angles.  
---|---  
`to_arr`() | Converts the quaternion to a numpy array.  
  
property x: float#
    

property y: float#
    

property z: float#
    

property w: float#
    

to_euler(_degrees =False_, _sequence ='XYZ'_)#
    

Converts the quaternion into euler angles.

to_arr()#
    

Converts the quaternion to a numpy array.

class fiftyone.core.threed.PointCloud(_name : str_, _pcd_path : str_, _material : [PointCloudMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.PointCloudMaterial "fiftyone.core.threed.material_3d.PointCloudMaterial") | None = None_, _center_geometry : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _flag_for_projection : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Object3D`](api__fiftyone.core.threed.object_3d.md#fiftyone.core.threed.object_3d.Object3D "fiftyone.core.threed.object_3d.Object3D")

Represents a point cloud.

Parameters:
    

  * **name** (_str_) â the name of the point cloud

  * **pcd_path** (_str_) â the path to the `.pcd` file. The path may be either absolute or relative to the directory containing the `.fo3d` file

  * **material** (`fiftyone.core.threed.PointCloudMaterial`, optional) â the material of the point cloud. If not specified, defaults to a new instance of `fiftyone.core.threed.PointCloudMaterial` with its default parameters

  * **center_geometry** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to center the geometry of the point cloud. Defaults to `False`

  * **flag_for_projection** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to flag the point cloud for usage in orthographic projection. Each `fiftyone.core.threed.Scene` can have at most one asset flagged for orthographic projection. Defaults to `False`. If multiple assets are flagged, the first one will be chosen

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
    

**material** (_PointCloudMaterial_) â The material to set as the default

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

class fiftyone.core.threed.Counter(_iterable =None_, _/_ , _** kwds_)#
    

Bases: `dict`

Dict subclass for counting hashable items. Sometimes called a bag or multiset. Elements are stored as dictionary keys and their counts are stored as dictionary values.
    
    
    >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
    
    
    
    >>> c.most_common(3)                # three most common elements
    [('a', 5), ('b', 4), ('c', 3)]
    >>> sorted(c)                       # list all unique elements
    ['a', 'b', 'c', 'd', 'e']
    >>> ''.join(sorted(c.elements()))   # list elements with repetitions
    'aaaaabbbbcccdde'
    >>> sum(c.values())                 # total of all counts
    15
    
    
    
    >>> c['a']                          # count of letter 'a'
    5
    >>> for elem in 'shazam':           # update counts from an iterable
    ...     c[elem] += 1                # by adding 1 to each element's count
    >>> c['a']                          # now there are seven 'a'
    7
    >>> del c['b']                      # remove all 'b'
    >>> c['b']                          # now there are zero 'b'
    0
    
    
    
    >>> d = Counter('simsalabim')       # make another counter
    >>> c.update(d)                     # add in the second counter
    >>> c['a']                          # now there are nine 'a'
    9
    
    
    
    >>> c.clear()                       # empty the counter
    >>> c
    Counter()
    

Note: If a count is set to zero or reduced to zero, it will remain in the counter until the entry is deleted or the counter is cleared:
    
    
    >>> c = Counter('aaabbc')
    >>> c['b'] -= 2                     # reduce the count of 'b' by two
    >>> c.most_common()                 # 'b' is still in, but its count is zero
    [('a', 3), ('c', 1), ('b', 0)]
    

**Methods:**

`total`() | Sum of the counts  
---|---  
`most_common`([n]) | List the n most common elements and their counts from the most common to the least.  
`elements`() | Iterator over elements repeating each as many times as its count.  
`fromkeys`(iterable[,Â v]) | Create a new dictionary with keys from iterable and values set to value.  
`update`([iterable]) | Like dict.update() but add counts instead of replacing them.  
`subtract`([iterable]) | Like dict.update() but subtracts counts instead of replacing them.  
`copy`() | Return a shallow copy.  
`clear`() |   
`get`(key[,Â default]) | Return the value for key if key is in the dictionary, else default.  
`items`() |   
`keys`() |   
`pop`(k[,d]) | If the key is not found, return the default if given; otherwise, raise a KeyError.  
`popitem`() | Remove and return a (key, value) pair as a 2-tuple.  
`setdefault`(key[,Â default]) | Insert key with a value of default if key is not in the dictionary.  
`values`() |   
  
total()#
    

Sum of the counts

most_common(_n =None_)#
    

List the n most common elements and their counts from the most common to the least. If n is None, then list all element counts.
    
    
    >>> Counter('abracadabra').most_common(3)
    [('a', 5), ('b', 2), ('r', 2)]
    

elements()#
    

Iterator over elements repeating each as many times as its count.
    
    
    >>> c = Counter('ABCABC')
    >>> sorted(c.elements())
    ['A', 'A', 'B', 'B', 'C', 'C']
    

# Knuthâs example for prime factors of 1836: 2**2 * 3**3 * 17**1 >>> import math >>> prime_factors = Counter({2: 2, 3: 3, 17: 1}) >>> math.prod(prime_factors.elements()) 1836

Note, if an elementâs count has been set to zero or is a negative number, elements() will ignore it.

classmethod fromkeys(_iterable_ , _v =None_)#
    

Create a new dictionary with keys from iterable and values set to value.

update(_iterable =None_, _/_ , _** kwds_)#
    

Like dict.update() but add counts instead of replacing them.

Source can be an iterable, a dictionary, or another Counter instance.
    
    
    >>> c = Counter('which')
    >>> c.update('witch')           # add elements from another iterable
    >>> d = Counter('watch')
    >>> c.update(d)                 # add elements from another counter
    >>> c['h']                      # four 'h' in which, witch, and watch
    4
    

subtract(_iterable =None_, _/_ , _** kwds_)#
    

Like dict.update() but subtracts counts instead of replacing them. Counts can be reduced below zero. Both the inputs and outputs are allowed to contain zero and negative counts.

Source can be an iterable, a dictionary, or another Counter instance.
    
    
    >>> c = Counter('which')
    >>> c.subtract('witch')             # subtract elements from another iterable
    >>> c.subtract(Counter('watch'))    # subtract elements from another counter
    >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
    0
    >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
    -1
    

copy()#
    

Return a shallow copy.

clear() → None. Remove all items from D.#
    

get(_key_ , _default =None_, _/_)#
    

Return the value for key if key is in the dictionary, else default.

items() → a set-like object providing a view on D's items#
    

keys() → a set-like object providing a view on D's keys#
    

pop(_k_[, _d_]) → v, remove specified key and return the corresponding value.#
    

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem()#
    

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault(_key_ , _default =None_, _/_)#
    

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

values() → an object providing a view on D's values#
    

class fiftyone.core.threed.PerspectiveCamera(_position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | None = None_, _look_at : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | None = None_, _up : Literal['X', 'Y', 'Z', '-X', '-Y', '-Z'] | None = None_, _aspect : float | None = None_, _fov : float = 50.0_, _near : float = 0.1_, _far : float = 2000.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents the configuration of a 3D perspective camera.

Parameters:
    

  * **position** (_None_) â the position of the camera. If `None`, the camera position is calculated based on the bounding box of the scene

  * **look_at** (_None_) â the point the camera is looking at. If `None`, the camera looks at the center of the scene

  * **up** (_None_) â the orthonormal axis that is considered up. Must be one of âXâ, âYâ, âZâ, â-Xâ, â-Yâ, or â-Zâ. If `None`, it will fallback to the global `up` as defined in 3D plugin settings. If that too is not defined, it will fallback to âZâ

  * **aspect** (_None_) â the aspect ratio of the camera. If `None`, the aspect ratio is calculated based on the width and height of the canvas

  * **fov** (_50_) â camera frustum vertical field of view in degrees. If `None`, the field of view is 50 degrees

  * **near** (_0.1_) â the near clipping plane of the camera

  * **far** (_2000_) â the far clipping plane of the camera




**Attributes:**

`position` |   
---|---  
`look_at` |   
`up` |   
`aspect` |   
`fov` |   
`near` |   
`far` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property position: [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3")#
    

property look_at: [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3")#
    

property up: str | None#
    

property aspect#
    

property fov: float#
    

property near: float#
    

property far: float#
    

as_dict() → dict#
    

class fiftyone.core.threed.Light(_name : str | None = None_, _color : str = '#ffffff'_, _intensity : float = 1.0_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

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

class fiftyone.core.threed.Shape3D(_name : str_, _material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Mesh`](api__fiftyone.core.threed.mesh.md#fiftyone.core.threed.mesh.Mesh "fiftyone.core.threed.mesh.Mesh")

Represents an abstract 3D shape.

Parameters:
    

  * **name** â the name of the mesh

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the shape mesh. Defaults to `fiftyone.core.threed.MeshStandardMaterial` if not provided

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

fiftyone.core.threed.convert_keys_to_snake_case(_d_)#
    

Convert all keys in a dictionary from camelCase to snake_case.

Parameters:
    

**d** â the dictionary

Returns:
    

a dictionary with snake case keys

class fiftyone.core.threed.BaseValidatedDataClass#
    

Bases: `object`

fiftyone.core.threed.validate_color(_v : str | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

fiftyone.core.threed.validate_list(_v : Any_, _length : int | None = None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")#
    

class fiftyone.core.threed.SceneBackground(_color : str | None = None_, _image : str | None = None_, _cube : List[str] | None = None_, _intensity : float | None = 1.0_)#
    

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
    

class fiftyone.core.threed.Scene(_camera : [PerspectiveCamera](api__fiftyone.core.threed.camera.md#fiftyone.core.threed.camera.PerspectiveCamera "fiftyone.core.threed.camera.PerspectiveCamera") | None = None_, _lights : List[[Light](api__fiftyone.core.threed.lights.md#fiftyone.core.threed.lights.Light "fiftyone.core.threed.lights.Light")] | None = None_, _background : [SceneBackground](api__fiftyone.core.threed.scene_3d.md#fiftyone.core.threed.scene_3d.SceneBackground "fiftyone.core.threed.scene_3d.SceneBackground") | None = None_)#
    

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
    

  * **camera** (_None_) â the default camera of the scene. If `None`, a default `fiftyone.core.threed.PerspectiveCamera` is created with reasonable defaults

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

class fiftyone.core.threed.BoxGeometry(_name : str_, _width : float = 1_, _height : float = 1_, _depth : float = 1_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Shape3D`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D "fiftyone.core.threed.shape_3d.Shape3D")

Represents a 3D box.

Parameters:
    

  * **name** (_str_) â name of the box

  * **width** (_float_) â the width of the box. Defaults to 1

  * **height** (_float_) â the height of the box. Defaults to 1

  * **depth** (_float_) â the depth of the box. Defaults to 1

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the box. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.PlaneGeometry(_name : str_, _width : float = 1_, _height : float = 1_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Shape3D`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D "fiftyone.core.threed.shape_3d.Shape3D")

Represents a 3D plane.

Parameters:
    

  * **name** (_str_) â name of the plane

  * **width** (_float_) â the width of the plane. Defaults to 1

  * **height** (_float_) â the height of the plane. Defaults to 1

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the plane. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.SphereGeometry(_name : str_, _radius : float = 1_, _width_segments : int = 32_, _height_segments : int = 16_, _phi_start : float = 0_, _phi_length : float = 6.283185307179586_, _theta_start : float = 0_, _theta_length : float = 3.141592653589793_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Shape3D`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D "fiftyone.core.threed.shape_3d.Shape3D")

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

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â the default material for the sphere. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.CylinderGeometry(_name : str_, _radius_top : float = 1_, _radius_bottom : float = 1_, _height : float = 1_, _radial_segments : int = 32_, _height_segments : int = 1_, _open_ended : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _theta_start : float = 0_, _theta_length : float = 6.283185307179586_, _default_material : [MeshMaterial](api__fiftyone.core.threed.material_3d.md#fiftyone.core.threed.material_3d.MeshMaterial "fiftyone.core.threed.material_3d.MeshMaterial") | None = None_, _visible =True_, _position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _scale : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | List[float] | Tuple[float] | array | None = None_, _quaternion : [Quaternion](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Quaternion "fiftyone.core.threed.transformation.Quaternion") | None = None_)#
    

Bases: [`Shape3D`](api__fiftyone.core.threed.shape_3d.md#fiftyone.core.threed.shape_3d.Shape3D "fiftyone.core.threed.shape_3d.Shape3D")

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

  * **material** (`fiftyone.core.threed.MeshMaterial`, optional) â default material for the cylinder. Defaults to `fiftyone.core.threed.MeshStandardMaterial`

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

class fiftyone.core.threed.Euler(_x : float = 0.0_, _y : float = 0.0_, _z : float = 0.0_, _degrees : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _sequence : Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'] = 'XYZ'_)#
    

Bases: [`Vector3`](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3")

Represents intrinsic rotations about the objectâs own principal axes.

**Attributes:**

`degrees` |   
---|---  
`sequence` |   
`x` |   
`y` |   
`z` |   
  
**Methods:**

`to_quaternion`() | Converts the euler angles to a quaternion.  
---|---  
`to_arr`() | Converts the vector to a numpy array.  
  
property degrees: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

property sequence: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']#
    

to_quaternion()#
    

Converts the euler angles to a quaternion.

to_arr()#
    

Converts the vector to a numpy array.

property x: float#
    

property y: float#
    

property z: float#
    

class fiftyone.core.threed.Vector3(_x : float = 0.0_, _y : float = 0.0_, _z : float = 0.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents a three-dimensional vector.

**Attributes:**

`x` |   
---|---  
`y` |   
`z` |   
  
**Methods:**

`to_arr`() | Converts the vector to a numpy array.  
---|---  
  
property x: float#
    

property y: float#
    

property z: float#
    

to_arr()#
    

Converts the vector to a numpy array.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
