---
source_url: https://docs.voxel51.com/api/fiftyone.core.ontology_validation.html
---

# fiftyone.core.ontology_validation#

Validation for [`fiftyone.core.ontology.AnnotationOntology`](api__fiftyone.core.ontology.md#fiftyone.core.ontology.AnnotationOntology "fiftyone.core.ontology.AnnotationOntology").

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`validate_annotation_ontology`(ontology) | Validates an `AnnotationOntology`.  
---|---  
  
fiftyone.core.ontology_validation.validate_annotation_ontology(_ontology : [AnnotationOntology](api__fiftyone.core.ontology.md#fiftyone.core.ontology.AnnotationOntology "fiftyone.core.ontology.AnnotationOntology")_) → None#
    

Validates an `AnnotationOntology`.

Aggregates all ontology-level failures into a single error. `When` operators are validated on construction.

Parameters:
    

**ontology** â the ontology to validate

Raises:
    

**ValueError** â if any rule fails

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
