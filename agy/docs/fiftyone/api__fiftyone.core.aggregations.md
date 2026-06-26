---
source_url: https://docs.voxel51.com/api/fiftyone.core.aggregations.html
---

# fiftyone.core.aggregations#

Aggregations.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Aggregation`(field_or_expr[,Â expr,Â safe]) | Abstract base class for all aggregations.  
---|---  
`Bounds`(field_or_expr[,Â expr,Â safe,Â ...]) | Computes the bounds of a numeric field of a collection.  
`Count`([field_or_expr,Â expr,Â safe,Â _hint,Â ...]) | Counts the number of field values in a collection.  
`CountValues`(field_or_expr[,Â expr,Â safe,Â ...]) | Counts the occurrences of field values in a collection.  
`Distinct`(field_or_expr[,Â expr,Â safe]) | Computes the distinct values of a field in a collection.  
`FacetAggregations`(field_name,Â aggregations) | Efficiently computes a set of aggregations rooted at a common path using faceted computations.  
`HistogramValues`(field_or_expr[,Â expr,Â bins,Â ...]) | Computes a histogram of the field values in a collection.  
`Min`(field_or_expr[,Â expr,Â safe]) | Computes the minimum of a numeric field of a collection.  
`Max`(field_or_expr[,Â expr,Â safe]) | Computes the maximum of a numeric field of a collection.  
`Mean`(field_or_expr[,Â expr,Â safe]) | Computes the arithmetic mean of the field values of a collection.  
`Quantiles`(field_or_expr,Â quantiles[,Â expr,Â safe]) | Computes the quantile(s) of the field values of a collection.  
`Schema`(field_or_expr[,Â expr,Â dynamic_only,Â ...]) | Extracts the names and types of the attributes of a specified embedded document field across all samples in a collection.  
`ListSchema`(field_or_expr[,Â expr]) | Extracts the value type(s) in a specified list field across all samples in a collection.  
`Std`(field_or_expr[,Â expr,Â safe,Â sample]) | Computes the standard deviation of the field values of a collection.  
`Sum`(field_or_expr[,Â expr,Â safe]) | Computes the sum of the field values of a collection.  
`Values`(field_or_expr[,Â expr,Â missing_value,Â ...]) | Extracts the values of the field from all samples in a collection.  
  
**Exceptions:**

`AggregationError` | An error raised during the execution of an `Aggregation`.  
---|---  
  
class fiftyone.core.aggregations.Aggregation(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Bases: `object`

Abstract base class for all aggregations.

`Aggregation` instances represent an aggregation or reduction of a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instance.

Parameters:
    

  * **field_or_expr** â a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Attributes:**

`field_name` | The name of the field being computed on, if any.  
---|---  
`expr` | The expression being computed, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
**Methods:**

`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`default_result`() | Returns the default result for this aggregation.  
  
property field_name#
    

The name of the field being computed on, if any.

property expr#
    

The expression being computed, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict, or, when `_is_big_batchable()` is True, the iterable of result dicts

Returns:
    

the aggregation result

default_result()#
    

Returns the default result for this aggregation.

Default results are used when aggregations are applied to empty collections.

Returns:
    

the aggregation result

exception fiftyone.core.aggregations.AggregationError#
    

Bases: `Exception`

An error raised during the execution of an `Aggregation`.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.core.aggregations.Bounds(_field_or_expr_ , _expr =None_, _safe =False_, __count_nonfinites =False_)#
    

Bases: `Aggregation`

Computes the bounds of a numeric field of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the bounds of a numeric field
    #
    
    aggregation = fo.Bounds("numeric_field")
    bounds = dataset.aggregate(aggregation)
    print(bounds)  # (min, max)
    
    #
    # Compute the bounds of a numeric list field
    #
    
    aggregation = fo.Bounds("numeric_list_field")
    bounds = dataset.aggregate(aggregation)
    print(bounds)  # (min, max)
    
    #
    # Compute the bounds of a transformation of a numeric field
    #
    
    aggregation = fo.Bounds(2 * (F("numeric_field") + 1))
    bounds = dataset.aggregate(aggregation)
    print(bounds)  # (min, max)
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`(None, None)`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the `(min, max)` bounds

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Count(_field_or_expr =None_, _expr =None_, _safe =False_, __hint =None_, __optimize =False_, __unwind =True_)#
    

Bases: `Aggregation`

Counts the number of field values in a collection.

`None`-valued fields are ignored.

If no field or expression is provided, the samples themselves are counted.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="dog"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="rabbit"),
                        fo.Detection(label="squirrel"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Count the number of samples in the dataset
    #
    
    aggregation = fo.Count()
    count = dataset.aggregate(aggregation)
    print(count)  # the count
    
    #
    # Count the number of samples with `predictions`
    #
    
    aggregation = fo.Count("predictions")
    count = dataset.aggregate(aggregation)
    print(count)  # the count
    
    #
    # Count the number of objects in the `predictions` field
    #
    
    aggregation = fo.Count("predictions.detections")
    count = dataset.aggregate(aggregation)
    print(count)  # the count
    
    #
    # Count the number of objects in samples with > 2 predictions
    #
    
    aggregation = fo.Count(
        (F("predictions.detections").length() > 2).if_else(
            F("predictions.detections"), None
        )
    )
    count = dataset.aggregate(aggregation)
    print(count)  # the count
    

Parameters:
    

  * **field_or_expr** (_None_) â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate. If neither `field_or_expr` or `expr` is provided, the samples themselves are counted

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`0`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the count

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.CountValues(_field_or_expr_ , _expr =None_, _safe =False_, __first =None_, __sort_by ='count'_, __asc =True_, __include =None_, __search =''_, __selected =[]_)#
    

Bases: `Aggregation`

Counts the occurrences of field values in a collection.

This aggregation is typically applied to _countable_ field types (or lists of such types):

  * [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                tags=["sunny"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="dog"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                tags=["cloudy"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Compute the tag counts in the dataset
    #
    
    aggregation = fo.CountValues("tags")
    counts = dataset.aggregate(aggregation)
    print(counts)  # dict mapping values to counts
    
    #
    # Compute the predicted label counts in the dataset
    #
    
    aggregation = fo.CountValues("predictions.detections.label")
    counts = dataset.aggregate(aggregation)
    print(counts)  # dict mapping values to counts
    
    #
    # Compute the predicted label counts after some normalization
    #
    
    aggregation = fo.CountValues(
        F("predictions.detections.label").map_values(
            {"cat": "pet", "dog": "pet"}
        ).upper()
    )
    counts = dataset.aggregate(aggregation)
    print(counts)  # dict mapping values to counts
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to treat nan/inf values as None when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`{}`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

a dict mapping values to counts

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Distinct(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Bases: `Aggregation`

Computes the distinct values of a field in a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _countable_ field types (or lists of such types):

  * [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                tags=["sunny"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="dog"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                tags=["sunny", "cloudy"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat"),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Get the distinct tags in a dataset
    #
    
    aggregation = fo.Distinct("tags")
    values = dataset.aggregate(aggregation)
    print(values)  # list of distinct values
    
    #
    # Get the distinct predicted labels in a dataset
    #
    
    aggregation = fo.Distinct("predictions.detections.label")
    values = dataset.aggregate(aggregation)
    print(values)  # list of distinct values
    
    #
    # Get the distinct predicted labels after some normalization
    #
    
    aggregation = fo.Distinct(
        F("predictions.detections.label").map_values(
            {"cat": "pet", "dog": "pet"}
        ).upper()
    )
    values = dataset.aggregate(aggregation)
    print(values)  # list of distinct values
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`[]`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

a sorted list of distinct values

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.FacetAggregations(_field_name_ , _aggregations_ , __compiled =False_)#
    

Bases: `Aggregation`

Efficiently computes a set of aggregations rooted at a common path using faceted computations.

Note

All `aggregations` provided to this method are interpreted relative to the provided `field_name`.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                tags=["sunny"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat", confidence=0.4),
                        fo.Detection(label="dog", confidence=0.5),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                tags=["sunny", "cloudy"],
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(label="cat", confidence=0.6),
                        fo.Detection(label="rabbit", confidence=0.7),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Compute prediction label value counts and confidence bounds
    #
    
    values, bounds = dataset.aggregate(
        fo.FacetAggregations(
            "predictions.detections",
            [fo.CountValues("label"), fo.Bounds("confidence")]
        )
    )
    print(values)  # label value counts
    print(bounds)  # confidence bounds
    

Parameters:
    

  * **field_name** â a field name or `embedded.field.name`

  * **aggregations** â a list or dict of `Aggregation` instances




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

the default result of each sub-aggregation in the same container type as the sub-aggregations were provided (list or dict)

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the parsed result of each sub-aggregation in the same container type as the sub-aggregations were provided (list or dict)

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.HistogramValues(_field_or_expr_ , _expr =None_, _bins =None_, _range =None_, _auto =False_)#
    

Bases: `Aggregation`

Computes a histogram of the field values in a collection.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = []
    for idx in range(100):
        samples.append(
            fo.Sample(
                filepath="/path/to/image%d.png" % idx,
                numeric_field=np.random.randn(),
                numeric_list_field=list(np.random.randn(10)),
            )
        )
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    def plot_hist(counts, edges):
        counts = np.asarray(counts)
        edges = np.asarray(edges)
        left_edges = edges[:-1]
        widths = edges[1:] - edges[:-1]
        plt.bar(left_edges, counts, width=widths, align="edge")
    
    #
    # Compute a histogram of a numeric field
    #
    
    aggregation = fo.HistogramValues("numeric_field", bins=50)
    counts, edges, other = dataset.aggregate(aggregation)
    
    plot_hist(counts, edges)
    plt.show(block=False)
    
    #
    # Compute the histogram of a numeric list field
    #
    
    aggregation = fo.HistogramValues("numeric_list_field", bins=50)
    counts, edges, other = dataset.aggregate(aggregation)
    
    plot_hist(counts, edges)
    plt.show(block=False)
    
    #
    # Compute the histogram of a transformation of a numeric field
    #
    
    aggregation = fo.HistogramValues(2 * (F("numeric_field") + 1), bins=50)
    counts, edges, other = dataset.aggregate(aggregation)
    
    plot_hist(counts, edges)
    plt.show(block=False)
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **bins** (_None_) â can be either an integer number of bins to generate or a monotonically increasing sequence specifying the bin edges to use. By default, 10 bins are created. If `bins` is an integer and no `range` is specified, bin edges are automatically computed from the bounds of the field

  * **range** (_None_) â a `(lower, upper)` tuple specifying a range in which to generate equal-width bins. Only applicable when `bins` is an integer or `None`

  * **auto** (_False_) â whether to automatically choose bin edges in an attempt to evenly distribute the counts in each bin. If this option is chosen, `bins` will only be used if it is an integer, and the `range` parameter is ignored




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

a tuple of

  * **counts** : `[]`

  * **edges** : `[]`

  * **other** : `0`




parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

a tuple of

  * **counts** : a list of counts in each bin

  * **edges** : an increasing list of bin edges of length `len(counts) + 1`. Note that each bin is treated as having an inclusive lower boundary and exclusive upper boundary, `[lower, upper)`, including the rightmost bin

  * **other** : the number of items outside the bins




to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Min(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Bases: `Aggregation`

Computes the minimum of a numeric field of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the minimum of a numeric field
    #
    
    aggregation = fo.Min("numeric_field")
    min = dataset.aggregate(aggregation)
    print(min)  # the min
    
    #
    # Compute the minimum of a numeric list field
    #
    
    aggregation = fo.Min("numeric_list_field")
    min = dataset.aggregate(aggregation)
    print(min)  # the min
    
    #
    # Compute the minimum of a transformation of a numeric field
    #
    
    aggregation = fo.Min(2 * (F("numeric_field") + 1))
    min = dataset.aggregate(aggregation)
    print(min)  # the min
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`None`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the minimum value

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Max(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Bases: `Aggregation`

Computes the maximum of a numeric field of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ or _date_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")

  * [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the maximum of a numeric field
    #
    
    aggregation = fo.Max("numeric_field")
    max = dataset.aggregate(aggregation)
    print(max)  # the max
    
    #
    # Compute the maximum of a numeric list field
    #
    
    aggregation = fo.Max("numeric_list_field")
    max = dataset.aggregate(aggregation)
    print(max)  # the max
    
    #
    # Compute the maximum of a transformation of a numeric field
    #
    
    aggregation = fo.Max(2 * (F("numeric_field") + 1))
    max = dataset.aggregate(aggregation)
    print(max)  # the max
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`None`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the maximum value

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Mean(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Bases: `Aggregation`

Computes the arithmetic mean of the field values of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the mean of a numeric field
    #
    
    aggregation = fo.Mean("numeric_field")
    mean = dataset.aggregate(aggregation)
    print(mean)  # the mean
    
    #
    # Compute the mean of a numeric list field
    #
    
    aggregation = fo.Mean("numeric_list_field")
    mean = dataset.aggregate(aggregation)
    print(mean)  # the mean
    
    #
    # Compute the mean of a transformation of a numeric field
    #
    
    aggregation = fo.Mean(2 * (F("numeric_field") + 1))
    mean = dataset.aggregate(aggregation)
    print(mean)  # the mean
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`0`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the mean

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Quantiles(_field_or_expr_ , _quantiles_ , _expr =None_, _safe =False_)#
    

Bases: `Aggregation`

Computes the quantile(s) of the field values of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the quantiles of a numeric field
    #
    
    aggregation = fo.Quantiles("numeric_field", [0.1, 0.5, 0.9])
    quantiles = dataset.aggregate(aggregation)
    print(quantiles)  # the quantiles
    
    #
    # Compute the quantiles of a numeric list field
    #
    
    aggregation = fo.Quantiles("numeric_list_field", [0.1, 0.5, 0.9])
    quantiles = dataset.aggregate(aggregation)
    print(quantiles)  # the quantiles
    
    #
    # Compute the mean of a transformation of a numeric field
    #
    
    aggregation = fo.Quantiles(2 * (F("numeric_field") + 1), [0.1, 0.5, 0.9])
    quantiles = dataset.aggregate(aggregation)
    print(quantiles)  # the quantiles
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **quantiles** â the quantile or iterable of quantiles to compute. Each quantile must be a numeric value in `[0, 1]`

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`None` or `[None, None, None]`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the quantile or list of quantiles

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Schema(_field_or_expr_ , _expr =None_, _dynamic_only =False_, __doc_type =None_, __include_private =False_)#
    

Bases: `Aggregation`

Extracts the names and types of the attributes of a specified embedded document field across all samples in a collection.

Schema aggregations are useful for detecting the presence and types of dynamic attributes of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields across a collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    
    sample1 = fo.Sample(
        filepath="image1.png",
        ground_truth=fo.Detections(
            detections=[
                fo.Detection(
                    label="cat",
                    bounding_box=[0.1, 0.1, 0.4, 0.4],
                    foo="bar",
                    hello=True,
                ),
                fo.Detection(
                    label="dog",
                    bounding_box=[0.5, 0.5, 0.4, 0.4],
                    hello=None,
                )
            ]
        )
    )
    
    sample2 = fo.Sample(
        filepath="image2.png",
        ground_truth=fo.Detections(
            detections=[
                fo.Detection(
                    label="rabbit",
                    bounding_box=[0.1, 0.1, 0.4, 0.4],
                    foo=None,
                ),
                fo.Detection(
                    label="squirrel",
                    bounding_box=[0.5, 0.5, 0.4, 0.4],
                    hello="there",
                ),
            ]
        )
    )
    
    dataset.add_samples([sample1, sample2])
    
    #
    # Get schema of all dynamic attributes on the detections in a
    # `Detections` field
    #
    
    aggregation = fo.Schema("ground_truth.detections", dynamic_only=True)
    print(dataset.aggregate(aggregation))
    # {'foo': StringField, 'hello': [BooleanField, StringField]}
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **dynamic_only** (_False_) â whether to only include dynamically added attributes




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`{}`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances. If a fieldâs values takes multiple non-None types, the list of observed types will be returned

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.ListSchema(_field_or_expr_ , _expr =None_)#
    

Bases: `Aggregation`

Extracts the value type(s) in a specified list field across all samples in a collection.

Examples:
    
    
    from datetime import datetime
    import fiftyone as fo
    
    dataset = fo.Dataset()
    
    sample1 = fo.Sample(
        filepath="image1.png",
        ground_truth=fo.Classification(
            label="cat",
            info=[
                fo.DynamicEmbeddedDocument(
                    task="initial_annotation",
                    author="Alice",
                    timestamp=datetime(1970, 1, 1),
                    notes=["foo", "bar"],
                ),
                fo.DynamicEmbeddedDocument(
                    task="editing_pass",
                    author="Bob",
                    timestamp=datetime.utcnow(),
                ),
            ],
        ),
    )
    
    sample2 = fo.Sample(
        filepath="image2.png",
        ground_truth=fo.Classification(
            label="dog",
            info=[
                fo.DynamicEmbeddedDocument(
                    task="initial_annotation",
                    author="Bob",
                    timestamp=datetime(2018, 10, 18),
                    notes=["spam", "eggs"],
                ),
            ],
        ),
    )
    
    dataset.add_samples([sample1, sample2])
    
    # Determine that `ground_truth.info` contains embedded documents
    aggregation = fo.ListSchema("ground_truth.info")
    print(dataset.aggregate(aggregation))
    # fo.EmbeddedDocumentField
    
    # Determine the fields of the embedded documents in the list
    aggregation = fo.Schema("ground_truth.info[]")
    print(dataset.aggregate(aggregation))
    # {'task': StringField, ..., 'notes': ListField}
    
    # Determine the type of the values in the nested `notes` list field
    # Since `ground_truth.info` is not yet declared on the dataset's
    # schema, we must manually include `[]` to unwind the info lists
    aggregation = fo.ListSchema("ground_truth.info[].notes")
    print(dataset.aggregate(aggregation))
    # fo.StringField
    
    # Declare the `ground_truth.info` field
    dataset.add_sample_field(
        "ground_truth.info",
        fo.ListField,
        subfield=fo.EmbeddedDocumentField,
        embedded_doc_type=fo.DynamicEmbeddedDocument,
    )
    
    # Now we can inspect the nested `notes` field without unwinding
    aggregation = fo.ListSchema("ground_truth.info.notes")
    print(dataset.aggregate(aggregation))
    # fo.StringField
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`[]`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") or list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances describing the value type(s) in the list

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Std(_field_or_expr_ , _expr =None_, _safe =False_, _sample =False_)#
    

Bases: `Aggregation`

Computes the standard deviation of the field values of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the standard deviation of a numeric field
    #
    
    aggregation = fo.Std("numeric_field")
    std = dataset.aggregate(aggregation)
    print(std)  # the standard deviation
    
    #
    # Compute the standard deviation of a numeric list field
    #
    
    aggregation = fo.Std("numeric_list_field")
    std = dataset.aggregate(aggregation)
    print(std)  # the standard deviation
    
    #
    # Compute the standard deviation of a transformation of a numeric field
    #
    
    aggregation = fo.Std(2 * (F("numeric_field") + 1))
    std = dataset.aggregate(aggregation)
    print(std)  # the standard deviation
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values

  * **sample** (_False_) â whether to compute the sample standard deviation rather than the population standard deviation




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`0`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the standard deviation

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Sum(_field_or_expr_ , _expr =None_, _safe =False_)#
    

Bases: `Aggregation`

Computes the sum of the field values of a collection.

`None`-valued fields are ignored.

This aggregation is typically applied to _numeric_ field types (or lists of such types):

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Compute the sum of a numeric field
    #
    
    aggregation = fo.Sum("numeric_field")
    total = dataset.aggregate(aggregation)
    print(total)  # the sum
    
    #
    # Compute the sum of a numeric list field
    #
    
    aggregation = fo.Sum("numeric_list_field")
    total = dataset.aggregate(aggregation)
    print(total)  # the sum
    
    #
    # Compute the sum of a transformation of a numeric field
    #
    
    aggregation = fo.Sum(2 * (F("numeric_field") + 1))
    total = dataset.aggregate(aggregation)
    print(total)  # the sum
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **safe** (_False_) â whether to ignore nan/inf values when dealing with floating point values




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()`.  
`to_mongo`(sample_collection[,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`0`

parse_result(_d_)#
    

Parses the output of `to_mongo()`.

Parameters:
    

**d** â the result dict

Returns:
    

the sum

to_mongo(_sample_collection_ , _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

class fiftyone.core.aggregations.Values(_field_or_expr_ , _expr =None_, _missing_value =None_, _unwind =False_, __allow_missing =False_, __big_result =True_, __raw =False_, __field =None_, __lazy =False_)#
    

Bases: `Aggregation`

Extracts the values of the field from all samples in a collection.

Values aggregations are useful for efficiently extracting a slice of field or embedded field values across all samples in a collection. See the examples below for more details.

The dual function of `Values` is [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values"), which can be used to efficiently set a field or embedded field of all samples in a collection by providing lists of values of same structure returned by this aggregation.

Note

Unlike other aggregations, `Values` does not automatically unwind list fields, which ensures that the returned values match the potentially-nested structure of the documents.

You can opt-in to unwinding specific list fields using the `[]` syntax, or you can pass the optional `unwind=True` parameter to unwind all supported list fields. See [Aggregating list fields](https://docs.voxel51.com/user_guide/using_aggregations.html#aggregations-list-fields) for more information.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                numeric_field=1.0,
                numeric_list_field=[1, 2, 3],
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                numeric_field=4.0,
                numeric_list_field=[1, 2],
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                numeric_field=None,
                numeric_list_field=None,
            ),
        ]
    )
    
    #
    # Get all values of a field
    #
    
    aggregation = fo.Values("numeric_field")
    values = dataset.aggregate(aggregation)
    print(values)  # [1.0, 4.0, None]
    
    #
    # Get all values of a list field
    #
    
    aggregation = fo.Values("numeric_list_field")
    values = dataset.aggregate(aggregation)
    print(values)  # [[1, 2, 3], [1, 2], None]
    
    #
    # Get all values of transformed field
    #
    
    aggregation = fo.Values(2 * (F("numeric_field") + 1))
    values = dataset.aggregate(aggregation)
    print(values)  # [4.0, 10.0, None]
    
    #
    # Get values from a label list field
    #
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # list of `Detections`
    aggregation = fo.Values("ground_truth")
    detections = dataset.aggregate(aggregation)
    
    # list of lists of `Detection` instances
    aggregation = fo.Values("ground_truth.detections")
    detections = dataset.aggregate(aggregation)
    
    # list of lists of detection labels
    aggregation = fo.Values("ground_truth.detections.label")
    labels = dataset.aggregate(aggregation)
    

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to aggregate

  * **expr** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before aggregating

  * **missing_value** (_None_) â a value to insert for missing or `None`-valued fields

  * **unwind** (_False_) â whether to automatically unwind all recognized list fields (True) or unwind all list fields except the top-level sample field (-1)




**Methods:**

`default_result`() | Returns the default result for this aggregation.  
---|---  
`parse_result`(d) | Parses the output of `to_mongo()` when the result is a dict or returns an expression that can be evaluated lazily.  
`to_mongo`(sample_collection[,Â big_field,Â context]) | Returns the MongoDB aggregation pipeline for this aggregation.  
  
**Attributes:**

`expr` | The expression being computed, if any.  
---|---  
`field_name` | The name of the field being computed on, if any.  
`safe` | Whether nan/inf values will be ignored when dealing with floating point values.  
  
default_result()#
    

Returns the default result for this aggregation.

Returns:
    

`[]`

parse_result(_d_)#
    

Parses the output of `to_mongo()` when the result is a dict or returns an expression that can be evaluated lazily.

Parameters:
    

**d** â the result dict or None

Returns:
    

the list of field values or a lazy partial result

to_mongo(_sample_collection_ , _big_field ='values'_, _context =None_)#
    

Returns the MongoDB aggregation pipeline for this aggregation.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the aggregation is being applied

  * **context** (_None_) â a path context from which to resolve



Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property expr#
    

The expression being computed, if any.

property field_name#
    

The name of the field being computed on, if any.

property safe#
    

Whether nan/inf values will be ignored when dealing with floating point values.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
