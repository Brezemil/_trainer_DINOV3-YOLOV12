---
source_url: https://docs.voxel51.com/api/fiftyone.core.annotation.hydrate_label_schemas.html
---

# fiftyone.core.annotation.hydrate_label_schemas#

Annotation label schema hydration

Resolves `applied_ontology` references in label schemas by merging the referenced annotation ontologyâs attributes into the schemaâs `attributes` list, tagging merged attributes with a `_source` marker.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`attributes_with_source`(ontology) | Returns ontology attributes as dicts tagged with a `_source` marker.  
---|---  
`hydrate_applied_ontology`(label_schema) | Merges a referenced annotation ontology's attributes into a label schema.  
`dehydrate_applied_ontology`(label_schema) | Strips hydration artifacts from a label schema before it is saved.  
`inline_applied_ontology`(label_schema,Â ontology) | Permanently inlines an annotation ontology's attributes into a label schema as local copies and removes the `applied_ontology` reference.  
  
fiftyone.core.annotation.hydrate_label_schemas.attributes_with_source(_ontology : Any_) → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[dict[str, Any]]#
    

Returns ontology attributes as dicts tagged with a `_source` marker.

Parameters:
    

**ontology** â an ontology object whose `.attributes` are attribute specs with a `.to_dict()` method and whose `.name` identifies the ontology

Returns:
    

a list of attribute dicts, each carrying `_source: ontology.name`

fiftyone.core.annotation.hydrate_label_schemas.hydrate_applied_ontology(_label_schema : dict_) → dict#
    

Merges a referenced annotation ontologyâs attributes into a label schema.

If `label_schema` has an `applied_ontology` key that resolves to an annotation ontology, returns a new dict with the ontologyâs attributes merged into the `attributes` list. Each merged attribute carries a `_source: <ontology_name>` marker. Attributes are matched by `name` and ontology values win on collision.

If the schema has no `applied_ontology` reference, the schema is returned unchanged. If the reference is dangling (deleted ontology) or points at a non-annotation ontology, the `applied_ontology` key is stripped from the returned schema and a WARNING is logged. This lets a subsequent save silently persist a clean schema rather than failing validation on the dangling reference.

Parameters:
    

**label_schema** â a label schema dict

Returns:
    

a hydrated copy of `label_schema`, a copy with `applied_ontology` stripped if the reference is dangling, or the schema unchanged when there is nothing to do

fiftyone.core.annotation.hydrate_label_schemas.dehydrate_applied_ontology(_label_schema : dict_) → dict#
    

Strips hydration artifacts from a label schema before it is saved.

Companion to `hydrate_applied_ontology()`. When the schema has an `applied_ontology` that resolves to an annotation ontology, drops any attribute whose `name` matches an ontology-owned attribute and strips the `_source` marker from the remaining attributes.

Otherwise (no reference, dangling reference, or non-annotation reference) the schema is returned unchanged â the validator will surface the reference-level problem.

Parameters:
    

**label_schema** â a label schema dict, possibly carrying hydration artifacts from `hydrate_applied_ontology()`

Returns:
    

a deep-copied schema with hydration artifacts removed, or `label_schema` unchanged when there is nothing to dehydrate

fiftyone.core.annotation.hydrate_label_schemas.inline_applied_ontology(_label_schema : dict_, _ontology : Any_) → dict#
    

Permanently inlines an annotation ontologyâs attributes into a label schema as local copies and removes the `applied_ontology` reference.

Used when the referenced ontology is about to be deleted (or for any other âfreeze the current ontology state into the schemaâ operation). Unlike `hydrate_applied_ontology()`, the merged attributes are NOT marked with `_source` â they are now first-class local attributes â and the `applied_ontology` key is stripped from the result.

The caller is responsible for resolving the ontology; this function does not load anything.

Parameters:
    

  * **label_schema** â a label schema dict

  * **ontology** â an `AnnotationOntology` whose attributes should be inlined



Returns:
    

a deep-copied schema with the ontologyâs attributes merged in as locals and the `applied_ontology` reference removed

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
