---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.aggregations.html
---

# @fiftyone/aggregations#

## Hooks#

### useAggregation#

@fiftyone/aggregations.useAggregation(_options_)#
    

Arguments:
    

  * **options** (`AggregationParams`)



Return type:
    

`Array<` `any` `>`

A hook for aggregating data from the **FiftyOne** backend.

**Aggregation Classes**

JavaScript | Python  
---|---  
`Values` | [`fiftyone.core.aggregations.Values`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Values "fiftyone.core.aggregations.Values")  
`Bounds` | [`fiftyone.core.aggregations.Bounds`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Bounds "fiftyone.core.aggregations.Bounds")  
`Count` | [`fiftyone.core.aggregations.Count`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Count "fiftyone.core.aggregations.Count")  
`CountValues` | [`fiftyone.core.aggregations.CountValues`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.CountValues "fiftyone.core.aggregations.CountValues")  
`Distinct` | [`fiftyone.core.aggregations.Distinct`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Distinct "fiftyone.core.aggregations.Distinct")  
`HistogramValues` | [`fiftyone.core.aggregations.HistogramValues`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.HistogramValues "fiftyone.core.aggregations.HistogramValues")  
`Mean` | [`fiftyone.core.aggregations.Mean`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Mean "fiftyone.core.aggregations.Mean")  
`Std` | [`fiftyone.core.aggregations.Std`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Std "fiftyone.core.aggregations.Std")  
`Sum` | [`fiftyone.core.aggregations.Sum`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Sum "fiftyone.core.aggregations.Sum")  
`Values` | [`fiftyone.core.aggregations.Values`](api__fiftyone.core.aggregations.md#fiftyone.core.aggregations.Values "fiftyone.core.aggregations.Values")  
  
**Example**
    
    
    const [aggregate, points, loading] = foa.useAggregation({
      dataset,
      filters,
      view,
    });
    
    React.useEffect(() => {
      aggregate(
        [
          new foa.aggregations.Values({
            fieldOrExpr: "id",
          }),
          new foa.aggregations.Values({
            fieldOrExpr: `${path}.point.coordinates`,
          }),
        ],
        dataset.name
      );
    }, [dataset, filters, view, path]);
    

## Types#

### Bounds#

class @fiftyone/aggregations.Bounds()#
    

@fiftyone/aggregations.new Bounds(_params_)#
    

Arguments:
    

  * **params** (`BoundsParams`)



Return type:
    

`plugins.fiftyone.aggregations.Bounds`

### Count#

class @fiftyone/aggregations.Count()#
    

@fiftyone/aggregations.new Count(_params_)#
    

Arguments:
    

  * **params** (`CountParams`)



Return type:
    

`plugins.fiftyone.aggregations.Count`

### CountValues#

class @fiftyone/aggregations.CountValues()#
    

@fiftyone/aggregations.new CountValues(_params_)#
    

Arguments:
    

  * **params** (`CountValuesParams`)



Return type:
    

`plugins.fiftyone.aggregations.CountValues`

### Distinct#

class @fiftyone/aggregations.Distinct()#
    

@fiftyone/aggregations.new Distinct(_params_)#
    

Arguments:
    

  * **params** (`DistinctParams`)



Return type:
    

`plugins.fiftyone.aggregations.Distinct`

### HistogramValues#

class @fiftyone/aggregations.HistogramValues()#
    

@fiftyone/aggregations.new HistogramValues(_params_)#
    

Arguments:
    

  * **params** (`HistogramValuesParams`)



Return type:
    

`plugins.fiftyone.aggregations.HistogramValues`

### Mean#

class @fiftyone/aggregations.Mean()#
    

@fiftyone/aggregations.new Mean(_params_)#
    

Arguments:
    

  * **params** (`MeanParams`)



Return type:
    

`plugins.fiftyone.aggregations.Mean`

### Std#

class @fiftyone/aggregations.Std()#
    

@fiftyone/aggregations.new Std(_params_)#
    

Arguments:
    

  * **params** (`StdParams`)



Return type:
    

`plugins.fiftyone.aggregations.Std`

### Sum#

class @fiftyone/aggregations.Sum()#
    

@fiftyone/aggregations.new Sum(_params_)#
    

Arguments:
    

  * **params** (`SumParams`)



Return type:
    

`plugins.fiftyone.aggregations.Sum`

### Values#

class @fiftyone/aggregations.Values()#
    

@fiftyone/aggregations.new Values(_params_)#
    

Arguments:
    

  * **params** (`ValuesParams`)



Return type:
    

`plugins.fiftyone.aggregations.Values`

class @fiftyone/aggregations.BoundsParams()#
    

### BoundsParams#

Name | Type | Description  
---|---|---  
BoundsParams.expr | `any` |   
BoundsParams.fieldOrExpr | `any` |   
BoundsParams.safe | `any` |   
  
class @fiftyone/aggregations.CountParams()#
    

### CountParams#

Name | Type | Description  
---|---|---  
CountParams.expr | `any` |   
CountParams.fieldOrExpr | `any` |   
CountParams.safe | `any` |   
  
class @fiftyone/aggregations.CountValuesParams()#
    

### CountValuesParams#

Name | Type | Description  
---|---|---  
CountValuesParams.expr | `any` |   
CountValuesParams.fieldOrExpr | `any` |   
CountValuesParams.safe | `any` |   
  
class @fiftyone/aggregations.DistinctParams()#
    

### DistinctParams#

Name | Type | Description  
---|---|---  
DistinctParams.expr | `any` |   
DistinctParams.fieldOrExpr | `any` |   
DistinctParams.safe | `any` |   
  
class @fiftyone/aggregations.HistogramValuesParams()#
    

### HistogramValuesParams#

Name | Type | Description  
---|---|---  
HistogramValuesParams.auto | `any` |   
HistogramValuesParams.bins | `any` |   
HistogramValuesParams.expr | `any` |   
HistogramValuesParams.fieldOrExpr | `any` |   
HistogramValuesParams.range | `any` |   
  
class @fiftyone/aggregations.MeanParams()#
    

### MeanParams#

Name | Type | Description  
---|---|---  
MeanParams.expr | `any` |   
MeanParams.fieldOrExpr | `any` |   
MeanParams.safe | `any` |   
  
class @fiftyone/aggregations.StdParams()#
    

### StdParams#

Name | Type | Description  
---|---|---  
StdParams.expr | `any` |   
StdParams.fieldOrExpr | `any` |   
StdParams.safe | `any` |   
StdParams.sample | `any` |   
  
class @fiftyone/aggregations.SumParams()#
    

### SumParams#

Name | Type | Description  
---|---|---  
SumParams.expr | `any` |   
SumParams.fieldOrExpr | `any` |   
SumParams.safe | `any` |   
  
class @fiftyone/aggregations.ValuesParams()#
    

### ValuesParams#

Name | Type | Description  
---|---|---  
ValuesParams.expr | `any` |   
ValuesParams.fieldOrExpr | `any` |   
ValuesParams.missingValue | `any` |   
ValuesParams.unwind | `any` |   
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
