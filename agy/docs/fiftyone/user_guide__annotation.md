---
source_url: https://docs.voxel51.com/user_guide/annotation.html
---

# In-App Annotation#

## Overview#

This guide will walk you through the basics of FiftyOneâs in-App annotation features.

Currently in-App annotation is designed for ad hoc, sample-by-sample metadata editing. The features and controls extend FiftyOneâs existing data visualization UI. Once you have samples loaded into a FiftyOne dataset, you can begin defining your Annotation Schema and labeling your data in the App.

* * *

## Basics#

### Supported Media and Label Types#

In-App annotation within FiftyOne supports datasets containing the following media and label types:

  * [media_type](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-media-type)

    * `image`

    * `3D`

  * [Labels](user_guide__basics.md#basics-labels)

    * `Classification`

    * `Detections`

    * `Instance segmentations`

    * `2D Polylines and Polygons`

    * `3D Polylines`

    * `3D Cuboids`




### Annotation UI: Sample Visualizer#

All in-App annotation controls now live in the [expanded view for samples](user_guide__app.md#app-sample-view). Open a sample in the expanded view, and find the new âAnnotateâ tab in the right sidebar.

![Annotate tab location](../_images/annotate_tab_grid.gif)

### Saving and Reverting Changes#

When you make changes to sample metadata with FiftyOneâs in-App annotation, your changes automatically save to the database. The auto-save functionality triggers either explicitly after an action (e.g., deleting a label) or after a short period of time (e.g., updating the spatial properties of a bounding box multiple times in succession), depending on the action.

You can tell whether your changes are saved or are in the process of being saved thanks to this indicator:

![Auto-save indicator](../_images/auto_save_indicator.png)

#### Undo/Redo#

![Undo/Redo buttons](../_images/undo_redo_buttons.png)

While editing metadata, you can undo and redo actions using the buttons in the upper-right corner of the âAnnotateâ panel, or via `Ctrl+`/`Cmd+z` and `Ctrl+`/`Cmd+y`. Your changes included in the undo stack are limited to your active annotation session, i.e., while the expanded view remains open.

* * *

## User Guide#

### Schema Import / Management#

To perform in-App annotation, your dataset must first have an âAnnotation Schemaâ. For a field, attribute, or value to be available in in-App annotation, it must be present in the Annotation Schema. Currently, you may only have one Annotation Schema per dataset, and your Annotation Schema applies across all samples and views on the dataset.

Warning

Only users with [âCan manageâ access](enterprise__roles_and_permissions.md#enterprise-can-manage) to a dataset may import and manage the Annotation Schema on that dataset.

![Create Annotation Schema button](../_images/create_annotation_schema.png)

When accessing the âAnnotateâ tab in the expanded view on a dataset for the first time, youâll see a button to create the Annotation Schema. By default, **no** [fields in the dataset schema](https://docs.voxel51.com/user_guide/using_datasets.html#using-fields) are included automatically in the Annotation Schema; youâll need to explicitly add fields, attributes, and values.

#### Supported Field Types#

FiftyOneâs in-App annotation supports two groups of field types: **label-type** fields (e.g., `Detections` or `Classification`) and non-label-type **primitive** fields (e.g., `StringField`s or `IntField`s). Your Annotation Schema can be a mix of fields within these groups. The parameters available for configuring fieldsâ schemas in your Annotation Schema will depend on the type of field (see: Annotation Schema Format).

#### Schema Manager#

![Schema Manager](../_images/schema_manager.png)

The âSchema Managerâ user interface defines the Annotation Schema for the dataset. The main page of the Schema Manager features two sections: âActive fieldsâ and âHidden fieldsâ.

âActive fieldsâ are fields included in your Annotation Schema.

âHidden fieldsâ are all fields not yet included in your Annotation Schema, but that can be activated for your Annotation Schema. To activate (a) field(s) for your Annotation Schema, check the box next to the field(s) you want, then click âMoveâ¦to active fieldsâ.

##### Ordering in the Annotation Schema#

Across the Schema Manager youâll see handles to drag-and-drop `fields`, `classes`, `attributes`, and `values` within sections. You can reorder this information to update how values appear in the âAnnotateâ tab of the sample expanded view.

For example, reordering a primitive field `foo` above another primitive field `bar` will cause `foo` to appear above `bar` in the list of primitives in the âAnnotateâ tab.

#### Configuring a Field Schema#

Before you can add a field to the Annotation Schema, you must first configure its schema. Click the âï¸ icon on any field in the Schema Manager (including both the âActive fieldsâ and âHidden fieldsâ sections) to open the âEdit field schemaâ page and configure that fieldâs schema.

You can compose a fieldâs schema from scratch, or scan all samples across the dataset to import metadata. If you choose to scan the dataset, you may edit the results of that scan before saving the schema.

Warning

Because scanning for metadata looks at samples across your entire dataset, it could take a few seconds or minutes.

The âEdit field schemaâ page includes two ways for you to configure the fieldâs schema: GUI or JSON. Both interfaces represent the same data model, and any updates you make in one interface should update the data modelâs representation in the other interface in realtime.

##### Annotation Schema Format#

The in-App Annotation Schema format is borrowed from [FiftyOneâs existing label_schema format](integrations__annotation.md#annotation-label-schema) (historically supported for requesting annotations from third-party backends).

For label-type fields, `classes` are a first-order list of classes available for selection on all instances of your label across samples in your dataset. Label-type fields also have `attributes`, which are optional semantic properties whose values may also be edited across samples on your dataset.

For both primitive fields and `attributes`, the following properties apply:

  * `type`: the data type (e.g., `int`, `str`).

  * `component`: the UI component through which values are edited on the âAnnotateâ tab. Available `component`s include:

    * `text`: a free text field. Applicable when `type` is `str`, `int`, `float`, or `list`.

    * `dropdown`: an autocomplete dropdown menu. Applicable when `type` is `str`, `int`, `float`, or `list`. `values` is required.

    * `radio`: a radio button group. Applicable when `type` is `str`, `int` or `float`. `values` is required.

    * `slider`: a numeric slider and numeric input boxes. Applicable when `type` is `int` or `float`. `range` is required.

    * `toggle`: a toggle where one and only one of two possible options must be selected. Applicable when `type` is `bool`.

    * `datepicker`: a calendar date picker component. Applicable when `type` is `date` or `datetime`.

    * `json`: an editable JSON code block. Applicable when `type` is `list` or `dict`.

  * `values`: the list of allowed values available for selection in the `attribute` or primitive.

  * `range`: the `[min, max]` values available for numeric `type`s, used in the `slider`. When `range` is defined, `values` must be omitted.

  * `default`: the default value assigned to the attribute on new label instances. Not applicable to primitive fields.




**Reserved attribute names**

When configuring your fieldâs schema, you may not use any of the following reserved key names:

  * `color`

  * `id`

  * `isNew`

  * `path`

  * `selected`

  * `sampleId`

  * `type`




##### Configuring with GUI#

Here youâll see different sections depending on whether your field is a label-type, or a non-label primitive field.

For label fields, youâll see sections for adding and editing label `classes` and `attributes`. Click the â+Add classâ or â+Add attributeâ buttons to create new `classes` and `attributes`, respectively.

For each `class` and `attribute` in the GUI:

  * Click the âï¸ icon to edit its properties.

  * Click the ðï¸ icon to delete.

  * Drag and drop `classes` or `attributes` within sections to reorder within the Annotation Schema (see: Ordering in the Annotation Schema).




For primitives, depending on your fieldâs data type, youâll see optional and/or required properties to configure for your fieldâs schema.

#### Creating New Fields#

Click the âNew fieldâ button in the Schema Manager to begin creating a new field on your dataset.

On the next screen, youâll need to provide a unique name for your new field. Next, choose whether your new field should be a label-type field, or primitive. In either case, open the âField typeâ dropdown menu to choose a data type for your new field.

Youâll then see different sections depending on your choices. Once you are satisfied with your new fieldâs configuration, click the âSaveâ button, and two things happen:

  1. Your new field immediately gets written to the database

  2. Your new field is added as an âActive fieldâ in the Annotation Schema




To cancel at any time while configuring your new field, click the âDiscardâ button.

#### Ontologies#

An Annotation Ontology is a global, named, versioned resource that bundles a reusable set of typed attributes â with optional conditional display logic â into a single document that can be attached to a label schema field. Ontologies live outside any dataset, so multiple datasets and fields can reference the same ontology by name.

Create and save an ontology with the SDK:
    
    
    import fiftyone as fo
    
    ontology = fo.AnnotationOntology(
        name="vehicle_damage_ontology",
        attributes=[
            fo.AttributeSpec(name="damage_present", type="bool", component="toggle"),
        ],
    )
    ontology.save()
    

Attach the ontology to a field on a datasetâs label schema:
    
    
    import fiftyone as fo
    
    dataset = fo.load_dataset("my_dataset")
    label_schemas = fo.apply_ontology(
        dataset.label_schemas,
        field_name="detections",
        ontology_name="vehicle_damage_ontology",
    )
    dataset.set_label_schemas(label_schemas)
    

Pass `ontology_name=None` to `apply_ontology()` to unset an existing reference on a field.

#### Conditional Attributes#

Attributes in an Annotation Ontology can be shown conditionally based on other values on the same label. Pass a `when` condition to `AttributeSpec` â the `field` may reference any attribute on the parent, including `label` itself.
    
    
    import fiftyone as fo
    
    fo.AnnotationOntology(
        name="vehicles",
        attributes=[
            fo.AttributeSpec(
                name="num_doors",
                type="int",
                component="text",
                when=fo.WhenEquals(field="label", value="car"),
            ),
            fo.AttributeSpec(
                name="cargo_capacity",
                type="float",
                component="text",
                when=fo.WhenEquals(field="label", value="truck"),
            ),
        ],
    ).save()
    

`num_doors` is editable only when the labelâs class is `car`, and `cargo_capacity` only when it is `truck`. Hidden attributes are not written to the label.

Once this ontology is attached to a label field, annotators will see these conditional attributes in the right sidebar of the in-App annotation UI as they annotate.

#### Bypassing Schema Configuration#

If you do not see a field or its contents in the âAnnotateâ tab of the sample expanded view, and you donât want to go through the process of configuring a schema for the field and adding it to the Annotation Schema, you can bypass interacting with the Schema Manager altogether and ask the FiftyOne App to take the requisite steps on your behalf.

Warning

Like the above features in the âSchema Import / Managementâ section, this bypass feature is only available to users with [âCan manageâ access](enterprise__roles_and_permissions.md#enterprise-can-manage) on a dataset.

![Quick-edit pencil icon on the Explore tab](../_images/bypass_schema_quick_edit.gif)

While on the âExploreâ tab of the sample expanded view, hover over the field with objects/values you wish to edit via in-App annotation, and youâll see a âï¸ icon. When you click the âï¸ icon, if no valid schema exists yet for that fieldâand the field does not exist in the Annotation Schema, the following happens:

  1. The App scans your dataset to impute a schema for the field

  2. The App then adds your field to the Annotation Schema, using the imputed field schema

  3. You are then navigated to the âAnnotateâ tab and placed into either an edit context for your field or a filtered list of label instances, depending on your fieldâs type




### Getting Started with Annotation#

To access fields in the âAnnotateâ tab, first check the box next to the field in the âExploreâ tab. Only those labels you are visualizing in the âExploreâ tab will be available for in-App annotation in the âAnnotateâ tab.

![Annotate tab overview with Canvas, Toolbar, and Labels list](../_images/annotate_tab_overview.png)

While in the âAnnotateâ tab, the sample expanded view consists of three parts:

  1. The âAnnotation Canvasâ

  2. Annotation actions toolbar

  3. List of label instances




#### Annotation Canvas#

The Annotation Canvas is where you visualize your sample and interact directly with label instances using mouse and keyboard actions. We refer to the Annotation Canvas below when describing 3D and 2D label creations and edits in more detail.

You can edit an existing label instance by clicking on that label instance on the Annotation Canvas.

#### Annotation Actions Toolbar#

The annotation actions toolbar is where you can create a new label instance or (if you are a user with âCan manageâ access on the dataset; see above) access the Schema Manager and Annotation Schema.

#### List of Label Instances#

Under the âLabelsâ header, youâll see a flattened list of all label instances included in fields enabled while in the âExploreâ tab. You can edit an existing label instance by clicking on that label instance within the âLabelsâ list.

For label types with spatial properties (e.g., 2D bounding boxes), youâll notice a visual indicator highlighting label instances in both the Annotation Canvas and âLabelsâ list as you hover over either part of the user interface.

#### List of Primitives#

Labels are not the only type of metadata available for edits in FiftyOneâs in-App annotation functionality. Primitive [fields](user_guide__basics.md#basics-fields) (e.g., `StringField`s or `IntField`s) on the dataset may also be made available in the Annotation Schema via the Schema Manager interface. When primitives exist in the Annotation Schema, youâll see a flattened list of all such fields under the âPrimitivesâ header.

* * *

## How to: 2D Label Annotation#

### Creating a Classification label#

![Creating a classification](../_images/create_classification_button.png)

Click the âCreate new classificationâ icon in the annotation actions toolbar to display the classification editor in the right sidebar. A field and label are required to save the new classification label. Only fields available in your schema will be displayed as options in the dropdown boxes.

### Creating a Detection label#

![Create detection icon](../_images/create_detection_button.png)

Click the âCreate new detectionâ icon in the annotation actions toolbar to enable the crosshair mouse cursor on the Annotation Canvas and display the detection editor in the right sidebar. Position the cursor at one corner of the new detection, then click and hold the mouse button while dragging diagonally to create a bounding box.

![Drawing a bounding box](../_images/draw_bounding_box.gif)

Once a bounding box has been created, it can be resized and repositioned as desired by clicking and holding any edge or corner drag handle while moving the mouse cursor. For finer adjustments, first zoom in on the image. To maintain the aspect ratio of the selection, hold down the shift key while dragging.

A field and label are required to save the new detection label. Only fields available in your schema will be displayed as options in the dropdown boxes.

A detection labelâs size and shape can be adjusted directly in the annotation canvas by clicking on the detection to select it, then dragging an edge or corner drag handle:

![Editing detection on canvas](../_images/edit_bounding_box_canvas.gif)

### Creating a Segmentation label#

![Create new mask button](../_images/create_mask_button.png)

Click the âCreate new maskâ icon in the annotation actions toolbar to enable the mask annotation toolbar displayed on the left side of the Annotation Canvas. Select the paintbrush, polyline, or AI tool to begin drawing masks.

![Mask annotation toolbar](../_images/mask_toolbar.png)

When drawing segmentation masks, the mask toolbar is shown on the left of the Annotation Canvas. From top to bottom of the image above, the icons depict the Selection tool to select specific label instances, the Brush tool, Polygon tool, or AI assistance tool for drawing new masks, the Merge tool to combine mask instances, and Close to stop editing the current label instance.

A field and label are required to save new mask labels. Only fields available in your schema will be displayed as options in the dropdown boxes. Instance segmentations fall under the `Detections` label field type, allowing for detection labels either with or without masks.

![Configuring a mask field schema](../_images/mask_field_schema.png) ![Kebab menu to add or remove a mask](../_images/detection_kebab_remove_mask.png)

The kebab menu on an existing detection label in the right sidebar allows you to either add or remove the mask from that label instance.

![AI assistance tool](../_images/mask_ai_assistance.gif)

The AI assistance tool allows you to use mask segmentation models to draw masks. This tool allows you to click any number of positive and negative points per object as prompts to the model to refine the mask boundaries. For FiftyOne Enterprise customers, ask your Voxel51 Customer Success representative about bringing your own finetuned models for AI assisted segmentation.

![Brush tool](../_images/mask_brush_tool.gif)

The Brush tool allows for pixel-level precision to create masks. By selecting the `-` Mode, you can use the brush tool to remove pixels from existing masks. The Brush tool also allows you to configure the size and shape of the brush.

![Polygon tool](../_images/mask_polygon_tool.gif)

Similar to the brush tool, the Polygon tool allows you to create or remove masks from detection instances. Click the canvas to place points on the polygon, then right click to confirm your selection.

![Merge tool](../_images/mask_merge_tool.gif)

If multiple masks have been created for the same object, the Merge tool allows you to select one object instance and merge the mask of another instance into it.

### Creating Polyline and Polygon labels#

![Create new polylines button](../_images/create_polylines_button.png)

Click the âCreate new polylinesâ icon in the annotation actions toolbar to enable the crosshair mouse cursor on the Annotation Canvas and display the polylines editor in the right sidebar.

![Drawing a polyline](../_images/draw_polyline.gif)

Click the canvas to begin placing vertices of the new polyline, with successive clicks connecting the vertices with line segments. Right click to finish editing the current polyline label instance. To add additional vertices onto an existing polyline, click the polyline segment at the desired location to place the new vertex.

![Drawing a polygon](../_images/draw_polygon.gif)

[Polygon labels in FiftyOne](https://docs.voxel51.com/user_guide/using_datasets.html#polylines) are simply polylines with the `closed` and `filled` attributes set to `True`. Configure the label schema to use default values for these attributes if desired, or configure these values for each label instance. Similar to polylines, edit polygons by clicking the canvas to place vertices defining the boundary of the polygon. Clicking an existing boundary segment allows you to add new vertices into an existing polygon. Right click the canvas to finish editing the current polygon.

### Editing in the Right Sidebar#

Labels can be selected by clicking on its bounding box or on the item in the list in the right sidebar, which will highlight the associated bounding box on the annotation canvas if the label is a detection, then clicking the chosen row. This will open the editing panel in the right sidebar.

![Right sidebar editor](../_images/edit_bounding_box_sidebar.gif)

#### Spatial Properties#

![Detection spatial properties editor](../_images/detection_spatial_properties.png) ![3D cuboid spatial properties editor](../_images/cuboid_spatial_properties.png)

Within the editing panel spatial coordinates of the label are displayed. For example, for detection type labels the x/y coordinates, width, and height can be adjusted. Editing the x/y coordinates and/or the width/height will display the changes in the annotation canvas. This allows finite adjustments that could be difficult with a mouse.

#### Attributes#

The editing panel also enables editing the label, tags, confidence, index properties, and custom properties depending on the configured annotation schema.

* * *

## Working with 3D#

### 3D Annotation Mode#

#### Supported 3D Datasets#

3D annotation mode is only supported for `3d` [type datasets](https://docs.voxel51.com/user_guide/using_datasets.html#d-datasets) and dataset views, or grouped datasets with `3d` slices.

Note

`point-cloud` [type datasets](https://docs.voxel51.com/user_guide/using_datasets.html#point-cloud-datasets) are deprecated and do not support annotation. We recommend converting them to `3d` type datasets.

For grouped datasets, you can use the slice selector within the Annotate tab to select the image or 3d slice you wish to annotate.

![Slice selector](../_images/3d_slice_selector.png)

#### Camera Projections#

**Pointcloud projections**

![Pointcloud projections](../_images/pointcloud_projections.png)

Projection surfaces allow you to flatten a 3D point cloud onto a 2D plane for easier annotation. You can toggle between different projection views using the dropdown menus.

**2D Image Projections**

If your dataset contains [groups](https://docs.voxel51.com/user_guide/groups.html#groups), where at least one group slice contains 2D images, youâll also see those slices available for visualization in the dropdown menu.

![2D image projections](../_images/image_projection_slices.png)

If you have defined the necessary [camera intrinsic and extrinsic parameters](https://docs.voxel51.com/user_guide/using_datasets.html#camera-intrinsics-extrinsics), then you will also be able to project the 3D labels onto the 2D images in real time.

![3D image projections](../_images/labels_projected_on_image.gif)

### 3D Annotation Controls#

#### Annotation Plane#

![Annotation plane concept](../_images/annotation_plane_concept.gif)

3D annotation mode in FiftyOne provides the concept of an âannotation planeâ. When a new point is created (for example the vertex of a polyline or cuboid), it gets placed at the location of the mouse pointer. However, the depth of the point would be ambiguous and so this annotation plane is used to define the point depth. By default, the annotation plane is set to be the XY plane.

![Annotation plane positioning](../_images/reposition_annotation_plane.gif)

The annotation plane can be repositioned by clicking the annotation plane icon in the left toolbar. Iteratively moving the annotation plane and placing vertices is an efficient way to annotate complex 3D shapes.

![Moving annotation plane](../_images/annotation_plane_workflow.gif)

#### Visualizer Controls#

The 3D annotation toolbar on the left side of the screen contains all options for spatially manipulating 3D cuboids and polylines. The icons represent the following actions:

  * Cancel the annotation of the current label, presenting the option to either save or discard changes


![Cancel annotation button](../_images/control_cancel_icon.png)

  * Begin annotation of a new cuboid


![Begin annotation of a new cuboid](../_images/control_new_cuboid_icon.png)

  * Begin annotation of a new polyline or segment


![Begin annotation of a new polyline or segment](../_images/control_new_polyline_icon.png)

  * Add a new vertex to the selected polyline


![Add a new vertex to the selected polyline](../_images/control_add_vertex_icon.png)

  * Enable a mode where double clicking automatically closes the polyline


![Enable a mode where double clicking automatically closes the polyline](../_images/control_auto_close_icon.png)

  * Enable visualization and manipulation of the annotation plane


![Enable visualization and manipulation of the annotation plane](../_images/control_show_plane_icon.png)

The camera position can be manipulated to snap to the X,Y,Z directions or to the annotation plane with the keyboard shortcuts. The number keys 1-4 and CTRL+1-4 correspond to the top/bottom, right/left, front/back, and annotation plane respectively as shown in the video below.

![Camera controls](../_images/camera_snap_shortcuts.gif)

### How to: 3D Cuboid Annotation#

To begin creating and editing 3D cuboids, enter polyline annotation mode by clicking on the cuboid icon in the annotate actions toolbar. When in cuboid annotation mode, the 3D cuboid toolbar becomes available on the left side of the Annotation Canvas.

![3D cuboid toolbar](../_images/cuboid_toolbar.png)

#### Creating 3D Cuboids#

After entering cuboid annotation mode, create a new 3D cuboid by clicking on the cuboid icon in the cuboid toolbar on the left side, then click the 3D scene to place the first corner of the cuboid. Click a second time to define the opposite corner of the base (XY plane) of the cuboid. This second click finishes the creation of the cuboid, always defaulting to a height of 1.0 in the lz direction.

![Creating a 3D cuboid](../_images/create_3d_cuboid.gif)

Newly created cuboids are oriented based on the current annotation plane. The depth of the first two clicks in the 3D scene is dictated by the location of the annotation plane which is described above (defaulting to the XY plane).

#### Transforming 3D Cuboids#

After selecting a cuboid, the left toolbar provides new actions to transform the cuboid via translation, rotation, and scaling.

**Translation**

![Translation mode](../_images/cuboid_translate.gif)

Click the translation icon in the left toolbar to enable translation mode. In this mode, the cuboid can be translated (moved) along the x, y, or z axes by clicking and dragging the corresponding directional arrow on the cuboid. Additionally, you can move the cuboid within a plane (XY, XZ, or YZ) by clicking and dragging the corresponding colored plane handle. For 3D translation in all directions, click and drag the white cube at the center of the cuboid.

**Rotation**

![Rotation mode](../_images/cuboid_rotate.gif)

After selecting a cuboid, click the rotation icon in the left toolbar to enable rotation mode. In this mode, the cuboid can be rotated about the x, y, or z axes by clicking and dragging the corresponding colored circle on the cuboid. You can also rotate about the plane orthogonal to the current camera view using the outermost yellow circle.

**Scaling**

![Scaling mode](../_images/cuboid_scale.gif)

After selecting a cuboid, click the scaling icon in the left toolbar to enable scaling mode. In this mode, the cuboid can be scaled (resized) along the x, y, or z axes by clicking and dragging the corresponding directional arrow on the cuboid. In addition to scaling along an axis, you can scale the cuboid within a plane (XY, XZ, or YZ) by clicking and dragging the corresponding colored plane handle.

#### Attribute Editing#

![Cuboid attributes panel](../_images/cuboid_attributes_panel.png)

Cuboid attributes can be edited in the right sidebar when a given cuboid is selected. Custom attributes in this panel are defined by the Schema Manager.

### How to: 3D Polyline Annotation#

![3D polyline annotation](../_images/polyline_annotation_intro.gif)

To begin creating and editing 3D polylines, enter polyline annotation mode by clicking on the polyline icon in the annotate actions toolbar. When in polyline annotation mode, the 3D polyline toolbar becomes available on the left side of the Annotation Canvas.

![Polyline toolbar](../_images/polyline_toolbar.png)

#### Creating Polylines#

After entering polyline annotation mode, create a new 3D polyline by clicking on the polyline icon in the polyline toolbar on the left side, then click the 3D scene to create the first vertex of the polyline. After placing the final vertex of your polyline, double click anywhere on the 3D scene to finish creation of the polyline segment.

![Creating a polyline](../_images/create_3d_polyline.gif)

Newly created vertices are placed at the location of the mouse pointer. The depth of a newly created vertex in the 3D scene is dictated by the location of the annotation plane which is described below (defaulting to the XY plane).

#### Polylines vs Segments#

The points of a single [Polyline in FiftyOne](https://docs.voxel51.com/user_guide/using_datasets.html#d-polylines) are represented as a list of lists of vertices:
    
    
    # A list of lists of `[x, y, z]` points in scene coordinates describing
    # the vertices of each shape in the polyline
    points3d = [[[-5, -99, -2], [-8, 99, -2]], [[4, -99, -2], [1, 99, -2]]]
    

This allows for the possibility of multiple disjointed segments within a single polyline as shown in the code example above. This may be useful, for example, if you are annotating a dashed lane marking where each dash is a disjointed segment of the same polyline, allowing all of the segments to share the same attributes.

![Polyline segments](../_images/polyline_segments_diagram.png)

In the right Annotate sidebar, you can see the number of segments and vertices in the current Polyline.

#### Adding New Segments#

![Adding new segments](../_images/add_polyline_segment.gif)

To add a new segment to an existing polyline, first select the polyline to be edited, then select the new polyline segment button in the left toolbar and finally click to annotate the new segment.

#### Vertex Manipulation#

When positioning a vertex in 3D space, the vertex controls become available when you click to select a given vertex (or the polyline centroid). These controls allow you to click either the 3 RGB directional arrows to move the vertex along the given axis, 3 CMY planes to move the vertex in the given plane, and a clickable center to position the vertex in 3D space.

![Vertex manipulation controls](../_images/polyline_vertex_controls.gif)

#### Adding and Deleting Vertices#

![Adding and deleting vertices](../_images/add_delete_polyline_vertex.gif)

Vertices can also be added to and deleted from existing polylines. To add a new vertex, first select the polyline to which the vertex should be added, then click on the new vertex icon in the left toolbar, and finally select the location on the polyline that the new vertex should be added. The new vertex can now be moved to the desired location.

A selected vertex can be deleted by pressing the trash can icon in the left toolbar (or by pressing the delete key).

![Delete vertex icon](../_images/delete_vertex_icon.png)

#### Attribute Editing#

![Polyline attributes panel](../_images/polyline_attributes_panel.png)

Polyline attributes can be edited in the right sidebar when a given polyline is selected. Custom attributes in this panel are defined by the Schema Manager.

In addition to custom attributes, the attribute sidebar for 3D polylines also shows the number of segments and vertices in the selected polyline, as well as the polyline-specific âclosedâ and âfilledâ attributes which affect how the polyline is rendered. Setting the âclosedâ attribute to True will automatically render a line segment from the first vertex of a polyline to the last vertex to close the shape. Setting the âfilledâ attribute to True will show the region enclosed by the polyline as filled.

![Closed polyline example](../_images/polyline_closed_example.png) ![Filled polyline example](../_images/polyline_filled_example.png) ![Closed and filled polyline](../_images/polyline_closed_filled_example.png)

Additionally, you can select the icon to the left to enter a mode that will automatically close the polyline when the annotation canvas is double clicked.

![Auto-close mode icon](../_images/polyline_auto_close_icon.png)

* * *

## How to: Editing Primitives#

### Editing in the Right Sidebar#

Clicking on a primitive field in the âAnnotateâ tab will open the editing panel in the right sidebar. Like editing a labelâs attributes, you can edit the primitiveâs values per the Annotation Schema.

![Editing primitives in the right sidebar](../_images/primitive_editing_panel.png)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
