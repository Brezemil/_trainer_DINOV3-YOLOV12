---
source_url: https://docs.voxel51.com/api/fiftyone.brain.internal.core.utils.html
---

# fiftyone.brain.internal.core.utils#

Utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`parse_data`(samples[,Â patches_field,Â data,Â ...]) |   
---|---  
`get_embeddings_from_index`(samples,Â ...[,Â ...]) |   
`get_ids`(samples[,Â patches_field,Â data,Â ...]) |   
`filter_ids`(samples,Â index_sample_ids,Â ...[,Â ...]) |   
`skip_ids`(samples,Â ids[,Â patches_field,Â ...]) |   
`add_ids`(sample_ids,Â label_ids,Â ...[,Â ...]) |   
`add_embeddings`(samples,Â embeddings,Â ...[,Â ...]) |   
`remove_ids`(sample_ids,Â label_ids,Â ...[,Â ...]) |   
`remove_embeddings`(samples,Â embeddings_field) |   
`filter_values`(values,Â keep_inds[,Â patches_field]) |   
`get_values`(samples,Â path_or_expr,Â ids[,Â ...]) |   
`parse_data_field`(samples,Â data_field[,Â ...]) |   
`get_embeddings`(samples[,Â model,Â ...]) |   
`get_unique_name`(name,Â ref_names_or_fcn[,Â ...]) |   
  
fiftyone.brain.internal.core.utils.parse_data(_samples_ , _patches_field =None_, _data =None_, _data_type ='embeddings'_, _allow_missing =True_, _warn_missing =True_)#
    

fiftyone.brain.internal.core.utils.get_embeddings_from_index(_samples_ , _similarity_index_ , _patches_field =None_, _allow_missing =True_, _warn_missing =True_)#
    

fiftyone.brain.internal.core.utils.get_ids(_samples_ , _patches_field =None_, _data =None_, _data_type ='embeddings'_, _handle_missing ='skip'_, _ref_sample_ids =None_)#
    

fiftyone.brain.internal.core.utils.filter_ids(_samples_ , _index_sample_ids_ , _index_label_ids_ , _patches_field =None_, _allow_missing =True_, _warn_missing =False_)#
    

fiftyone.brain.internal.core.utils.skip_ids(_samples_ , _ids_ , _patches_field =None_, _warn_existing =False_)#
    

fiftyone.brain.internal.core.utils.add_ids(_sample_ids_ , _label_ids_ , _index_sample_ids_ , _index_label_ids_ , _patches_field =None_, _overwrite =True_, _allow_existing =True_, _warn_existing =False_)#
    

fiftyone.brain.internal.core.utils.add_embeddings(_samples_ , _embeddings_ , _sample_ids_ , _label_ids_ , _embeddings_field_ , _patches_field =None_)#
    

fiftyone.brain.internal.core.utils.remove_ids(_sample_ids_ , _label_ids_ , _index_sample_ids_ , _index_label_ids_ , _patches_field =None_, _allow_missing =True_, _warn_missing =False_)#
    

fiftyone.brain.internal.core.utils.remove_embeddings(_samples_ , _embeddings_field_ , _sample_ids =None_, _label_ids =None_, _patches_field =None_)#
    

fiftyone.brain.internal.core.utils.filter_values(_values_ , _keep_inds_ , _patches_field =None_)#
    

fiftyone.brain.internal.core.utils.get_values(_samples_ , _path_or_expr_ , _ids_ , _patches_field =None_)#
    

fiftyone.brain.internal.core.utils.parse_data_field(_samples_ , _data_field_ , _patches_field =None_, _data_type ='embeddings'_)#
    

fiftyone.brain.internal.core.utils.get_embeddings(_samples_ , _model =None_, _model_kwargs =None_, _patches_field =None_, _embeddings_field =None_, _embeddings =None_, _similarity_index =None_, _force_square =False_, _alpha =None_, _handle_missing ='skip'_, _agg_fcn =None_, _batch_size =None_, _num_workers =None_, _skip_failures =True_, _progress =None_)#
    

fiftyone.brain.internal.core.utils.get_unique_name(_name_ , _ref_names_or_fcn_ , _max_len =None_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
