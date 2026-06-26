---
source_url: https://docs.voxel51.com/api/fiftyone.core.ontology.html
---

# fiftyone.core.ontology#

Ontology classes for defining reusable annotation and taxonomy structures.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Ontology`(name[,Â description]) | Abstract base class for ontology types.  
---|---  
`AnnotationOntology`(name[,Â description,Â ...]) | Ontology for defining annotation structures.  
`LabelSchemaOntologyRef`(dataset_id,Â field_names) | One dataset's `applied_ontology` references for a given ontology.  
  
**Functions:**

`load_ontology`(name) | Loads the latest version of an ontology by name.  
---|---  
`list_ontologies`([glob_patt]) | Lists ontology names in the database.  
`ontology_exists`(name) | Checks if an ontology with the given name exists.  
`delete_ontology`(name[,Â force]) | Deletes an ontology and all its versions from the database.  
`apply_ontology`(label_schemas,Â field_name,Â ...) | Returns a new `label_schemas` dict with an annotation ontology attached to (or removed from) the given field.  
  
class fiftyone.core.ontology.Ontology(_name : str_, _description : str | None = None_)#
    

Bases: `ABC`

Abstract base class for ontology types.

Ontologies are global, named, versioned resources that define reusable annotation structures. They are not scoped to any single dataset. `save()` and `load()` populate `version`, `created_at`, and `last_modified_at`.

Parameters:
    

  * **name** â the ontology name

  * **description** â optional description




**Attributes:**

`version` | The version of this ontology, or `None` if not yet saved.  
---|---  
`created_at` | The datetime this ontology was created, or `None` if not yet saved.  
`last_modified_at` | The datetime this ontology was last modified, or `None` if not yet saved.  
`is_annotation_ontology` | Whether this ontology is an annotation ontology.  
`is_taxonomy` | Whether this ontology is a taxonomy.  
  
**Methods:**

`save`() | Saves this ontology to the database.  
---|---  
`reload`() | Reloads this ontology from the database.  
`delete`() | Deletes this ontology from the database.  
`clone`(new_name) | Clones this ontology under a new name.  
`to_dict`() | Serializes this ontology to a dict.  
`from_dict`(d) | Creates an ontology from a dict.  
  
property version: int | None#
    

The version of this ontology, or `None` if not yet saved.

property created_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

The datetime this ontology was created, or `None` if not yet saved.

property last_modified_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

The datetime this ontology was last modified, or `None` if not yet saved.

property is_annotation_ontology: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether this ontology is an annotation ontology.

property is_taxonomy: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether this ontology is a taxonomy.

save() → None#
    

Saves this ontology to the database.

reload() → None#
    

Reloads this ontology from the database.

delete() → None#
    

Deletes this ontology from the database.

clone(_new_name : str_) → Ontology#
    

Clones this ontology under a new name.

Parameters:
    

**new_name** â the name for the clone

Returns:
    

the cloned `Ontology`

to_dict() → dict#
    

Serializes this ontology to a dict.

Returns:
    

a dict

abstractmethod classmethod from_dict(_d : dict_) → Ontology#
    

Creates an ontology from a dict.

Parameters:
    

**d** â an ontology dict

Returns:
    

an `Ontology`

class fiftyone.core.ontology.AnnotationOntology(_name : str_, _description : str | None = None_, _taxonomies : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str] | None = None_, _attributes : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[[AttributeSpec](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec "fiftyone.core.annotation.attributes.AttributeSpec")] | None = None_)#
    

Bases: `Ontology`

Ontology for defining annotation structures.

Bundles typed attributes (with optional conditional display logic) and taxonomy references into a single document that gets connected to a label schema on a field.

Parameters:
    

  * **name** â the ontology name

  * **description** â optional description

  * **taxonomies** â list of taxonomy names referenced by this ontology

  * **attributes** â list of `AttributeSpec` instances




Example:
    
    
    AnnotationOntology(
        name="vehicle_damage_ontology",
        description="Vehicle damage annotation",
        taxonomies=["vehicle_classes"],
        attributes=[
            AttributeSpec(
                name="damage_present",
                type="bool",
                component="checkbox",
            ),
            AttributeSpec(
                name="damage_location",
                type="str",
                component="dropdown",
                values=["front", "rear", "driver_side", "passenger_side"],
                when=WhenEquals(field="damage_present", value=True),
            ),
        ],
    )
    

**Methods:**

`to_dict`() | Serializes this annotation ontology to a dict.  
---|---  
`from_dict`(d) | Creates an `AnnotationOntology` from a dict.  
`clone`(new_name) | Clones this ontology under a new name.  
`delete`() | Deletes this ontology from the database.  
`reload`() | Reloads this ontology from the database.  
`save`() | Saves this ontology to the database.  
  
**Attributes:**

`created_at` | The datetime this ontology was created, or `None` if not yet saved.  
---|---  
`is_annotation_ontology` | Whether this ontology is an annotation ontology.  
`is_taxonomy` | Whether this ontology is a taxonomy.  
`last_modified_at` | The datetime this ontology was last modified, or `None` if not yet saved.  
`version` | The version of this ontology, or `None` if not yet saved.  
  
to_dict() → dict#
    

Serializes this annotation ontology to a dict.

Returns:
    

a dict

classmethod from_dict(_d : dict_) → AnnotationOntology#
    

Creates an `AnnotationOntology` from a dict.

Parameters:
    

**d** â an annotation ontology dict

Returns:
    

an `AnnotationOntology`

clone(_new_name : str_) → Ontology#
    

Clones this ontology under a new name.

Parameters:
    

**new_name** â the name for the clone

Returns:
    

the cloned `Ontology`

property created_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

The datetime this ontology was created, or `None` if not yet saved.

delete() → None#
    

Deletes this ontology from the database.

property is_annotation_ontology: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether this ontology is an annotation ontology.

property is_taxonomy: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether this ontology is a taxonomy.

property last_modified_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

The datetime this ontology was last modified, or `None` if not yet saved.

reload() → None#
    

Reloads this ontology from the database.

save() → None#
    

Saves this ontology to the database.

property version: int | None#
    

The version of this ontology, or `None` if not yet saved.

fiftyone.core.ontology.load_ontology(_name : str_) → Ontology#
    

Loads the latest version of an ontology by name.

Parameters:
    

**name** â the ontology name

Returns:
    

an `Ontology`

Raises:
    

**ValueError** â if no ontology with the given name exists

fiftyone.core.ontology.list_ontologies(_glob_patt : str | None = None_) → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]#
    

Lists ontology names in the database.

Parameters:
    

**glob_patt** â an optional glob pattern to filter names

Returns:
    

a sorted list of ontology names

fiftyone.core.ontology.ontology_exists(_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Checks if an ontology with the given name exists.

Parameters:
    

**name** â the ontology name

Returns:
    

True/False

class fiftyone.core.ontology.LabelSchemaOntologyRef(_dataset_id : str_, _field_names : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]_)#
    

Bases: `NamedTuple`

One datasetâs `applied_ontology` references for a given ontology.

dataset_id#
    

the `DatasetDocument` id (string form)

Type:
    

str

field_names#
    

the label-schema field names on that dataset that reference the ontology

Type:
    

[list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]

**Attributes:**

`dataset_id` | Alias for field number 0  
---|---  
`field_names` | Alias for field number 1  
  
**Methods:**

`count`(value,Â /) | Return number of occurrences of value.  
---|---  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
dataset_id: str#
    

Alias for field number 0

field_names: [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]#
    

Alias for field number 1

count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

fiftyone.core.ontology.delete_ontology(_name : str_, _force : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Deletes an ontology and all its versions from the database.

If any label schema references this ontology (via `applied_ontology` on a field), the default behavior is to raise rather than silently break those schemas. Pass `force=True` to inline the ontologyâs attributes into each affected schema as permanent local copies and then delete the ontology.

Inlining and deletion run as two phases: every affected schema is inlined and saved first, and the ontology is deleted only if every save succeeds. If something fails mid-inline, the ontology still exists and the call is safely re-runnable â already-inlined schemas no longer match the lookup.

Parameters:
    

  * **name** â the ontology name

  * **force** â if False (default), raise if any label schema references the ontology. If True, inline the ontologyâs attributes into each affected schema as local copies before deleting.



Raises:
    

**ValueError** â if the ontology does not exist, or if it is in use and `force=False`

fiftyone.core.ontology.apply_ontology(_label_schemas : dict_, _field_name : str_, _ontology_name : str | None_) → dict#
    

Returns a new `label_schemas` dict with an annotation ontology attached to (or removed from) the given field.

Pure function â does not mutate the input. Apply the result via [`fiftyone.core.dataset.Dataset.set_label_schemas()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.set_label_schemas "fiftyone.core.dataset.Dataset.set_label_schemas") to persist.

Parameters:
    

  * **label_schemas** â a label schemas dict

  * **field_name** â the field to attach the ontology to

  * **ontology_name** â name of an annotation ontology to attach, or `None` to unset an existing reference



Returns:
    

a new label schemas dict

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
