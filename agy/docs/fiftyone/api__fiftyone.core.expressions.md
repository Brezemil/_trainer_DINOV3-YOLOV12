---
source_url: https://docs.voxel51.com/api/fiftyone.core.expressions.html
---

# fiftyone.core.expressions#

Expressions for [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage") definitions.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`to_mongo`(expr[,Â prefix]) | Converts an expression to its MongoDB representation.  
---|---  
`is_frames_expr`(expr) | Determines whether the given expression involves a `"frames"` field.  
`get_group_slices`(expr) | Extracts the group slices from the given expression, if any.  
  
**Classes:**

`ViewExpression`(expr) | An expression defining a possibly-complex manipulation of a document.  
---|---  
`ViewField`([name]) | A `ViewExpression` that refers to a field or embedded field of a document.  
`ObjectId`(oid) | A `ViewExpression` that refers to an [ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId) of a document.  
  
**Data:**

`VALUE` | A `ViewExpression` that refers to the current `$$value` in a MongoDB reduction expression.  
---|---  
  
fiftyone.core.expressions.to_mongo(_expr_ , _prefix =None_)#
    

Converts an expression to its MongoDB representation.

Parameters:
    

  * **expr** â a `ViewExpression` or an already serialized [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions)

  * **prefix** (_None_) â an optional prefix to prepend to all `ViewField` instances in the expression



Returns:
    

a MongoDB expression

fiftyone.core.expressions.is_frames_expr(_expr_)#
    

Determines whether the given expression involves a `"frames"` field.

Parameters:
    

**expr** â 

a `ViewExpression` or an already serialized [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions)

Returns:
    

True/False

fiftyone.core.expressions.get_group_slices(_expr_)#
    

Extracts the group slices from the given expression, if any.

Parameters:
    

**expr** â 

a `ViewExpression` or an already serialized [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions)

Returns:
    

a (possibly-empty) list of group slices

class fiftyone.core.expressions.ViewExpression(_expr_)#
    

Bases: `object`

An expression defining a possibly-complex manipulation of a document.

View expressions enable you to specify manipulations of documents that can then be executed on your data in the context of a [`fiftyone.core.stages.ViewStage`](api__fiftyone.core.stages.md#fiftyone.core.stages.ViewStage "fiftyone.core.stages.ViewStage").

Typically, `ViewExpression` instances are built by creating one or more `ViewField` instances and then defining the desired operation by recursively invoking methods on these objects:
    
    
    from fiftyone import ViewField as F
    
    # An expression that tests whether the `confidence` field of a document
    # is greater than 0.9
    F("confidence") > 0.9
    
    # An expression that computes the area of a bounding box
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    F("bounding_box")[2] * F("bounding_box")[3]
    
    #
    # A more complex expression that returns one of three strings based on
    # the number of high confidence predictions in the `detections` field
    # of a document with the label "cat" or "dog" after normalizing to
    # lowercase
    #
    F("detections").map(
        F().set_field("label", F("label").lower())
    ).filter(
        F("label").is_in(("cat", "dog")) & (F("confidence") > 0.9)
    ).length().switch(
        {
            (F() >= 10): "zoo",
            (F() > 2) & (F() < 10): "party",
            (F() <= 2): "home",
        }
    )
    

There are a few cases where you may need to instantitate a `ViewExpression` directly, typically when you need to write an expression that begins with a literal Python value:
    
    
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    # Concatenates the "-animal" string to the `label` field of a document
    F("label").concat("-animal")
    
    # Prepends the "animal-" string to the `label` field
    E("animal-").concat(F("label"))
    
    # Appends the strings "test" and "validation" to the contents of the
    # `tags` field array
    # assumed to be an array
    F("tags").extend(["test", "validation"])
    
    # Prepends the "test" and "validation" strings to the `tags` field
    E(["test", "validation"]).extend(F("tags"))
    

See [MongoDB expressions](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) for more details about the underlying expression language that this class encapsulates.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    #
    # Create a view that only contains predictions whose bounding boxes
    # have area < 0.2 with confidence > 0.9, and only include samples with
    # at least 15 such objects
    #
    view = dataset.filter_labels(
        "predictions",
        (bbox_area < 0.2) & (F("confidence") > 0.9)
    ).match(
        F("predictions.detections").length() > 15
    )
    
    session = fo.launch_app(view=view)
    

__eq__(_other_)#
    

Determines whether this expression is equal to the given value or expression, `self == other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "cifar10", split="test", max_samples=500, shuffle=True
    )
    
    # Get samples whose ground truth `label` is "airplane"
    view = dataset.match(F("ground_truth.label") == "airplane")
    
    print(view.distinct("ground_truth.label"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__ge__(_other_)#
    

Determines whether this expression is greater than or equal to the given value or expression, `self >= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness") >= 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__gt__(_other_)#
    

Determines whether this expression is greater than the given value or expression, `self >= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is > 0.5
    view = dataset.match(F("uniqueness") > 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__le__(_other_)#
    

Determines whether this expression is less than or equal to the given value or expression, `self <= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is <= 0.5
    view = dataset.match(F("uniqueness") <= 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

  * **other** â a literal value or `ViewExpression`

  * **other** â a `ViewExpression` or a python primitive understood by MongoDB



Returns:
    

a `ViewExpression`

__lt__(_other_)#
    

Determines whether this expression is less than the given value or expression, `self <= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is < 0.5
    view = dataset.match(F("uniqueness") < 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__ne__(_other_)#
    

Determines whether this expression is not equal to the given value or expression, `self != other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "cifar10", split="test", max_samples=500, shuffle=True
    )
    
    # Get samples whose ground truth `label` is NOT "airplane"
    view = dataset.match(F("ground_truth.label") != "airplane")
    
    print("airplane" in view.distinct("ground_truth.label"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__and__(_other_)#
    

Computes the logical AND of this expression and the given value or expression, `self & other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions with label "cat" and confidence > 0.9
    view = dataset.filter_labels(
        "predictions",
        (F("label") == "cat") & (F("confidence") > 0.9)
    )
    
    print(view.count_values("predictions.detections.label"))
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__invert__()#
    

Inverts this expression, `~self`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a new field to one sample
    sample = dataset.first()
    sample["new_field"] = ["hello", "there"]
    sample.save()
    
    # Get samples that do NOT have a value for `new_field`
    view = dataset.match(~F("new_field").exists())
    
    print(len(view))
    

Returns:
    

a `ViewExpression`

__or__(_other_)#
    

Computes the logical OR of this expression and the given value or expression, `self | other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions with label "cat" or confidence > 0.9
    view = dataset.filter_labels(
        "predictions",
        (F("label") == "cat") | (F("confidence") > 0.9)
    )
    
    print(view.count_values("predictions.detections.label"))
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__abs__()#
    

Computes the absolute value of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(abs(F("uniqueness") - 0.5) < 0.25)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__add__(_other_)#
    

Adds the given value to this expression, which must resolve to a numeric value, `self + other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    manhattan_dist = F("bounding_box")[0] + F("bounding_box")[1]
    
    # Only contains predictions whose bounding boxes' upper left corner
    # is a Manhattan distance of at least 1 from the origin
    dataset.filter_labels("predictions, manhattan_dist > 1)
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__ceil__()#
    

Computes the ceiling of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match(math.ceil(F("uniqueness") + 0.5) == 2)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__floor__()#
    

Computes the floor of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match(math.floor(F("uniqueness") + 0.5) == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__round__(_place =0_)#
    

Rounds this expression, which must resolve to a numeric value, at the given decimal place.

Positive values of `place` will round to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.57
    

Negative values of `place` will round digits left of the decimal:
    
    
    place=-2: 1234.5678 --> 1200
    

Parameters:
    

**place** (_0_) â the decimal place at which to round. Must be an integer in range `(-20, 100)`

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(round(2 * F("uniqueness")) == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__mod__(_other_)#
    

Computes the modulus of this expression, which must resolve to a numeric value, `self % other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with an even number of predictions
    view = dataset.match(
        (F("predictions.detections").length() % 2) == 0
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__mul__(_other_)#
    

Computes the product of the given value and this expression, which must resolve to a numeric value, `self * other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only contains predictions whose bounding box area is > 0.2
    view = dataset.filter_labels("predictions", bbox_area > 0.2)
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__pow__(_power_ , _modulo =None_)#
    

Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5) ** 2 +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5) ** 2
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**power** â the power

Returns:
    

a `ViewExpression`

__sub__(_other_)#
    

Subtracts the given value from this expression, which must resolve to a numeric value, `self - other`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    rectangleness = abs(
        F("$metadata.width") * F("bounding_box")[2] -
        F("$metadata.height") * F("bounding_box")[3]
    )
    
    # Only contains predictions whose bounding boxes are within 1 pixel
    # of being square
    view = (
        dataset
        .select_fields("predictions")
        .filter_labels("predictions", rectangleness <= 1)
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__truediv__(_other_)#
    

Divides this expression, which must resolve to a numeric value, by the given value, `self / other`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    aspect_ratio = (
        (F("$metadata.width") * F("bounding_box")[2]) /
        (F("$metadata.height") * F("bounding_box")[3])
    )
    
    # Only contains predictions whose aspect ratio is > 2
    view = (
        dataset
        .select_fields("predictions")
        .filter_labels("predictions", aspect_ratio > 2)
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__getitem__(_idx_or_slice_)#
    

Returns the element or slice of this expression, which must resolve to an array.

All of the typical slicing operations are supported, except for specifying a non-unit step:
    
    
    expr[3]      # the fourth element
    expr[-1]     # the last element
    expr[:10]    # the first (up to) 10 elements
    expr[-3:]    # the last (up to) 3 elements
    expr[3:10]   # the fourth through tenth elements
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only contains objects in the `predictions` field with area > 0.2
    view = dataset.filter_labels("predictions", bbox_area > 0.2)
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**idx_or_slice** â the index or slice

Returns:
    

a `ViewExpression`

Parameters:
    

**expr** â the MongoDB expression

**Attributes:**

`is_frozen` | Whether this expression's prefix is frozen.  
---|---  
  
**Methods:**

`to_mongo`([prefix]) | Returns a MongoDB representation of the expression.  
---|---  
`exists`([bool]) | Determines whether this expression, which must resolve to a field, exists and is not None.  
`abs`() | Computes the absolute value of this expression, which must resolve to a numeric value.  
`floor`() | Computes the floor of this expression, which must resolve to a numeric value.  
`ceil`() | Computes the ceiling of this expression, which must resolve to a numeric value.  
`round`([place]) | Rounds this expression, which must resolve to a numeric value, at the given decimal place.  
`trunc`([place]) | Truncates this expression, which must resolve to a numeric value, at the specified decimal place.  
`exp`() | Raises Euler's number to this expression, which must resolve to a numeric value.  
`ln`() | Computes the natural logarithm of this expression, which must resolve to a numeric value.  
`log`(base) | Computes the logarithm base `base` of this expression, which must resolve to a numeric value.  
`log10`() | Computes the logarithm base 10 of this expression, which must resolve to a numeric value.  
`pow`(power) | Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.  
`sqrt`() | Computes the square root of this expression, which must resolve to a numeric value.  
`cos`() | Computes the cosine of this expression, which must resolve to a numeric value, in radians.  
`cosh`() | Computes the hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.  
`sin`() | Computes the sine of this expression, which must resolve to a numeric value, in radians.  
`sinh`() | Computes the hyperbolic sine of this expression, which must resolve to a numeric value, in radians.  
`tan`() | Computes the tangent of this expression, which must resolve to a numeric value, in radians.  
`tanh`() | Computes the hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.  
`arccos`() | Computes the inverse cosine of this expression, which must resolve to a numeric value, in radians.  
`arccosh`() | Computes the inverse hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.  
`arcsin`() | Computes the inverse sine of this expression, which must resolve to a numeric value, in radians.  
`arcsinh`() | Computes the inverse hyperbolic sine of this expression, which must resolve to a numeric value, in radians.  
`arctan`() | Computes the inverse tangent of this expression, which must resolve to a numeric value, in radians.  
`arctanh`() | Computes the inverse hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.  
`type`() | Returns the type string of this expression.  
`is_null`() | Determines whether this expression is null.  
`is_number`() | Determines whether this expression is a number.  
`is_string`() | Determines whether this expression is a string.  
`is_array`() | Determines whether this expression is an array.  
`is_missing`() | Determines whether this expression refers to a missing field.  
`is_in`(values) | Creates an expression that returns a boolean indicating whether `self in values`.  
`to_bool`() | Converts the expression to a boolean value.  
`to_int`() | Converts the expression to an integer value.  
`to_double`() | Converts the expression to a double precision value.  
`to_string`() | Converts the expression to a string value.  
`to_date`() | Converts the expression to a date value.  
`apply`(expr) | Applies the given expression to this expression.  
`if_else`(true_expr,Â false_expr) | Returns either `true_expr` or `false_expr` depending on the value of this expression, which must resolve to a boolean.  
`if_null`(false_expr) | Returns either this expression or `false_expr` if this expression is null.  
`cases`(mapping[,Â default]) | Applies a case statement to this expression, which effectively computes the following pseudocode.  
`switch`(mapping[,Â default]) | Applies a switch statement to this expression, which effectively computes the given pseudocode.  
`map_values`(mapping) | Replaces this expression with the corresponding value in the provided mapping dict, if it is present as a key.  
`set_field`(field,Â value_or_expr[,Â relative]) | Sets the specified field or embedded field of this expression, which must resolve to a document, to the given value or expression.  
`let_in`(expr) | Returns an equivalent expression where this expression is defined as a variable that is used wherever necessary in the given expression.  
`min`([value]) | Returns the minimum value of either this expression, which must resolve to an array, or the minimum of this expression and the given value.  
`max`([value]) | Returns the maximum value of either this expression, which must resolve to an array, or the maximum of this expression and the given value.  
`length`() | Computes the length of this expression, which must resolve to an array.  
`contains`(values[,Â all]) | Checks whether this expression, which must resolve to an array, contains any of the given values.  
`is_subset`(values) | Checks whether this expression's contents, which must resolve to an array, are a subset of the given array or array expression's contents.  
`set_equals`(*args) | Checks whether this expression, which must resolve to an array, contains the same distinct values as each of the given array(s) or array expression(s).  
`unique`() | Returns an array containing the unique values in this expression, which must resolve to an array.  
`union`(*args) | Computes the set union of this expression, which must resolve to an array, and the given array(s) or array expression(s).  
`intersection`(*args) | Computes the set intersection of this expression, which must resolve to an array, and the given array(s) or array expression(s).  
`difference`(values) | Computes the set difference of this expression, which must resolve to an array, and the given array or array expression.  
`reverse`() | Reverses the order of the elements in the expression, which must resolve to an array.  
`sort`([key,Â numeric,Â reverse]) | Sorts this expression, which must resolve to an array.  
`filter`(expr) | Applies the given filter to the elements of this expression, which must resolve to an array.  
`map`(expr) | Applies the given expression to the elements of this expression, which must resolve to an array.  
`reduce`(expr[,Â init_val]) | Applies the given reduction to this expression, which must resolve to an array, and returns the single value computed.  
`prepend`(value) | Prepends the given value to this expression, which must resolve to an array.  
`append`(value) | Appends the given value to this expression, which must resolve to an array.  
`insert`(index,Â value) | Inserts the value before the given index in this expression, which must resolve to an array.  
`extend`(*args) | Concatenates the given array(s) or array expression(s) to this expression, which must resolve to an array.  
`sum`() | Returns the sum of the values in this expression, which must resolve to a numeric array.  
`mean`() | Returns the average value in this expression, which must resolve to a numeric array.  
`std`([sample]) | Returns the standard deviation of the values in this expression, which must resolve to a numeric array.  
`join`(delimiter) | Joins the elements of this expression, which must resolve to a string array, by the given delimiter.  
`substr`([start,Â end,Â count]) | Extracts the specified substring from this expression, which must resolve to a string.  
`strlen`() | Computes the length of this expression, which must resolve to a string.  
`lower`() | Converts this expression, which must resolve to a string, to lowercase.  
`upper`() | Converts this expression, which must resolve to a string, to uppercase.  
`concat`(*args) | Concatenates the given string(s) to this expression, which must resolve to a string.  
`strip`([chars]) | Removes whitespace characters from the beginning and end of this expression, which must resolve to a string.  
`lstrip`([chars]) | Removes whitespace characters from the beginning of this expression, which must resolve to a string.  
`rstrip`([chars]) | Removes whitespace characters from the end of this expression, which must resolve to a string.  
`replace`(old,Â new) | Replaces all occurrences of `old` with `new` in this expression, which must resolve to a string.  
`re_match`(regex[,Â options]) | Performs a regular expression pattern match on this expression, which must resolve to a string.  
`starts_with`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, starts with the given string or string(s).  
`ends_with`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, ends with the given string or string(s).  
`contains_str`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, contains the given string or string(s).  
`matches_str`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, exactly matches the given string or string(s).  
`split`(delimiter[,Â maxsplit]) | Splits this expression, which must resolve to a string, by the given delimiter.  
`rsplit`(delimiter[,Â maxsplit]) | Splits this expression, which must resolve to a string, by the given delimiter.  
`millisecond`() | Returns the millisecond portion of this date expression (in UTC) as an integer between 0 and 999.  
`second`() | Returns the second portion of this date expression (in UTC) as a number between 0 and 59.  
`minute`() | Returns the minute portion of this date expression (in UTC) as a number between 0 and 59.  
`hour`() | Returns the hour portion of this date expression (in UTC) as a number between 0 and 23.  
`day_of_week`() | Returns the day of the week of this date expression (in UTC) as a number between 1 (Sunday) and 7 (Saturday).  
`day_of_month`() | Returns the day of the month of this date expression (in UTC) as a number between 1 and 31.  
`day_of_year`() | Returns the day of the year of this date expression (in UTC) as a number between 1 and 366.  
`week`() | Returns the week of the year of this date expression (in UTC) as a number between 0 and 53.  
`month`() | Returns the month of this date expression (in UTC) as a number between 1 and 12.  
`year`() | Returns the year of this date expression (in UTC).  
`literal`(value) | Returns an expression representing the given value without parsing.  
`rand`() | Returns an expression that generates a uniform random float in `[0, 1]` each time it is called.  
`randn`() | Returns an expression that generates a sample from the standard Gaussian distribution each time it is called.  
`any`(exprs) | Checks whether any of the given expressions evaluate to True.  
`all`(exprs) | Checks whether all of the given expressions evaluate to True.  
`range`(start[,Â stop]) | Returns an array expression containing the sequence of integers from the specified start (inclusive) to stop (exclusive).  
`enumerate`(array[,Â start]) | Returns an array of `[index, element]` pairs enumerating the elements of the given expression, which must resolve to an array.  
`zip`(*args[,Â use_longest,Â defaults]) | Zips the given expressions, which must resolve to arrays, into an array whose ith element is an array containing the ith element from each input array.  
  
property is_frozen#
    

Whether this expressionâs prefix is frozen.

to_mongo(_prefix =None_)#
    

Returns a MongoDB representation of the expression.

Parameters:
    

**prefix** (_None_) â an optional prefix to prepend to all `ViewField` instances in the expression

Returns:
    

a MongoDB expression

exists(_bool =True_)#
    

Determines whether this expression, which must resolve to a field, exists and is not None.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "quickstart", dataset_name=fo.get_default_dataset_name()
    )
    
    # Add a new field to one sample
    sample = dataset.first()
    sample["new_field"] = ["hello", "there"]
    sample.save()
    
    # Get samples that have a value for `new_field`
    view = dataset.match(F("new_field").exists())
    
    print(len(view))
    

Parameters:
    

**bool** (_True_) â whether to determine whether this expression exists (True) or is None or non-existent (False)

Returns:
    

a `ViewExpression`

abs()#
    

Computes the absolute value of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match((F("uniqueness") - 0.5).abs() < 0.25)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

floor()#
    

Computes the floor of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match((F("uniqueness") + 0.5).floor() == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

ceil()#
    

Computes the ceiling of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match((F("uniqueness") + 0.5).ceil() == 2)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

round(_place =0_)#
    

Rounds this expression, which must resolve to a numeric value, at the given decimal place.

Positive values of `place` will round to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.57
    

Negative values of `place` will round `place` digits left of the decimal:
    
    
    place=-1: 1234.5678 --> 1230
    

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match((2 * F("uniqueness")).round() == 1)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**place** (_0_) â the decimal place at which to round. Must be an integer in range `(-20, 100)`

Returns:
    

a `ViewExpression`

trunc(_place =0_)#
    

Truncates this expression, which must resolve to a numeric value, at the specified decimal place.

Positive values of `place` will truncate to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.56
    

Negative values of `place` will replace `place` digits left of the decimal with zero:
    
    
    place=-1: 1234.5678 --> 1230
    

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Only contains samples whose height is in [500, 600) pixels
    view = dataset.match(F("metadata.height").trunc(-2) == 500)
    
    print(view.bounds("metadata.height"))
    

Parameters:
    

**place** (_0_) â the decimal place at which to truncate

Returns:
    

a `ViewExpression`

exp()#
    

Raises Eulerâs number to this expression, which must resolve to a numeric value.

Returns:
    

a `ViewExpression`

ln()#
    

Computes the natural logarithm of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").ln() >= math.log(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

log(_base_)#
    

Computes the logarithm base `base` of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").log(2) >= math.log2(0.5))
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**base** â the logarithm base

Returns:
    

a `ViewExpression`

log10()#
    

Computes the logarithm base 10 of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").log10() >= math.log10(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

pow(_power_)#
    

Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5).pow(2) +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5).pow(2)
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**power** â the power

Returns:
    

a `ViewExpression`

sqrt()#
    

Computes the square root of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5) ** 2 +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5) ** 2
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Returns:
    

a `ViewExpression`

cos()#
    

Computes the cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `cos()`
    view = dataset.match(F("uniqueness").cos() <= np.cos(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

cosh()#
    

Computes the hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `cosh()`
    view = dataset.match(F("uniqueness").cosh() >= np.cosh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

sin()#
    

Computes the sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `sin()`
    view = dataset.match(F("uniqueness").sin() >= np.sin(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

sinh()#
    

Computes the hyperbolic sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `sinh()`
    view = dataset.match(F("uniqueness").sinh() >= np.sinh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

tan()#
    

Computes the tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `tan()`
    view = dataset.match(F("uniqueness").tan() >= np.tan(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

tanh()#
    

Computes the hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `tanh()`
    view = dataset.match(F("uniqueness").tanh() >= np.tanh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arccos()#
    

Computes the inverse cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arccos()`
    view = dataset.match(F("uniqueness").arccos() <= np.arccos(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arccosh()#
    

Computes the inverse hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arccosh()`
    view = dataset.match((1 + F("uniqueness")).arccosh() >= np.arccosh(1.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arcsin()#
    

Computes the inverse sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arcsin()`
    view = dataset.match(F("uniqueness").arcsin() >= np.arcsin(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arcsinh()#
    

Computes the inverse hyperbolic sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arcsinh()`
    view = dataset.match(F("uniqueness").arcsinh() >= np.arcsinh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arctan()#
    

Computes the inverse tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arctan()`
    view = dataset.match(F("uniqueness").arctan() >= np.arctan(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arctanh()#
    

Computes the inverse hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arctanh()`
    view = dataset.match(F("uniqueness").arctanh() >= np.arctanh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

type()#
    

Returns the type string of this expression.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/type) for more details.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    # Create a view that only contains samples with non-None uniqueness
    unique_only_view = view.match(F("uniqueness").type() != "null")
    
    print(len(unique_only_view))
    

Returns:
    

a `ViewExpression`

is_null()#
    

Determines whether this expression is null.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.25 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.25).if_else(F("uniqueness"), None)
    )
    
    # Create view that only contains samples with uniqueness = None
    not_unique_view = view.match(F("uniqueness").is_null())
    
    print(len(not_unique_view))
    

Returns:
    

`ViewExpression`

is_number()#
    

Determines whether this expression is a number.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.25 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.25).if_else(F("uniqueness"), None)
    )
    
    # Create view that only contains samples with uniqueness values
    has_unique_view = view.match(F("uniqueness").is_number())
    
    print(len(has_unique_view))
    

Returns:
    

`ViewExpression`

is_string()#
    

Determines whether this expression is a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that filepaths are strings
    view = dataset.match(F("filepath").is_string())
    
    print(len(view))
    

Returns:
    

`ViewExpression`

is_array()#
    

Determines whether this expression is an array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that tags are arrays
    view = dataset.match(F("tags").is_array())
    
    print(len(view))
    

Returns:
    

`ViewExpression`

is_missing()#
    

Determines whether this expression refers to a missing field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that `foobar` is a non-existent field on all samples
    view = dataset.match(F("foobar").is_missing())
    
    print(len(view) == len(dataset))
    

Returns:
    

`ViewExpression`

is_in(_values_)#
    

Creates an expression that returns a boolean indicating whether `self in values`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains animal predictions
    view = dataset.filter_labels(
        "predictions", F("label").is_in(ANIMALS)
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

**values** â a value or iterable of values

Returns:
    

a `ViewExpression`

to_bool()#
    

Converts the expression to a boolean value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toBool) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_bool` field that is False when
    # `uniqueness < 0.5` and True when `uniqueness >= 0.5`
    dataset.add_sample_field("uniqueness_bool", fo.BooleanField)
    view = dataset.set_field(
        "uniqueness_bool", (2.0 * F("uniqueness")).floor().to_bool()
    )
    
    print(view.count_values("uniqueness_bool"))
    

Returns:
    

a `ViewExpression`

to_int()#
    

Converts the expression to an integer value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toInt) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_int` field that contains the value of the
    # first decimal point of the `uniqueness` field
    dataset.add_sample_field("uniqueness_int", fo.IntField)
    view = dataset.set_field(
        "uniqueness_int", (10.0 * F("uniqueness")).floor().to_int()
    )
    
    print(view.count_values("uniqueness_int"))
    

Returns:
    

a `ViewExpression`

to_double()#
    

Converts the expression to a double precision value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_float` field that is 0.0 when
    # `uniqueness < 0.5` and 1.0 when `uniqueness >= 0.5`
    dataset.add_sample_field("uniqueness_float", fo.FloatField)
    view = dataset.set_field(
        "uniqueness_float", (F("uniqueness") >= 0.5).to_double()
    )
    
    print(view.count_values("uniqueness_float"))
    

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toDouble) for conversion rules.

Returns:
    

a `ViewExpression`

to_string()#
    

Converts the expression to a string value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toString) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_str` field that is "true" when
    # `uniqueness >= 0.5` and "false" when `uniqueness < 0.5`
    dataset.add_sample_field("uniqueness_str", fo.StringField)
    view = dataset.set_field(
        "uniqueness_str", (F("uniqueness") >= 0.5).to_string()
    )
    
    print(view.count_values("uniqueness_str"))
    

Returns:
    

a `ViewExpression`

to_date()#
    

Converts the expression to a date value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toDate) for conversion rules.

Examples:
    
    
    from datetime import datetime
    import pytz
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    
    sample = fo.Sample(
        filepath="image.png",
        date_ms=1000 * now.timestamp(),
        date_str=now.isoformat(),
    )
    
    dataset = fo.Dataset()
    dataset.add_sample(sample)
    
    # Convert string/millisecond representations into datetimes
    dataset.add_sample_field("date1", fo.DateTimeField)
    dataset.add_sample_field("date2", fo.DateTimeField)
    (
        dataset
        .set_field("date1", F("date_ms").to_date())
        .set_field("date2", F("date_str").to_date())
        .save()
    )
    
    print(dataset.first())
    

Returns:
    

a `ViewExpression`

apply(_expr_)#
    

Applies the given expression to this expression.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(
        F("uniqueness").apply((F() > 0.25) & (F() < 0.75))
    )
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

if_else(_true_expr_ , _false_expr_)#
    

Returns either `true_expr` or `false_expr` depending on the value of this expression, which must resolve to a boolean.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

  * **true_expr** â a `ViewExpression` or MongoDB expression dict

  * **false_expr** â a `ViewExpression` or MongoDB expression dict



Returns:
    

a `ViewExpression`

if_null(_false_expr_)#
    

Returns either this expression or `false_expr` if this expression is null. This is a shortcut for `self.is_null().if_else(false_expr, self)` and is useful for replacing null values in a field with a default value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `gt.detection.label` field to "unknown" if it does not exist
    view = dataset.set_field(
        "gt.detection.label",
        F("gt.detection.label").if_null("unknown")
    )
    

Parameters:
    

**false_expr** â a `ViewExpression` or MongoDB expression dict

Returns:
    

a `ViewExpression`

cases(_mapping_ , _default =None_)#
    

Applies a case statement to this expression, which effectively computes the following pseudocode:
    
    
    for key, value in mapping.items():
        if self == key:
            return value
    
    if default is not None:
        return default
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    # Map numeric `uniqueness` values to 1 and null values to 0
    cases_view = view.set_field(
        "uniqueness",
        F("uniqueness").type().cases({"double": 1, "null": 0}),
    )
    
    print(cases_view.count_values("uniqueness"))
    

Parameters:
    

  * **mapping** â a dict mapping literals or `ViewExpression` keys to literal or `ViewExpression` values

  * **default** (_None_) â an optional literal or `ViewExpression` to return if none of the switch branches are taken



Returns:
    

a `ViewExpression`

switch(_mapping_ , _default =None_)#
    

Applies a switch statement to this expression, which effectively computes the given pseudocode:
    
    
    for key, value in mapping.items():
        if self.apply(key):
            return value
    
    if default is not None:
        return default
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Round `uniqueness` values to either 0.25 or 0.75
    view = dataset.set_field(
        "uniqueness",
        F("uniqueness").switch(
            {
                (0.0 < F()) & (F() <= 0.5): 0.25,
                (0.5 < F()) & (F() <= 1.0): 0.75,
            },
        )
    )
    
    print(view.count_values("uniqueness"))
    

Parameters:
    

  * **mapping** â a dict mapping boolean `ViewExpression` keys to literal or `ViewExpression` values

  * **default** (_None_) â an optional literal or `ViewExpression` to return if none of the switch branches are taken



Returns:
    

a `ViewExpression`

map_values(_mapping_)#
    

Replaces this expression with the corresponding value in the provided mapping dict, if it is present as a key.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replace the `label` of all animal objects in the `predictions`
    # field with "animal"
    #
    mapping = {a: "animal" for a in ANIMALS}
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(
            F().set_field("label", F("label").map_values(mapping))
        )
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

**mapping** â a dict mapping keys to replacement values

Returns:
    

a `ViewExpression`

set_field(_field_ , _value_or_expr_ , _relative =True_)#
    

Sets the specified field or embedded field of this expression, which must resolve to a document, to the given value or expression.

By default, the provided expression is computed by applying it to this expression via `self.apply(value_or_expr)`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replaces the `label` attributes of the objects in the
    # `predictions` field according to the following rule:
    #
    #   If the `label` starts with `b`, replace it with `b`. Otherwise,
    #   replace it with "other"
    #
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(
            F().set_field(
                "label",
                F("label").re_match("^b").if_else("b", "other"),
            )
        )
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

  * **field** â the âfieldâ or âembedded.field.nameâ to set

  * **value_or_expr** â a literal value or `ViewExpression` defining the field to set

  * **relative** (_True_) â whether to compute `value_or_expr` by applying it to this expression (True), or to use it untouched (False)



Returns:
    

a `ViewExpression`

let_in(_expr_)#
    

Returns an equivalent expression where this expression is defined as a variable that is used wherever necessary in the given expression.

This method is useful when `expr` contains multiple instances of this expression, since it avoids duplicate computation of this expression in the final pipeline.

If `expr` is a simple expression such as a `ViewField`, no variable is defined and `expr` is directly returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    good_bboxes = (bbox_area > 0.25) & (bbox_area < 0.75)
    
    # Optimize the expression
    good_bboxes_opt = bbox_area.let_in(good_bboxes)
    
    # Contains predictions whose bounding box areas are in [0.25, 0.75]
    view = dataset.filter_labels("predictions", good_bboxes_opt)
    
    print(good_bboxes)
    print(good_bboxes_opt)
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

min(_value =None_)#
    

Returns the minimum value of either this expression, which must resolve to an array, or the minimum of this expression and the given value.

Missing or `None` values are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Adds a `min_area` property to the `predictions` field that
    # records the minimum prediction area in that sample
    view = dataset.set_field(
        "predictions.min_area",
        F("detections").map(bbox_area).min()
    )
    
    print(view.bounds("predictions.min_area"))
    

Parameters:
    

**value** (_None_) â an optional value to compare to

Returns:
    

a `ViewExpression`

max(_value =None_)#
    

Returns the maximum value of either this expression, which must resolve to an array, or the maximum of this expression and the given value.

Missing or `None` values are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Adds a `max_area` property to the `predictions` field that
    # records the maximum prediction area in that sample
    view = dataset.set_field(
        "predictions.max_area",
        F("detections").map(bbox_area).max()
    )
    
    print(view.bounds("predictions.max_area"))
    

Parameters:
    

**value** (_None_) â an optional value to compare to

Returns:
    

a `ViewExpression`

length()#
    

Computes the length of this expression, which must resolve to an array.

If this expressionâs value is null or missing, zero is returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with at least 15 predicted objects
    view = dataset.match(F("predictions.detections").length() >= 15)
    
    print(dataset.count())
    print(view.count())
    

Returns:
    

a `ViewExpression`

contains(_values_ , _all =False_)#
    

Checks whether this expression, which must resolve to an array, contains any of the given values.

Pass `all=True` to require that this expression contains all of the given values.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    print(dataset.count())
    
    # Only contains samples with a "cat" prediction
    view = dataset.match(
        F("predictions.detections.label").contains("cat")
    )
    print(view.count())
    
    # Only contains samples with "cat" or "dog" predictions
    view = dataset.match(
        F("predictions.detections.label").contains(["cat", "dog"])
    )
    print(view.count())
    
    # Only contains samples with "cat" and "dog" predictions
    view = dataset.match(
        F("predictions.detections.label").contains(["cat", "dog"], all=True)
    )
    print(view.count())
    

Parameters:
    

  * **values** â a value, iterable of values, or `ViewExpression` that resolves to an array of values

  * **all** (_False_) â whether this expression must contain all (True) or any (False) of the given values



Returns:
    

a `ViewExpression`

is_subset(_values_)#
    

Checks whether this expressionâs contents, which must resolve to an array, are a subset of the given array or array expressionâs contents.

The arrays are treated as sets, so duplicate values are ignored.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
                other_tags=["a", "b", "c"],
            )
        ]
    )
    
    print(dataset.values(F("tags").is_subset(F("other_tags"))))
    # [True]
    

Parameters:
    

**values** â an iterable of values or a `ViewExpression` that resolves to an array

Returns:
    

a `ViewExpression`

set_equals(_* args_)#
    

Checks whether this expression, which must resolve to an array, contains the same distinct values as each of the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are ignored.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
                other_tags=["a", "b", "b"],
            )
        ]
    )
    
    print(dataset.values(F("tags").set_equals(F("other_tags"))))
    # [True]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

unique()#
    

Returns an array containing the unique values in this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
            )
        ]
    )
    
    print(dataset.values(F("tags").unique()))
    # [['a', 'b']]
    

Returns:
    

a `ViewExpression`

union(_* args_)#
    

Computes the set union of this expression, which must resolve to an array, and the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").union(F("other_tags"))))
    # [['a', 'b', 'c']]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

intersection(_* args_)#
    

Computes the set intersection of this expression, which must resolve to an array, and the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").intersection(F("other_tags"))))
    # [['a']]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

difference(_values_)#
    

Computes the set difference of this expression, which must resolve to an array, and the given array or array expression.

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").difference(F("other_tags"))))
    # [['b']]
    

Parameters:
    

**values** â an iterable of values or a `ViewExpression` that resolves to an array

Returns:
    

a `ViewExpression`

reverse()#
    

Reverses the order of the elements in the expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    first_obj = F("predictions.detections")[0]
    last_obj = F("predictions.detections").reverse()[0]
    
    # Only contains samples whose first and last prediction have the
    # same label
    view = dataset.match(
        first_obj.apply(F("label")) == last_obj.apply(F("label"))
    )
    
    print(dataset.count())
    print(view.count())
    

Returns:
    

a `ViewExpression`

sort(_key =None_, _numeric =False_, _reverse =False_)#
    

Sorts this expression, which must resolve to an array.

If no `key` is provided, this array must contain elements whose BSON representation can be sorted by JavaScriptâs `.sort()` method.

If a `key` is provided, the array must contain documents, which are sorted by `key`, which must be a field or embedded field.

Examples:
    
    
    #
    # Sort the tags of each sample in a dataset
    #
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="im1.jpg", tags=["z", "f", "p", "a"]),
            fo.Sample(filepath="im2.jpg", tags=["y", "q", "h", "d"]),
            fo.Sample(filepath="im3.jpg", tags=["w", "c", "v", "l"]),
        ]
    )
    
    # Sort the `tags` of each sample
    view = dataset.set_field("tags", F("tags").sort())
    
    print(view.first().tags)
    
    #
    # Sort the predictions in each sample of a dataset by `confidence`
    #
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    view = dataset.set_field(
        "predictions.detections",
        F("detections").sort(key="confidence", numeric=True, reverse=True)
    )
    
    sample = view.first()
    print(sample.predictions.detections[0].confidence)
    print(sample.predictions.detections[-1].confidence)
    

Parameters:
    

  * **key** (_None_) â an optional field or `embedded.field.name` to sort by

  * **numeric** (_False_) â whether the array contains numeric values. By default, the values will be sorted alphabetically by their string representations

  * **reverse** (_False_) â whether to sort in descending order



Returns:
    

a `ViewExpression`

filter(_expr_)#
    

Applies the given filter to the elements of this expression, which must resolve to an array.

The output array will only contain elements of the input array for which `expr` returns `True`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only include predictions with `confidence` of at least 0.9
    view = dataset.set_field(
        "predictions.detections",
        F("detections").filter(F("confidence") > 0.9)
    )
    
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**expr** â a `ViewExpression` that returns a boolean

Returns:
    

a `ViewExpression`

map(_expr_)#
    

Applies the given expression to the elements of this expression, which must resolve to an array.

The output will be an array with the applied results.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only include predictions with `confidence` of at least 0.9
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(F().set_field("area", bbox_area))
    )
    
    print(view.bounds("predictions.detections.area"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

reduce(_expr_ , _init_val =0_)#
    

Applies the given reduction to this expression, which must resolve to an array, and returns the single value computed.

The provided `expr` must include the `VALUE` expression to properly define the reduction.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    from fiftyone.core.expressions import VALUE
    
    #
    # Compute the number of keypoints in each sample of a dataset
    #
    
    dataset = fo.Dataset()
    dataset.add_sample(
        fo.Sample(
            filepath="image.jpg",
            keypoints=fo.Keypoints(
                keypoints=[
                    fo.Keypoint(points=[(0, 0), (1, 1)]),
                    fo.Keypoint(points=[(0, 0), (1, 0), (1, 1), (0, 1)]),
                ]
            )
        )
    )
    
    view = dataset.set_field(
        "keypoints.count",
        F("$keypoints.keypoints").reduce(VALUE + F("points").length()),
    )
    
    print(view.first().keypoints.count)
    
    #
    # Generate a `list,of,labels` for the `predictions` of each sample
    #
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    join_labels = F("detections").reduce(
        VALUE.concat(",", F("label")), init_val=""
    ).lstrip(",")
    
    view = dataset.set_field("predictions.labels", join_labels)
    
    print(view.first().predictions.labels)
    

Parameters:
    

  * **expr** â a `ViewExpression` defining the reduction expression to apply. Must contain the `VALUE` expression

  * **init_val** (_0_) â an initial value for the reduction



Returns:
    

a `ViewExpression`

prepend(_value_)#
    

Prepends the given value to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["b", "c"]),
        ]
    )
    
    # Adds the "a" tag to each sample
    view = dataset.set_field("tags", F("tags").prepend("a"))
    
    print(view.first().tags)
    

Parameters:
    

**value** â the value or `ViewExpression`

Returns:
    

a `ViewExpression`

append(_value_)#
    

Appends the given value to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "b"]),
        ]
    )
    
    # Appends the "c" tag to each sample
    view = dataset.set_field("tags", F("tags").append("c"))
    
    print(view.first().tags)
    

Parameters:
    

**value** â the value or `ViewExpression`

Returns:
    

a `ViewExpression`

insert(_index_ , _value_)#
    

Inserts the value before the given index in this expression, which must resolve to an array.

If `index <= 0`, the value is prepended to this array. If `index >= self.length()`, the value is appended to this array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "c"]),
        ]
    )
    
    # Adds the "ready" tag to each sample
    view = dataset.set_field("tags", F("tags").insert(1, "b"))
    
    print(view.first().tags)
    

Parameters:
    

  * **index** â the index at which to insert the value

  * **value** â the value or `ViewExpression`



Returns:
    

a `ViewExpression`

extend(_* args_)#
    

Concatenates the given array(s) or array expression(s) to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "b"]),
        ]
    )
    
    # Adds the "c" and "d" tags to each sample
    view = dataset.set_field("tags", F("tags").extend(["c", "d"]))
    
    print(view.first().tags)
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

sum()#
    

Returns the sum of the values in this expression, which must resolve to a numeric array.

Missing, non-numeric, or `None`-valued elements are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the total
    # confidence of the predictions
    view = dataset.set_field(
        "predictions.total_conf",
        F("detections").map(F("confidence")).sum()
    )
    
    print(view.bounds("predictions.total_conf"))
    

Returns:
    

a `ViewExpression`

mean()#
    

Returns the average value in this expression, which must resolve to a numeric array.

Missing or `None`-valued elements are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the average
    # confidence of the predictions
    view = dataset.set_field(
        "predictions.conf_mean",
        F("detections").map(F("confidence")).mean()
    )
    
    print(view.bounds("predictions.conf_mean"))
    

Returns:
    

a `ViewExpression`

std(_sample =False_)#
    

Returns the standard deviation of the values in this expression, which must resolve to a numeric array.

Missing or `None`-valued elements are ignored.

By default, the population standard deviation is returned. If you wish to compute the sample standard deviation instead, set `sample=True`.

See <https://en.wikipedia.org/wiki/Standard_deviation#Estimation> for more information on population (biased) vs sample (unbiased) standard deviation.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the
    # standard deviation of the confidences
    view = dataset.set_field(
        "predictions.conf_std",
        F("detections").map(F("confidence")).std()
    )
    
    print(view.bounds("predictions.conf_std"))
    

Parameters:
    

**sample** (_False_) â whether to compute the sample standard deviation rather than the population standard deviation

Returns:
    

a `ViewExpression`

join(_delimiter_)#
    

Joins the elements of this expression, which must resolve to a string array, by the given delimiter.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Generate a `list,of,labels` for the `predictions` of each sample
    view = dataset.set_field(
        "predictions.labels",
        F("detections").map(F("label")).join(",")
    )
    
    print(view.first().predictions.labels)
    

Parameters:
    

**delimiter** â the delimiter string

Returns:
    

a `ViewExpression`

substr(_start =None_, _end =None_, _count =None_)#
    

Extracts the specified substring from this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Truncate the `label` of each prediction to 3 characters
    truncate_label = F().set_field("label", F("label").substr(count=3))
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(truncate_label),
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **start** (_None_) â the starting index of the substring. If negative, specifies an offset from the end of the string

  * **end** (_None_) â the ending index of the substring. If negative, specifies an offset from the end of the string

  * **count** (_None_) â the substring length to extract. If `None`, the rest of the string is returned



Returns:
    

a `ViewExpression`

strlen()#
    

Computes the length of this expression, which must resolve to a string.

If this expressionâs value is null or missing, zero is returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Records the length of each predicted object's `label`
    label_len = F().set_field("label_len", F("label").strlen())
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(label_len),
    )
    
    print(view.bounds("predictions.detections.label_len"))
    

Returns:
    

a `ViewExpression`

lower()#
    

Converts this expression, which must resolve to a string, to lowercase.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Converts all tags to lowercase
    transform_tag = F().lower()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Returns:
    

a `ViewExpression`

upper()#
    

Converts this expression, which must resolve to a string, to uppercase.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Converts all tags to uppercase
    transform_tag = F().upper()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Returns:
    

a `ViewExpression`

concat(_* args_)#
    

Concatenates the given string(s) to this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Appends "-tag" to all tags
    transform_tag = F().concat("-tag")
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

  * ***args** â one or more strings or string `ViewExpression` instances

  * **before** (_False_) â whether to position `args` before this string in the output string



Returns:
    

a `ViewExpression`

strip(_chars =None_)#
    

Removes whitespace characters from the beginning and end of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from each tag
    transform_tag = E(" ").concat(F(), " ").rstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

lstrip(_chars =None_)#
    

Removes whitespace characters from the beginning of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from the beginning of each tag
    transform_tag = E(" ").concat(F()).lstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

rstrip(_chars =None_)#
    

Removes whitespace characters from the end of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from the end of each tag
    transform_tag = F().concat(" ").rstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

replace(_old_ , _new_)#
    

Replaces all occurrences of `old` with `new` in this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Replaces "val" with "VAL" in each tag
    transform_tag = F().replace("val", "VAL")
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

  * **old** â a string or `ViewExpression` resolving to a string expression specifying the substring to replace

  * **new** â a string or `ViewExpression` resolving to a string expression specifying the replacement value



Returns:
    

a `ViewExpression`

re_match(_regex_ , _options =None_)#
    

Performs a regular expression pattern match on this expression, which must resolve to a string.

The output of the expression will be `True` if the pattern matches and `False` otherwise.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Get samples whose images are JPEGs
    #
    
    view = dataset.match(F("filepath").re_match("\.jpg$"))
    
    print(view.count())
    print(view.first().filepath)
    
    #
    # Get samples whose images are in the "/Users" directory
    #
    
    view = dataset.match(F("filepath").re_match("^/Users/"))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **regex** â the regular expression to apply. Must be a Perl Compatible Regular Expression (PCRE). See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/#regexmatch-regex) for details

  * **options** (_None_) â an optional string of regex options to apply. See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/#regexmatch-options) for the available options



Returns:
    

a `ViewExpression`

starts_with(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, starts with the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose images are in "/Users" or "/home" directories
    view = dataset.match(F("filepath").starts_with(("/Users", "/home"))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

ends_with(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, ends with the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose images are JPEGs or PNGs
    view = dataset.match(F("filepath").ends_with((".jpg", ".png")))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

contains_str(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, contains the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions whose `label` contains "be"
    view = dataset.filter_labels(
        "predictions", F("label").contains_str("be")
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

matches_str(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, exactly matches the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions whose `label` is "cat" or "dog", case
    # insensitive
    view = dataset.map_labels(
        "predictions", {"cat": "CAT", "dog": "DOG"}
    ).filter_labels(
        "predictions",
        F("label").matches_str(("cat", "dog"), case_sensitive=False)
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

split(_delimiter_ , _maxsplit =None_)#
    

Splits this expression, which must resolve to a string, by the given delimiter.

The result is a string array that contains the chunks with the delimiter removed. If the delimiter is not found, this full string is returned as a single element array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add "-good" to the first tag and then split on "-" to create two
    # tags for each sample
    view = dataset.set_field(
        "tags", F("tags")[0].concat("-good").split("-")
    )
    
    print(view.first().tags)
    

Parameters:
    

  * **delimiter** â the delimiter string or `ViewExpression` resolving to a string expression

  * **maxsplit** (_None_) â a maximum number of splits to perform, from the left



Returns:
    

a `ViewExpression`

rsplit(_delimiter_ , _maxsplit =None_)#
    

Splits this expression, which must resolve to a string, by the given delimiter.

If the number of chunks exceeds `maxsplit`, splits are only performed on the last `maxsplit` occurrences of the delimiter.

The result is a string array that contains the chunks with the delimiter removed. If the delimiter is not found, this full string is returned as a single element array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add "-ok-go" to the first tag and then split once on "-" from the
    # right to create two tags for each sample
    view = dataset.set_field(
        "tags", F("tags")[0].concat("-ok-go").rsplit("-", 1)
    )
    
    print(view.first().tags)
    

Parameters:
    

  * **delimiter** â the delimiter string or `ViewExpression` resolving to a string expression

  * **maxsplit** (_None_) â a maximum number of splits to perform, from the right



Returns:
    

a `ViewExpression`

millisecond()#
    

Returns the millisecond portion of this date expression (in UTC) as an integer between 0 and 999.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 1000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 2000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 3000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 4000),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the millisecond portion of the dates in the dataset
    print(dataset.values(F("created_at").millisecond()))
    
    # Samples with even milliseconds
    view = dataset.match(F("created_at").millisecond() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

second()#
    

Returns the second portion of this date expression (in UTC) as a number between 0 and 59.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the second portion of the dates in the dataset
    print(dataset.values(F("created_at").second()))
    
    # Samples with even seconds
    view = dataset.match(F("created_at").second() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

minute()#
    

Returns the minute portion of this date expression (in UTC) as a number between 0 and 59.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the minute portion of the dates in the dataset
    print(dataset.values(F("created_at").minute()))
    
    # Samples with even minutes
    view = dataset.match(F("created_at").minute() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

hour()#
    

Returns the hour portion of this date expression (in UTC) as a number between 0 and 23.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the hour portion of the dates in the dataset
    print(dataset.values(F("created_at").hour()))
    
    # Samples with even hours
    view = dataset.match(F("created_at").hour() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_week()#
    

Returns the day of the week of this date expression (in UTC) as a number between 1 (Sunday) and 7 (Saturday).

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 5),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 6),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 7),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the week for the dataset
    print(dataset.values(F("created_at").day_of_week()))
    
    # Samples with even days of the week
    view = dataset.match(F("created_at").day_of_week() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_month()#
    

Returns the day of the month of this date expression (in UTC) as a number between 1 and 31.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the month for the dataset
    print(dataset.values(F("created_at").day_of_month()))
    
    # Samples with even days of the month
    view = dataset.match(F("created_at").day_of_month() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_year()#
    

Returns the day of the year of this date expression (in UTC) as a number between 1 and 366.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the year for the dataset
    print(dataset.values(F("created_at").day_of_year()))
    
    # Samples with even days of the year
    view = dataset.match(F("created_at").day_of_year() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

week()#
    

Returns the week of the year of this date expression (in UTC) as a number between 0 and 53.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 2, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 3, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 4, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the weeks of the year for the dataset
    print(dataset.values(F("created_at").week()))
    
    # Samples with even months of the week
    view = dataset.match(F("created_at").week() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

month()#
    

Returns the month of this date expression (in UTC) as a number between 1 and 12.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 2, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 3, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 4, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the months of the year for the dataset
    print(dataset.values(F("created_at").month()))
    
    # Samples from even months of the year
    view = dataset.match(F("created_at").month() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

year()#
    

Returns the year of this date expression (in UTC).

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1971, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1972, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1973, 1, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the years for the dataset
    print(dataset.values(F("created_at").year()))
    
    # Samples from even years
    view = dataset.match(F("created_at").year() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

static literal(_value_)#
    

Returns an expression representing the given value without parsing.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/literal) for more information on when this method is required.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add the "$money" tag to each sample
    # The "$" character ordinarily has special meaning, so we must wrap
    # it in `literal()` in order to add it via this method
    view = dataset.set_field(
        "tags", F("tags").append(F.literal("$money"))
    )
    
    print(view.first().tags)
    

Parameters:
    

**value** â a value

Returns:
    

a `ViewExpression`

static rand()#
    

Returns an expression that generates a uniform random float in `[0, 1]` each time it is called.

Warning

This expression will generate new values each time it is used, so you likely do not want to use it to construct dataset views, since such views would produce different outputs each time they are used.

A typical usage for this expression is in conjunction with [`fiftyone.core.view.DatasetView.set_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.set_field "fiftyone.core.view.DatasetView.set_field") and [`fiftyone.core.view.DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to populate a randomized field on a dataset.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    #
    # Populate a new `rand` field with random numbers
    #
    
    dataset.add_sample_field("rand", fo.FloatField)
    dataset.set_field("rand", E.rand()).save("rand")
    
    print(dataset.bounds("rand"))
    
    #
    # Create a view that contains a different 10%% of the dataset each
    # time it is used
    #
    
    view = dataset.match(E.rand() < 0.1)
    
    print(view.first().id)
    print(view.first().id)  # probably different!
    

Returns:
    

a `ViewExpression`

static randn()#
    

Returns an expression that generates a sample from the standard Gaussian distribution each time it is called.

Warning

This expression will generate new values each time it is used, so you likely do not want to use it to construct dataset views, since such views would produce different outputs each time they are used.

A typical usage for this expression is in conjunction with [`fiftyone.core.view.DatasetView.set_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.set_field "fiftyone.core.view.DatasetView.set_field") and [`fiftyone.core.view.DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to populate a randomized field on a dataset.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    #
    # Populate a new `randn` field with random numbers
    #
    
    dataset.add_sample_field("randn", fo.FloatField)
    dataset.set_field("randn", E.randn()).save("randn")
    
    print(dataset.bounds("randn"))
    
    #
    # Create a view that contains a different 50%% of the dataset each
    # time it is used
    #
    
    view = dataset.match(E.randn() < 0)
    
    print(view.first().id)
    print(view.first().id)  # probably different!
    

Returns:
    

a `ViewExpression`

static any(_exprs_)#
    

Checks whether any of the given expressions evaluate to True.

If no expressions are provided, returns False.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains predictions that are "cat" or
    # highly confident
    is_cat = F("label") == "cat"
    is_confident = F("confidence") > 0.95
    view = dataset.filter_labels(
        "predictions", F.any([is_cat, is_confident])
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**exprs** â a `ViewExpression` or iterable of `ViewExpression` instances

Returns:
    

a `ViewExpression`

static all(_exprs_)#
    

Checks whether all of the given expressions evaluate to True.

If no expressions are provided, returns True.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains predictions that are "cat" and
    # highly confident
    is_cat = F("label") == "cat"
    is_confident = F("confidence") > 0.95
    view = dataset.filter_labels(
        "predictions", F.all([is_cat, is_confident])
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**exprs** â a `ViewExpression` or iterable of `ViewExpression` instances

Returns:
    

a `ViewExpression`

static range(_start_ , _stop =None_)#
    

Returns an array expression containing the sequence of integers from the specified start (inclusive) to stop (exclusive).

If `stop` is provided, returns `[start, start + 1, ..., stop - 1]`.

If no `stop` is provided, returns `[0, 1, ..., start - 1]`.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["y", "z"]),
        ]
    )
    
    # Populates an `ints` field based on the number of `tags`
    dataset.add_sample_field("ints", fo.ListField)
    view = dataset.set_field("ints", F.range(F("tags").length()))
    
    print(view.first())
    

Parameters:
    

  * **start** â the starting value, or stopping value if no `stop` is provided

  * **stop** (_None_) â the stopping value, if both input arguments are provided



Returns:
    

a `ViewExpression`

static enumerate(_array_ , _start =0_)#
    

Returns an array of `[index, element]` pairs enumerating the elements of the given expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["y", "z"]),
        ]
    )
    
    # Populates an `enumerated_tags` field with the enumerated `tag`
    dataset.add_sample_field("enumerated_tags", fo.ListField)
    view = dataset.set_field("enumerated_tags", F.enumerate(F("tags")))
    
    print(view.first())
    

Parameters:
    

  * **array** â a `ViewExpression` that resolves to an array

  * **start** (_0_) â the starting enumeration index to use



Returns:
    

a `ViewExpression`

static zip(_* args_, _use_longest =False_, _defaults =None_)#
    

Zips the given expressions, which must resolve to arrays, into an array whose ith element is an array containing the ith element from each input array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "c"],
                ints=[1, 2, 3, 4, 5],
            ),
            fo.Sample(
                filepath="image2.jpg",
                tags=["y", "z"],
                ints=[25, 26, 27, 28],
            ),
        ]
    )
    
    dataset.add_sample_field("tags_ints", fo.ListField)
    
    # Populates an `tags_ints` field with the zipped `tags` and `ints`
    view = dataset.set_field("tags_ints", F.zip(F("tags"), F("ints")))
    
    print(view.first())
    
    # Same as above but use the longest array to determine output size
    view = dataset.set_field(
        "tags_ints",
        F.zip(F("tags"), F("ints"), use_longest=True, defaults=("", 0))
    )
    
    print(view.first())
    

Parameters:
    

  * ***args** â one or more arrays or `ViewExpression` instances resolving to arrays

  * **use_longest** (_False_) â whether to use the longest array to determine the number of elements in the output array. By default, the length of the shortest array is used

  * **defaults** (_None_) â an optional array of default values of same length as `*args` to use when `use_longest == True` and the input arrays are of different lengths. If no defaults are provided and `use_longest == True`, then missing values are set to `None`



Returns:
    

a `ViewExpression`

class fiftyone.core.expressions.ViewField(_name =None_)#
    

Bases: `ViewExpression`

A `ViewExpression` that refers to a field or embedded field of a document.

You can use [dot notation](https://docs.mongodb.com/manual/core/document/#dot-notation) to refer to subfields of embedded objects within fields.

When you create a `ViewField` using a string field like `ViewField("embedded.field.name")`, the meaning of this field is interpreted relative to the context in which the `ViewField` object is used. For example, when passed to the `ViewExpression.map()` method, this object will refer to the `embedded.field.name` object of the array element being processed.

In other cases, you may wish to create a `ViewField` that always refers to the root document. You can do this by prepending `"$"` to the name of the field, as in `ViewField("$embedded.field.name")`.

Examples:
    
    
    from fiftyone import ViewField as F
    
    # Reference the root of the current context
    F()
    
    # Reference the `ground_truth` field in the current context
    F("ground_truth")
    
    # Reference the `label` field of the `ground_truth` object in the
    # current context
    F("ground_truth.label")
    
    # Reference the root document in any context
    F("$")
    
    # Reference the `label` field of the root document in any context
    F("$label")
    
    # Reference the `label` field of the `ground_truth` object in the root
    # document in any context
    F("$ground_truth.label")
    

__eq__(_other_)#
    

Determines whether this expression is equal to the given value or expression, `self == other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "cifar10", split="test", max_samples=500, shuffle=True
    )
    
    # Get samples whose ground truth `label` is "airplane"
    view = dataset.match(F("ground_truth.label") == "airplane")
    
    print(view.distinct("ground_truth.label"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__ge__(_other_)#
    

Determines whether this expression is greater than or equal to the given value or expression, `self >= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness") >= 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__gt__(_other_)#
    

Determines whether this expression is greater than the given value or expression, `self >= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is > 0.5
    view = dataset.match(F("uniqueness") > 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__le__(_other_)#
    

Determines whether this expression is less than or equal to the given value or expression, `self <= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is <= 0.5
    view = dataset.match(F("uniqueness") <= 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

  * **other** â a literal value or `ViewExpression`

  * **other** â a `ViewExpression` or a python primitive understood by MongoDB



Returns:
    

a `ViewExpression`

__lt__(_other_)#
    

Determines whether this expression is less than the given value or expression, `self <= other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is < 0.5
    view = dataset.match(F("uniqueness") < 0.5)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__ne__(_other_)#
    

Determines whether this expression is not equal to the given value or expression, `self != other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "cifar10", split="test", max_samples=500, shuffle=True
    )
    
    # Get samples whose ground truth `label` is NOT "airplane"
    view = dataset.match(F("ground_truth.label") != "airplane")
    
    print("airplane" in view.distinct("ground_truth.label"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__and__(_other_)#
    

Computes the logical AND of this expression and the given value or expression, `self & other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions with label "cat" and confidence > 0.9
    view = dataset.filter_labels(
        "predictions",
        (F("label") == "cat") & (F("confidence") > 0.9)
    )
    
    print(view.count_values("predictions.detections.label"))
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__invert__()#
    

Inverts this expression, `~self`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a new field to one sample
    sample = dataset.first()
    sample["new_field"] = ["hello", "there"]
    sample.save()
    
    # Get samples that do NOT have a value for `new_field`
    view = dataset.match(~F("new_field").exists())
    
    print(len(view))
    

Returns:
    

a `ViewExpression`

__or__(_other_)#
    

Computes the logical OR of this expression and the given value or expression, `self | other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions with label "cat" or confidence > 0.9
    view = dataset.filter_labels(
        "predictions",
        (F("label") == "cat") | (F("confidence") > 0.9)
    )
    
    print(view.count_values("predictions.detections.label"))
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**other** â a literal value or `ViewExpression`

Returns:
    

a `ViewExpression`

__abs__()#
    

Computes the absolute value of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(abs(F("uniqueness") - 0.5) < 0.25)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__add__(_other_)#
    

Adds the given value to this expression, which must resolve to a numeric value, `self + other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    manhattan_dist = F("bounding_box")[0] + F("bounding_box")[1]
    
    # Only contains predictions whose bounding boxes' upper left corner
    # is a Manhattan distance of at least 1 from the origin
    dataset.filter_labels("predictions, manhattan_dist > 1)
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__ceil__()#
    

Computes the ceiling of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match(math.ceil(F("uniqueness") + 0.5) == 2)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__floor__()#
    

Computes the floor of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match(math.floor(F("uniqueness") + 0.5) == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__round__(_place =0_)#
    

Rounds this expression, which must resolve to a numeric value, at the given decimal place.

Positive values of `place` will round to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.57
    

Negative values of `place` will round digits left of the decimal:
    
    
    place=-2: 1234.5678 --> 1200
    

Parameters:
    

**place** (_0_) â the decimal place at which to round. Must be an integer in range `(-20, 100)`

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(round(2 * F("uniqueness")) == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

__mod__(_other_)#
    

Computes the modulus of this expression, which must resolve to a numeric value, `self % other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with an even number of predictions
    view = dataset.match(
        (F("predictions.detections").length() % 2) == 0
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__mul__(_other_)#
    

Computes the product of the given value and this expression, which must resolve to a numeric value, `self * other`.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only contains predictions whose bounding box area is > 0.2
    view = dataset.filter_labels("predictions", bbox_area > 0.2)
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__pow__(_power_ , _modulo =None_)#
    

Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5) ** 2 +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5) ** 2
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**power** â the power

Returns:
    

a `ViewExpression`

__sub__(_other_)#
    

Subtracts the given value from this expression, which must resolve to a numeric value, `self - other`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    rectangleness = abs(
        F("$metadata.width") * F("bounding_box")[2] -
        F("$metadata.height") * F("bounding_box")[3]
    )
    
    # Only contains predictions whose bounding boxes are within 1 pixel
    # of being square
    view = (
        dataset
        .select_fields("predictions")
        .filter_labels("predictions", rectangleness <= 1)
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__truediv__(_other_)#
    

Divides this expression, which must resolve to a numeric value, by the given value, `self / other`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    aspect_ratio = (
        (F("$metadata.width") * F("bounding_box")[2]) /
        (F("$metadata.height") * F("bounding_box")[3])
    )
    
    # Only contains predictions whose aspect ratio is > 2
    view = (
        dataset
        .select_fields("predictions")
        .filter_labels("predictions", aspect_ratio > 2)
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**other** â a number or `ViewExpression`

Returns:
    

a `ViewExpression`

__getitem__(_idx_or_slice_)#
    

Returns the element or slice of this expression, which must resolve to an array.

All of the typical slicing operations are supported, except for specifying a non-unit step:
    
    
    expr[3]      # the fourth element
    expr[-1]     # the last element
    expr[:10]    # the first (up to) 10 elements
    expr[-3:]    # the last (up to) 3 elements
    expr[3:10]   # the fourth through tenth elements
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only contains objects in the `predictions` field with area > 0.2
    view = dataset.filter_labels("predictions", bbox_area > 0.2)
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**idx_or_slice** â the index or slice

Returns:
    

a `ViewExpression`

Parameters:
    

**name** (_None_) â the name of the field, with an optional â$â prepended if you wish to freeze this field to the root document

**Methods:**

`to_mongo`([prefix]) | Returns a MongoDB representation of the field.  
---|---  
`abs`() | Computes the absolute value of this expression, which must resolve to a numeric value.  
`all`(exprs) | Checks whether all of the given expressions evaluate to True.  
`any`(exprs) | Checks whether any of the given expressions evaluate to True.  
`append`(value) | Appends the given value to this expression, which must resolve to an array.  
`apply`(expr) | Applies the given expression to this expression.  
`arccos`() | Computes the inverse cosine of this expression, which must resolve to a numeric value, in radians.  
`arccosh`() | Computes the inverse hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.  
`arcsin`() | Computes the inverse sine of this expression, which must resolve to a numeric value, in radians.  
`arcsinh`() | Computes the inverse hyperbolic sine of this expression, which must resolve to a numeric value, in radians.  
`arctan`() | Computes the inverse tangent of this expression, which must resolve to a numeric value, in radians.  
`arctanh`() | Computes the inverse hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.  
`cases`(mapping[,Â default]) | Applies a case statement to this expression, which effectively computes the following pseudocode.  
`ceil`() | Computes the ceiling of this expression, which must resolve to a numeric value.  
`concat`(*args) | Concatenates the given string(s) to this expression, which must resolve to a string.  
`contains`(values[,Â all]) | Checks whether this expression, which must resolve to an array, contains any of the given values.  
`contains_str`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, contains the given string or string(s).  
`cos`() | Computes the cosine of this expression, which must resolve to a numeric value, in radians.  
`cosh`() | Computes the hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.  
`day_of_month`() | Returns the day of the month of this date expression (in UTC) as a number between 1 and 31.  
`day_of_week`() | Returns the day of the week of this date expression (in UTC) as a number between 1 (Sunday) and 7 (Saturday).  
`day_of_year`() | Returns the day of the year of this date expression (in UTC) as a number between 1 and 366.  
`difference`(values) | Computes the set difference of this expression, which must resolve to an array, and the given array or array expression.  
`ends_with`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, ends with the given string or string(s).  
`enumerate`(array[,Â start]) | Returns an array of `[index, element]` pairs enumerating the elements of the given expression, which must resolve to an array.  
`exists`([bool]) | Determines whether this expression, which must resolve to a field, exists and is not None.  
`exp`() | Raises Euler's number to this expression, which must resolve to a numeric value.  
`extend`(*args) | Concatenates the given array(s) or array expression(s) to this expression, which must resolve to an array.  
`filter`(expr) | Applies the given filter to the elements of this expression, which must resolve to an array.  
`floor`() | Computes the floor of this expression, which must resolve to a numeric value.  
`hour`() | Returns the hour portion of this date expression (in UTC) as a number between 0 and 23.  
`if_else`(true_expr,Â false_expr) | Returns either `true_expr` or `false_expr` depending on the value of this expression, which must resolve to a boolean.  
`if_null`(false_expr) | Returns either this expression or `false_expr` if this expression is null.  
`insert`(index,Â value) | Inserts the value before the given index in this expression, which must resolve to an array.  
`intersection`(*args) | Computes the set intersection of this expression, which must resolve to an array, and the given array(s) or array expression(s).  
`is_array`() | Determines whether this expression is an array.  
`is_in`(values) | Creates an expression that returns a boolean indicating whether `self in values`.  
`is_missing`() | Determines whether this expression refers to a missing field.  
`is_null`() | Determines whether this expression is null.  
`is_number`() | Determines whether this expression is a number.  
`is_string`() | Determines whether this expression is a string.  
`is_subset`(values) | Checks whether this expression's contents, which must resolve to an array, are a subset of the given array or array expression's contents.  
`join`(delimiter) | Joins the elements of this expression, which must resolve to a string array, by the given delimiter.  
`length`() | Computes the length of this expression, which must resolve to an array.  
`let_in`(expr) | Returns an equivalent expression where this expression is defined as a variable that is used wherever necessary in the given expression.  
`literal`(value) | Returns an expression representing the given value without parsing.  
`ln`() | Computes the natural logarithm of this expression, which must resolve to a numeric value.  
`log`(base) | Computes the logarithm base `base` of this expression, which must resolve to a numeric value.  
`log10`() | Computes the logarithm base 10 of this expression, which must resolve to a numeric value.  
`lower`() | Converts this expression, which must resolve to a string, to lowercase.  
`lstrip`([chars]) | Removes whitespace characters from the beginning of this expression, which must resolve to a string.  
`map`(expr) | Applies the given expression to the elements of this expression, which must resolve to an array.  
`map_values`(mapping) | Replaces this expression with the corresponding value in the provided mapping dict, if it is present as a key.  
`matches_str`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, exactly matches the given string or string(s).  
`max`([value]) | Returns the maximum value of either this expression, which must resolve to an array, or the maximum of this expression and the given value.  
`mean`() | Returns the average value in this expression, which must resolve to a numeric array.  
`millisecond`() | Returns the millisecond portion of this date expression (in UTC) as an integer between 0 and 999.  
`min`([value]) | Returns the minimum value of either this expression, which must resolve to an array, or the minimum of this expression and the given value.  
`minute`() | Returns the minute portion of this date expression (in UTC) as a number between 0 and 59.  
`month`() | Returns the month of this date expression (in UTC) as a number between 1 and 12.  
`pow`(power) | Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.  
`prepend`(value) | Prepends the given value to this expression, which must resolve to an array.  
`rand`() | Returns an expression that generates a uniform random float in `[0, 1]` each time it is called.  
`randn`() | Returns an expression that generates a sample from the standard Gaussian distribution each time it is called.  
`range`(start[,Â stop]) | Returns an array expression containing the sequence of integers from the specified start (inclusive) to stop (exclusive).  
`re_match`(regex[,Â options]) | Performs a regular expression pattern match on this expression, which must resolve to a string.  
`reduce`(expr[,Â init_val]) | Applies the given reduction to this expression, which must resolve to an array, and returns the single value computed.  
`replace`(old,Â new) | Replaces all occurrences of `old` with `new` in this expression, which must resolve to a string.  
`reverse`() | Reverses the order of the elements in the expression, which must resolve to an array.  
`round`([place]) | Rounds this expression, which must resolve to a numeric value, at the given decimal place.  
`rsplit`(delimiter[,Â maxsplit]) | Splits this expression, which must resolve to a string, by the given delimiter.  
`rstrip`([chars]) | Removes whitespace characters from the end of this expression, which must resolve to a string.  
`second`() | Returns the second portion of this date expression (in UTC) as a number between 0 and 59.  
`set_equals`(*args) | Checks whether this expression, which must resolve to an array, contains the same distinct values as each of the given array(s) or array expression(s).  
`set_field`(field,Â value_or_expr[,Â relative]) | Sets the specified field or embedded field of this expression, which must resolve to a document, to the given value or expression.  
`sin`() | Computes the sine of this expression, which must resolve to a numeric value, in radians.  
`sinh`() | Computes the hyperbolic sine of this expression, which must resolve to a numeric value, in radians.  
`sort`([key,Â numeric,Â reverse]) | Sorts this expression, which must resolve to an array.  
`split`(delimiter[,Â maxsplit]) | Splits this expression, which must resolve to a string, by the given delimiter.  
`sqrt`() | Computes the square root of this expression, which must resolve to a numeric value.  
`starts_with`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, starts with the given string or string(s).  
`std`([sample]) | Returns the standard deviation of the values in this expression, which must resolve to a numeric array.  
`strip`([chars]) | Removes whitespace characters from the beginning and end of this expression, which must resolve to a string.  
`strlen`() | Computes the length of this expression, which must resolve to a string.  
`substr`([start,Â end,Â count]) | Extracts the specified substring from this expression, which must resolve to a string.  
`sum`() | Returns the sum of the values in this expression, which must resolve to a numeric array.  
`switch`(mapping[,Â default]) | Applies a switch statement to this expression, which effectively computes the given pseudocode.  
`tan`() | Computes the tangent of this expression, which must resolve to a numeric value, in radians.  
`tanh`() | Computes the hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.  
`to_bool`() | Converts the expression to a boolean value.  
`to_date`() | Converts the expression to a date value.  
`to_double`() | Converts the expression to a double precision value.  
`to_int`() | Converts the expression to an integer value.  
`to_string`() | Converts the expression to a string value.  
`trunc`([place]) | Truncates this expression, which must resolve to a numeric value, at the specified decimal place.  
`type`() | Returns the type string of this expression.  
`union`(*args) | Computes the set union of this expression, which must resolve to an array, and the given array(s) or array expression(s).  
`unique`() | Returns an array containing the unique values in this expression, which must resolve to an array.  
`upper`() | Converts this expression, which must resolve to a string, to uppercase.  
`week`() | Returns the week of the year of this date expression (in UTC) as a number between 0 and 53.  
`year`() | Returns the year of this date expression (in UTC).  
`zip`(*args[,Â use_longest,Â defaults]) | Zips the given expressions, which must resolve to arrays, into an array whose ith element is an array containing the ith element from each input array.  
  
**Attributes:**

`is_frozen` | Whether this expression's prefix is frozen.  
---|---  
  
to_mongo(_prefix =None_)#
    

Returns a MongoDB representation of the field.

Parameters:
    

**prefix** (_None_) â an optional prefix to prepend to the field name

Returns:
    

a string

abs()#
    

Computes the absolute value of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match((F("uniqueness") - 0.5).abs() < 0.25)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

static all(_exprs_)#
    

Checks whether all of the given expressions evaluate to True.

If no expressions are provided, returns True.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains predictions that are "cat" and
    # highly confident
    is_cat = F("label") == "cat"
    is_confident = F("confidence") > 0.95
    view = dataset.filter_labels(
        "predictions", F.all([is_cat, is_confident])
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**exprs** â a `ViewExpression` or iterable of `ViewExpression` instances

Returns:
    

a `ViewExpression`

static any(_exprs_)#
    

Checks whether any of the given expressions evaluate to True.

If no expressions are provided, returns False.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains predictions that are "cat" or
    # highly confident
    is_cat = F("label") == "cat"
    is_confident = F("confidence") > 0.95
    view = dataset.filter_labels(
        "predictions", F.any([is_cat, is_confident])
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**exprs** â a `ViewExpression` or iterable of `ViewExpression` instances

Returns:
    

a `ViewExpression`

append(_value_)#
    

Appends the given value to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "b"]),
        ]
    )
    
    # Appends the "c" tag to each sample
    view = dataset.set_field("tags", F("tags").append("c"))
    
    print(view.first().tags)
    

Parameters:
    

**value** â the value or `ViewExpression`

Returns:
    

a `ViewExpression`

apply(_expr_)#
    

Applies the given expression to this expression.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(
        F("uniqueness").apply((F() > 0.25) & (F() < 0.75))
    )
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

arccos()#
    

Computes the inverse cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arccos()`
    view = dataset.match(F("uniqueness").arccos() <= np.arccos(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arccosh()#
    

Computes the inverse hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arccosh()`
    view = dataset.match((1 + F("uniqueness")).arccosh() >= np.arccosh(1.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arcsin()#
    

Computes the inverse sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arcsin()`
    view = dataset.match(F("uniqueness").arcsin() >= np.arcsin(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arcsinh()#
    

Computes the inverse hyperbolic sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arcsinh()`
    view = dataset.match(F("uniqueness").arcsinh() >= np.arcsinh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arctan()#
    

Computes the inverse tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arctan()`
    view = dataset.match(F("uniqueness").arctan() >= np.arctan(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arctanh()#
    

Computes the inverse hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arctanh()`
    view = dataset.match(F("uniqueness").arctanh() >= np.arctanh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

cases(_mapping_ , _default =None_)#
    

Applies a case statement to this expression, which effectively computes the following pseudocode:
    
    
    for key, value in mapping.items():
        if self == key:
            return value
    
    if default is not None:
        return default
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    # Map numeric `uniqueness` values to 1 and null values to 0
    cases_view = view.set_field(
        "uniqueness",
        F("uniqueness").type().cases({"double": 1, "null": 0}),
    )
    
    print(cases_view.count_values("uniqueness"))
    

Parameters:
    

  * **mapping** â a dict mapping literals or `ViewExpression` keys to literal or `ViewExpression` values

  * **default** (_None_) â an optional literal or `ViewExpression` to return if none of the switch branches are taken



Returns:
    

a `ViewExpression`

ceil()#
    

Computes the ceiling of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match((F("uniqueness") + 0.5).ceil() == 2)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

concat(_* args_)#
    

Concatenates the given string(s) to this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Appends "-tag" to all tags
    transform_tag = F().concat("-tag")
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

  * ***args** â one or more strings or string `ViewExpression` instances

  * **before** (_False_) â whether to position `args` before this string in the output string



Returns:
    

a `ViewExpression`

contains(_values_ , _all =False_)#
    

Checks whether this expression, which must resolve to an array, contains any of the given values.

Pass `all=True` to require that this expression contains all of the given values.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    print(dataset.count())
    
    # Only contains samples with a "cat" prediction
    view = dataset.match(
        F("predictions.detections.label").contains("cat")
    )
    print(view.count())
    
    # Only contains samples with "cat" or "dog" predictions
    view = dataset.match(
        F("predictions.detections.label").contains(["cat", "dog"])
    )
    print(view.count())
    
    # Only contains samples with "cat" and "dog" predictions
    view = dataset.match(
        F("predictions.detections.label").contains(["cat", "dog"], all=True)
    )
    print(view.count())
    

Parameters:
    

  * **values** â a value, iterable of values, or `ViewExpression` that resolves to an array of values

  * **all** (_False_) â whether this expression must contain all (True) or any (False) of the given values



Returns:
    

a `ViewExpression`

contains_str(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, contains the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions whose `label` contains "be"
    view = dataset.filter_labels(
        "predictions", F("label").contains_str("be")
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

cos()#
    

Computes the cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `cos()`
    view = dataset.match(F("uniqueness").cos() <= np.cos(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

cosh()#
    

Computes the hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `cosh()`
    view = dataset.match(F("uniqueness").cosh() >= np.cosh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

day_of_month()#
    

Returns the day of the month of this date expression (in UTC) as a number between 1 and 31.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the month for the dataset
    print(dataset.values(F("created_at").day_of_month()))
    
    # Samples with even days of the month
    view = dataset.match(F("created_at").day_of_month() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_week()#
    

Returns the day of the week of this date expression (in UTC) as a number between 1 (Sunday) and 7 (Saturday).

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 5),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 6),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 7),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the week for the dataset
    print(dataset.values(F("created_at").day_of_week()))
    
    # Samples with even days of the week
    view = dataset.match(F("created_at").day_of_week() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_year()#
    

Returns the day of the year of this date expression (in UTC) as a number between 1 and 366.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the year for the dataset
    print(dataset.values(F("created_at").day_of_year()))
    
    # Samples with even days of the year
    view = dataset.match(F("created_at").day_of_year() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

difference(_values_)#
    

Computes the set difference of this expression, which must resolve to an array, and the given array or array expression.

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").difference(F("other_tags"))))
    # [['b']]
    

Parameters:
    

**values** â an iterable of values or a `ViewExpression` that resolves to an array

Returns:
    

a `ViewExpression`

ends_with(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, ends with the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose images are JPEGs or PNGs
    view = dataset.match(F("filepath").ends_with((".jpg", ".png")))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

static enumerate(_array_ , _start =0_)#
    

Returns an array of `[index, element]` pairs enumerating the elements of the given expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["y", "z"]),
        ]
    )
    
    # Populates an `enumerated_tags` field with the enumerated `tag`
    dataset.add_sample_field("enumerated_tags", fo.ListField)
    view = dataset.set_field("enumerated_tags", F.enumerate(F("tags")))
    
    print(view.first())
    

Parameters:
    

  * **array** â a `ViewExpression` that resolves to an array

  * **start** (_0_) â the starting enumeration index to use



Returns:
    

a `ViewExpression`

exists(_bool =True_)#
    

Determines whether this expression, which must resolve to a field, exists and is not None.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "quickstart", dataset_name=fo.get_default_dataset_name()
    )
    
    # Add a new field to one sample
    sample = dataset.first()
    sample["new_field"] = ["hello", "there"]
    sample.save()
    
    # Get samples that have a value for `new_field`
    view = dataset.match(F("new_field").exists())
    
    print(len(view))
    

Parameters:
    

**bool** (_True_) â whether to determine whether this expression exists (True) or is None or non-existent (False)

Returns:
    

a `ViewExpression`

exp()#
    

Raises Eulerâs number to this expression, which must resolve to a numeric value.

Returns:
    

a `ViewExpression`

extend(_* args_)#
    

Concatenates the given array(s) or array expression(s) to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "b"]),
        ]
    )
    
    # Adds the "c" and "d" tags to each sample
    view = dataset.set_field("tags", F("tags").extend(["c", "d"]))
    
    print(view.first().tags)
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

filter(_expr_)#
    

Applies the given filter to the elements of this expression, which must resolve to an array.

The output array will only contain elements of the input array for which `expr` returns `True`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only include predictions with `confidence` of at least 0.9
    view = dataset.set_field(
        "predictions.detections",
        F("detections").filter(F("confidence") > 0.9)
    )
    
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**expr** â a `ViewExpression` that returns a boolean

Returns:
    

a `ViewExpression`

floor()#
    

Computes the floor of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match((F("uniqueness") + 0.5).floor() == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

hour()#
    

Returns the hour portion of this date expression (in UTC) as a number between 0 and 23.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the hour portion of the dates in the dataset
    print(dataset.values(F("created_at").hour()))
    
    # Samples with even hours
    view = dataset.match(F("created_at").hour() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

if_else(_true_expr_ , _false_expr_)#
    

Returns either `true_expr` or `false_expr` depending on the value of this expression, which must resolve to a boolean.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

  * **true_expr** â a `ViewExpression` or MongoDB expression dict

  * **false_expr** â a `ViewExpression` or MongoDB expression dict



Returns:
    

a `ViewExpression`

if_null(_false_expr_)#
    

Returns either this expression or `false_expr` if this expression is null. This is a shortcut for `self.is_null().if_else(false_expr, self)` and is useful for replacing null values in a field with a default value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `gt.detection.label` field to "unknown" if it does not exist
    view = dataset.set_field(
        "gt.detection.label",
        F("gt.detection.label").if_null("unknown")
    )
    

Parameters:
    

**false_expr** â a `ViewExpression` or MongoDB expression dict

Returns:
    

a `ViewExpression`

insert(_index_ , _value_)#
    

Inserts the value before the given index in this expression, which must resolve to an array.

If `index <= 0`, the value is prepended to this array. If `index >= self.length()`, the value is appended to this array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "c"]),
        ]
    )
    
    # Adds the "ready" tag to each sample
    view = dataset.set_field("tags", F("tags").insert(1, "b"))
    
    print(view.first().tags)
    

Parameters:
    

  * **index** â the index at which to insert the value

  * **value** â the value or `ViewExpression`



Returns:
    

a `ViewExpression`

intersection(_* args_)#
    

Computes the set intersection of this expression, which must resolve to an array, and the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").intersection(F("other_tags"))))
    # [['a']]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

is_array()#
    

Determines whether this expression is an array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that tags are arrays
    view = dataset.match(F("tags").is_array())
    
    print(len(view))
    

Returns:
    

`ViewExpression`

property is_frozen#
    

Whether this expressionâs prefix is frozen.

is_in(_values_)#
    

Creates an expression that returns a boolean indicating whether `self in values`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains animal predictions
    view = dataset.filter_labels(
        "predictions", F("label").is_in(ANIMALS)
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

**values** â a value or iterable of values

Returns:
    

a `ViewExpression`

is_missing()#
    

Determines whether this expression refers to a missing field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that `foobar` is a non-existent field on all samples
    view = dataset.match(F("foobar").is_missing())
    
    print(len(view) == len(dataset))
    

Returns:
    

`ViewExpression`

is_null()#
    

Determines whether this expression is null.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.25 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.25).if_else(F("uniqueness"), None)
    )
    
    # Create view that only contains samples with uniqueness = None
    not_unique_view = view.match(F("uniqueness").is_null())
    
    print(len(not_unique_view))
    

Returns:
    

`ViewExpression`

is_number()#
    

Determines whether this expression is a number.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.25 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.25).if_else(F("uniqueness"), None)
    )
    
    # Create view that only contains samples with uniqueness values
    has_unique_view = view.match(F("uniqueness").is_number())
    
    print(len(has_unique_view))
    

Returns:
    

`ViewExpression`

is_string()#
    

Determines whether this expression is a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that filepaths are strings
    view = dataset.match(F("filepath").is_string())
    
    print(len(view))
    

Returns:
    

`ViewExpression`

is_subset(_values_)#
    

Checks whether this expressionâs contents, which must resolve to an array, are a subset of the given array or array expressionâs contents.

The arrays are treated as sets, so duplicate values are ignored.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
                other_tags=["a", "b", "c"],
            )
        ]
    )
    
    print(dataset.values(F("tags").is_subset(F("other_tags"))))
    # [True]
    

Parameters:
    

**values** â an iterable of values or a `ViewExpression` that resolves to an array

Returns:
    

a `ViewExpression`

join(_delimiter_)#
    

Joins the elements of this expression, which must resolve to a string array, by the given delimiter.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Generate a `list,of,labels` for the `predictions` of each sample
    view = dataset.set_field(
        "predictions.labels",
        F("detections").map(F("label")).join(",")
    )
    
    print(view.first().predictions.labels)
    

Parameters:
    

**delimiter** â the delimiter string

Returns:
    

a `ViewExpression`

length()#
    

Computes the length of this expression, which must resolve to an array.

If this expressionâs value is null or missing, zero is returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with at least 15 predicted objects
    view = dataset.match(F("predictions.detections").length() >= 15)
    
    print(dataset.count())
    print(view.count())
    

Returns:
    

a `ViewExpression`

let_in(_expr_)#
    

Returns an equivalent expression where this expression is defined as a variable that is used wherever necessary in the given expression.

This method is useful when `expr` contains multiple instances of this expression, since it avoids duplicate computation of this expression in the final pipeline.

If `expr` is a simple expression such as a `ViewField`, no variable is defined and `expr` is directly returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    good_bboxes = (bbox_area > 0.25) & (bbox_area < 0.75)
    
    # Optimize the expression
    good_bboxes_opt = bbox_area.let_in(good_bboxes)
    
    # Contains predictions whose bounding box areas are in [0.25, 0.75]
    view = dataset.filter_labels("predictions", good_bboxes_opt)
    
    print(good_bboxes)
    print(good_bboxes_opt)
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

static literal(_value_)#
    

Returns an expression representing the given value without parsing.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/literal) for more information on when this method is required.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add the "$money" tag to each sample
    # The "$" character ordinarily has special meaning, so we must wrap
    # it in `literal()` in order to add it via this method
    view = dataset.set_field(
        "tags", F("tags").append(F.literal("$money"))
    )
    
    print(view.first().tags)
    

Parameters:
    

**value** â a value

Returns:
    

a `ViewExpression`

ln()#
    

Computes the natural logarithm of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").ln() >= math.log(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

log(_base_)#
    

Computes the logarithm base `base` of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").log(2) >= math.log2(0.5))
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**base** â the logarithm base

Returns:
    

a `ViewExpression`

log10()#
    

Computes the logarithm base 10 of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").log10() >= math.log10(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

lower()#
    

Converts this expression, which must resolve to a string, to lowercase.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Converts all tags to lowercase
    transform_tag = F().lower()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Returns:
    

a `ViewExpression`

lstrip(_chars =None_)#
    

Removes whitespace characters from the beginning of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from the beginning of each tag
    transform_tag = E(" ").concat(F()).lstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

map(_expr_)#
    

Applies the given expression to the elements of this expression, which must resolve to an array.

The output will be an array with the applied results.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only include predictions with `confidence` of at least 0.9
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(F().set_field("area", bbox_area))
    )
    
    print(view.bounds("predictions.detections.area"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

map_values(_mapping_)#
    

Replaces this expression with the corresponding value in the provided mapping dict, if it is present as a key.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replace the `label` of all animal objects in the `predictions`
    # field with "animal"
    #
    mapping = {a: "animal" for a in ANIMALS}
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(
            F().set_field("label", F("label").map_values(mapping))
        )
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

**mapping** â a dict mapping keys to replacement values

Returns:
    

a `ViewExpression`

matches_str(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, exactly matches the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions whose `label` is "cat" or "dog", case
    # insensitive
    view = dataset.map_labels(
        "predictions", {"cat": "CAT", "dog": "DOG"}
    ).filter_labels(
        "predictions",
        F("label").matches_str(("cat", "dog"), case_sensitive=False)
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

max(_value =None_)#
    

Returns the maximum value of either this expression, which must resolve to an array, or the maximum of this expression and the given value.

Missing or `None` values are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Adds a `max_area` property to the `predictions` field that
    # records the maximum prediction area in that sample
    view = dataset.set_field(
        "predictions.max_area",
        F("detections").map(bbox_area).max()
    )
    
    print(view.bounds("predictions.max_area"))
    

Parameters:
    

**value** (_None_) â an optional value to compare to

Returns:
    

a `ViewExpression`

mean()#
    

Returns the average value in this expression, which must resolve to a numeric array.

Missing or `None`-valued elements are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the average
    # confidence of the predictions
    view = dataset.set_field(
        "predictions.conf_mean",
        F("detections").map(F("confidence")).mean()
    )
    
    print(view.bounds("predictions.conf_mean"))
    

Returns:
    

a `ViewExpression`

millisecond()#
    

Returns the millisecond portion of this date expression (in UTC) as an integer between 0 and 999.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 1000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 2000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 3000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 4000),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the millisecond portion of the dates in the dataset
    print(dataset.values(F("created_at").millisecond()))
    
    # Samples with even milliseconds
    view = dataset.match(F("created_at").millisecond() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

min(_value =None_)#
    

Returns the minimum value of either this expression, which must resolve to an array, or the minimum of this expression and the given value.

Missing or `None` values are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Adds a `min_area` property to the `predictions` field that
    # records the minimum prediction area in that sample
    view = dataset.set_field(
        "predictions.min_area",
        F("detections").map(bbox_area).min()
    )
    
    print(view.bounds("predictions.min_area"))
    

Parameters:
    

**value** (_None_) â an optional value to compare to

Returns:
    

a `ViewExpression`

minute()#
    

Returns the minute portion of this date expression (in UTC) as a number between 0 and 59.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the minute portion of the dates in the dataset
    print(dataset.values(F("created_at").minute()))
    
    # Samples with even minutes
    view = dataset.match(F("created_at").minute() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

month()#
    

Returns the month of this date expression (in UTC) as a number between 1 and 12.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 2, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 3, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 4, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the months of the year for the dataset
    print(dataset.values(F("created_at").month()))
    
    # Samples from even months of the year
    view = dataset.match(F("created_at").month() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

pow(_power_)#
    

Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5).pow(2) +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5).pow(2)
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**power** â the power

Returns:
    

a `ViewExpression`

prepend(_value_)#
    

Prepends the given value to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["b", "c"]),
        ]
    )
    
    # Adds the "a" tag to each sample
    view = dataset.set_field("tags", F("tags").prepend("a"))
    
    print(view.first().tags)
    

Parameters:
    

**value** â the value or `ViewExpression`

Returns:
    

a `ViewExpression`

static rand()#
    

Returns an expression that generates a uniform random float in `[0, 1]` each time it is called.

Warning

This expression will generate new values each time it is used, so you likely do not want to use it to construct dataset views, since such views would produce different outputs each time they are used.

A typical usage for this expression is in conjunction with [`fiftyone.core.view.DatasetView.set_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.set_field "fiftyone.core.view.DatasetView.set_field") and [`fiftyone.core.view.DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to populate a randomized field on a dataset.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    #
    # Populate a new `rand` field with random numbers
    #
    
    dataset.add_sample_field("rand", fo.FloatField)
    dataset.set_field("rand", E.rand()).save("rand")
    
    print(dataset.bounds("rand"))
    
    #
    # Create a view that contains a different 10%% of the dataset each
    # time it is used
    #
    
    view = dataset.match(E.rand() < 0.1)
    
    print(view.first().id)
    print(view.first().id)  # probably different!
    

Returns:
    

a `ViewExpression`

static randn()#
    

Returns an expression that generates a sample from the standard Gaussian distribution each time it is called.

Warning

This expression will generate new values each time it is used, so you likely do not want to use it to construct dataset views, since such views would produce different outputs each time they are used.

A typical usage for this expression is in conjunction with [`fiftyone.core.view.DatasetView.set_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.set_field "fiftyone.core.view.DatasetView.set_field") and [`fiftyone.core.view.DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to populate a randomized field on a dataset.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    #
    # Populate a new `randn` field with random numbers
    #
    
    dataset.add_sample_field("randn", fo.FloatField)
    dataset.set_field("randn", E.randn()).save("randn")
    
    print(dataset.bounds("randn"))
    
    #
    # Create a view that contains a different 50%% of the dataset each
    # time it is used
    #
    
    view = dataset.match(E.randn() < 0)
    
    print(view.first().id)
    print(view.first().id)  # probably different!
    

Returns:
    

a `ViewExpression`

static range(_start_ , _stop =None_)#
    

Returns an array expression containing the sequence of integers from the specified start (inclusive) to stop (exclusive).

If `stop` is provided, returns `[start, start + 1, ..., stop - 1]`.

If no `stop` is provided, returns `[0, 1, ..., start - 1]`.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["y", "z"]),
        ]
    )
    
    # Populates an `ints` field based on the number of `tags`
    dataset.add_sample_field("ints", fo.ListField)
    view = dataset.set_field("ints", F.range(F("tags").length()))
    
    print(view.first())
    

Parameters:
    

  * **start** â the starting value, or stopping value if no `stop` is provided

  * **stop** (_None_) â the stopping value, if both input arguments are provided



Returns:
    

a `ViewExpression`

re_match(_regex_ , _options =None_)#
    

Performs a regular expression pattern match on this expression, which must resolve to a string.

The output of the expression will be `True` if the pattern matches and `False` otherwise.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Get samples whose images are JPEGs
    #
    
    view = dataset.match(F("filepath").re_match("\.jpg$"))
    
    print(view.count())
    print(view.first().filepath)
    
    #
    # Get samples whose images are in the "/Users" directory
    #
    
    view = dataset.match(F("filepath").re_match("^/Users/"))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **regex** â the regular expression to apply. Must be a Perl Compatible Regular Expression (PCRE). See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/#regexmatch-regex) for details

  * **options** (_None_) â an optional string of regex options to apply. See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/#regexmatch-options) for the available options



Returns:
    

a `ViewExpression`

reduce(_expr_ , _init_val =0_)#
    

Applies the given reduction to this expression, which must resolve to an array, and returns the single value computed.

The provided `expr` must include the `VALUE` expression to properly define the reduction.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    from fiftyone.core.expressions import VALUE
    
    #
    # Compute the number of keypoints in each sample of a dataset
    #
    
    dataset = fo.Dataset()
    dataset.add_sample(
        fo.Sample(
            filepath="image.jpg",
            keypoints=fo.Keypoints(
                keypoints=[
                    fo.Keypoint(points=[(0, 0), (1, 1)]),
                    fo.Keypoint(points=[(0, 0), (1, 0), (1, 1), (0, 1)]),
                ]
            )
        )
    )
    
    view = dataset.set_field(
        "keypoints.count",
        F("$keypoints.keypoints").reduce(VALUE + F("points").length()),
    )
    
    print(view.first().keypoints.count)
    
    #
    # Generate a `list,of,labels` for the `predictions` of each sample
    #
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    join_labels = F("detections").reduce(
        VALUE.concat(",", F("label")), init_val=""
    ).lstrip(",")
    
    view = dataset.set_field("predictions.labels", join_labels)
    
    print(view.first().predictions.labels)
    

Parameters:
    

  * **expr** â a `ViewExpression` defining the reduction expression to apply. Must contain the `VALUE` expression

  * **init_val** (_0_) â an initial value for the reduction



Returns:
    

a `ViewExpression`

replace(_old_ , _new_)#
    

Replaces all occurrences of `old` with `new` in this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Replaces "val" with "VAL" in each tag
    transform_tag = F().replace("val", "VAL")
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

  * **old** â a string or `ViewExpression` resolving to a string expression specifying the substring to replace

  * **new** â a string or `ViewExpression` resolving to a string expression specifying the replacement value



Returns:
    

a `ViewExpression`

reverse()#
    

Reverses the order of the elements in the expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    first_obj = F("predictions.detections")[0]
    last_obj = F("predictions.detections").reverse()[0]
    
    # Only contains samples whose first and last prediction have the
    # same label
    view = dataset.match(
        first_obj.apply(F("label")) == last_obj.apply(F("label"))
    )
    
    print(dataset.count())
    print(view.count())
    

Returns:
    

a `ViewExpression`

round(_place =0_)#
    

Rounds this expression, which must resolve to a numeric value, at the given decimal place.

Positive values of `place` will round to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.57
    

Negative values of `place` will round `place` digits left of the decimal:
    
    
    place=-1: 1234.5678 --> 1230
    

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match((2 * F("uniqueness")).round() == 1)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**place** (_0_) â the decimal place at which to round. Must be an integer in range `(-20, 100)`

Returns:
    

a `ViewExpression`

rsplit(_delimiter_ , _maxsplit =None_)#
    

Splits this expression, which must resolve to a string, by the given delimiter.

If the number of chunks exceeds `maxsplit`, splits are only performed on the last `maxsplit` occurrences of the delimiter.

The result is a string array that contains the chunks with the delimiter removed. If the delimiter is not found, this full string is returned as a single element array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add "-ok-go" to the first tag and then split once on "-" from the
    # right to create two tags for each sample
    view = dataset.set_field(
        "tags", F("tags")[0].concat("-ok-go").rsplit("-", 1)
    )
    
    print(view.first().tags)
    

Parameters:
    

  * **delimiter** â the delimiter string or `ViewExpression` resolving to a string expression

  * **maxsplit** (_None_) â a maximum number of splits to perform, from the right



Returns:
    

a `ViewExpression`

rstrip(_chars =None_)#
    

Removes whitespace characters from the end of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from the end of each tag
    transform_tag = F().concat(" ").rstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

second()#
    

Returns the second portion of this date expression (in UTC) as a number between 0 and 59.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the second portion of the dates in the dataset
    print(dataset.values(F("created_at").second()))
    
    # Samples with even seconds
    view = dataset.match(F("created_at").second() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

set_equals(_* args_)#
    

Checks whether this expression, which must resolve to an array, contains the same distinct values as each of the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are ignored.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
                other_tags=["a", "b", "b"],
            )
        ]
    )
    
    print(dataset.values(F("tags").set_equals(F("other_tags"))))
    # [True]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

set_field(_field_ , _value_or_expr_ , _relative =True_)#
    

Sets the specified field or embedded field of this expression, which must resolve to a document, to the given value or expression.

By default, the provided expression is computed by applying it to this expression via `self.apply(value_or_expr)`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replaces the `label` attributes of the objects in the
    # `predictions` field according to the following rule:
    #
    #   If the `label` starts with `b`, replace it with `b`. Otherwise,
    #   replace it with "other"
    #
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(
            F().set_field(
                "label",
                F("label").re_match("^b").if_else("b", "other"),
            )
        )
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

  * **field** â the âfieldâ or âembedded.field.nameâ to set

  * **value_or_expr** â a literal value or `ViewExpression` defining the field to set

  * **relative** (_True_) â whether to compute `value_or_expr` by applying it to this expression (True), or to use it untouched (False)



Returns:
    

a `ViewExpression`

sin()#
    

Computes the sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `sin()`
    view = dataset.match(F("uniqueness").sin() >= np.sin(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

sinh()#
    

Computes the hyperbolic sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `sinh()`
    view = dataset.match(F("uniqueness").sinh() >= np.sinh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

sort(_key =None_, _numeric =False_, _reverse =False_)#
    

Sorts this expression, which must resolve to an array.

If no `key` is provided, this array must contain elements whose BSON representation can be sorted by JavaScriptâs `.sort()` method.

If a `key` is provided, the array must contain documents, which are sorted by `key`, which must be a field or embedded field.

Examples:
    
    
    #
    # Sort the tags of each sample in a dataset
    #
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="im1.jpg", tags=["z", "f", "p", "a"]),
            fo.Sample(filepath="im2.jpg", tags=["y", "q", "h", "d"]),
            fo.Sample(filepath="im3.jpg", tags=["w", "c", "v", "l"]),
        ]
    )
    
    # Sort the `tags` of each sample
    view = dataset.set_field("tags", F("tags").sort())
    
    print(view.first().tags)
    
    #
    # Sort the predictions in each sample of a dataset by `confidence`
    #
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    view = dataset.set_field(
        "predictions.detections",
        F("detections").sort(key="confidence", numeric=True, reverse=True)
    )
    
    sample = view.first()
    print(sample.predictions.detections[0].confidence)
    print(sample.predictions.detections[-1].confidence)
    

Parameters:
    

  * **key** (_None_) â an optional field or `embedded.field.name` to sort by

  * **numeric** (_False_) â whether the array contains numeric values. By default, the values will be sorted alphabetically by their string representations

  * **reverse** (_False_) â whether to sort in descending order



Returns:
    

a `ViewExpression`

split(_delimiter_ , _maxsplit =None_)#
    

Splits this expression, which must resolve to a string, by the given delimiter.

The result is a string array that contains the chunks with the delimiter removed. If the delimiter is not found, this full string is returned as a single element array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add "-good" to the first tag and then split on "-" to create two
    # tags for each sample
    view = dataset.set_field(
        "tags", F("tags")[0].concat("-good").split("-")
    )
    
    print(view.first().tags)
    

Parameters:
    

  * **delimiter** â the delimiter string or `ViewExpression` resolving to a string expression

  * **maxsplit** (_None_) â a maximum number of splits to perform, from the left



Returns:
    

a `ViewExpression`

sqrt()#
    

Computes the square root of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5) ** 2 +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5) ** 2
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Returns:
    

a `ViewExpression`

starts_with(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, starts with the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose images are in "/Users" or "/home" directories
    view = dataset.match(F("filepath").starts_with(("/Users", "/home"))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

std(_sample =False_)#
    

Returns the standard deviation of the values in this expression, which must resolve to a numeric array.

Missing or `None`-valued elements are ignored.

By default, the population standard deviation is returned. If you wish to compute the sample standard deviation instead, set `sample=True`.

See <https://en.wikipedia.org/wiki/Standard_deviation#Estimation> for more information on population (biased) vs sample (unbiased) standard deviation.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the
    # standard deviation of the confidences
    view = dataset.set_field(
        "predictions.conf_std",
        F("detections").map(F("confidence")).std()
    )
    
    print(view.bounds("predictions.conf_std"))
    

Parameters:
    

**sample** (_False_) â whether to compute the sample standard deviation rather than the population standard deviation

Returns:
    

a `ViewExpression`

strip(_chars =None_)#
    

Removes whitespace characters from the beginning and end of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from each tag
    transform_tag = E(" ").concat(F(), " ").rstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

strlen()#
    

Computes the length of this expression, which must resolve to a string.

If this expressionâs value is null or missing, zero is returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Records the length of each predicted object's `label`
    label_len = F().set_field("label_len", F("label").strlen())
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(label_len),
    )
    
    print(view.bounds("predictions.detections.label_len"))
    

Returns:
    

a `ViewExpression`

substr(_start =None_, _end =None_, _count =None_)#
    

Extracts the specified substring from this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Truncate the `label` of each prediction to 3 characters
    truncate_label = F().set_field("label", F("label").substr(count=3))
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(truncate_label),
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **start** (_None_) â the starting index of the substring. If negative, specifies an offset from the end of the string

  * **end** (_None_) â the ending index of the substring. If negative, specifies an offset from the end of the string

  * **count** (_None_) â the substring length to extract. If `None`, the rest of the string is returned



Returns:
    

a `ViewExpression`

sum()#
    

Returns the sum of the values in this expression, which must resolve to a numeric array.

Missing, non-numeric, or `None`-valued elements are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the total
    # confidence of the predictions
    view = dataset.set_field(
        "predictions.total_conf",
        F("detections").map(F("confidence")).sum()
    )
    
    print(view.bounds("predictions.total_conf"))
    

Returns:
    

a `ViewExpression`

switch(_mapping_ , _default =None_)#
    

Applies a switch statement to this expression, which effectively computes the given pseudocode:
    
    
    for key, value in mapping.items():
        if self.apply(key):
            return value
    
    if default is not None:
        return default
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Round `uniqueness` values to either 0.25 or 0.75
    view = dataset.set_field(
        "uniqueness",
        F("uniqueness").switch(
            {
                (0.0 < F()) & (F() <= 0.5): 0.25,
                (0.5 < F()) & (F() <= 1.0): 0.75,
            },
        )
    )
    
    print(view.count_values("uniqueness"))
    

Parameters:
    

  * **mapping** â a dict mapping boolean `ViewExpression` keys to literal or `ViewExpression` values

  * **default** (_None_) â an optional literal or `ViewExpression` to return if none of the switch branches are taken



Returns:
    

a `ViewExpression`

tan()#
    

Computes the tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `tan()`
    view = dataset.match(F("uniqueness").tan() >= np.tan(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

tanh()#
    

Computes the hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `tanh()`
    view = dataset.match(F("uniqueness").tanh() >= np.tanh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

to_bool()#
    

Converts the expression to a boolean value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toBool) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_bool` field that is False when
    # `uniqueness < 0.5` and True when `uniqueness >= 0.5`
    dataset.add_sample_field("uniqueness_bool", fo.BooleanField)
    view = dataset.set_field(
        "uniqueness_bool", (2.0 * F("uniqueness")).floor().to_bool()
    )
    
    print(view.count_values("uniqueness_bool"))
    

Returns:
    

a `ViewExpression`

to_date()#
    

Converts the expression to a date value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toDate) for conversion rules.

Examples:
    
    
    from datetime import datetime
    import pytz
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    
    sample = fo.Sample(
        filepath="image.png",
        date_ms=1000 * now.timestamp(),
        date_str=now.isoformat(),
    )
    
    dataset = fo.Dataset()
    dataset.add_sample(sample)
    
    # Convert string/millisecond representations into datetimes
    dataset.add_sample_field("date1", fo.DateTimeField)
    dataset.add_sample_field("date2", fo.DateTimeField)
    (
        dataset
        .set_field("date1", F("date_ms").to_date())
        .set_field("date2", F("date_str").to_date())
        .save()
    )
    
    print(dataset.first())
    

Returns:
    

a `ViewExpression`

to_double()#
    

Converts the expression to a double precision value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_float` field that is 0.0 when
    # `uniqueness < 0.5` and 1.0 when `uniqueness >= 0.5`
    dataset.add_sample_field("uniqueness_float", fo.FloatField)
    view = dataset.set_field(
        "uniqueness_float", (F("uniqueness") >= 0.5).to_double()
    )
    
    print(view.count_values("uniqueness_float"))
    

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toDouble) for conversion rules.

Returns:
    

a `ViewExpression`

to_int()#
    

Converts the expression to an integer value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toInt) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_int` field that contains the value of the
    # first decimal point of the `uniqueness` field
    dataset.add_sample_field("uniqueness_int", fo.IntField)
    view = dataset.set_field(
        "uniqueness_int", (10.0 * F("uniqueness")).floor().to_int()
    )
    
    print(view.count_values("uniqueness_int"))
    

Returns:
    

a `ViewExpression`

to_string()#
    

Converts the expression to a string value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toString) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_str` field that is "true" when
    # `uniqueness >= 0.5` and "false" when `uniqueness < 0.5`
    dataset.add_sample_field("uniqueness_str", fo.StringField)
    view = dataset.set_field(
        "uniqueness_str", (F("uniqueness") >= 0.5).to_string()
    )
    
    print(view.count_values("uniqueness_str"))
    

Returns:
    

a `ViewExpression`

trunc(_place =0_)#
    

Truncates this expression, which must resolve to a numeric value, at the specified decimal place.

Positive values of `place` will truncate to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.56
    

Negative values of `place` will replace `place` digits left of the decimal with zero:
    
    
    place=-1: 1234.5678 --> 1230
    

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Only contains samples whose height is in [500, 600) pixels
    view = dataset.match(F("metadata.height").trunc(-2) == 500)
    
    print(view.bounds("metadata.height"))
    

Parameters:
    

**place** (_0_) â the decimal place at which to truncate

Returns:
    

a `ViewExpression`

type()#
    

Returns the type string of this expression.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/type) for more details.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    # Create a view that only contains samples with non-None uniqueness
    unique_only_view = view.match(F("uniqueness").type() != "null")
    
    print(len(unique_only_view))
    

Returns:
    

a `ViewExpression`

union(_* args_)#
    

Computes the set union of this expression, which must resolve to an array, and the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").union(F("other_tags"))))
    # [['a', 'b', 'c']]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

unique()#
    

Returns an array containing the unique values in this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
            )
        ]
    )
    
    print(dataset.values(F("tags").unique()))
    # [['a', 'b']]
    

Returns:
    

a `ViewExpression`

upper()#
    

Converts this expression, which must resolve to a string, to uppercase.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Converts all tags to uppercase
    transform_tag = F().upper()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Returns:
    

a `ViewExpression`

week()#
    

Returns the week of the year of this date expression (in UTC) as a number between 0 and 53.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 2, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 3, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 4, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the weeks of the year for the dataset
    print(dataset.values(F("created_at").week()))
    
    # Samples with even months of the week
    view = dataset.match(F("created_at").week() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

year()#
    

Returns the year of this date expression (in UTC).

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1971, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1972, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1973, 1, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the years for the dataset
    print(dataset.values(F("created_at").year()))
    
    # Samples from even years
    view = dataset.match(F("created_at").year() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

static zip(_* args_, _use_longest =False_, _defaults =None_)#
    

Zips the given expressions, which must resolve to arrays, into an array whose ith element is an array containing the ith element from each input array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "c"],
                ints=[1, 2, 3, 4, 5],
            ),
            fo.Sample(
                filepath="image2.jpg",
                tags=["y", "z"],
                ints=[25, 26, 27, 28],
            ),
        ]
    )
    
    dataset.add_sample_field("tags_ints", fo.ListField)
    
    # Populates an `tags_ints` field with the zipped `tags` and `ints`
    view = dataset.set_field("tags_ints", F.zip(F("tags"), F("ints")))
    
    print(view.first())
    
    # Same as above but use the longest array to determine output size
    view = dataset.set_field(
        "tags_ints",
        F.zip(F("tags"), F("ints"), use_longest=True, defaults=("", 0))
    )
    
    print(view.first())
    

Parameters:
    

  * ***args** â one or more arrays or `ViewExpression` instances resolving to arrays

  * **use_longest** (_False_) â whether to use the longest array to determine the number of elements in the output array. By default, the length of the shortest array is used

  * **defaults** (_None_) â an optional array of default values of same length as `*args` to use when `use_longest == True` and the input arrays are of different lengths. If no defaults are provided and `use_longest == True`, then missing values are set to `None`



Returns:
    

a `ViewExpression`

class fiftyone.core.expressions.ObjectId(_oid_)#
    

Bases: `ViewExpression`

A `ViewExpression` that refers to an [ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId) of a document.

The typical use case for this class is writing an expression that involves checking if the ID of a document matches a particular known ID.

Example:
    
    
    from fiftyone import ViewField as F
    from fiftyone.core.expressions import ObjectId
    
    # Check if the ID of the document matches the given ID
    expr = F("_id") == ObjectId("5f452489ef00e6374aad384a")
    

Parameters:
    

**oid** â the object ID string

**Methods:**

`to_mongo`([prefix]) | Returns a MongoDB representation of the ObjectId.  
---|---  
`abs`() | Computes the absolute value of this expression, which must resolve to a numeric value.  
`all`(exprs) | Checks whether all of the given expressions evaluate to True.  
`any`(exprs) | Checks whether any of the given expressions evaluate to True.  
`append`(value) | Appends the given value to this expression, which must resolve to an array.  
`apply`(expr) | Applies the given expression to this expression.  
`arccos`() | Computes the inverse cosine of this expression, which must resolve to a numeric value, in radians.  
`arccosh`() | Computes the inverse hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.  
`arcsin`() | Computes the inverse sine of this expression, which must resolve to a numeric value, in radians.  
`arcsinh`() | Computes the inverse hyperbolic sine of this expression, which must resolve to a numeric value, in radians.  
`arctan`() | Computes the inverse tangent of this expression, which must resolve to a numeric value, in radians.  
`arctanh`() | Computes the inverse hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.  
`cases`(mapping[,Â default]) | Applies a case statement to this expression, which effectively computes the following pseudocode.  
`ceil`() | Computes the ceiling of this expression, which must resolve to a numeric value.  
`concat`(*args) | Concatenates the given string(s) to this expression, which must resolve to a string.  
`contains`(values[,Â all]) | Checks whether this expression, which must resolve to an array, contains any of the given values.  
`contains_str`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, contains the given string or string(s).  
`cos`() | Computes the cosine of this expression, which must resolve to a numeric value, in radians.  
`cosh`() | Computes the hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.  
`day_of_month`() | Returns the day of the month of this date expression (in UTC) as a number between 1 and 31.  
`day_of_week`() | Returns the day of the week of this date expression (in UTC) as a number between 1 (Sunday) and 7 (Saturday).  
`day_of_year`() | Returns the day of the year of this date expression (in UTC) as a number between 1 and 366.  
`difference`(values) | Computes the set difference of this expression, which must resolve to an array, and the given array or array expression.  
`ends_with`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, ends with the given string or string(s).  
`enumerate`(array[,Â start]) | Returns an array of `[index, element]` pairs enumerating the elements of the given expression, which must resolve to an array.  
`exists`([bool]) | Determines whether this expression, which must resolve to a field, exists and is not None.  
`exp`() | Raises Euler's number to this expression, which must resolve to a numeric value.  
`extend`(*args) | Concatenates the given array(s) or array expression(s) to this expression, which must resolve to an array.  
`filter`(expr) | Applies the given filter to the elements of this expression, which must resolve to an array.  
`floor`() | Computes the floor of this expression, which must resolve to a numeric value.  
`hour`() | Returns the hour portion of this date expression (in UTC) as a number between 0 and 23.  
`if_else`(true_expr,Â false_expr) | Returns either `true_expr` or `false_expr` depending on the value of this expression, which must resolve to a boolean.  
`if_null`(false_expr) | Returns either this expression or `false_expr` if this expression is null.  
`insert`(index,Â value) | Inserts the value before the given index in this expression, which must resolve to an array.  
`intersection`(*args) | Computes the set intersection of this expression, which must resolve to an array, and the given array(s) or array expression(s).  
`is_array`() | Determines whether this expression is an array.  
`is_in`(values) | Creates an expression that returns a boolean indicating whether `self in values`.  
`is_missing`() | Determines whether this expression refers to a missing field.  
`is_null`() | Determines whether this expression is null.  
`is_number`() | Determines whether this expression is a number.  
`is_string`() | Determines whether this expression is a string.  
`is_subset`(values) | Checks whether this expression's contents, which must resolve to an array, are a subset of the given array or array expression's contents.  
`join`(delimiter) | Joins the elements of this expression, which must resolve to a string array, by the given delimiter.  
`length`() | Computes the length of this expression, which must resolve to an array.  
`let_in`(expr) | Returns an equivalent expression where this expression is defined as a variable that is used wherever necessary in the given expression.  
`literal`(value) | Returns an expression representing the given value without parsing.  
`ln`() | Computes the natural logarithm of this expression, which must resolve to a numeric value.  
`log`(base) | Computes the logarithm base `base` of this expression, which must resolve to a numeric value.  
`log10`() | Computes the logarithm base 10 of this expression, which must resolve to a numeric value.  
`lower`() | Converts this expression, which must resolve to a string, to lowercase.  
`lstrip`([chars]) | Removes whitespace characters from the beginning of this expression, which must resolve to a string.  
`map`(expr) | Applies the given expression to the elements of this expression, which must resolve to an array.  
`map_values`(mapping) | Replaces this expression with the corresponding value in the provided mapping dict, if it is present as a key.  
`matches_str`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, exactly matches the given string or string(s).  
`max`([value]) | Returns the maximum value of either this expression, which must resolve to an array, or the maximum of this expression and the given value.  
`mean`() | Returns the average value in this expression, which must resolve to a numeric array.  
`millisecond`() | Returns the millisecond portion of this date expression (in UTC) as an integer between 0 and 999.  
`min`([value]) | Returns the minimum value of either this expression, which must resolve to an array, or the minimum of this expression and the given value.  
`minute`() | Returns the minute portion of this date expression (in UTC) as a number between 0 and 59.  
`month`() | Returns the month of this date expression (in UTC) as a number between 1 and 12.  
`pow`(power) | Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.  
`prepend`(value) | Prepends the given value to this expression, which must resolve to an array.  
`rand`() | Returns an expression that generates a uniform random float in `[0, 1]` each time it is called.  
`randn`() | Returns an expression that generates a sample from the standard Gaussian distribution each time it is called.  
`range`(start[,Â stop]) | Returns an array expression containing the sequence of integers from the specified start (inclusive) to stop (exclusive).  
`re_match`(regex[,Â options]) | Performs a regular expression pattern match on this expression, which must resolve to a string.  
`reduce`(expr[,Â init_val]) | Applies the given reduction to this expression, which must resolve to an array, and returns the single value computed.  
`replace`(old,Â new) | Replaces all occurrences of `old` with `new` in this expression, which must resolve to a string.  
`reverse`() | Reverses the order of the elements in the expression, which must resolve to an array.  
`round`([place]) | Rounds this expression, which must resolve to a numeric value, at the given decimal place.  
`rsplit`(delimiter[,Â maxsplit]) | Splits this expression, which must resolve to a string, by the given delimiter.  
`rstrip`([chars]) | Removes whitespace characters from the end of this expression, which must resolve to a string.  
`second`() | Returns the second portion of this date expression (in UTC) as a number between 0 and 59.  
`set_equals`(*args) | Checks whether this expression, which must resolve to an array, contains the same distinct values as each of the given array(s) or array expression(s).  
`set_field`(field,Â value_or_expr[,Â relative]) | Sets the specified field or embedded field of this expression, which must resolve to a document, to the given value or expression.  
`sin`() | Computes the sine of this expression, which must resolve to a numeric value, in radians.  
`sinh`() | Computes the hyperbolic sine of this expression, which must resolve to a numeric value, in radians.  
`sort`([key,Â numeric,Â reverse]) | Sorts this expression, which must resolve to an array.  
`split`(delimiter[,Â maxsplit]) | Splits this expression, which must resolve to a string, by the given delimiter.  
`sqrt`() | Computes the square root of this expression, which must resolve to a numeric value.  
`starts_with`(str_or_strs[,Â case_sensitive]) | Determines whether this expression, which must resolve to a string, starts with the given string or string(s).  
`std`([sample]) | Returns the standard deviation of the values in this expression, which must resolve to a numeric array.  
`strip`([chars]) | Removes whitespace characters from the beginning and end of this expression, which must resolve to a string.  
`strlen`() | Computes the length of this expression, which must resolve to a string.  
`substr`([start,Â end,Â count]) | Extracts the specified substring from this expression, which must resolve to a string.  
`sum`() | Returns the sum of the values in this expression, which must resolve to a numeric array.  
`switch`(mapping[,Â default]) | Applies a switch statement to this expression, which effectively computes the given pseudocode.  
`tan`() | Computes the tangent of this expression, which must resolve to a numeric value, in radians.  
`tanh`() | Computes the hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.  
`to_bool`() | Converts the expression to a boolean value.  
`to_date`() | Converts the expression to a date value.  
`to_double`() | Converts the expression to a double precision value.  
`to_int`() | Converts the expression to an integer value.  
`to_string`() | Converts the expression to a string value.  
`trunc`([place]) | Truncates this expression, which must resolve to a numeric value, at the specified decimal place.  
`type`() | Returns the type string of this expression.  
`union`(*args) | Computes the set union of this expression, which must resolve to an array, and the given array(s) or array expression(s).  
`unique`() | Returns an array containing the unique values in this expression, which must resolve to an array.  
`upper`() | Converts this expression, which must resolve to a string, to uppercase.  
`week`() | Returns the week of the year of this date expression (in UTC) as a number between 0 and 53.  
`year`() | Returns the year of this date expression (in UTC).  
`zip`(*args[,Â use_longest,Â defaults]) | Zips the given expressions, which must resolve to arrays, into an array whose ith element is an array containing the ith element from each input array.  
  
**Attributes:**

`is_frozen` | Whether this expression's prefix is frozen.  
---|---  
  
to_mongo(_prefix =None_)#
    

Returns a MongoDB representation of the ObjectId.

Parameters:
    

**prefix** (_None_) â unused

Returns:
    

a MongoDB expression

abs()#
    

Computes the absolute value of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match((F("uniqueness") - 0.5).abs() < 0.25)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

static all(_exprs_)#
    

Checks whether all of the given expressions evaluate to True.

If no expressions are provided, returns True.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains predictions that are "cat" and
    # highly confident
    is_cat = F("label") == "cat"
    is_confident = F("confidence") > 0.95
    view = dataset.filter_labels(
        "predictions", F.all([is_cat, is_confident])
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**exprs** â a `ViewExpression` or iterable of `ViewExpression` instances

Returns:
    

a `ViewExpression`

static any(_exprs_)#
    

Checks whether any of the given expressions evaluate to True.

If no expressions are provided, returns False.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains predictions that are "cat" or
    # highly confident
    is_cat = F("label") == "cat"
    is_confident = F("confidence") > 0.95
    view = dataset.filter_labels(
        "predictions", F.any([is_cat, is_confident])
    )
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**exprs** â a `ViewExpression` or iterable of `ViewExpression` instances

Returns:
    

a `ViewExpression`

append(_value_)#
    

Appends the given value to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "b"]),
        ]
    )
    
    # Appends the "c" tag to each sample
    view = dataset.set_field("tags", F("tags").append("c"))
    
    print(view.first().tags)
    

Parameters:
    

**value** â the value or `ViewExpression`

Returns:
    

a `ViewExpression`

apply(_expr_)#
    

Applies the given expression to this expression.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match(
        F("uniqueness").apply((F() > 0.25) & (F() < 0.75))
    )
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

arccos()#
    

Computes the inverse cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arccos()`
    view = dataset.match(F("uniqueness").arccos() <= np.arccos(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arccosh()#
    

Computes the inverse hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arccosh()`
    view = dataset.match((1 + F("uniqueness")).arccosh() >= np.arccosh(1.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arcsin()#
    

Computes the inverse sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arcsin()`
    view = dataset.match(F("uniqueness").arcsin() >= np.arcsin(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arcsinh()#
    

Computes the inverse hyperbolic sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arcsinh()`
    view = dataset.match(F("uniqueness").arcsinh() >= np.arcsinh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arctan()#
    

Computes the inverse tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arctan()`
    view = dataset.match(F("uniqueness").arctan() >= np.arctan(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

arctanh()#
    

Computes the inverse hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `arctanh()`
    view = dataset.match(F("uniqueness").arctanh() >= np.arctanh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

cases(_mapping_ , _default =None_)#
    

Applies a case statement to this expression, which effectively computes the following pseudocode:
    
    
    for key, value in mapping.items():
        if self == key:
            return value
    
    if default is not None:
        return default
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    # Map numeric `uniqueness` values to 1 and null values to 0
    cases_view = view.set_field(
        "uniqueness",
        F("uniqueness").type().cases({"double": 1, "null": 0}),
    )
    
    print(cases_view.count_values("uniqueness"))
    

Parameters:
    

  * **mapping** â a dict mapping literals or `ViewExpression` keys to literal or `ViewExpression` values

  * **default** (_None_) â an optional literal or `ViewExpression` to return if none of the switch branches are taken



Returns:
    

a `ViewExpression`

ceil()#
    

Computes the ceiling of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match((F("uniqueness") + 0.5).ceil() == 2)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

concat(_* args_)#
    

Concatenates the given string(s) to this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Appends "-tag" to all tags
    transform_tag = F().concat("-tag")
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

  * ***args** â one or more strings or string `ViewExpression` instances

  * **before** (_False_) â whether to position `args` before this string in the output string



Returns:
    

a `ViewExpression`

contains(_values_ , _all =False_)#
    

Checks whether this expression, which must resolve to an array, contains any of the given values.

Pass `all=True` to require that this expression contains all of the given values.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    print(dataset.count())
    
    # Only contains samples with a "cat" prediction
    view = dataset.match(
        F("predictions.detections.label").contains("cat")
    )
    print(view.count())
    
    # Only contains samples with "cat" or "dog" predictions
    view = dataset.match(
        F("predictions.detections.label").contains(["cat", "dog"])
    )
    print(view.count())
    
    # Only contains samples with "cat" and "dog" predictions
    view = dataset.match(
        F("predictions.detections.label").contains(["cat", "dog"], all=True)
    )
    print(view.count())
    

Parameters:
    

  * **values** â a value, iterable of values, or `ViewExpression` that resolves to an array of values

  * **all** (_False_) â whether this expression must contain all (True) or any (False) of the given values



Returns:
    

a `ViewExpression`

contains_str(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, contains the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions whose `label` contains "be"
    view = dataset.filter_labels(
        "predictions", F("label").contains_str("be")
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

cos()#
    

Computes the cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `cos()`
    view = dataset.match(F("uniqueness").cos() <= np.cos(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

cosh()#
    

Computes the hyperbolic cosine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `cosh()`
    view = dataset.match(F("uniqueness").cosh() >= np.cosh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

day_of_month()#
    

Returns the day of the month of this date expression (in UTC) as a number between 1 and 31.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the month for the dataset
    print(dataset.values(F("created_at").day_of_month()))
    
    # Samples with even days of the month
    view = dataset.match(F("created_at").day_of_month() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_week()#
    

Returns the day of the week of this date expression (in UTC) as a number between 1 (Sunday) and 7 (Saturday).

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 5),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 6),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 7),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the week for the dataset
    print(dataset.values(F("created_at").day_of_week()))
    
    # Samples with even days of the week
    view = dataset.match(F("created_at").day_of_week() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

day_of_year()#
    

Returns the day of the year of this date expression (in UTC) as a number between 1 and 366.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the days of the year for the dataset
    print(dataset.values(F("created_at").day_of_year()))
    
    # Samples with even days of the year
    view = dataset.match(F("created_at").day_of_year() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

difference(_values_)#
    

Computes the set difference of this expression, which must resolve to an array, and the given array or array expression.

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").difference(F("other_tags"))))
    # [['b']]
    

Parameters:
    

**values** â an iterable of values or a `ViewExpression` that resolves to an array

Returns:
    

a `ViewExpression`

ends_with(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, ends with the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose images are JPEGs or PNGs
    view = dataset.match(F("filepath").ends_with((".jpg", ".png")))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

static enumerate(_array_ , _start =0_)#
    

Returns an array of `[index, element]` pairs enumerating the elements of the given expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["y", "z"]),
        ]
    )
    
    # Populates an `enumerated_tags` field with the enumerated `tag`
    dataset.add_sample_field("enumerated_tags", fo.ListField)
    view = dataset.set_field("enumerated_tags", F.enumerate(F("tags")))
    
    print(view.first())
    

Parameters:
    

  * **array** â a `ViewExpression` that resolves to an array

  * **start** (_0_) â the starting enumeration index to use



Returns:
    

a `ViewExpression`

exists(_bool =True_)#
    

Determines whether this expression, which must resolve to a field, exists and is not None.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset(
        "quickstart", dataset_name=fo.get_default_dataset_name()
    )
    
    # Add a new field to one sample
    sample = dataset.first()
    sample["new_field"] = ["hello", "there"]
    sample.save()
    
    # Get samples that have a value for `new_field`
    view = dataset.match(F("new_field").exists())
    
    print(len(view))
    

Parameters:
    

**bool** (_True_) â whether to determine whether this expression exists (True) or is None or non-existent (False)

Returns:
    

a `ViewExpression`

exp()#
    

Raises Eulerâs number to this expression, which must resolve to a numeric value.

Returns:
    

a `ViewExpression`

extend(_* args_)#
    

Concatenates the given array(s) or array expression(s) to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "b"]),
        ]
    )
    
    # Adds the "c" and "d" tags to each sample
    view = dataset.set_field("tags", F("tags").extend(["c", "d"]))
    
    print(view.first().tags)
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

filter(_expr_)#
    

Applies the given filter to the elements of this expression, which must resolve to an array.

The output array will only contain elements of the input array for which `expr` returns `True`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only include predictions with `confidence` of at least 0.9
    view = dataset.set_field(
        "predictions.detections",
        F("detections").filter(F("confidence") > 0.9)
    )
    
    print(view.bounds("predictions.detections.confidence"))
    

Parameters:
    

**expr** â a `ViewExpression` that returns a boolean

Returns:
    

a `ViewExpression`

floor()#
    

Computes the floor of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.5, 1]
    view = dataset.match((F("uniqueness") + 0.5).floor() == 1)
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

hour()#
    

Returns the hour portion of this date expression (in UTC) as a number between 0 and 23.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the hour portion of the dates in the dataset
    print(dataset.values(F("created_at").hour()))
    
    # Samples with even hours
    view = dataset.match(F("created_at").hour() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

if_else(_true_expr_ , _false_expr_)#
    

Returns either `true_expr` or `false_expr` depending on the value of this expression, which must resolve to a boolean.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

  * **true_expr** â a `ViewExpression` or MongoDB expression dict

  * **false_expr** â a `ViewExpression` or MongoDB expression dict



Returns:
    

a `ViewExpression`

if_null(_false_expr_)#
    

Returns either this expression or `false_expr` if this expression is null. This is a shortcut for `self.is_null().if_else(false_expr, self)` and is useful for replacing null values in a field with a default value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `gt.detection.label` field to "unknown" if it does not exist
    view = dataset.set_field(
        "gt.detection.label",
        F("gt.detection.label").if_null("unknown")
    )
    

Parameters:
    

**false_expr** â a `ViewExpression` or MongoDB expression dict

Returns:
    

a `ViewExpression`

insert(_index_ , _value_)#
    

Inserts the value before the given index in this expression, which must resolve to an array.

If `index <= 0`, the value is prepended to this array. If `index >= self.length()`, the value is appended to this array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["a", "c"]),
        ]
    )
    
    # Adds the "ready" tag to each sample
    view = dataset.set_field("tags", F("tags").insert(1, "b"))
    
    print(view.first().tags)
    

Parameters:
    

  * **index** â the index at which to insert the value

  * **value** â the value or `ViewExpression`



Returns:
    

a `ViewExpression`

intersection(_* args_)#
    

Computes the set intersection of this expression, which must resolve to an array, and the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").intersection(F("other_tags"))))
    # [['a']]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

is_array()#
    

Determines whether this expression is an array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that tags are arrays
    view = dataset.match(F("tags").is_array())
    
    print(len(view))
    

Returns:
    

`ViewExpression`

property is_frozen#
    

Whether this expressionâs prefix is frozen.

is_in(_values_)#
    

Creates an expression that returns a boolean indicating whether `self in values`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Create a view that only contains animal predictions
    view = dataset.filter_labels(
        "predictions", F("label").is_in(ANIMALS)
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

**values** â a value or iterable of values

Returns:
    

a `ViewExpression`

is_missing()#
    

Determines whether this expression refers to a missing field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that `foobar` is a non-existent field on all samples
    view = dataset.match(F("foobar").is_missing())
    
    print(len(view) == len(dataset))
    

Returns:
    

`ViewExpression`

is_null()#
    

Determines whether this expression is null.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.25 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.25).if_else(F("uniqueness"), None)
    )
    
    # Create view that only contains samples with uniqueness = None
    not_unique_view = view.match(F("uniqueness").is_null())
    
    print(len(not_unique_view))
    

Returns:
    

`ViewExpression`

is_number()#
    

Determines whether this expression is a number.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.25 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") >= 0.25).if_else(F("uniqueness"), None)
    )
    
    # Create view that only contains samples with uniqueness values
    has_unique_view = view.match(F("uniqueness").is_number())
    
    print(len(has_unique_view))
    

Returns:
    

`ViewExpression`

is_string()#
    

Determines whether this expression is a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Verify that filepaths are strings
    view = dataset.match(F("filepath").is_string())
    
    print(len(view))
    

Returns:
    

`ViewExpression`

is_subset(_values_)#
    

Checks whether this expressionâs contents, which must resolve to an array, are a subset of the given array or array expressionâs contents.

The arrays are treated as sets, so duplicate values are ignored.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
                other_tags=["a", "b", "c"],
            )
        ]
    )
    
    print(dataset.values(F("tags").is_subset(F("other_tags"))))
    # [True]
    

Parameters:
    

**values** â an iterable of values or a `ViewExpression` that resolves to an array

Returns:
    

a `ViewExpression`

join(_delimiter_)#
    

Joins the elements of this expression, which must resolve to a string array, by the given delimiter.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Generate a `list,of,labels` for the `predictions` of each sample
    view = dataset.set_field(
        "predictions.labels",
        F("detections").map(F("label")).join(",")
    )
    
    print(view.first().predictions.labels)
    

Parameters:
    

**delimiter** â the delimiter string

Returns:
    

a `ViewExpression`

length()#
    

Computes the length of this expression, which must resolve to an array.

If this expressionâs value is null or missing, zero is returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with at least 15 predicted objects
    view = dataset.match(F("predictions.detections").length() >= 15)
    
    print(dataset.count())
    print(view.count())
    

Returns:
    

a `ViewExpression`

let_in(_expr_)#
    

Returns an equivalent expression where this expression is defined as a variable that is used wherever necessary in the given expression.

This method is useful when `expr` contains multiple instances of this expression, since it avoids duplicate computation of this expression in the final pipeline.

If `expr` is a simple expression such as a `ViewField`, no variable is defined and `expr` is directly returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    good_bboxes = (bbox_area > 0.25) & (bbox_area < 0.75)
    
    # Optimize the expression
    good_bboxes_opt = bbox_area.let_in(good_bboxes)
    
    # Contains predictions whose bounding box areas are in [0.25, 0.75]
    view = dataset.filter_labels("predictions", good_bboxes_opt)
    
    print(good_bboxes)
    print(good_bboxes_opt)
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

static literal(_value_)#
    

Returns an expression representing the given value without parsing.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/literal) for more information on when this method is required.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add the "$money" tag to each sample
    # The "$" character ordinarily has special meaning, so we must wrap
    # it in `literal()` in order to add it via this method
    view = dataset.set_field(
        "tags", F("tags").append(F.literal("$money"))
    )
    
    print(view.first().tags)
    

Parameters:
    

**value** â a value

Returns:
    

a `ViewExpression`

ln()#
    

Computes the natural logarithm of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").ln() >= math.log(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

log(_base_)#
    

Computes the logarithm base `base` of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").log(2) >= math.log2(0.5))
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**base** â the logarithm base

Returns:
    

a `ViewExpression`

log10()#
    

Computes the logarithm base 10 of this expression, which must resolve to a numeric value.

Examples:
    
    
    import math
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5
    view = dataset.match(F("uniqueness").log10() >= math.log10(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

lower()#
    

Converts this expression, which must resolve to a string, to lowercase.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Converts all tags to lowercase
    transform_tag = F().lower()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Returns:
    

a `ViewExpression`

lstrip(_chars =None_)#
    

Removes whitespace characters from the beginning of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from the beginning of each tag
    transform_tag = E(" ").concat(F()).lstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

map(_expr_)#
    

Applies the given expression to the elements of this expression, which must resolve to an array.

The output will be an array with the applied results.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Only include predictions with `confidence` of at least 0.9
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(F().set_field("area", bbox_area))
    )
    
    print(view.bounds("predictions.detections.area"))
    

Parameters:
    

**expr** â a `ViewExpression`

Returns:
    

a `ViewExpression`

map_values(_mapping_)#
    

Replaces this expression with the corresponding value in the provided mapping dict, if it is present as a key.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replace the `label` of all animal objects in the `predictions`
    # field with "animal"
    #
    mapping = {a: "animal" for a in ANIMALS}
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(
            F().set_field("label", F("label").map_values(mapping))
        )
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

**mapping** â a dict mapping keys to replacement values

Returns:
    

a `ViewExpression`

matches_str(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, exactly matches the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains predictions whose `label` is "cat" or "dog", case
    # insensitive
    view = dataset.map_labels(
        "predictions", {"cat": "CAT", "dog": "DOG"}
    ).filter_labels(
        "predictions",
        F("label").matches_str(("cat", "dog"), case_sensitive=False)
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

max(_value =None_)#
    

Returns the maximum value of either this expression, which must resolve to an array, or the maximum of this expression and the given value.

Missing or `None` values are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Adds a `max_area` property to the `predictions` field that
    # records the maximum prediction area in that sample
    view = dataset.set_field(
        "predictions.max_area",
        F("detections").map(bbox_area).max()
    )
    
    print(view.bounds("predictions.max_area"))
    

Parameters:
    

**value** (_None_) â an optional value to compare to

Returns:
    

a `ViewExpression`

mean()#
    

Returns the average value in this expression, which must resolve to a numeric array.

Missing or `None`-valued elements are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the average
    # confidence of the predictions
    view = dataset.set_field(
        "predictions.conf_mean",
        F("detections").map(F("confidence")).mean()
    )
    
    print(view.bounds("predictions.conf_mean"))
    

Returns:
    

a `ViewExpression`

millisecond()#
    

Returns the millisecond portion of this date expression (in UTC) as an integer between 0 and 999.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 1000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 2000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 3000),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 0, 4000),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the millisecond portion of the dates in the dataset
    print(dataset.values(F("created_at").millisecond()))
    
    # Samples with even milliseconds
    view = dataset.match(F("created_at").millisecond() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

min(_value =None_)#
    

Returns the minimum value of either this expression, which must resolve to an array, or the minimum of this expression and the given value.

Missing or `None` values are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    # Adds a `min_area` property to the `predictions` field that
    # records the minimum prediction area in that sample
    view = dataset.set_field(
        "predictions.min_area",
        F("detections").map(bbox_area).min()
    )
    
    print(view.bounds("predictions.min_area"))
    

Parameters:
    

**value** (_None_) â an optional value to compare to

Returns:
    

a `ViewExpression`

minute()#
    

Returns the minute portion of this date expression (in UTC) as a number between 0 and 59.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the minute portion of the dates in the dataset
    print(dataset.values(F("created_at").minute()))
    
    # Samples with even minutes
    view = dataset.match(F("created_at").minute() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

month()#
    

Returns the month of this date expression (in UTC) as a number between 1 and 12.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 2, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 3, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 4, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the months of the year for the dataset
    print(dataset.values(F("created_at").month()))
    
    # Samples from even months of the year
    view = dataset.match(F("created_at").month() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

pow(_power_)#
    

Raises this expression, which must resolve to a numeric value, to the given power, `self ** power`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5).pow(2) +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5).pow(2)
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Parameters:
    

**power** â the power

Returns:
    

a `ViewExpression`

prepend(_value_)#
    

Prepends the given value to this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["b", "c"]),
        ]
    )
    
    # Adds the "a" tag to each sample
    view = dataset.set_field("tags", F("tags").prepend("a"))
    
    print(view.first().tags)
    

Parameters:
    

**value** â the value or `ViewExpression`

Returns:
    

a `ViewExpression`

static rand()#
    

Returns an expression that generates a uniform random float in `[0, 1]` each time it is called.

Warning

This expression will generate new values each time it is used, so you likely do not want to use it to construct dataset views, since such views would produce different outputs each time they are used.

A typical usage for this expression is in conjunction with [`fiftyone.core.view.DatasetView.set_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.set_field "fiftyone.core.view.DatasetView.set_field") and [`fiftyone.core.view.DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to populate a randomized field on a dataset.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    #
    # Populate a new `rand` field with random numbers
    #
    
    dataset.add_sample_field("rand", fo.FloatField)
    dataset.set_field("rand", E.rand()).save("rand")
    
    print(dataset.bounds("rand"))
    
    #
    # Create a view that contains a different 10%% of the dataset each
    # time it is used
    #
    
    view = dataset.match(E.rand() < 0.1)
    
    print(view.first().id)
    print(view.first().id)  # probably different!
    

Returns:
    

a `ViewExpression`

static randn()#
    

Returns an expression that generates a sample from the standard Gaussian distribution each time it is called.

Warning

This expression will generate new values each time it is used, so you likely do not want to use it to construct dataset views, since such views would produce different outputs each time they are used.

A typical usage for this expression is in conjunction with [`fiftyone.core.view.DatasetView.set_field()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.set_field "fiftyone.core.view.DatasetView.set_field") and [`fiftyone.core.view.DatasetView.save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to populate a randomized field on a dataset.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    #
    # Populate a new `randn` field with random numbers
    #
    
    dataset.add_sample_field("randn", fo.FloatField)
    dataset.set_field("randn", E.randn()).save("randn")
    
    print(dataset.bounds("randn"))
    
    #
    # Create a view that contains a different 50%% of the dataset each
    # time it is used
    #
    
    view = dataset.match(E.randn() < 0)
    
    print(view.first().id)
    print(view.first().id)  # probably different!
    

Returns:
    

a `ViewExpression`

static range(_start_ , _stop =None_)#
    

Returns an array expression containing the sequence of integers from the specified start (inclusive) to stop (exclusive).

If `stop` is provided, returns `[start, start + 1, ..., stop - 1]`.

If no `stop` is provided, returns `[0, 1, ..., start - 1]`.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.jpg", tags=["a", "b", "c"]),
            fo.Sample(filepath="image2.jpg", tags=["y", "z"]),
        ]
    )
    
    # Populates an `ints` field based on the number of `tags`
    dataset.add_sample_field("ints", fo.ListField)
    view = dataset.set_field("ints", F.range(F("tags").length()))
    
    print(view.first())
    

Parameters:
    

  * **start** â the starting value, or stopping value if no `stop` is provided

  * **stop** (_None_) â the stopping value, if both input arguments are provided



Returns:
    

a `ViewExpression`

re_match(_regex_ , _options =None_)#
    

Performs a regular expression pattern match on this expression, which must resolve to a string.

The output of the expression will be `True` if the pattern matches and `False` otherwise.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Get samples whose images are JPEGs
    #
    
    view = dataset.match(F("filepath").re_match("\.jpg$"))
    
    print(view.count())
    print(view.first().filepath)
    
    #
    # Get samples whose images are in the "/Users" directory
    #
    
    view = dataset.match(F("filepath").re_match("^/Users/"))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **regex** â the regular expression to apply. Must be a Perl Compatible Regular Expression (PCRE). See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/#regexmatch-regex) for details

  * **options** (_None_) â an optional string of regex options to apply. See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/#regexmatch-options) for the available options



Returns:
    

a `ViewExpression`

reduce(_expr_ , _init_val =0_)#
    

Applies the given reduction to this expression, which must resolve to an array, and returns the single value computed.

The provided `expr` must include the `VALUE` expression to properly define the reduction.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    from fiftyone.core.expressions import VALUE
    
    #
    # Compute the number of keypoints in each sample of a dataset
    #
    
    dataset = fo.Dataset()
    dataset.add_sample(
        fo.Sample(
            filepath="image.jpg",
            keypoints=fo.Keypoints(
                keypoints=[
                    fo.Keypoint(points=[(0, 0), (1, 1)]),
                    fo.Keypoint(points=[(0, 0), (1, 0), (1, 1), (0, 1)]),
                ]
            )
        )
    )
    
    view = dataset.set_field(
        "keypoints.count",
        F("$keypoints.keypoints").reduce(VALUE + F("points").length()),
    )
    
    print(view.first().keypoints.count)
    
    #
    # Generate a `list,of,labels` for the `predictions` of each sample
    #
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    join_labels = F("detections").reduce(
        VALUE.concat(",", F("label")), init_val=""
    ).lstrip(",")
    
    view = dataset.set_field("predictions.labels", join_labels)
    
    print(view.first().predictions.labels)
    

Parameters:
    

  * **expr** â a `ViewExpression` defining the reduction expression to apply. Must contain the `VALUE` expression

  * **init_val** (_0_) â an initial value for the reduction



Returns:
    

a `ViewExpression`

replace(_old_ , _new_)#
    

Replaces all occurrences of `old` with `new` in this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Replaces "val" with "VAL" in each tag
    transform_tag = F().replace("val", "VAL")
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

  * **old** â a string or `ViewExpression` resolving to a string expression specifying the substring to replace

  * **new** â a string or `ViewExpression` resolving to a string expression specifying the replacement value



Returns:
    

a `ViewExpression`

reverse()#
    

Reverses the order of the elements in the expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    first_obj = F("predictions.detections")[0]
    last_obj = F("predictions.detections").reverse()[0]
    
    # Only contains samples whose first and last prediction have the
    # same label
    view = dataset.match(
        first_obj.apply(F("label")) == last_obj.apply(F("label"))
    )
    
    print(dataset.count())
    print(view.count())
    

Returns:
    

a `ViewExpression`

round(_place =0_)#
    

Rounds this expression, which must resolve to a numeric value, at the given decimal place.

Positive values of `place` will round to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.57
    

Negative values of `place` will round `place` digits left of the decimal:
    
    
    place=-1: 1234.5678 --> 1230
    

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Only contains samples with `uniqueness` in [0.25, 0.75]
    view = dataset.match((2 * F("uniqueness")).round() == 1)
    
    print(view.bounds("uniqueness"))
    

Parameters:
    

**place** (_0_) â the decimal place at which to round. Must be an integer in range `(-20, 100)`

Returns:
    

a `ViewExpression`

rsplit(_delimiter_ , _maxsplit =None_)#
    

Splits this expression, which must resolve to a string, by the given delimiter.

If the number of chunks exceeds `maxsplit`, splits are only performed on the last `maxsplit` occurrences of the delimiter.

The result is a string array that contains the chunks with the delimiter removed. If the delimiter is not found, this full string is returned as a single element array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add "-ok-go" to the first tag and then split once on "-" from the
    # right to create two tags for each sample
    view = dataset.set_field(
        "tags", F("tags")[0].concat("-ok-go").rsplit("-", 1)
    )
    
    print(view.first().tags)
    

Parameters:
    

  * **delimiter** â the delimiter string or `ViewExpression` resolving to a string expression

  * **maxsplit** (_None_) â a maximum number of splits to perform, from the right



Returns:
    

a `ViewExpression`

rstrip(_chars =None_)#
    

Removes whitespace characters from the end of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from the end of each tag
    transform_tag = F().concat(" ").rstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

second()#
    

Returns the second portion of this date expression (in UTC) as a number between 0 and 59.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 2),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 3),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1, 0, 0, 4),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the second portion of the dates in the dataset
    print(dataset.values(F("created_at").second()))
    
    # Samples with even seconds
    view = dataset.match(F("created_at").second() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

set_equals(_* args_)#
    

Checks whether this expression, which must resolve to an array, contains the same distinct values as each of the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are ignored.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
                other_tags=["a", "b", "b"],
            )
        ]
    )
    
    print(dataset.values(F("tags").set_equals(F("other_tags"))))
    # [True]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

set_field(_field_ , _value_or_expr_ , _relative =True_)#
    

Sets the specified field or embedded field of this expression, which must resolve to a document, to the given value or expression.

By default, the provided expression is computed by applying it to this expression via `self.apply(value_or_expr)`.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replaces the `label` attributes of the objects in the
    # `predictions` field according to the following rule:
    #
    #   If the `label` starts with `b`, replace it with `b`. Otherwise,
    #   replace it with "other"
    #
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(
            F().set_field(
                "label",
                F("label").re_match("^b").if_else("b", "other"),
            )
        )
    )
    
    print(view.count_values("predictions.detections.label"))
    

Parameters:
    

  * **field** â the âfieldâ or âembedded.field.nameâ to set

  * **value_or_expr** â a literal value or `ViewExpression` defining the field to set

  * **relative** (_True_) â whether to compute `value_or_expr` by applying it to this expression (True), or to use it untouched (False)



Returns:
    

a `ViewExpression`

sin()#
    

Computes the sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `sin()`
    view = dataset.match(F("uniqueness").sin() >= np.sin(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

sinh()#
    

Computes the hyperbolic sine of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `sinh()`
    view = dataset.match(F("uniqueness").sinh() >= np.sinh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

sort(_key =None_, _numeric =False_, _reverse =False_)#
    

Sorts this expression, which must resolve to an array.

If no `key` is provided, this array must contain elements whose BSON representation can be sorted by JavaScriptâs `.sort()` method.

If a `key` is provided, the array must contain documents, which are sorted by `key`, which must be a field or embedded field.

Examples:
    
    
    #
    # Sort the tags of each sample in a dataset
    #
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="im1.jpg", tags=["z", "f", "p", "a"]),
            fo.Sample(filepath="im2.jpg", tags=["y", "q", "h", "d"]),
            fo.Sample(filepath="im3.jpg", tags=["w", "c", "v", "l"]),
        ]
    )
    
    # Sort the `tags` of each sample
    view = dataset.set_field("tags", F("tags").sort())
    
    print(view.first().tags)
    
    #
    # Sort the predictions in each sample of a dataset by `confidence`
    #
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    view = dataset.set_field(
        "predictions.detections",
        F("detections").sort(key="confidence", numeric=True, reverse=True)
    )
    
    sample = view.first()
    print(sample.predictions.detections[0].confidence)
    print(sample.predictions.detections[-1].confidence)
    

Parameters:
    

  * **key** (_None_) â an optional field or `embedded.field.name` to sort by

  * **numeric** (_False_) â whether the array contains numeric values. By default, the values will be sorted alphabetically by their string representations

  * **reverse** (_False_) â whether to sort in descending order



Returns:
    

a `ViewExpression`

split(_delimiter_ , _maxsplit =None_)#
    

Splits this expression, which must resolve to a string, by the given delimiter.

The result is a string array that contains the chunks with the delimiter removed. If the delimiter is not found, this full string is returned as a single element array.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add "-good" to the first tag and then split on "-" to create two
    # tags for each sample
    view = dataset.set_field(
        "tags", F("tags")[0].concat("-good").split("-")
    )
    
    print(view.first().tags)
    

Parameters:
    

  * **delimiter** â the delimiter string or `ViewExpression` resolving to a string expression

  * **maxsplit** (_None_) â a maximum number of splits to perform, from the left



Returns:
    

a `ViewExpression`

sqrt()#
    

Computes the square root of this expression, which must resolve to a numeric value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    center_dist = (
        (F("bounding_box")[0] + 0.5 * F("bounding_box")[2] - 0.5) ** 2 +
        (F("bounding_box")[1] + 0.5 * F("bounding_box")[3] - 0.5) ** 2
    ).sqrt()
    
    # Only contains predictions whose bounding box center is a distance
    # of at most 0.02 from the center of the image
    view = dataset.select_fields("predictions").filter_labels(
        "predictions", center_dist < 0.02
    )
    
    session = fo.launch_app(view=view)
    

Returns:
    

a `ViewExpression`

starts_with(_str_or_strs_ , _case_sensitive =True_)#
    

Determines whether this expression, which must resolve to a string, starts with the given string or string(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose images are in "/Users" or "/home" directories
    view = dataset.match(F("filepath").starts_with(("/Users", "/home"))
    
    print(view.count())
    print(view.first().filepath)
    

Parameters:
    

  * **str_or_strs** â a string or iterable of strings

  * **case_sensitive** (_True_) â whether to perform a case sensitive match



Returns:
    

a `ViewExpression`

std(_sample =False_)#
    

Returns the standard deviation of the values in this expression, which must resolve to a numeric array.

Missing or `None`-valued elements are ignored.

By default, the population standard deviation is returned. If you wish to compute the sample standard deviation instead, set `sample=True`.

See <https://en.wikipedia.org/wiki/Standard_deviation#Estimation> for more information on population (biased) vs sample (unbiased) standard deviation.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the
    # standard deviation of the confidences
    view = dataset.set_field(
        "predictions.conf_std",
        F("detections").map(F("confidence")).std()
    )
    
    print(view.bounds("predictions.conf_std"))
    

Parameters:
    

**sample** (_False_) â whether to compute the sample standard deviation rather than the population standard deviation

Returns:
    

a `ViewExpression`

strip(_chars =None_)#
    

Removes whitespace characters from the beginning and end of this expression, which must resolve to a string.

If `chars` is provided, those characters are removed instead of whitespace.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewExpression as E
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Adds and then strips whitespace from each tag
    transform_tag = E(" ").concat(F(), " ").rstrip()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Parameters:
    

**chars** (_None_) â an optional string or `ViewExpression` resolving to a string expression specifying characters to remove

Returns:
    

a `ViewExpression`

strlen()#
    

Computes the length of this expression, which must resolve to a string.

If this expressionâs value is null or missing, zero is returned.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Records the length of each predicted object's `label`
    label_len = F().set_field("label_len", F("label").strlen())
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(label_len),
    )
    
    print(view.bounds("predictions.detections.label_len"))
    

Returns:
    

a `ViewExpression`

substr(_start =None_, _end =None_, _count =None_)#
    

Extracts the specified substring from this expression, which must resolve to a string.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Truncate the `label` of each prediction to 3 characters
    truncate_label = F().set_field("label", F("label").substr(count=3))
    view = dataset.set_field(
        "predictions.detections",
        F("detections").map(truncate_label),
    )
    
    print(view.distinct("predictions.detections.label"))
    

Parameters:
    

  * **start** (_None_) â the starting index of the substring. If negative, specifies an offset from the end of the string

  * **end** (_None_) â the ending index of the substring. If negative, specifies an offset from the end of the string

  * **count** (_None_) â the substring length to extract. If `None`, the rest of the string is returned



Returns:
    

a `ViewExpression`

sum()#
    

Returns the sum of the values in this expression, which must resolve to a numeric array.

Missing, non-numeric, or `None`-valued elements are ignored.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Add a field to each `predictions` object that records the total
    # confidence of the predictions
    view = dataset.set_field(
        "predictions.total_conf",
        F("detections").map(F("confidence")).sum()
    )
    
    print(view.bounds("predictions.total_conf"))
    

Returns:
    

a `ViewExpression`

switch(_mapping_ , _default =None_)#
    

Applies a switch statement to this expression, which effectively computes the given pseudocode:
    
    
    for key, value in mapping.items():
        if self.apply(key):
            return value
    
    if default is not None:
        return default
    

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Round `uniqueness` values to either 0.25 or 0.75
    view = dataset.set_field(
        "uniqueness",
        F("uniqueness").switch(
            {
                (0.0 < F()) & (F() <= 0.5): 0.25,
                (0.5 < F()) & (F() <= 1.0): 0.75,
            },
        )
    )
    
    print(view.count_values("uniqueness"))
    

Parameters:
    

  * **mapping** â a dict mapping boolean `ViewExpression` keys to literal or `ViewExpression` values

  * **default** (_None_) â an optional literal or `ViewExpression` to return if none of the switch branches are taken



Returns:
    

a `ViewExpression`

tan()#
    

Computes the tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `tan()`
    view = dataset.match(F("uniqueness").tan() >= np.tan(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

tanh()#
    

Computes the hyperbolic tangent of this expression, which must resolve to a numeric value, in radians.

Examples:
    
    
    import numpy as np
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Get samples whose `uniqueness` value is >= 0.5 using `tanh()`
    view = dataset.match(F("uniqueness").tanh() >= np.tanh(0.5))
    
    print(view.bounds("uniqueness"))
    

Returns:
    

a `ViewExpression`

to_bool()#
    

Converts the expression to a boolean value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toBool) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_bool` field that is False when
    # `uniqueness < 0.5` and True when `uniqueness >= 0.5`
    dataset.add_sample_field("uniqueness_bool", fo.BooleanField)
    view = dataset.set_field(
        "uniqueness_bool", (2.0 * F("uniqueness")).floor().to_bool()
    )
    
    print(view.count_values("uniqueness_bool"))
    

Returns:
    

a `ViewExpression`

to_date()#
    

Converts the expression to a date value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toDate) for conversion rules.

Examples:
    
    
    from datetime import datetime
    import pytz
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    
    sample = fo.Sample(
        filepath="image.png",
        date_ms=1000 * now.timestamp(),
        date_str=now.isoformat(),
    )
    
    dataset = fo.Dataset()
    dataset.add_sample(sample)
    
    # Convert string/millisecond representations into datetimes
    dataset.add_sample_field("date1", fo.DateTimeField)
    dataset.add_sample_field("date2", fo.DateTimeField)
    (
        dataset
        .set_field("date1", F("date_ms").to_date())
        .set_field("date2", F("date_str").to_date())
        .save()
    )
    
    print(dataset.first())
    

Returns:
    

a `ViewExpression`

to_double()#
    

Converts the expression to a double precision value.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_float` field that is 0.0 when
    # `uniqueness < 0.5` and 1.0 when `uniqueness >= 0.5`
    dataset.add_sample_field("uniqueness_float", fo.FloatField)
    view = dataset.set_field(
        "uniqueness_float", (F("uniqueness") >= 0.5).to_double()
    )
    
    print(view.count_values("uniqueness_float"))
    

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toDouble) for conversion rules.

Returns:
    

a `ViewExpression`

to_int()#
    

Converts the expression to an integer value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toInt) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_int` field that contains the value of the
    # first decimal point of the `uniqueness` field
    dataset.add_sample_field("uniqueness_int", fo.IntField)
    view = dataset.set_field(
        "uniqueness_int", (10.0 * F("uniqueness")).floor().to_int()
    )
    
    print(view.count_values("uniqueness_int"))
    

Returns:
    

a `ViewExpression`

to_string()#
    

Converts the expression to a string value.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/toString) for conversion rules.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart").clone()
    
    # Adds a `uniqueness_str` field that is "true" when
    # `uniqueness >= 0.5` and "false" when `uniqueness < 0.5`
    dataset.add_sample_field("uniqueness_str", fo.StringField)
    view = dataset.set_field(
        "uniqueness_str", (F("uniqueness") >= 0.5).to_string()
    )
    
    print(view.count_values("uniqueness_str"))
    

Returns:
    

a `ViewExpression`

trunc(_place =0_)#
    

Truncates this expression, which must resolve to a numeric value, at the specified decimal place.

Positive values of `place` will truncate to `place` decimal places:
    
    
    place=2: 1234.5678 --> 1234.56
    

Negative values of `place` will replace `place` digits left of the decimal with zero:
    
    
    place=-1: 1234.5678 --> 1230
    

Examples:
    
    
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    # Only contains samples whose height is in [500, 600) pixels
    view = dataset.match(F("metadata.height").trunc(-2) == 500)
    
    print(view.bounds("metadata.height"))
    

Parameters:
    

**place** (_0_) â the decimal place at which to truncate

Returns:
    

a `ViewExpression`

type()#
    

Returns the type string of this expression.

See [this page](https://docs.mongodb.com/manual/reference/operator/aggregation/type) for more details.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Set `uniqueness` values below 0.75 to None
    view = dataset.set_field(
        "uniqueness",
        (F("uniqueness") > 0.75).if_else(F("uniqueness"), None)
    )
    
    # Create a view that only contains samples with non-None uniqueness
    unique_only_view = view.match(F("uniqueness").type() != "null")
    
    print(len(unique_only_view))
    

Returns:
    

a `ViewExpression`

union(_* args_)#
    

Computes the set union of this expression, which must resolve to an array, and the given array(s) or array expression(s).

The arrays are treated as sets, so all duplicates are removed.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b"],
                other_tags=["a", "c"]
            )
        ]
    )
    
    print(dataset.values(F("tags").union(F("other_tags"))))
    # [['a', 'b', 'c']]
    

Parameters:
    

***args** â one or more arrays or `ViewExpression` instances that resolve to array expressions

Returns:
    

a `ViewExpression`

unique()#
    

Returns an array containing the unique values in this expression, which must resolve to an array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "a", "b"],
            )
        ]
    )
    
    print(dataset.values(F("tags").unique()))
    # [['a', 'b']]
    

Returns:
    

a `ViewExpression`

upper()#
    

Converts this expression, which must resolve to a string, to uppercase.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Converts all tags to uppercase
    transform_tag = F().upper()
    view = dataset.set_field("tags", F("tags").map(transform_tag))
    
    print(dataset.distinct("tags"))
    print(view.distinct("tags"))
    

Returns:
    

a `ViewExpression`

week()#
    

Returns the week of the year of this date expression (in UTC) as a number between 0 and 53.

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 2, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 3, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 4, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the weeks of the year for the dataset
    print(dataset.values(F("created_at").week()))
    
    # Samples with even months of the week
    view = dataset.match(F("created_at").week() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

year()#
    

Returns the year of this date expression (in UTC).

Examples:
    
    
    from datetime import datetime
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    samples = [
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1970, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1971, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1972, 1, 1),
        ),
        fo.Sample(
            filepath="image1.jpg",
            created_at=datetime(1973, 1, 1),
        ),
    ]
    
    dataset = fo.Dataset()
    dataset.add_samples(samples)
    
    # Get the years for the dataset
    print(dataset.values(F("created_at").year()))
    
    # Samples from even years
    view = dataset.match(F("created_at").year() % 2 == 0)
    print(len(view))
    

Returns:
    

a `ViewExpression`

static zip(_* args_, _use_longest =False_, _defaults =None_)#
    

Zips the given expressions, which must resolve to arrays, into an array whose ith element is an array containing the ith element from each input array.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="image1.jpg",
                tags=["a", "b", "c"],
                ints=[1, 2, 3, 4, 5],
            ),
            fo.Sample(
                filepath="image2.jpg",
                tags=["y", "z"],
                ints=[25, 26, 27, 28],
            ),
        ]
    )
    
    dataset.add_sample_field("tags_ints", fo.ListField)
    
    # Populates an `tags_ints` field with the zipped `tags` and `ints`
    view = dataset.set_field("tags_ints", F.zip(F("tags"), F("ints")))
    
    print(view.first())
    
    # Same as above but use the longest array to determine output size
    view = dataset.set_field(
        "tags_ints",
        F.zip(F("tags"), F("ints"), use_longest=True, defaults=("", 0))
    )
    
    print(view.first())
    

Parameters:
    

  * ***args** â one or more arrays or `ViewExpression` instances resolving to arrays

  * **use_longest** (_False_) â whether to use the longest array to determine the number of elements in the output array. By default, the length of the shortest array is used

  * **defaults** (_None_) â an optional array of default values of same length as `*args` to use when `use_longest == True` and the input arrays are of different lengths. If no defaults are provided and `use_longest == True`, then missing values are set to `None`



Returns:
    

a `ViewExpression`

fiftyone.core.expressions.VALUE(_field_) = '$$value'#
    

A `ViewExpression` that refers to the current `$$value` in a MongoDB reduction expression.

See `ViewExpression.reduce()` for more information.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
