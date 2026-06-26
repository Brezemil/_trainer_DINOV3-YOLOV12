---
source_url: https://docs.voxel51.com/api/fiftyone.brain.internal.models.simple_resnet.html
---

# fiftyone.brain.internal.models.simple_resnet#

Implementation of a simple ResNet that is suitable only for smallish data.

The original implementation of this is from David Pageâs work on fast model training with resnets at [davidcpage/cifar10-fast](https://github.com/davidcpage/cifar10-fast).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`simple_resnet`([channels,Â weight,Â pool,Â ...]) |   
---|---  
`has_inputs`(node) |   
`build_graph`(net) |   
`pipeline`(net) |   
`conv_bn`(c_in,Â c_out) |   
`residual`(c) |   
`path_iter`(nested_dict[,Â pfx]) |   
  
**Classes:**

`Network`(net[,Â input_layer,Â output_layer]) |   
---|---  
`Crop`(h,Â w) |   
`FlipLR`() |   
`Cutout`(h,Â w) |   
`PiecewiseLinear`(knots,Â vals) |   
`Const`(val) |   
`Identity`() |   
`Add`() |   
`AddWeighted`(wx,Â wy) |   
`Mul`(weight) |   
`Flatten`(*args,Â **kwargs) |   
`Concat`(*args,Â **kwargs) |   
`BatchNorm`(num_features[,Â eps,Â momentum,Â ...]) |   
  
fiftyone.brain.internal.models.simple_resnet.simple_resnet(_channels =None_, _weight =0.125_, _pool =MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)_, _extra_layers =()_, _res_layers =('layer1', 'layer3')_)#
    

class fiftyone.brain.internal.models.simple_resnet.Network(_net_ , _input_layer =None_, _output_layer =None_)#
    

Bases: [`Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

**Methods:**

`nodes`() |   
---|---  
`forward`(inputs) | Define the computation performed at every call.  
`half`() | Casts all floating point parameters and buffers to `half` datatype.  
`add_module`(name,Â module) | Add a child module to the current module.  
`apply`(fn) | Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.  
`bfloat16`() | Casts all floating point parameters and buffers to `bfloat16` datatype.  
`buffers`([recurse]) | Return an iterator over module buffers.  
`children`() | Return an iterator over immediate children modules.  
`compile`(*args,Â **kwargs) | Compile this Module's forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").  
`cpu`() | Move all model parameters and buffers to the CPU.  
`cuda`([device]) | Move all model parameters and buffers to the GPU.  
`double`() | Casts all floating point parameters and buffers to `double` datatype.  
`eval`() | Set the module in evaluation mode.  
`extra_repr`() | Return the extra representation of the module.  
`float`() | Casts all floating point parameters and buffers to `float` datatype.  
`get_buffer`(target) | Return the buffer given by `target` if it exists, otherwise throw an error.  
`get_extra_state`() | Return any extra state to include in the module's state_dict.  
`get_parameter`(target) | Return the parameter given by `target` if it exists, otherwise throw an error.  
`get_submodule`(target) | Return the submodule given by `target` if it exists, otherwise throw an error.  
`ipu`([device]) | Move all model parameters and buffers to the IPU.  
`load_state_dict`(state_dict[,Â strict,Â assign]) | Copy parameters and buffers from `state_dict` into this module and its descendants.  
`modules`([remove_duplicate]) | Return an iterator over all modules in the network.  
`mtia`([device]) | Move all model parameters and buffers to the MTIA.  
`named_buffers`([prefix,Â recurse,Â ...]) | Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.  
`named_children`() | Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.  
`named_modules`([memo,Â prefix,Â remove_duplicate]) | Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.  
`named_parameters`([prefix,Â recurse,Â ...]) | Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.  
`parameters`([recurse]) | Return an iterator over module parameters.  
`register_backward_hook`(hook) | Register a backward hook on the module.  
`register_buffer`(name,Â tensor[,Â persistent]) | Add a buffer to the module.  
`register_forward_hook`(hook,Â *[,Â prepend,Â ...]) | Register a forward hook on the module.  
`register_forward_pre_hook`(hook,Â *[,Â ...]) | Register a forward pre-hook on the module.  
`register_full_backward_hook`(hook[,Â prepend]) | Register a backward hook on the module.  
`register_full_backward_pre_hook`(hook[,Â prepend]) | Register a backward pre-hook on the module.  
`register_load_state_dict_post_hook`(hook) | Register a post-hook to be run after module's `load_state_dict()` is called.  
`register_load_state_dict_pre_hook`(hook) | Register a pre-hook to be run before module's `load_state_dict()` is called.  
`register_module`(name,Â module) | Alias for `add_module()`.  
`register_parameter`(name,Â param) | Add a parameter to the module.  
`register_state_dict_post_hook`(hook) | Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`register_state_dict_pre_hook`(hook) | Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`requires_grad_`([requires_grad]) | Change if autograd should record operations on parameters in this module.  
`set_extra_state`(state) | Set extra state contained in the loaded `state_dict`.  
`set_submodule`(target,Â module[,Â strict]) | Set the submodule given by `target` if it exists, otherwise throw an error.  
`share_memory`() | See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").  
`state_dict`(*args[,Â destination,Â prefix,Â ...]) | Return a dictionary containing references to the whole state of the module.  
`to`(*args,Â **kwargs) | Move and/or cast the parameters and buffers.  
`to_empty`(*,Â device[,Â recurse]) | Move the parameters and buffers to the specified device without copying storage.  
`train`([mode]) | Set the module in training mode.  
`type`(dst_type) | Casts all parameters and buffers to `dst_type`.  
`xpu`([device]) | Move all model parameters and buffers to the XPU.  
`zero_grad`([set_to_none]) | Reset gradients of all model parameters.  
  
**Attributes:**

`T_destination` |   
---|---  
`call_super_init` |   
`dump_patches` |   
`training` |   
  
nodes()#
    

forward(_inputs_)#
    

Define the computation performed at every call.

Should be overridden by all subclasses.

Note

Although the recipe for forward pass needs to be defined within this function, one should call the `Module` instance afterwards instead of this since the former takes care of running the registered hooks while the latter silently ignores them.

half()#
    

Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

T_destination = ~T_destination#
    

add_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Parameters:
    

  * **name** (_str_) â name of the child module. The child module can be accessed from this module using the given name

  * **module** (_Module_) â child module to be added to the module.




apply(_fn : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")], None]_) → Self#
    

Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.

Typical use includes initializing the parameters of a model (see also [torch.nn.init](https://docs.pytorch.org/docs/stable/nn.init.html#nn-init-doc "\(in PyTorch v2.12\)")).

Parameters:
    

**fn** (`Module` -> None) â function to be applied to each submodule

Returns:
    

self

Return type:
    

Module

Example:
    
    
    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    

bfloat16() → Self#
    

Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

buffers(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]#
    

Return an iterator over module buffers.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module.

Yields:
    

_torch.Tensor_ â module buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

call_super_init: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

children() → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over immediate children modules.

Yields:
    

_Module_ â a child module

compile(_* args_, _** kwargs_) → None#
    

Compile this Moduleâs forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

This Moduleâs `__call__` method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)") for details on the arguments for this function.

cpu() → Self#
    

Move all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

cuda(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

double() → Self#
    

Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

dump_patches: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

eval() → Self#
    

Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e. whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "\(in PyTorch v2.12\)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.eval()` and several similar mechanisms that may be confused with it.

Returns:
    

self

Return type:
    

Module

extra_repr() → str#
    

Return the extra representation of the module.

To print customized extra information, you should re-implement this method in your own modules. Both single-line and multi-line strings are acceptable.

float() → Self#
    

Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

get_buffer(_target : str_) → [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")#
    

Return the buffer given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the buffer to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The buffer referenced by `target`

Return type:
    

[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not a buffer

get_extra_state() → Any#
    

Return any extra state to include in the moduleâs state_dict.

Implement this and a corresponding `set_extra_state()` for your module if you need to store extra state. This function is called when building the moduleâs `state_dict()`.

Note that extra state should be picklable to ensure working serialization of the state_dict. We only provide backwards compatibility guarantees for serializing Tensors; other objects may break backwards compatibility if their serialized pickled form changes.

Returns:
    

Any extra state to store in the moduleâs state_dict

Return type:
    

object

get_parameter(_target : str_) → [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")#
    

Return the parameter given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the Parameter to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The Parameter referenced by `target`

Return type:
    

torch.nn.Parameter

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not an `nn.Parameter`

get_submodule(_target : str_) → [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")#
    

Return the submodule given by `target` if it exists, otherwise throw an error.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` which has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To check whether or not we have the `linear` submodule, we would call `get_submodule("net_b.linear")`. To check whether we have the `conv` submodule, we would call `get_submodule("net_b.net_c.conv")`.

The runtime of `get_submodule` is bounded by the degree of module nesting in `target`. A query against `named_modules` achieves the same result, but it is O(N) in the number of transitive modules. So, for a simple check to see if some submodule exists, `get_submodule` should always be used.

Parameters:
    

**target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

Returns:
    

The submodule referenced by `target`

Return type:
    

[torch.nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If at any point along the path resulting from the target string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.

ipu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on IPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

load_state_dict(_state_dict : Mapping[str, Any]_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _assign : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

Copy parameters and buffers from `state_dict` into this module and its descendants.

If `strict` is `True`, then the keys of `state_dict` must exactly match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function.

Warning

If `assign` is `True` the optimizer must be created after the call to `load_state_dict` unless [`get_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/stable/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "\(in PyTorch v2.12\)") is `True`.

Parameters:
    

  * **state_dict** (_dict_) â a dict containing parameters and persistent buffers.

  * **strict** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to strictly enforce that the keys in `state_dict` match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function. Default: `True`

  * **assign** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â When set to `False`, the properties of the tensors in the current module are preserved whereas setting it to `True` preserves properties of the Tensors in the state dict. The only exception is the `requires_grad` field of `Parameter` for which the value from the module is preserved. Default: `False`



Returns:
    

  * `missing_keys` is a list of str containing any keys that are expected
    

by this module but missing from the provided `state_dict`.

  * `unexpected_keys` is a list of str containing the keys that are not
    

expected by this module but present in the provided `state_dict`.




Return type:
    

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

Note

If a parameter or buffer is registered as `None` and its corresponding key exists in `state_dict`, `load_state_dict()` will raise a `RuntimeError`.

modules(_remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over all modules in the network.

Parameters:
    

**remove_duplicate** â whether to remove the duplicated module instances in the result or not.

Yields:
    

_Module_ â a module in the network

Note

Duplicate modules are returned only once by default. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)
    
    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)
    

mtia(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on MTIA while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

named_buffers(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all buffer names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module. Defaults to True.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated buffers in the result. Defaults to True.



Yields:
    

_(str, torch.Tensor)_ â Tuple containing the name and buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())
    

named_children() → Iterator[tuple[str, [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]]#
    

Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    

_(str, Module)_ â Tuple containing a name and child module

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)
    

named_modules(_memo : set[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")] | None = None_, _prefix : str = ''_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_)#
    

Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Parameters:
    

  * **memo** â a memo to store the set of modules already added to the result

  * **prefix** â a prefix that will be added to the name of the module

  * **remove_duplicate** â whether to remove the duplicated module instances in the result or not



Yields:
    

_(str, Module)_ â Tuple of name and module

Note

Duplicate modules are returned only once. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)
    
    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))
    

named_parameters(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all parameter names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated parameters in the result. Defaults to True.



Yields:
    

_(str, Parameter)_ â Tuple containing the name and parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())
    

parameters(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]#
    

Return an iterator over module parameters.

This is typically passed to an optimizer.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

Yields:
    

_Parameter_ â module parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

register_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_) → RemovableHandle#
    

Register a backward hook on the module.

This function is deprecated in favor of [`register_full_backward_hook()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "\(in PyTorch v2.12\)") and the behavior of this function will change in future versions.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_buffer(_name : str_, _tensor : [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None_, _persistent : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Add a buffer to the module.

This is typically used to register a buffer that should not be considered a model parameter. For example, BatchNormâs `running_mean` is not a parameter, but is part of the moduleâs state. Buffers, by default, are persistent and will be saved alongside parameters. This behavior can be changed by setting `persistent` to `False`. The only difference between a persistent buffer and a non-persistent buffer is that the latter will not be a part of this moduleâs `state_dict`.

Buffers can be accessed as attributes using given names.

Parameters:
    

  * **name** (_str_) â name of the buffer. The buffer can be accessed from this module using the given name

  * **tensor** (_Tensor_ _or_ _None_) â buffer to be registered. If `None`, then operations that run on buffers, such as `cuda`, are ignored. If `None`, the buffer is **not** included in the moduleâs `state_dict`.

  * **persistent** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the buffer is part of this moduleâs `state_dict`.




Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))
    

register_forward_hook(_hook : Callable[[T, tuple[Any, ...], Any], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any], Any], Any | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _always_call : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward hook on the module.

The hook will be called every time after `forward()` has computed an output.

If `with_kwargs` is `False` or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the output. It can modify the input inplace but it will not have effect on forward since this is called after `forward()` is called. The hook should have the following signature:
    
    
    hook(module, args, output) -> None or modified output
    

If `with_kwargs` is `True`, the forward hook will be passed the `kwargs` given to the forward function and be expected to return the output possibly modified. The hook should have the following signature:
    
    
    hook(module, args, kwargs, output) -> None or modified output
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the provided `hook` will be fired before all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward` hooks registered with `register_module_forward_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the `hook` will be passed the kwargs given to the forward function. Default: `False`

  * **always_call** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True` the `hook` will be run regardless of whether an exception is raised while calling the Module. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_forward_pre_hook(_hook : Callable[[T, tuple[Any, ...]], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any]], tuple[Any, dict[str, Any]] | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward pre-hook on the module.

The hook will be called every time before `forward()` is invoked.

If `with_kwargs` is false or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the input. User can either return a tuple or a single modified value in the hook. We will wrap the value into a tuple if a single value is returned (unless that value is already a tuple). The hook should have the following signature:
    
    
    hook(module, args) -> None or modified input
    

If `with_kwargs` is true, the forward pre-hook will be passed the kwargs given to the forward function. And if the hook modifies the input, both the args and kwargs should be returned. The hook should have the following signature:
    
    
    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward_pre` hooks registered with `register_module_forward_pre_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the `hook` will be passed the kwargs given to the forward function. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

>   1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
> 
>   2. If none of the module inputs require gradients, the hook will fire when the gradients are computed with respect to module outputs.
> 
>   3. If none of the module outputs require gradients, then the hooks will not fire.
> 
> 


The hook should have the following signature:
    
    
    hook(module, grad_input, grad_output) -> tuple(Tensor) or None
    

The `grad_input` and `grad_output` are tuples that contain the gradients with respect to the inputs and outputs respectively. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the input that will be used in place of `grad_input` in subsequent computations. `grad_input` will only correspond to the inputs given as positional arguments and all kwarg arguments are ignored. Entries in `grad_input` and `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs or outputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward` hooks registered with `register_module_full_backward_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_pre_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed. The hook should have the following signature:
    
    
    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None
    

The `grad_output` is a tuple. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the output that will be used in place of `grad_output` in subsequent computations. Entries in `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward_pre` hooks registered with `register_module_full_backward_pre_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_post_hook(_hook_)#
    

Register a post-hook to be run after moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, incompatible_keys) -> None

The `module` argument is the current module that this hook is registered on, and the `incompatible_keys` argument is a `NamedTuple` consisting of attributes `missing_keys` and `unexpected_keys`. `missing_keys` is a `list` of `str` containing the missing keys and `unexpected_keys` is a `list` of `str` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling `load_state_dict()` with `strict=True` are affected by modifications the hook makes to `missing_keys` or `unexpected_keys`, as expected. Additions to either set of keys will result in an error being thrown when `strict=True`, and clearing out both missing and unexpected keys will avoid an error.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_pre_hook(_hook_)#
    

Register a pre-hook to be run before moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None # noqa: B950

Parameters:
    

**hook** (_Callable_) â Callable hook that will be invoked before loading the state dict.

register_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Alias for `add_module()`.

register_parameter(_name : str_, _param : [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)") | None_) → None#
    

Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Parameters:
    

  * **name** (_str_) â name of the parameter. The parameter can be accessed from this module using the given name

  * **param** (_Parameter_ _or_ _None_) â parameter to be added to the module. If `None`, then operations that run on parameters, such as `cuda`, are ignored. If `None`, the parameter is **not** included in the moduleâs `state_dict`.




register_state_dict_post_hook(_hook_)#
    

Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the `state_dict` inplace.

register_state_dict_pre_hook(_hook_)#
    

Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the `state_dict` call is made.

requires_grad_(_requires_grad : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Change if autograd should record operations on parameters in this module.

This method sets the parametersâ `requires_grad` attributes in-place.

This method is helpful for freezing part of the module for finetuning or training parts of a model individually (e.g., GAN training).

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.requires_grad_()` and several similar mechanisms that may be confused with it.

Parameters:
    

**requires_grad** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether autograd should record operations on parameters in this module. Default: `True`.

Returns:
    

self

Return type:
    

Module

set_extra_state(_state : Any_) → None#
    

Set extra state contained in the loaded `state_dict`.

This function is called from `load_state_dict()` to handle any extra state found within the `state_dict`. Implement this function and a corresponding `get_extra_state()` for your module if you need to store extra state within its `state_dict`.

Parameters:
    

**state** (_dict_) â Extra state from the `state_dict`

set_submodule(_target : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Set the submodule given by `target` if it exists, otherwise throw an error.

Note

If `strict` is set to `False` (default), the method will replace an existing submodule or create a new submodule if the parent module exists. If `strict` is set to `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule does not exist.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To override the `Conv2d` with a new submodule `Linear`, you could call `set_submodule("net_b.net_c.conv", nn.Linear(1, 1))` where `strict` could be `True` or `False`

To add a new submodule `Conv2d` to the existing `net_b` module, you would call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))`.

In the above if you set `strict=True` and call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)`, an AttributeError will be raised because `net_b` does not have a submodule named `conv`.

Parameters:
    

  * **target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

  * **module** â The module to set the submodule to.

  * **strict** â If `False`, the method will replace an existing submodule or create a new submodule if the parent module exists. If `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule doesnât already exist.



Raises:
    

  * **ValueError** â If the `target` string is empty or if `module` is not an instance of `nn.Module`.

  * **AttributeError** â If at any point along the path resulting from the `target` string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.




share_memory() → Self#
    

See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").

state_dict(_* args_, _destination =None_, _prefix =''_, _keep_vars =False_)#
    

Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are included. Keys are corresponding parameter and buffer names. Parameters and buffers set to `None` are not included.

Note

The returned object is a shallow copy. It contains references to the moduleâs parameters and buffers.

Warning

Currently `state_dict()` also accepts positional arguments for `destination`, `prefix` and `keep_vars` in order. However, this is being deprecated and keyword arguments will be enforced in future releases.

Warning

Please avoid the use of argument `destination` as it is not designed for end-users.

Parameters:
    

  * **destination** (_dict_ _,__optional_) â If provided, the state of module will be updated into the dict and the same object is returned. Otherwise, an `OrderedDict` will be created and returned. Default: `None`.

  * **prefix** (_str_ _,__optional_) â a prefix added to parameter and buffer names to compose the keys in state_dict. Default: `''`.

  * **keep_vars** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â by default the [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") s returned in the state dict are detached from autograd. If itâs set to `True`, detaching will not be performed. Default: `False`.



Returns:
    

a dictionary containing a whole state of the module

Return type:
    

dict

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']
    

to(_* args_, _** kwargs_)#
    

Move and/or cast the parameters and buffers.

This can be called as

to(_device =None_, _dtype =None_, _non_blocking =False_)
    

to(_dtype_ , _non_blocking =False_)
    

to(_tensor_ , _non_blocking =False_)
    

to(_memory_format =torch.channels_last_)
    

Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "\(in PyTorch v2.12\)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â the desired device of the parameters and buffers in this module

  * **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)")) â the desired floating point or complex dtype of the parameters and buffers in this module

  * **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")) â Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

  * **memory_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "\(in PyTorch v2.12\)")) â the desired memory format for 4D parameters and buffers in this module (keyword only argument)



Returns:
    

self

Return type:
    

Module

Examples:
    
    
    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)
    
    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)
    

to_empty(_*_ , _device : str | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | int | None_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Move the parameters and buffers to the specified device without copying storage.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â The desired device of the parameters and buffers in this module.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â Whether parameters and buffers of submodules should be recursively moved to the specified device.



Returns:
    

self

Return type:
    

Module

train(_mode : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Set the module in training mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e., whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
    

**mode** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
    

self

Return type:
    

Module

type(_dst_type : [dtype](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)") | str_) → Self#
    

Casts all parameters and buffers to `dst_type`.

Note

This method modifies the module in-place.

Parameters:
    

**dst_type** ([_type_](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type") _or_ _string_) â the desired type

Returns:
    

self

Return type:
    

Module

xpu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on XPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

zero_grad(_set_to_none : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Reset gradients of all model parameters.

See similar function under [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "\(in PyTorch v2.12\)") for more context.

Parameters:
    

**set_to_none** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â instead of setting to zero, set the grads to None. See [`torch.optim.Optimizer.zero_grad()`](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "\(in PyTorch v2.12\)") for details.

training: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

fiftyone.brain.internal.models.simple_resnet.has_inputs(_node_)#
    

fiftyone.brain.internal.models.simple_resnet.build_graph(_net_)#
    

fiftyone.brain.internal.models.simple_resnet.pipeline(_net_)#
    

class fiftyone.brain.internal.models.simple_resnet.Crop(_h_ , _w_)#
    

Bases: `Crop`

**Methods:**

`options`(shape) |   
---|---  
`output_shape`(shape) |   
`count`(value,Â /) | Return number of occurrences of value.  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
**Attributes:**

`h` | Alias for field number 0  
---|---  
`w` | Alias for field number 1  
  
options(_shape_)#
    

output_shape(_shape_)#
    

count(_value_ , _/_)#
    

Return number of occurrences of value.

h#
    

Alias for field number 0

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

w#
    

Alias for field number 1

class fiftyone.brain.internal.models.simple_resnet.FlipLR#
    

Bases: `FlipLR`

**Methods:**

`options`(shape) |   
---|---  
`count`(value,Â /) | Return number of occurrences of value.  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
options(_shape_)#
    

count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

class fiftyone.brain.internal.models.simple_resnet.Cutout(_h_ , _w_)#
    

Bases: `Cutout`

**Methods:**

`options`(shape) |   
---|---  
`count`(value,Â /) | Return number of occurrences of value.  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
**Attributes:**

`h` | Alias for field number 0  
---|---  
`w` | Alias for field number 1  
  
options(_shape_)#
    

count(_value_ , _/_)#
    

Return number of occurrences of value.

h#
    

Alias for field number 0

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

w#
    

Alias for field number 1

class fiftyone.brain.internal.models.simple_resnet.PiecewiseLinear(_knots_ , _vals_)#
    

Bases: `PiecewiseLinear`

**Methods:**

`count`(value,Â /) | Return number of occurrences of value.  
---|---  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
**Attributes:**

`knots` | Alias for field number 0  
---|---  
`vals` | Alias for field number 1  
  
count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

knots#
    

Alias for field number 0

vals#
    

Alias for field number 1

class fiftyone.brain.internal.models.simple_resnet.Const(_val_)#
    

Bases: `Const`

**Methods:**

`count`(value,Â /) | Return number of occurrences of value.  
---|---  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
**Attributes:**

`val` | Alias for field number 0  
---|---  
  
count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

val#
    

Alias for field number 0

class fiftyone.brain.internal.models.simple_resnet.Identity#
    

Bases: `Identity`

**Methods:**

`count`(value,Â /) | Return number of occurrences of value.  
---|---  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

class fiftyone.brain.internal.models.simple_resnet.Add#
    

Bases: `Add`

**Methods:**

`count`(value,Â /) | Return number of occurrences of value.  
---|---  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

class fiftyone.brain.internal.models.simple_resnet.AddWeighted(_wx_ , _wy_)#
    

Bases: `AddWeighted`

**Methods:**

`count`(value,Â /) | Return number of occurrences of value.  
---|---  
`index`(value[,Â start,Â stop]) | Return first index of value.  
  
**Attributes:**

`wx` | Alias for field number 0  
---|---  
`wy` | Alias for field number 1  
  
count(_value_ , _/_)#
    

Return number of occurrences of value.

index(_value_ , _start =0_, _stop =9223372036854775807_, _/_)#
    

Return first index of value.

Raises ValueError if the value is not present.

wx#
    

Alias for field number 0

wy#
    

Alias for field number 1

class fiftyone.brain.internal.models.simple_resnet.Mul(_weight_)#
    

Bases: [`Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

**Attributes:**

`T_destination` |   
---|---  
`call_super_init` |   
`dump_patches` |   
`training` |   
  
**Methods:**

`add_module`(name,Â module) | Add a child module to the current module.  
---|---  
`apply`(fn) | Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.  
`bfloat16`() | Casts all floating point parameters and buffers to `bfloat16` datatype.  
`buffers`([recurse]) | Return an iterator over module buffers.  
`children`() | Return an iterator over immediate children modules.  
`compile`(*args,Â **kwargs) | Compile this Module's forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").  
`cpu`() | Move all model parameters and buffers to the CPU.  
`cuda`([device]) | Move all model parameters and buffers to the GPU.  
`double`() | Casts all floating point parameters and buffers to `double` datatype.  
`eval`() | Set the module in evaluation mode.  
`extra_repr`() | Return the extra representation of the module.  
`float`() | Casts all floating point parameters and buffers to `float` datatype.  
`forward`(*input) | Define the computation performed at every call.  
`get_buffer`(target) | Return the buffer given by `target` if it exists, otherwise throw an error.  
`get_extra_state`() | Return any extra state to include in the module's state_dict.  
`get_parameter`(target) | Return the parameter given by `target` if it exists, otherwise throw an error.  
`get_submodule`(target) | Return the submodule given by `target` if it exists, otherwise throw an error.  
`half`() | Casts all floating point parameters and buffers to `half` datatype.  
`ipu`([device]) | Move all model parameters and buffers to the IPU.  
`load_state_dict`(state_dict[,Â strict,Â assign]) | Copy parameters and buffers from `state_dict` into this module and its descendants.  
`modules`([remove_duplicate]) | Return an iterator over all modules in the network.  
`mtia`([device]) | Move all model parameters and buffers to the MTIA.  
`named_buffers`([prefix,Â recurse,Â ...]) | Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.  
`named_children`() | Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.  
`named_modules`([memo,Â prefix,Â remove_duplicate]) | Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.  
`named_parameters`([prefix,Â recurse,Â ...]) | Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.  
`parameters`([recurse]) | Return an iterator over module parameters.  
`register_backward_hook`(hook) | Register a backward hook on the module.  
`register_buffer`(name,Â tensor[,Â persistent]) | Add a buffer to the module.  
`register_forward_hook`(hook,Â *[,Â prepend,Â ...]) | Register a forward hook on the module.  
`register_forward_pre_hook`(hook,Â *[,Â ...]) | Register a forward pre-hook on the module.  
`register_full_backward_hook`(hook[,Â prepend]) | Register a backward hook on the module.  
`register_full_backward_pre_hook`(hook[,Â prepend]) | Register a backward pre-hook on the module.  
`register_load_state_dict_post_hook`(hook) | Register a post-hook to be run after module's `load_state_dict()` is called.  
`register_load_state_dict_pre_hook`(hook) | Register a pre-hook to be run before module's `load_state_dict()` is called.  
`register_module`(name,Â module) | Alias for `add_module()`.  
`register_parameter`(name,Â param) | Add a parameter to the module.  
`register_state_dict_post_hook`(hook) | Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`register_state_dict_pre_hook`(hook) | Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`requires_grad_`([requires_grad]) | Change if autograd should record operations on parameters in this module.  
`set_extra_state`(state) | Set extra state contained in the loaded `state_dict`.  
`set_submodule`(target,Â module[,Â strict]) | Set the submodule given by `target` if it exists, otherwise throw an error.  
`share_memory`() | See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").  
`state_dict`(*args[,Â destination,Â prefix,Â ...]) | Return a dictionary containing references to the whole state of the module.  
`to`(*args,Â **kwargs) | Move and/or cast the parameters and buffers.  
`to_empty`(*,Â device[,Â recurse]) | Move the parameters and buffers to the specified device without copying storage.  
`train`([mode]) | Set the module in training mode.  
`type`(dst_type) | Casts all parameters and buffers to `dst_type`.  
`xpu`([device]) | Move all model parameters and buffers to the XPU.  
`zero_grad`([set_to_none]) | Reset gradients of all model parameters.  
  
T_destination = ~T_destination#
    

add_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Parameters:
    

  * **name** (_str_) â name of the child module. The child module can be accessed from this module using the given name

  * **module** (_Module_) â child module to be added to the module.




apply(_fn : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")], None]_) → Self#
    

Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.

Typical use includes initializing the parameters of a model (see also [torch.nn.init](https://docs.pytorch.org/docs/stable/nn.init.html#nn-init-doc "\(in PyTorch v2.12\)")).

Parameters:
    

**fn** (`Module` -> None) â function to be applied to each submodule

Returns:
    

self

Return type:
    

Module

Example:
    
    
    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    

bfloat16() → Self#
    

Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

buffers(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]#
    

Return an iterator over module buffers.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module.

Yields:
    

_torch.Tensor_ â module buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

call_super_init: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

children() → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over immediate children modules.

Yields:
    

_Module_ â a child module

compile(_* args_, _** kwargs_) → None#
    

Compile this Moduleâs forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

This Moduleâs `__call__` method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)") for details on the arguments for this function.

cpu() → Self#
    

Move all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

cuda(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

double() → Self#
    

Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

dump_patches: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

eval() → Self#
    

Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e. whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "\(in PyTorch v2.12\)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.eval()` and several similar mechanisms that may be confused with it.

Returns:
    

self

Return type:
    

Module

extra_repr() → str#
    

Return the extra representation of the module.

To print customized extra information, you should re-implement this method in your own modules. Both single-line and multi-line strings are acceptable.

float() → Self#
    

Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

forward(_* input: Any_) → None#
    

Define the computation performed at every call.

Should be overridden by all subclasses.

Note

Although the recipe for forward pass needs to be defined within this function, one should call the `Module` instance afterwards instead of this since the former takes care of running the registered hooks while the latter silently ignores them.

get_buffer(_target : str_) → [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")#
    

Return the buffer given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the buffer to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The buffer referenced by `target`

Return type:
    

[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not a buffer

get_extra_state() → Any#
    

Return any extra state to include in the moduleâs state_dict.

Implement this and a corresponding `set_extra_state()` for your module if you need to store extra state. This function is called when building the moduleâs `state_dict()`.

Note that extra state should be picklable to ensure working serialization of the state_dict. We only provide backwards compatibility guarantees for serializing Tensors; other objects may break backwards compatibility if their serialized pickled form changes.

Returns:
    

Any extra state to store in the moduleâs state_dict

Return type:
    

object

get_parameter(_target : str_) → [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")#
    

Return the parameter given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the Parameter to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The Parameter referenced by `target`

Return type:
    

torch.nn.Parameter

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not an `nn.Parameter`

get_submodule(_target : str_) → [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")#
    

Return the submodule given by `target` if it exists, otherwise throw an error.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` which has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To check whether or not we have the `linear` submodule, we would call `get_submodule("net_b.linear")`. To check whether we have the `conv` submodule, we would call `get_submodule("net_b.net_c.conv")`.

The runtime of `get_submodule` is bounded by the degree of module nesting in `target`. A query against `named_modules` achieves the same result, but it is O(N) in the number of transitive modules. So, for a simple check to see if some submodule exists, `get_submodule` should always be used.

Parameters:
    

**target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

Returns:
    

The submodule referenced by `target`

Return type:
    

[torch.nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If at any point along the path resulting from the target string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.

half() → Self#
    

Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

ipu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on IPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

load_state_dict(_state_dict : Mapping[str, Any]_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _assign : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

Copy parameters and buffers from `state_dict` into this module and its descendants.

If `strict` is `True`, then the keys of `state_dict` must exactly match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function.

Warning

If `assign` is `True` the optimizer must be created after the call to `load_state_dict` unless [`get_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/stable/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "\(in PyTorch v2.12\)") is `True`.

Parameters:
    

  * **state_dict** (_dict_) â a dict containing parameters and persistent buffers.

  * **strict** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to strictly enforce that the keys in `state_dict` match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function. Default: `True`

  * **assign** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â When set to `False`, the properties of the tensors in the current module are preserved whereas setting it to `True` preserves properties of the Tensors in the state dict. The only exception is the `requires_grad` field of `Parameter` for which the value from the module is preserved. Default: `False`



Returns:
    

  * `missing_keys` is a list of str containing any keys that are expected
    

by this module but missing from the provided `state_dict`.

  * `unexpected_keys` is a list of str containing the keys that are not
    

expected by this module but present in the provided `state_dict`.




Return type:
    

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

Note

If a parameter or buffer is registered as `None` and its corresponding key exists in `state_dict`, `load_state_dict()` will raise a `RuntimeError`.

modules(_remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over all modules in the network.

Parameters:
    

**remove_duplicate** â whether to remove the duplicated module instances in the result or not.

Yields:
    

_Module_ â a module in the network

Note

Duplicate modules are returned only once by default. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)
    
    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)
    

mtia(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on MTIA while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

named_buffers(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all buffer names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module. Defaults to True.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated buffers in the result. Defaults to True.



Yields:
    

_(str, torch.Tensor)_ â Tuple containing the name and buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())
    

named_children() → Iterator[tuple[str, [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]]#
    

Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    

_(str, Module)_ â Tuple containing a name and child module

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)
    

named_modules(_memo : set[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")] | None = None_, _prefix : str = ''_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_)#
    

Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Parameters:
    

  * **memo** â a memo to store the set of modules already added to the result

  * **prefix** â a prefix that will be added to the name of the module

  * **remove_duplicate** â whether to remove the duplicated module instances in the result or not



Yields:
    

_(str, Module)_ â Tuple of name and module

Note

Duplicate modules are returned only once. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)
    
    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))
    

named_parameters(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all parameter names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated parameters in the result. Defaults to True.



Yields:
    

_(str, Parameter)_ â Tuple containing the name and parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())
    

parameters(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]#
    

Return an iterator over module parameters.

This is typically passed to an optimizer.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

Yields:
    

_Parameter_ â module parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

register_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_) → RemovableHandle#
    

Register a backward hook on the module.

This function is deprecated in favor of [`register_full_backward_hook()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "\(in PyTorch v2.12\)") and the behavior of this function will change in future versions.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_buffer(_name : str_, _tensor : [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None_, _persistent : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Add a buffer to the module.

This is typically used to register a buffer that should not be considered a model parameter. For example, BatchNormâs `running_mean` is not a parameter, but is part of the moduleâs state. Buffers, by default, are persistent and will be saved alongside parameters. This behavior can be changed by setting `persistent` to `False`. The only difference between a persistent buffer and a non-persistent buffer is that the latter will not be a part of this moduleâs `state_dict`.

Buffers can be accessed as attributes using given names.

Parameters:
    

  * **name** (_str_) â name of the buffer. The buffer can be accessed from this module using the given name

  * **tensor** (_Tensor_ _or_ _None_) â buffer to be registered. If `None`, then operations that run on buffers, such as `cuda`, are ignored. If `None`, the buffer is **not** included in the moduleâs `state_dict`.

  * **persistent** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the buffer is part of this moduleâs `state_dict`.




Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))
    

register_forward_hook(_hook : Callable[[T, tuple[Any, ...], Any], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any], Any], Any | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _always_call : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward hook on the module.

The hook will be called every time after `forward()` has computed an output.

If `with_kwargs` is `False` or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the output. It can modify the input inplace but it will not have effect on forward since this is called after `forward()` is called. The hook should have the following signature:
    
    
    hook(module, args, output) -> None or modified output
    

If `with_kwargs` is `True`, the forward hook will be passed the `kwargs` given to the forward function and be expected to return the output possibly modified. The hook should have the following signature:
    
    
    hook(module, args, kwargs, output) -> None or modified output
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the provided `hook` will be fired before all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward` hooks registered with `register_module_forward_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the `hook` will be passed the kwargs given to the forward function. Default: `False`

  * **always_call** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True` the `hook` will be run regardless of whether an exception is raised while calling the Module. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_forward_pre_hook(_hook : Callable[[T, tuple[Any, ...]], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any]], tuple[Any, dict[str, Any]] | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward pre-hook on the module.

The hook will be called every time before `forward()` is invoked.

If `with_kwargs` is false or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the input. User can either return a tuple or a single modified value in the hook. We will wrap the value into a tuple if a single value is returned (unless that value is already a tuple). The hook should have the following signature:
    
    
    hook(module, args) -> None or modified input
    

If `with_kwargs` is true, the forward pre-hook will be passed the kwargs given to the forward function. And if the hook modifies the input, both the args and kwargs should be returned. The hook should have the following signature:
    
    
    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward_pre` hooks registered with `register_module_forward_pre_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the `hook` will be passed the kwargs given to the forward function. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

>   1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
> 
>   2. If none of the module inputs require gradients, the hook will fire when the gradients are computed with respect to module outputs.
> 
>   3. If none of the module outputs require gradients, then the hooks will not fire.
> 
> 


The hook should have the following signature:
    
    
    hook(module, grad_input, grad_output) -> tuple(Tensor) or None
    

The `grad_input` and `grad_output` are tuples that contain the gradients with respect to the inputs and outputs respectively. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the input that will be used in place of `grad_input` in subsequent computations. `grad_input` will only correspond to the inputs given as positional arguments and all kwarg arguments are ignored. Entries in `grad_input` and `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs or outputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward` hooks registered with `register_module_full_backward_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_pre_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed. The hook should have the following signature:
    
    
    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None
    

The `grad_output` is a tuple. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the output that will be used in place of `grad_output` in subsequent computations. Entries in `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward_pre` hooks registered with `register_module_full_backward_pre_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_post_hook(_hook_)#
    

Register a post-hook to be run after moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, incompatible_keys) -> None

The `module` argument is the current module that this hook is registered on, and the `incompatible_keys` argument is a `NamedTuple` consisting of attributes `missing_keys` and `unexpected_keys`. `missing_keys` is a `list` of `str` containing the missing keys and `unexpected_keys` is a `list` of `str` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling `load_state_dict()` with `strict=True` are affected by modifications the hook makes to `missing_keys` or `unexpected_keys`, as expected. Additions to either set of keys will result in an error being thrown when `strict=True`, and clearing out both missing and unexpected keys will avoid an error.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_pre_hook(_hook_)#
    

Register a pre-hook to be run before moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None # noqa: B950

Parameters:
    

**hook** (_Callable_) â Callable hook that will be invoked before loading the state dict.

register_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Alias for `add_module()`.

register_parameter(_name : str_, _param : [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)") | None_) → None#
    

Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Parameters:
    

  * **name** (_str_) â name of the parameter. The parameter can be accessed from this module using the given name

  * **param** (_Parameter_ _or_ _None_) â parameter to be added to the module. If `None`, then operations that run on parameters, such as `cuda`, are ignored. If `None`, the parameter is **not** included in the moduleâs `state_dict`.




register_state_dict_post_hook(_hook_)#
    

Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the `state_dict` inplace.

register_state_dict_pre_hook(_hook_)#
    

Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the `state_dict` call is made.

requires_grad_(_requires_grad : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Change if autograd should record operations on parameters in this module.

This method sets the parametersâ `requires_grad` attributes in-place.

This method is helpful for freezing part of the module for finetuning or training parts of a model individually (e.g., GAN training).

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.requires_grad_()` and several similar mechanisms that may be confused with it.

Parameters:
    

**requires_grad** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether autograd should record operations on parameters in this module. Default: `True`.

Returns:
    

self

Return type:
    

Module

set_extra_state(_state : Any_) → None#
    

Set extra state contained in the loaded `state_dict`.

This function is called from `load_state_dict()` to handle any extra state found within the `state_dict`. Implement this function and a corresponding `get_extra_state()` for your module if you need to store extra state within its `state_dict`.

Parameters:
    

**state** (_dict_) â Extra state from the `state_dict`

set_submodule(_target : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Set the submodule given by `target` if it exists, otherwise throw an error.

Note

If `strict` is set to `False` (default), the method will replace an existing submodule or create a new submodule if the parent module exists. If `strict` is set to `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule does not exist.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To override the `Conv2d` with a new submodule `Linear`, you could call `set_submodule("net_b.net_c.conv", nn.Linear(1, 1))` where `strict` could be `True` or `False`

To add a new submodule `Conv2d` to the existing `net_b` module, you would call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))`.

In the above if you set `strict=True` and call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)`, an AttributeError will be raised because `net_b` does not have a submodule named `conv`.

Parameters:
    

  * **target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

  * **module** â The module to set the submodule to.

  * **strict** â If `False`, the method will replace an existing submodule or create a new submodule if the parent module exists. If `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule doesnât already exist.



Raises:
    

  * **ValueError** â If the `target` string is empty or if `module` is not an instance of `nn.Module`.

  * **AttributeError** â If at any point along the path resulting from the `target` string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.




share_memory() → Self#
    

See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").

state_dict(_* args_, _destination =None_, _prefix =''_, _keep_vars =False_)#
    

Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are included. Keys are corresponding parameter and buffer names. Parameters and buffers set to `None` are not included.

Note

The returned object is a shallow copy. It contains references to the moduleâs parameters and buffers.

Warning

Currently `state_dict()` also accepts positional arguments for `destination`, `prefix` and `keep_vars` in order. However, this is being deprecated and keyword arguments will be enforced in future releases.

Warning

Please avoid the use of argument `destination` as it is not designed for end-users.

Parameters:
    

  * **destination** (_dict_ _,__optional_) â If provided, the state of module will be updated into the dict and the same object is returned. Otherwise, an `OrderedDict` will be created and returned. Default: `None`.

  * **prefix** (_str_ _,__optional_) â a prefix added to parameter and buffer names to compose the keys in state_dict. Default: `''`.

  * **keep_vars** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â by default the [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") s returned in the state dict are detached from autograd. If itâs set to `True`, detaching will not be performed. Default: `False`.



Returns:
    

a dictionary containing a whole state of the module

Return type:
    

dict

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']
    

to(_* args_, _** kwargs_)#
    

Move and/or cast the parameters and buffers.

This can be called as

to(_device =None_, _dtype =None_, _non_blocking =False_)
    

to(_dtype_ , _non_blocking =False_)
    

to(_tensor_ , _non_blocking =False_)
    

to(_memory_format =torch.channels_last_)
    

Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "\(in PyTorch v2.12\)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â the desired device of the parameters and buffers in this module

  * **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)")) â the desired floating point or complex dtype of the parameters and buffers in this module

  * **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")) â Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

  * **memory_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "\(in PyTorch v2.12\)")) â the desired memory format for 4D parameters and buffers in this module (keyword only argument)



Returns:
    

self

Return type:
    

Module

Examples:
    
    
    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)
    
    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)
    

to_empty(_*_ , _device : str | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | int | None_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Move the parameters and buffers to the specified device without copying storage.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â The desired device of the parameters and buffers in this module.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â Whether parameters and buffers of submodules should be recursively moved to the specified device.



Returns:
    

self

Return type:
    

Module

train(_mode : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Set the module in training mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e., whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
    

**mode** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
    

self

Return type:
    

Module

type(_dst_type : [dtype](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)") | str_) → Self#
    

Casts all parameters and buffers to `dst_type`.

Note

This method modifies the module in-place.

Parameters:
    

**dst_type** ([_type_](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type") _or_ _string_) â the desired type

Returns:
    

self

Return type:
    

Module

xpu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on XPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

zero_grad(_set_to_none : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Reset gradients of all model parameters.

See similar function under [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "\(in PyTorch v2.12\)") for more context.

Parameters:
    

**set_to_none** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â instead of setting to zero, set the grads to None. See [`torch.optim.Optimizer.zero_grad()`](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "\(in PyTorch v2.12\)") for details.

training: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

class fiftyone.brain.internal.models.simple_resnet.Flatten(_* args: Any_, _** kwargs: Any_)#
    

Bases: [`Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

**Methods:**

`forward`(x) | Define the computation performed at every call.  
---|---  
`add_module`(name,Â module) | Add a child module to the current module.  
`apply`(fn) | Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.  
`bfloat16`() | Casts all floating point parameters and buffers to `bfloat16` datatype.  
`buffers`([recurse]) | Return an iterator over module buffers.  
`children`() | Return an iterator over immediate children modules.  
`compile`(*args,Â **kwargs) | Compile this Module's forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").  
`cpu`() | Move all model parameters and buffers to the CPU.  
`cuda`([device]) | Move all model parameters and buffers to the GPU.  
`double`() | Casts all floating point parameters and buffers to `double` datatype.  
`eval`() | Set the module in evaluation mode.  
`extra_repr`() | Return the extra representation of the module.  
`float`() | Casts all floating point parameters and buffers to `float` datatype.  
`get_buffer`(target) | Return the buffer given by `target` if it exists, otherwise throw an error.  
`get_extra_state`() | Return any extra state to include in the module's state_dict.  
`get_parameter`(target) | Return the parameter given by `target` if it exists, otherwise throw an error.  
`get_submodule`(target) | Return the submodule given by `target` if it exists, otherwise throw an error.  
`half`() | Casts all floating point parameters and buffers to `half` datatype.  
`ipu`([device]) | Move all model parameters and buffers to the IPU.  
`load_state_dict`(state_dict[,Â strict,Â assign]) | Copy parameters and buffers from `state_dict` into this module and its descendants.  
`modules`([remove_duplicate]) | Return an iterator over all modules in the network.  
`mtia`([device]) | Move all model parameters and buffers to the MTIA.  
`named_buffers`([prefix,Â recurse,Â ...]) | Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.  
`named_children`() | Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.  
`named_modules`([memo,Â prefix,Â remove_duplicate]) | Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.  
`named_parameters`([prefix,Â recurse,Â ...]) | Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.  
`parameters`([recurse]) | Return an iterator over module parameters.  
`register_backward_hook`(hook) | Register a backward hook on the module.  
`register_buffer`(name,Â tensor[,Â persistent]) | Add a buffer to the module.  
`register_forward_hook`(hook,Â *[,Â prepend,Â ...]) | Register a forward hook on the module.  
`register_forward_pre_hook`(hook,Â *[,Â ...]) | Register a forward pre-hook on the module.  
`register_full_backward_hook`(hook[,Â prepend]) | Register a backward hook on the module.  
`register_full_backward_pre_hook`(hook[,Â prepend]) | Register a backward pre-hook on the module.  
`register_load_state_dict_post_hook`(hook) | Register a post-hook to be run after module's `load_state_dict()` is called.  
`register_load_state_dict_pre_hook`(hook) | Register a pre-hook to be run before module's `load_state_dict()` is called.  
`register_module`(name,Â module) | Alias for `add_module()`.  
`register_parameter`(name,Â param) | Add a parameter to the module.  
`register_state_dict_post_hook`(hook) | Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`register_state_dict_pre_hook`(hook) | Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`requires_grad_`([requires_grad]) | Change if autograd should record operations on parameters in this module.  
`set_extra_state`(state) | Set extra state contained in the loaded `state_dict`.  
`set_submodule`(target,Â module[,Â strict]) | Set the submodule given by `target` if it exists, otherwise throw an error.  
`share_memory`() | See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").  
`state_dict`(*args[,Â destination,Â prefix,Â ...]) | Return a dictionary containing references to the whole state of the module.  
`to`(*args,Â **kwargs) | Move and/or cast the parameters and buffers.  
`to_empty`(*,Â device[,Â recurse]) | Move the parameters and buffers to the specified device without copying storage.  
`train`([mode]) | Set the module in training mode.  
`type`(dst_type) | Casts all parameters and buffers to `dst_type`.  
`xpu`([device]) | Move all model parameters and buffers to the XPU.  
`zero_grad`([set_to_none]) | Reset gradients of all model parameters.  
  
**Attributes:**

`T_destination` |   
---|---  
`call_super_init` |   
`dump_patches` |   
`training` |   
  
forward(_x_)#
    

Define the computation performed at every call.

Should be overridden by all subclasses.

Note

Although the recipe for forward pass needs to be defined within this function, one should call the `Module` instance afterwards instead of this since the former takes care of running the registered hooks while the latter silently ignores them.

T_destination = ~T_destination#
    

add_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Parameters:
    

  * **name** (_str_) â name of the child module. The child module can be accessed from this module using the given name

  * **module** (_Module_) â child module to be added to the module.




apply(_fn : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")], None]_) → Self#
    

Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.

Typical use includes initializing the parameters of a model (see also [torch.nn.init](https://docs.pytorch.org/docs/stable/nn.init.html#nn-init-doc "\(in PyTorch v2.12\)")).

Parameters:
    

**fn** (`Module` -> None) â function to be applied to each submodule

Returns:
    

self

Return type:
    

Module

Example:
    
    
    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    

bfloat16() → Self#
    

Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

buffers(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]#
    

Return an iterator over module buffers.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module.

Yields:
    

_torch.Tensor_ â module buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

call_super_init: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

children() → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over immediate children modules.

Yields:
    

_Module_ â a child module

compile(_* args_, _** kwargs_) → None#
    

Compile this Moduleâs forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

This Moduleâs `__call__` method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)") for details on the arguments for this function.

cpu() → Self#
    

Move all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

cuda(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

double() → Self#
    

Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

dump_patches: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

eval() → Self#
    

Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e. whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "\(in PyTorch v2.12\)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.eval()` and several similar mechanisms that may be confused with it.

Returns:
    

self

Return type:
    

Module

extra_repr() → str#
    

Return the extra representation of the module.

To print customized extra information, you should re-implement this method in your own modules. Both single-line and multi-line strings are acceptable.

float() → Self#
    

Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

get_buffer(_target : str_) → [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")#
    

Return the buffer given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the buffer to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The buffer referenced by `target`

Return type:
    

[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not a buffer

get_extra_state() → Any#
    

Return any extra state to include in the moduleâs state_dict.

Implement this and a corresponding `set_extra_state()` for your module if you need to store extra state. This function is called when building the moduleâs `state_dict()`.

Note that extra state should be picklable to ensure working serialization of the state_dict. We only provide backwards compatibility guarantees for serializing Tensors; other objects may break backwards compatibility if their serialized pickled form changes.

Returns:
    

Any extra state to store in the moduleâs state_dict

Return type:
    

object

get_parameter(_target : str_) → [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")#
    

Return the parameter given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the Parameter to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The Parameter referenced by `target`

Return type:
    

torch.nn.Parameter

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not an `nn.Parameter`

get_submodule(_target : str_) → [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")#
    

Return the submodule given by `target` if it exists, otherwise throw an error.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` which has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To check whether or not we have the `linear` submodule, we would call `get_submodule("net_b.linear")`. To check whether we have the `conv` submodule, we would call `get_submodule("net_b.net_c.conv")`.

The runtime of `get_submodule` is bounded by the degree of module nesting in `target`. A query against `named_modules` achieves the same result, but it is O(N) in the number of transitive modules. So, for a simple check to see if some submodule exists, `get_submodule` should always be used.

Parameters:
    

**target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

Returns:
    

The submodule referenced by `target`

Return type:
    

[torch.nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If at any point along the path resulting from the target string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.

half() → Self#
    

Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

ipu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on IPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

load_state_dict(_state_dict : Mapping[str, Any]_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _assign : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

Copy parameters and buffers from `state_dict` into this module and its descendants.

If `strict` is `True`, then the keys of `state_dict` must exactly match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function.

Warning

If `assign` is `True` the optimizer must be created after the call to `load_state_dict` unless [`get_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/stable/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "\(in PyTorch v2.12\)") is `True`.

Parameters:
    

  * **state_dict** (_dict_) â a dict containing parameters and persistent buffers.

  * **strict** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to strictly enforce that the keys in `state_dict` match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function. Default: `True`

  * **assign** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â When set to `False`, the properties of the tensors in the current module are preserved whereas setting it to `True` preserves properties of the Tensors in the state dict. The only exception is the `requires_grad` field of `Parameter` for which the value from the module is preserved. Default: `False`



Returns:
    

  * `missing_keys` is a list of str containing any keys that are expected
    

by this module but missing from the provided `state_dict`.

  * `unexpected_keys` is a list of str containing the keys that are not
    

expected by this module but present in the provided `state_dict`.




Return type:
    

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

Note

If a parameter or buffer is registered as `None` and its corresponding key exists in `state_dict`, `load_state_dict()` will raise a `RuntimeError`.

modules(_remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over all modules in the network.

Parameters:
    

**remove_duplicate** â whether to remove the duplicated module instances in the result or not.

Yields:
    

_Module_ â a module in the network

Note

Duplicate modules are returned only once by default. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)
    
    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)
    

mtia(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on MTIA while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

named_buffers(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all buffer names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module. Defaults to True.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated buffers in the result. Defaults to True.



Yields:
    

_(str, torch.Tensor)_ â Tuple containing the name and buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())
    

named_children() → Iterator[tuple[str, [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]]#
    

Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    

_(str, Module)_ â Tuple containing a name and child module

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)
    

named_modules(_memo : set[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")] | None = None_, _prefix : str = ''_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_)#
    

Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Parameters:
    

  * **memo** â a memo to store the set of modules already added to the result

  * **prefix** â a prefix that will be added to the name of the module

  * **remove_duplicate** â whether to remove the duplicated module instances in the result or not



Yields:
    

_(str, Module)_ â Tuple of name and module

Note

Duplicate modules are returned only once. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)
    
    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))
    

named_parameters(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all parameter names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated parameters in the result. Defaults to True.



Yields:
    

_(str, Parameter)_ â Tuple containing the name and parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())
    

parameters(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]#
    

Return an iterator over module parameters.

This is typically passed to an optimizer.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

Yields:
    

_Parameter_ â module parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

register_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_) → RemovableHandle#
    

Register a backward hook on the module.

This function is deprecated in favor of [`register_full_backward_hook()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "\(in PyTorch v2.12\)") and the behavior of this function will change in future versions.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_buffer(_name : str_, _tensor : [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None_, _persistent : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Add a buffer to the module.

This is typically used to register a buffer that should not be considered a model parameter. For example, BatchNormâs `running_mean` is not a parameter, but is part of the moduleâs state. Buffers, by default, are persistent and will be saved alongside parameters. This behavior can be changed by setting `persistent` to `False`. The only difference between a persistent buffer and a non-persistent buffer is that the latter will not be a part of this moduleâs `state_dict`.

Buffers can be accessed as attributes using given names.

Parameters:
    

  * **name** (_str_) â name of the buffer. The buffer can be accessed from this module using the given name

  * **tensor** (_Tensor_ _or_ _None_) â buffer to be registered. If `None`, then operations that run on buffers, such as `cuda`, are ignored. If `None`, the buffer is **not** included in the moduleâs `state_dict`.

  * **persistent** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the buffer is part of this moduleâs `state_dict`.




Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))
    

register_forward_hook(_hook : Callable[[T, tuple[Any, ...], Any], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any], Any], Any | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _always_call : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward hook on the module.

The hook will be called every time after `forward()` has computed an output.

If `with_kwargs` is `False` or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the output. It can modify the input inplace but it will not have effect on forward since this is called after `forward()` is called. The hook should have the following signature:
    
    
    hook(module, args, output) -> None or modified output
    

If `with_kwargs` is `True`, the forward hook will be passed the `kwargs` given to the forward function and be expected to return the output possibly modified. The hook should have the following signature:
    
    
    hook(module, args, kwargs, output) -> None or modified output
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the provided `hook` will be fired before all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward` hooks registered with `register_module_forward_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the `hook` will be passed the kwargs given to the forward function. Default: `False`

  * **always_call** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True` the `hook` will be run regardless of whether an exception is raised while calling the Module. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_forward_pre_hook(_hook : Callable[[T, tuple[Any, ...]], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any]], tuple[Any, dict[str, Any]] | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward pre-hook on the module.

The hook will be called every time before `forward()` is invoked.

If `with_kwargs` is false or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the input. User can either return a tuple or a single modified value in the hook. We will wrap the value into a tuple if a single value is returned (unless that value is already a tuple). The hook should have the following signature:
    
    
    hook(module, args) -> None or modified input
    

If `with_kwargs` is true, the forward pre-hook will be passed the kwargs given to the forward function. And if the hook modifies the input, both the args and kwargs should be returned. The hook should have the following signature:
    
    
    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward_pre` hooks registered with `register_module_forward_pre_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the `hook` will be passed the kwargs given to the forward function. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

>   1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
> 
>   2. If none of the module inputs require gradients, the hook will fire when the gradients are computed with respect to module outputs.
> 
>   3. If none of the module outputs require gradients, then the hooks will not fire.
> 
> 


The hook should have the following signature:
    
    
    hook(module, grad_input, grad_output) -> tuple(Tensor) or None
    

The `grad_input` and `grad_output` are tuples that contain the gradients with respect to the inputs and outputs respectively. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the input that will be used in place of `grad_input` in subsequent computations. `grad_input` will only correspond to the inputs given as positional arguments and all kwarg arguments are ignored. Entries in `grad_input` and `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs or outputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward` hooks registered with `register_module_full_backward_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_pre_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed. The hook should have the following signature:
    
    
    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None
    

The `grad_output` is a tuple. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the output that will be used in place of `grad_output` in subsequent computations. Entries in `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward_pre` hooks registered with `register_module_full_backward_pre_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_post_hook(_hook_)#
    

Register a post-hook to be run after moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, incompatible_keys) -> None

The `module` argument is the current module that this hook is registered on, and the `incompatible_keys` argument is a `NamedTuple` consisting of attributes `missing_keys` and `unexpected_keys`. `missing_keys` is a `list` of `str` containing the missing keys and `unexpected_keys` is a `list` of `str` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling `load_state_dict()` with `strict=True` are affected by modifications the hook makes to `missing_keys` or `unexpected_keys`, as expected. Additions to either set of keys will result in an error being thrown when `strict=True`, and clearing out both missing and unexpected keys will avoid an error.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_pre_hook(_hook_)#
    

Register a pre-hook to be run before moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None # noqa: B950

Parameters:
    

**hook** (_Callable_) â Callable hook that will be invoked before loading the state dict.

register_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Alias for `add_module()`.

register_parameter(_name : str_, _param : [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)") | None_) → None#
    

Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Parameters:
    

  * **name** (_str_) â name of the parameter. The parameter can be accessed from this module using the given name

  * **param** (_Parameter_ _or_ _None_) â parameter to be added to the module. If `None`, then operations that run on parameters, such as `cuda`, are ignored. If `None`, the parameter is **not** included in the moduleâs `state_dict`.




register_state_dict_post_hook(_hook_)#
    

Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the `state_dict` inplace.

register_state_dict_pre_hook(_hook_)#
    

Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the `state_dict` call is made.

requires_grad_(_requires_grad : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Change if autograd should record operations on parameters in this module.

This method sets the parametersâ `requires_grad` attributes in-place.

This method is helpful for freezing part of the module for finetuning or training parts of a model individually (e.g., GAN training).

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.requires_grad_()` and several similar mechanisms that may be confused with it.

Parameters:
    

**requires_grad** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether autograd should record operations on parameters in this module. Default: `True`.

Returns:
    

self

Return type:
    

Module

set_extra_state(_state : Any_) → None#
    

Set extra state contained in the loaded `state_dict`.

This function is called from `load_state_dict()` to handle any extra state found within the `state_dict`. Implement this function and a corresponding `get_extra_state()` for your module if you need to store extra state within its `state_dict`.

Parameters:
    

**state** (_dict_) â Extra state from the `state_dict`

set_submodule(_target : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Set the submodule given by `target` if it exists, otherwise throw an error.

Note

If `strict` is set to `False` (default), the method will replace an existing submodule or create a new submodule if the parent module exists. If `strict` is set to `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule does not exist.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To override the `Conv2d` with a new submodule `Linear`, you could call `set_submodule("net_b.net_c.conv", nn.Linear(1, 1))` where `strict` could be `True` or `False`

To add a new submodule `Conv2d` to the existing `net_b` module, you would call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))`.

In the above if you set `strict=True` and call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)`, an AttributeError will be raised because `net_b` does not have a submodule named `conv`.

Parameters:
    

  * **target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

  * **module** â The module to set the submodule to.

  * **strict** â If `False`, the method will replace an existing submodule or create a new submodule if the parent module exists. If `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule doesnât already exist.



Raises:
    

  * **ValueError** â If the `target` string is empty or if `module` is not an instance of `nn.Module`.

  * **AttributeError** â If at any point along the path resulting from the `target` string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.




share_memory() → Self#
    

See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").

state_dict(_* args_, _destination =None_, _prefix =''_, _keep_vars =False_)#
    

Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are included. Keys are corresponding parameter and buffer names. Parameters and buffers set to `None` are not included.

Note

The returned object is a shallow copy. It contains references to the moduleâs parameters and buffers.

Warning

Currently `state_dict()` also accepts positional arguments for `destination`, `prefix` and `keep_vars` in order. However, this is being deprecated and keyword arguments will be enforced in future releases.

Warning

Please avoid the use of argument `destination` as it is not designed for end-users.

Parameters:
    

  * **destination** (_dict_ _,__optional_) â If provided, the state of module will be updated into the dict and the same object is returned. Otherwise, an `OrderedDict` will be created and returned. Default: `None`.

  * **prefix** (_str_ _,__optional_) â a prefix added to parameter and buffer names to compose the keys in state_dict. Default: `''`.

  * **keep_vars** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â by default the [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") s returned in the state dict are detached from autograd. If itâs set to `True`, detaching will not be performed. Default: `False`.



Returns:
    

a dictionary containing a whole state of the module

Return type:
    

dict

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']
    

to(_* args_, _** kwargs_)#
    

Move and/or cast the parameters and buffers.

This can be called as

to(_device =None_, _dtype =None_, _non_blocking =False_)
    

to(_dtype_ , _non_blocking =False_)
    

to(_tensor_ , _non_blocking =False_)
    

to(_memory_format =torch.channels_last_)
    

Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "\(in PyTorch v2.12\)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â the desired device of the parameters and buffers in this module

  * **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)")) â the desired floating point or complex dtype of the parameters and buffers in this module

  * **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")) â Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

  * **memory_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "\(in PyTorch v2.12\)")) â the desired memory format for 4D parameters and buffers in this module (keyword only argument)



Returns:
    

self

Return type:
    

Module

Examples:
    
    
    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)
    
    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)
    

to_empty(_*_ , _device : str | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | int | None_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Move the parameters and buffers to the specified device without copying storage.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â The desired device of the parameters and buffers in this module.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â Whether parameters and buffers of submodules should be recursively moved to the specified device.



Returns:
    

self

Return type:
    

Module

train(_mode : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Set the module in training mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e., whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
    

**mode** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
    

self

Return type:
    

Module

type(_dst_type : [dtype](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)") | str_) → Self#
    

Casts all parameters and buffers to `dst_type`.

Note

This method modifies the module in-place.

Parameters:
    

**dst_type** ([_type_](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type") _or_ _string_) â the desired type

Returns:
    

self

Return type:
    

Module

xpu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on XPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

zero_grad(_set_to_none : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Reset gradients of all model parameters.

See similar function under [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "\(in PyTorch v2.12\)") for more context.

Parameters:
    

**set_to_none** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â instead of setting to zero, set the grads to None. See [`torch.optim.Optimizer.zero_grad()`](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "\(in PyTorch v2.12\)") for details.

training: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

class fiftyone.brain.internal.models.simple_resnet.Concat(_* args: Any_, _** kwargs: Any_)#
    

Bases: [`Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

**Methods:**

`forward`(*xs) | Define the computation performed at every call.  
---|---  
`add_module`(name,Â module) | Add a child module to the current module.  
`apply`(fn) | Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.  
`bfloat16`() | Casts all floating point parameters and buffers to `bfloat16` datatype.  
`buffers`([recurse]) | Return an iterator over module buffers.  
`children`() | Return an iterator over immediate children modules.  
`compile`(*args,Â **kwargs) | Compile this Module's forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").  
`cpu`() | Move all model parameters and buffers to the CPU.  
`cuda`([device]) | Move all model parameters and buffers to the GPU.  
`double`() | Casts all floating point parameters and buffers to `double` datatype.  
`eval`() | Set the module in evaluation mode.  
`extra_repr`() | Return the extra representation of the module.  
`float`() | Casts all floating point parameters and buffers to `float` datatype.  
`get_buffer`(target) | Return the buffer given by `target` if it exists, otherwise throw an error.  
`get_extra_state`() | Return any extra state to include in the module's state_dict.  
`get_parameter`(target) | Return the parameter given by `target` if it exists, otherwise throw an error.  
`get_submodule`(target) | Return the submodule given by `target` if it exists, otherwise throw an error.  
`half`() | Casts all floating point parameters and buffers to `half` datatype.  
`ipu`([device]) | Move all model parameters and buffers to the IPU.  
`load_state_dict`(state_dict[,Â strict,Â assign]) | Copy parameters and buffers from `state_dict` into this module and its descendants.  
`modules`([remove_duplicate]) | Return an iterator over all modules in the network.  
`mtia`([device]) | Move all model parameters and buffers to the MTIA.  
`named_buffers`([prefix,Â recurse,Â ...]) | Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.  
`named_children`() | Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.  
`named_modules`([memo,Â prefix,Â remove_duplicate]) | Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.  
`named_parameters`([prefix,Â recurse,Â ...]) | Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.  
`parameters`([recurse]) | Return an iterator over module parameters.  
`register_backward_hook`(hook) | Register a backward hook on the module.  
`register_buffer`(name,Â tensor[,Â persistent]) | Add a buffer to the module.  
`register_forward_hook`(hook,Â *[,Â prepend,Â ...]) | Register a forward hook on the module.  
`register_forward_pre_hook`(hook,Â *[,Â ...]) | Register a forward pre-hook on the module.  
`register_full_backward_hook`(hook[,Â prepend]) | Register a backward hook on the module.  
`register_full_backward_pre_hook`(hook[,Â prepend]) | Register a backward pre-hook on the module.  
`register_load_state_dict_post_hook`(hook) | Register a post-hook to be run after module's `load_state_dict()` is called.  
`register_load_state_dict_pre_hook`(hook) | Register a pre-hook to be run before module's `load_state_dict()` is called.  
`register_module`(name,Â module) | Alias for `add_module()`.  
`register_parameter`(name,Â param) | Add a parameter to the module.  
`register_state_dict_post_hook`(hook) | Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`register_state_dict_pre_hook`(hook) | Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`requires_grad_`([requires_grad]) | Change if autograd should record operations on parameters in this module.  
`set_extra_state`(state) | Set extra state contained in the loaded `state_dict`.  
`set_submodule`(target,Â module[,Â strict]) | Set the submodule given by `target` if it exists, otherwise throw an error.  
`share_memory`() | See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").  
`state_dict`(*args[,Â destination,Â prefix,Â ...]) | Return a dictionary containing references to the whole state of the module.  
`to`(*args,Â **kwargs) | Move and/or cast the parameters and buffers.  
`to_empty`(*,Â device[,Â recurse]) | Move the parameters and buffers to the specified device without copying storage.  
`train`([mode]) | Set the module in training mode.  
`type`(dst_type) | Casts all parameters and buffers to `dst_type`.  
`xpu`([device]) | Move all model parameters and buffers to the XPU.  
`zero_grad`([set_to_none]) | Reset gradients of all model parameters.  
  
**Attributes:**

`T_destination` |   
---|---  
`call_super_init` |   
`dump_patches` |   
`training` |   
  
forward(_* xs_)#
    

Define the computation performed at every call.

Should be overridden by all subclasses.

Note

Although the recipe for forward pass needs to be defined within this function, one should call the `Module` instance afterwards instead of this since the former takes care of running the registered hooks while the latter silently ignores them.

T_destination = ~T_destination#
    

add_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Parameters:
    

  * **name** (_str_) â name of the child module. The child module can be accessed from this module using the given name

  * **module** (_Module_) â child module to be added to the module.




apply(_fn : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")], None]_) → Self#
    

Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.

Typical use includes initializing the parameters of a model (see also [torch.nn.init](https://docs.pytorch.org/docs/stable/nn.init.html#nn-init-doc "\(in PyTorch v2.12\)")).

Parameters:
    

**fn** (`Module` -> None) â function to be applied to each submodule

Returns:
    

self

Return type:
    

Module

Example:
    
    
    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    

bfloat16() → Self#
    

Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

buffers(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]#
    

Return an iterator over module buffers.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module.

Yields:
    

_torch.Tensor_ â module buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

call_super_init: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

children() → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over immediate children modules.

Yields:
    

_Module_ â a child module

compile(_* args_, _** kwargs_) → None#
    

Compile this Moduleâs forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

This Moduleâs `__call__` method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)") for details on the arguments for this function.

cpu() → Self#
    

Move all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

cuda(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

double() → Self#
    

Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

dump_patches: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

eval() → Self#
    

Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e. whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "\(in PyTorch v2.12\)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.eval()` and several similar mechanisms that may be confused with it.

Returns:
    

self

Return type:
    

Module

extra_repr() → str#
    

Return the extra representation of the module.

To print customized extra information, you should re-implement this method in your own modules. Both single-line and multi-line strings are acceptable.

float() → Self#
    

Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

get_buffer(_target : str_) → [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")#
    

Return the buffer given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the buffer to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The buffer referenced by `target`

Return type:
    

[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not a buffer

get_extra_state() → Any#
    

Return any extra state to include in the moduleâs state_dict.

Implement this and a corresponding `set_extra_state()` for your module if you need to store extra state. This function is called when building the moduleâs `state_dict()`.

Note that extra state should be picklable to ensure working serialization of the state_dict. We only provide backwards compatibility guarantees for serializing Tensors; other objects may break backwards compatibility if their serialized pickled form changes.

Returns:
    

Any extra state to store in the moduleâs state_dict

Return type:
    

object

get_parameter(_target : str_) → [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")#
    

Return the parameter given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the Parameter to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The Parameter referenced by `target`

Return type:
    

torch.nn.Parameter

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not an `nn.Parameter`

get_submodule(_target : str_) → [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")#
    

Return the submodule given by `target` if it exists, otherwise throw an error.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` which has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To check whether or not we have the `linear` submodule, we would call `get_submodule("net_b.linear")`. To check whether we have the `conv` submodule, we would call `get_submodule("net_b.net_c.conv")`.

The runtime of `get_submodule` is bounded by the degree of module nesting in `target`. A query against `named_modules` achieves the same result, but it is O(N) in the number of transitive modules. So, for a simple check to see if some submodule exists, `get_submodule` should always be used.

Parameters:
    

**target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

Returns:
    

The submodule referenced by `target`

Return type:
    

[torch.nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If at any point along the path resulting from the target string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.

half() → Self#
    

Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

ipu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on IPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

load_state_dict(_state_dict : Mapping[str, Any]_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _assign : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

Copy parameters and buffers from `state_dict` into this module and its descendants.

If `strict` is `True`, then the keys of `state_dict` must exactly match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function.

Warning

If `assign` is `True` the optimizer must be created after the call to `load_state_dict` unless [`get_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/stable/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "\(in PyTorch v2.12\)") is `True`.

Parameters:
    

  * **state_dict** (_dict_) â a dict containing parameters and persistent buffers.

  * **strict** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to strictly enforce that the keys in `state_dict` match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function. Default: `True`

  * **assign** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â When set to `False`, the properties of the tensors in the current module are preserved whereas setting it to `True` preserves properties of the Tensors in the state dict. The only exception is the `requires_grad` field of `Parameter` for which the value from the module is preserved. Default: `False`



Returns:
    

  * `missing_keys` is a list of str containing any keys that are expected
    

by this module but missing from the provided `state_dict`.

  * `unexpected_keys` is a list of str containing the keys that are not
    

expected by this module but present in the provided `state_dict`.




Return type:
    

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

Note

If a parameter or buffer is registered as `None` and its corresponding key exists in `state_dict`, `load_state_dict()` will raise a `RuntimeError`.

modules(_remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over all modules in the network.

Parameters:
    

**remove_duplicate** â whether to remove the duplicated module instances in the result or not.

Yields:
    

_Module_ â a module in the network

Note

Duplicate modules are returned only once by default. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)
    
    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)
    

mtia(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on MTIA while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

named_buffers(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all buffer names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module. Defaults to True.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated buffers in the result. Defaults to True.



Yields:
    

_(str, torch.Tensor)_ â Tuple containing the name and buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())
    

named_children() → Iterator[tuple[str, [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]]#
    

Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    

_(str, Module)_ â Tuple containing a name and child module

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)
    

named_modules(_memo : set[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")] | None = None_, _prefix : str = ''_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_)#
    

Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Parameters:
    

  * **memo** â a memo to store the set of modules already added to the result

  * **prefix** â a prefix that will be added to the name of the module

  * **remove_duplicate** â whether to remove the duplicated module instances in the result or not



Yields:
    

_(str, Module)_ â Tuple of name and module

Note

Duplicate modules are returned only once. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)
    
    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))
    

named_parameters(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all parameter names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated parameters in the result. Defaults to True.



Yields:
    

_(str, Parameter)_ â Tuple containing the name and parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())
    

parameters(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]#
    

Return an iterator over module parameters.

This is typically passed to an optimizer.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

Yields:
    

_Parameter_ â module parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

register_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_) → RemovableHandle#
    

Register a backward hook on the module.

This function is deprecated in favor of [`register_full_backward_hook()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "\(in PyTorch v2.12\)") and the behavior of this function will change in future versions.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_buffer(_name : str_, _tensor : [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None_, _persistent : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Add a buffer to the module.

This is typically used to register a buffer that should not be considered a model parameter. For example, BatchNormâs `running_mean` is not a parameter, but is part of the moduleâs state. Buffers, by default, are persistent and will be saved alongside parameters. This behavior can be changed by setting `persistent` to `False`. The only difference between a persistent buffer and a non-persistent buffer is that the latter will not be a part of this moduleâs `state_dict`.

Buffers can be accessed as attributes using given names.

Parameters:
    

  * **name** (_str_) â name of the buffer. The buffer can be accessed from this module using the given name

  * **tensor** (_Tensor_ _or_ _None_) â buffer to be registered. If `None`, then operations that run on buffers, such as `cuda`, are ignored. If `None`, the buffer is **not** included in the moduleâs `state_dict`.

  * **persistent** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the buffer is part of this moduleâs `state_dict`.




Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))
    

register_forward_hook(_hook : Callable[[T, tuple[Any, ...], Any], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any], Any], Any | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _always_call : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward hook on the module.

The hook will be called every time after `forward()` has computed an output.

If `with_kwargs` is `False` or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the output. It can modify the input inplace but it will not have effect on forward since this is called after `forward()` is called. The hook should have the following signature:
    
    
    hook(module, args, output) -> None or modified output
    

If `with_kwargs` is `True`, the forward hook will be passed the `kwargs` given to the forward function and be expected to return the output possibly modified. The hook should have the following signature:
    
    
    hook(module, args, kwargs, output) -> None or modified output
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the provided `hook` will be fired before all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward` hooks registered with `register_module_forward_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the `hook` will be passed the kwargs given to the forward function. Default: `False`

  * **always_call** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True` the `hook` will be run regardless of whether an exception is raised while calling the Module. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_forward_pre_hook(_hook : Callable[[T, tuple[Any, ...]], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any]], tuple[Any, dict[str, Any]] | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward pre-hook on the module.

The hook will be called every time before `forward()` is invoked.

If `with_kwargs` is false or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the input. User can either return a tuple or a single modified value in the hook. We will wrap the value into a tuple if a single value is returned (unless that value is already a tuple). The hook should have the following signature:
    
    
    hook(module, args) -> None or modified input
    

If `with_kwargs` is true, the forward pre-hook will be passed the kwargs given to the forward function. And if the hook modifies the input, both the args and kwargs should be returned. The hook should have the following signature:
    
    
    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward_pre` hooks registered with `register_module_forward_pre_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the `hook` will be passed the kwargs given to the forward function. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

>   1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
> 
>   2. If none of the module inputs require gradients, the hook will fire when the gradients are computed with respect to module outputs.
> 
>   3. If none of the module outputs require gradients, then the hooks will not fire.
> 
> 


The hook should have the following signature:
    
    
    hook(module, grad_input, grad_output) -> tuple(Tensor) or None
    

The `grad_input` and `grad_output` are tuples that contain the gradients with respect to the inputs and outputs respectively. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the input that will be used in place of `grad_input` in subsequent computations. `grad_input` will only correspond to the inputs given as positional arguments and all kwarg arguments are ignored. Entries in `grad_input` and `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs or outputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward` hooks registered with `register_module_full_backward_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_pre_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed. The hook should have the following signature:
    
    
    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None
    

The `grad_output` is a tuple. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the output that will be used in place of `grad_output` in subsequent computations. Entries in `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward_pre` hooks registered with `register_module_full_backward_pre_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_post_hook(_hook_)#
    

Register a post-hook to be run after moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, incompatible_keys) -> None

The `module` argument is the current module that this hook is registered on, and the `incompatible_keys` argument is a `NamedTuple` consisting of attributes `missing_keys` and `unexpected_keys`. `missing_keys` is a `list` of `str` containing the missing keys and `unexpected_keys` is a `list` of `str` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling `load_state_dict()` with `strict=True` are affected by modifications the hook makes to `missing_keys` or `unexpected_keys`, as expected. Additions to either set of keys will result in an error being thrown when `strict=True`, and clearing out both missing and unexpected keys will avoid an error.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_pre_hook(_hook_)#
    

Register a pre-hook to be run before moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None # noqa: B950

Parameters:
    

**hook** (_Callable_) â Callable hook that will be invoked before loading the state dict.

register_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Alias for `add_module()`.

register_parameter(_name : str_, _param : [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)") | None_) → None#
    

Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Parameters:
    

  * **name** (_str_) â name of the parameter. The parameter can be accessed from this module using the given name

  * **param** (_Parameter_ _or_ _None_) â parameter to be added to the module. If `None`, then operations that run on parameters, such as `cuda`, are ignored. If `None`, the parameter is **not** included in the moduleâs `state_dict`.




register_state_dict_post_hook(_hook_)#
    

Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the `state_dict` inplace.

register_state_dict_pre_hook(_hook_)#
    

Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the `state_dict` call is made.

requires_grad_(_requires_grad : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Change if autograd should record operations on parameters in this module.

This method sets the parametersâ `requires_grad` attributes in-place.

This method is helpful for freezing part of the module for finetuning or training parts of a model individually (e.g., GAN training).

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.requires_grad_()` and several similar mechanisms that may be confused with it.

Parameters:
    

**requires_grad** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether autograd should record operations on parameters in this module. Default: `True`.

Returns:
    

self

Return type:
    

Module

set_extra_state(_state : Any_) → None#
    

Set extra state contained in the loaded `state_dict`.

This function is called from `load_state_dict()` to handle any extra state found within the `state_dict`. Implement this function and a corresponding `get_extra_state()` for your module if you need to store extra state within its `state_dict`.

Parameters:
    

**state** (_dict_) â Extra state from the `state_dict`

set_submodule(_target : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Set the submodule given by `target` if it exists, otherwise throw an error.

Note

If `strict` is set to `False` (default), the method will replace an existing submodule or create a new submodule if the parent module exists. If `strict` is set to `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule does not exist.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To override the `Conv2d` with a new submodule `Linear`, you could call `set_submodule("net_b.net_c.conv", nn.Linear(1, 1))` where `strict` could be `True` or `False`

To add a new submodule `Conv2d` to the existing `net_b` module, you would call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))`.

In the above if you set `strict=True` and call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)`, an AttributeError will be raised because `net_b` does not have a submodule named `conv`.

Parameters:
    

  * **target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

  * **module** â The module to set the submodule to.

  * **strict** â If `False`, the method will replace an existing submodule or create a new submodule if the parent module exists. If `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule doesnât already exist.



Raises:
    

  * **ValueError** â If the `target` string is empty or if `module` is not an instance of `nn.Module`.

  * **AttributeError** â If at any point along the path resulting from the `target` string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.




share_memory() → Self#
    

See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").

state_dict(_* args_, _destination =None_, _prefix =''_, _keep_vars =False_)#
    

Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are included. Keys are corresponding parameter and buffer names. Parameters and buffers set to `None` are not included.

Note

The returned object is a shallow copy. It contains references to the moduleâs parameters and buffers.

Warning

Currently `state_dict()` also accepts positional arguments for `destination`, `prefix` and `keep_vars` in order. However, this is being deprecated and keyword arguments will be enforced in future releases.

Warning

Please avoid the use of argument `destination` as it is not designed for end-users.

Parameters:
    

  * **destination** (_dict_ _,__optional_) â If provided, the state of module will be updated into the dict and the same object is returned. Otherwise, an `OrderedDict` will be created and returned. Default: `None`.

  * **prefix** (_str_ _,__optional_) â a prefix added to parameter and buffer names to compose the keys in state_dict. Default: `''`.

  * **keep_vars** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â by default the [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") s returned in the state dict are detached from autograd. If itâs set to `True`, detaching will not be performed. Default: `False`.



Returns:
    

a dictionary containing a whole state of the module

Return type:
    

dict

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']
    

to(_* args_, _** kwargs_)#
    

Move and/or cast the parameters and buffers.

This can be called as

to(_device =None_, _dtype =None_, _non_blocking =False_)
    

to(_dtype_ , _non_blocking =False_)
    

to(_tensor_ , _non_blocking =False_)
    

to(_memory_format =torch.channels_last_)
    

Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "\(in PyTorch v2.12\)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â the desired device of the parameters and buffers in this module

  * **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)")) â the desired floating point or complex dtype of the parameters and buffers in this module

  * **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")) â Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

  * **memory_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "\(in PyTorch v2.12\)")) â the desired memory format for 4D parameters and buffers in this module (keyword only argument)



Returns:
    

self

Return type:
    

Module

Examples:
    
    
    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)
    
    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)
    

to_empty(_*_ , _device : str | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | int | None_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Move the parameters and buffers to the specified device without copying storage.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â The desired device of the parameters and buffers in this module.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â Whether parameters and buffers of submodules should be recursively moved to the specified device.



Returns:
    

self

Return type:
    

Module

train(_mode : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Set the module in training mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e., whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
    

**mode** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
    

self

Return type:
    

Module

type(_dst_type : [dtype](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)") | str_) → Self#
    

Casts all parameters and buffers to `dst_type`.

Note

This method modifies the module in-place.

Parameters:
    

**dst_type** ([_type_](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type") _or_ _string_) â the desired type

Returns:
    

self

Return type:
    

Module

xpu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on XPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

zero_grad(_set_to_none : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Reset gradients of all model parameters.

See similar function under [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "\(in PyTorch v2.12\)") for more context.

Parameters:
    

**set_to_none** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â instead of setting to zero, set the grads to None. See [`torch.optim.Optimizer.zero_grad()`](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "\(in PyTorch v2.12\)") for details.

training: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

class fiftyone.brain.internal.models.simple_resnet.BatchNorm(_num_features_ , _eps =1e-05_, _momentum =0.1_, _weight_freeze =False_, _bias_freeze =False_, _weight_init =1.0_, _bias_init =0.0_)#
    

Bases: [`BatchNorm2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.modules.batchnorm.BatchNorm2d.html#torch.nn.modules.batchnorm.BatchNorm2d "\(in PyTorch v2.12\)")

**Attributes:**

`T_destination` |   
---|---  
`call_super_init` |   
`dump_patches` |   
`num_features` |   
`eps` |   
`momentum` |   
`affine` |   
`track_running_stats` |   
`training` |   
  
**Methods:**

`add_module`(name,Â module) | Add a child module to the current module.  
---|---  
`apply`(fn) | Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.  
`bfloat16`() | Casts all floating point parameters and buffers to `bfloat16` datatype.  
`buffers`([recurse]) | Return an iterator over module buffers.  
`children`() | Return an iterator over immediate children modules.  
`compile`(*args,Â **kwargs) | Compile this Module's forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").  
`cpu`() | Move all model parameters and buffers to the CPU.  
`cuda`([device]) | Move all model parameters and buffers to the GPU.  
`double`() | Casts all floating point parameters and buffers to `double` datatype.  
`eval`() | Set the module in evaluation mode.  
`extra_repr`() | Return the extra representation of the module.  
`float`() | Casts all floating point parameters and buffers to `float` datatype.  
`forward`(input) | Define the computation performed at every call.  
`get_buffer`(target) | Return the buffer given by `target` if it exists, otherwise throw an error.  
`get_extra_state`() | Return any extra state to include in the module's state_dict.  
`get_parameter`(target) | Return the parameter given by `target` if it exists, otherwise throw an error.  
`get_submodule`(target) | Return the submodule given by `target` if it exists, otherwise throw an error.  
`half`() | Casts all floating point parameters and buffers to `half` datatype.  
`ipu`([device]) | Move all model parameters and buffers to the IPU.  
`load_state_dict`(state_dict[,Â strict,Â assign]) | Copy parameters and buffers from `state_dict` into this module and its descendants.  
`modules`([remove_duplicate]) | Return an iterator over all modules in the network.  
`mtia`([device]) | Move all model parameters and buffers to the MTIA.  
`named_buffers`([prefix,Â recurse,Â ...]) | Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.  
`named_children`() | Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.  
`named_modules`([memo,Â prefix,Â remove_duplicate]) | Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.  
`named_parameters`([prefix,Â recurse,Â ...]) | Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.  
`parameters`([recurse]) | Return an iterator over module parameters.  
`register_backward_hook`(hook) | Register a backward hook on the module.  
`register_buffer`(name,Â tensor[,Â persistent]) | Add a buffer to the module.  
`register_forward_hook`(hook,Â *[,Â prepend,Â ...]) | Register a forward hook on the module.  
`register_forward_pre_hook`(hook,Â *[,Â ...]) | Register a forward pre-hook on the module.  
`register_full_backward_hook`(hook[,Â prepend]) | Register a backward hook on the module.  
`register_full_backward_pre_hook`(hook[,Â prepend]) | Register a backward pre-hook on the module.  
`register_load_state_dict_post_hook`(hook) | Register a post-hook to be run after module's `load_state_dict()` is called.  
`register_load_state_dict_pre_hook`(hook) | Register a pre-hook to be run before module's `load_state_dict()` is called.  
`register_module`(name,Â module) | Alias for `add_module()`.  
`register_parameter`(name,Â param) | Add a parameter to the module.  
`register_state_dict_post_hook`(hook) | Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`register_state_dict_pre_hook`(hook) | Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.  
`requires_grad_`([requires_grad]) | Change if autograd should record operations on parameters in this module.  
`reset_parameters`() |   
`reset_running_stats`() |   
`set_extra_state`(state) | Set extra state contained in the loaded `state_dict`.  
`set_submodule`(target,Â module[,Â strict]) | Set the submodule given by `target` if it exists, otherwise throw an error.  
`share_memory`() | See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").  
`state_dict`(*args[,Â destination,Â prefix,Â ...]) | Return a dictionary containing references to the whole state of the module.  
`to`(*args,Â **kwargs) | Move and/or cast the parameters and buffers.  
`to_empty`(*,Â device[,Â recurse]) | Move the parameters and buffers to the specified device without copying storage.  
`train`([mode]) | Set the module in training mode.  
`type`(dst_type) | Casts all parameters and buffers to `dst_type`.  
`xpu`([device]) | Move all model parameters and buffers to the XPU.  
`zero_grad`([set_to_none]) | Reset gradients of all model parameters.  
  
T_destination = ~T_destination#
    

add_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Parameters:
    

  * **name** (_str_) â name of the child module. The child module can be accessed from this module using the given name

  * **module** (_Module_) â child module to be added to the module.




apply(_fn : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")], None]_) → Self#
    

Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.

Typical use includes initializing the parameters of a model (see also [torch.nn.init](https://docs.pytorch.org/docs/stable/nn.init.html#nn-init-doc "\(in PyTorch v2.12\)")).

Parameters:
    

**fn** (`Module` -> None) â function to be applied to each submodule

Returns:
    

self

Return type:
    

Module

Example:
    
    
    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    

bfloat16() → Self#
    

Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

buffers(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]#
    

Return an iterator over module buffers.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module.

Yields:
    

_torch.Tensor_ â module buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

call_super_init: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

children() → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over immediate children modules.

Yields:
    

_Module_ â a child module

compile(_* args_, _** kwargs_) → None#
    

Compile this Moduleâs forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

This Moduleâs `__call__` method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "\(in PyTorch v2.12\)") for details on the arguments for this function.

cpu() → Self#
    

Move all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

cuda(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

double() → Self#
    

Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

dump_patches: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

eval() → Self#
    

Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e. whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "\(in PyTorch v2.12\)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.eval()` and several similar mechanisms that may be confused with it.

Returns:
    

self

Return type:
    

Module

extra_repr()#
    

Return the extra representation of the module.

To print customized extra information, you should re-implement this method in your own modules. Both single-line and multi-line strings are acceptable.

float() → Self#
    

Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

forward(_input : [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")_) → [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")#
    

Define the computation performed at every call.

Should be overridden by all subclasses.

Note

Although the recipe for forward pass needs to be defined within this function, one should call the `Module` instance afterwards instead of this since the former takes care of running the registered hooks while the latter silently ignores them.

get_buffer(_target : str_) → [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")#
    

Return the buffer given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the buffer to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The buffer referenced by `target`

Return type:
    

[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not a buffer

get_extra_state() → Any#
    

Return any extra state to include in the moduleâs state_dict.

Implement this and a corresponding `set_extra_state()` for your module if you need to store extra state. This function is called when building the moduleâs `state_dict()`.

Note that extra state should be picklable to ensure working serialization of the state_dict. We only provide backwards compatibility guarantees for serializing Tensors; other objects may break backwards compatibility if their serialized pickled form changes.

Returns:
    

Any extra state to store in the moduleâs state_dict

Return type:
    

object

get_parameter(_target : str_) → [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")#
    

Return the parameter given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this methodâs functionality as well as how to correctly specify `target`.

Parameters:
    

**target** â The fully-qualified string name of the Parameter to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:
    

The Parameter referenced by `target`

Return type:
    

torch.nn.Parameter

Raises:
    

**AttributeError** â If the target string references an invalid path or resolves to something that is not an `nn.Parameter`

get_submodule(_target : str_) → [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")#
    

Return the submodule given by `target` if it exists, otherwise throw an error.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` which has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To check whether or not we have the `linear` submodule, we would call `get_submodule("net_b.linear")`. To check whether we have the `conv` submodule, we would call `get_submodule("net_b.net_c.conv")`.

The runtime of `get_submodule` is bounded by the degree of module nesting in `target`. A query against `named_modules` achieves the same result, but it is O(N) in the number of transitive modules. So, for a simple check to see if some submodule exists, `get_submodule` should always be used.

Parameters:
    

**target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

Returns:
    

The submodule referenced by `target`

Return type:
    

[torch.nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

Raises:
    

**AttributeError** â If at any point along the path resulting from the target string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.

half() → Self#
    

Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
    

self

Return type:
    

Module

ipu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on IPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

load_state_dict(_state_dict : Mapping[str, Any]_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _assign : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

Copy parameters and buffers from `state_dict` into this module and its descendants.

If `strict` is `True`, then the keys of `state_dict` must exactly match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function.

Warning

If `assign` is `True` the optimizer must be created after the call to `load_state_dict` unless [`get_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/stable/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "\(in PyTorch v2.12\)") is `True`.

Parameters:
    

  * **state_dict** (_dict_) â a dict containing parameters and persistent buffers.

  * **strict** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to strictly enforce that the keys in `state_dict` match the keys returned by this moduleâs [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") function. Default: `True`

  * **assign** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â When set to `False`, the properties of the tensors in the current module are preserved whereas setting it to `True` preserves properties of the Tensors in the state dict. The only exception is the `requires_grad` field of `Parameter` for which the value from the module is preserved. Default: `False`



Returns:
    

  * `missing_keys` is a list of str containing any keys that are expected
    

by this module but missing from the provided `state_dict`.

  * `unexpected_keys` is a list of str containing the keys that are not
    

expected by this module but present in the provided `state_dict`.




Return type:
    

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

Note

If a parameter or buffer is registered as `None` and its corresponding key exists in `state_dict`, `load_state_dict()` will raise a `RuntimeError`.

modules(_remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]#
    

Return an iterator over all modules in the network.

Parameters:
    

**remove_duplicate** â whether to remove the duplicated module instances in the result or not.

Yields:
    

_Module_ â a module in the network

Note

Duplicate modules are returned only once by default. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)
    
    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)
    

mtia(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on MTIA while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

named_buffers(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all buffer names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module. Defaults to True.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated buffers in the result. Defaults to True.



Yields:
    

_(str, torch.Tensor)_ â Tuple containing the name and buffer

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())
    

named_children() → Iterator[tuple[str, [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")]]#
    

Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    

_(str, Module)_ â Tuple containing a name and child module

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)
    

named_modules(_memo : set[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")] | None = None_, _prefix : str = ''_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_)#
    

Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Parameters:
    

  * **memo** â a memo to store the set of modules already added to the result

  * **prefix** â a prefix that will be added to the name of the module

  * **remove_duplicate** â whether to remove the duplicated module instances in the result or not



Yields:
    

_(str, Module)_ â Tuple of name and module

Note

Duplicate modules are returned only once. In the following example, `l` will be returned only once.

Example:
    
    
    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)
    
    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))
    

named_parameters(_prefix : str = ''_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _remove_duplicate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[tuple[str, [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]]#
    

Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Parameters:
    

  * **prefix** (_str_) â prefix to prepend to all parameter names.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

  * **remove_duplicate** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â whether to remove the duplicated parameters in the result. Defaults to True.



Yields:
    

_(str, Parameter)_ â Tuple containing the name and parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())
    

parameters(_recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[[Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)")]#
    

Return an iterator over module parameters.

This is typically passed to an optimizer.

Parameters:
    

**recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

Yields:
    

_Parameter_ â module parameter

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)
    

register_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_) → RemovableHandle#
    

Register a backward hook on the module.

This function is deprecated in favor of [`register_full_backward_hook()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "\(in PyTorch v2.12\)") and the behavior of this function will change in future versions.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_buffer(_name : str_, _tensor : [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None_, _persistent : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Add a buffer to the module.

This is typically used to register a buffer that should not be considered a model parameter. For example, BatchNormâs `running_mean` is not a parameter, but is part of the moduleâs state. Buffers, by default, are persistent and will be saved alongside parameters. This behavior can be changed by setting `persistent` to `False`. The only difference between a persistent buffer and a non-persistent buffer is that the latter will not be a part of this moduleâs `state_dict`.

Buffers can be accessed as attributes using given names.

Parameters:
    

  * **name** (_str_) â name of the buffer. The buffer can be accessed from this module using the given name

  * **tensor** (_Tensor_ _or_ _None_) â buffer to be registered. If `None`, then operations that run on buffers, such as `cuda`, are ignored. If `None`, the buffer is **not** included in the moduleâs `state_dict`.

  * **persistent** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether the buffer is part of this moduleâs `state_dict`.




Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))
    

register_forward_hook(_hook : Callable[[T, tuple[Any, ...], Any], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any], Any], Any | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _always_call : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward hook on the module.

The hook will be called every time after `forward()` has computed an output.

If `with_kwargs` is `False` or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the output. It can modify the input inplace but it will not have effect on forward since this is called after `forward()` is called. The hook should have the following signature:
    
    
    hook(module, args, output) -> None or modified output
    

If `with_kwargs` is `True`, the forward hook will be passed the `kwargs` given to the forward function and be expected to return the output possibly modified. The hook should have the following signature:
    
    
    hook(module, args, kwargs, output) -> None or modified output
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the provided `hook` will be fired before all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward` hooks registered with `register_module_forward_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True`, the `hook` will be passed the kwargs given to the forward function. Default: `False`

  * **always_call** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If `True` the `hook` will be run regardless of whether an exception is raised while calling the Module. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_forward_pre_hook(_hook : Callable[[T, tuple[Any, ...]], Any | None] | Callable[[T, tuple[Any, ...], dict[str, Any]], tuple[Any, dict[str, Any]] | None]_, _*_ , _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _with_kwargs : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a forward pre-hook on the module.

The hook will be called every time before `forward()` is invoked.

If `with_kwargs` is false or not specified, the input contains only the positional arguments given to the module. Keyword arguments wonât be passed to the hooks and only to the `forward`. The hook can modify the input. User can either return a tuple or a single modified value in the hook. We will wrap the value into a tuple if a single value is returned (unless that value is already a tuple). The hook should have the following signature:
    
    
    hook(module, args) -> None or modified input
    

If `with_kwargs` is true, the forward pre-hook will be passed the kwargs given to the forward function. And if the hook modifies the input, both the args and kwargs should be returned. The hook should have the following signature:
    
    
    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs
    

Parameters:
    

  * **hook** (_Callable_) â The user defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `forward_pre` hooks registered with `register_module_forward_pre_hook()` will fire before all hooks registered by this method. Default: `False`

  * **with_kwargs** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the `hook` will be passed the kwargs given to the forward function. Default: `False`



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

>   1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
> 
>   2. If none of the module inputs require gradients, the hook will fire when the gradients are computed with respect to module outputs.
> 
>   3. If none of the module outputs require gradients, then the hooks will not fire.
> 
> 


The hook should have the following signature:
    
    
    hook(module, grad_input, grad_output) -> tuple(Tensor) or None
    

The `grad_input` and `grad_output` are tuples that contain the gradients with respect to the inputs and outputs respectively. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the input that will be used in place of `grad_input` in subsequent computations. `grad_input` will only correspond to the inputs given as positional arguments and all kwarg arguments are ignored. Entries in `grad_input` and `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs or outputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward` hooks registered with `register_module_full_backward_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_full_backward_pre_hook(_hook : Callable[[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"), tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")], tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)"), ...] | [Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") | None]_, _prepend : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → RemovableHandle#
    

Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed. The hook should have the following signature:
    
    
    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None
    

The `grad_output` is a tuple. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the output that will be used in place of `grad_output` in subsequent computations. Entries in `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Moduleâs forward function.

Warning

Modifying inputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:
    

  * **hook** (_Callable_) â The user-defined hook to be registered.

  * **prepend** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â If true, the provided `hook` will be fired before all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Otherwise, the provided `hook` will be fired after all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)"). Note that global `backward_pre` hooks registered with `register_module_full_backward_pre_hook()` will fire before all hooks registered by this method.



Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_post_hook(_hook_)#
    

Register a post-hook to be run after moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, incompatible_keys) -> None

The `module` argument is the current module that this hook is registered on, and the `incompatible_keys` argument is a `NamedTuple` consisting of attributes `missing_keys` and `unexpected_keys`. `missing_keys` is a `list` of `str` containing the missing keys and `unexpected_keys` is a `list` of `str` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling `load_state_dict()` with `strict=True` are affected by modifications the hook makes to `missing_keys` or `unexpected_keys`, as expected. Additions to either set of keys will result in an error being thrown when `strict=True`, and clearing out both missing and unexpected keys will avoid an error.

Returns:
    

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:
    

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_pre_hook(_hook_)#
    

Register a pre-hook to be run before moduleâs `load_state_dict()` is called.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None # noqa: B950

Parameters:
    

**hook** (_Callable_) â Callable hook that will be invoked before loading the state dict.

register_module(_name : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") | None_) → None#
    

Alias for `add_module()`.

register_parameter(_name : str_, _param : [Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "\(in PyTorch v2.12\)") | None_) → None#
    

Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Parameters:
    

  * **name** (_str_) â name of the parameter. The parameter can be accessed from this module using the given name

  * **param** (_Parameter_ _or_ _None_) â parameter to be added to the module. If `None`, then operations that run on parameters, such as `cuda`, are ignored. If `None`, the parameter is **not** included in the moduleâs `state_dict`.




register_state_dict_post_hook(_hook_)#
    

Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the `state_dict` inplace.

register_state_dict_pre_hook(_hook_)#
    

Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict "\(in PyTorch v2.12\)") method.

It should have the following signature::
    

hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the `state_dict` call is made.

requires_grad_(_requires_grad : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Change if autograd should record operations on parameters in this module.

This method sets the parametersâ `requires_grad` attributes in-place.

This method is helpful for freezing part of the module for finetuning or training parts of a model individually (e.g., GAN training).

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "\(in PyTorch v2.12\)") for a comparison between `.requires_grad_()` and several similar mechanisms that may be confused with it.

Parameters:
    

**requires_grad** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether autograd should record operations on parameters in this module. Default: `True`.

Returns:
    

self

Return type:
    

Module

reset_parameters() → None#
    

reset_running_stats() → None#
    

set_extra_state(_state : Any_) → None#
    

Set extra state contained in the loaded `state_dict`.

This function is called from `load_state_dict()` to handle any extra state found within the `state_dict`. Implement this function and a corresponding `get_extra_state()` for your module if you need to store extra state within its `state_dict`.

Parameters:
    

**state** (_dict_) â Extra state from the `state_dict`

set_submodule(_target : str_, _module : [Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")_, _strict : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Set the submodule given by `target` if it exists, otherwise throw an error.

Note

If `strict` is set to `False` (default), the method will replace an existing submodule or create a new submodule if the parent module exists. If `strict` is set to `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule does not exist.

For example, letâs say you have an `nn.Module` `A` that looks like this:
    
    
    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )
    

(The diagram shows an `nn.Module` `A`. `A` has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To override the `Conv2d` with a new submodule `Linear`, you could call `set_submodule("net_b.net_c.conv", nn.Linear(1, 1))` where `strict` could be `True` or `False`

To add a new submodule `Conv2d` to the existing `net_b` module, you would call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))`.

In the above if you set `strict=True` and call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)`, an AttributeError will be raised because `net_b` does not have a submodule named `conv`.

Parameters:
    

  * **target** â The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

  * **module** â The module to set the submodule to.

  * **strict** â If `False`, the method will replace an existing submodule or create a new submodule if the parent module exists. If `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule doesnât already exist.



Raises:
    

  * **ValueError** â If the `target` string is empty or if `module` is not an instance of `nn.Module`.

  * **AttributeError** â If at any point along the path resulting from the `target` string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.




share_memory() → Self#
    

See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "\(in PyTorch v2.12\)").

state_dict(_* args_, _destination =None_, _prefix =''_, _keep_vars =False_)#
    

Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are included. Keys are corresponding parameter and buffer names. Parameters and buffers set to `None` are not included.

Note

The returned object is a shallow copy. It contains references to the moduleâs parameters and buffers.

Warning

Currently `state_dict()` also accepts positional arguments for `destination`, `prefix` and `keep_vars` in order. However, this is being deprecated and keyword arguments will be enforced in future releases.

Warning

Please avoid the use of argument `destination` as it is not designed for end-users.

Parameters:
    

  * **destination** (_dict_ _,__optional_) â If provided, the state of module will be updated into the dict and the same object is returned. Otherwise, an `OrderedDict` will be created and returned. Default: `None`.

  * **prefix** (_str_ _,__optional_) â a prefix added to parameter and buffer names to compose the keys in state_dict. Default: `''`.

  * **keep_vars** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â by default the [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)") s returned in the state dict are detached from autograd. If itâs set to `True`, detaching will not be performed. Default: `False`.



Returns:
    

a dictionary containing a whole state of the module

Return type:
    

dict

Example:
    
    
    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']
    

to(_* args_, _** kwargs_)#
    

Move and/or cast the parameters and buffers.

This can be called as

to(_device =None_, _dtype =None_, _non_blocking =False_)
    

to(_dtype_ , _non_blocking =False_)
    

to(_tensor_ , _non_blocking =False_)
    

to(_memory_format =torch.channels_last_)
    

Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "\(in PyTorch v2.12\)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â the desired device of the parameters and buffers in this module

  * **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)")) â the desired floating point or complex dtype of the parameters and buffers in this module

  * **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "\(in PyTorch v2.12\)")) â Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

  * **memory_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "\(in PyTorch v2.12\)")) â the desired memory format for 4D parameters and buffers in this module (keyword only argument)



Returns:
    

self

Return type:
    

Module

Examples:
    
    
    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)
    
    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)
    

to_empty(_*_ , _device : str | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | int | None_, _recurse : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Move the parameters and buffers to the specified device without copying storage.

Parameters:
    

  * **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)")) â The desired device of the parameters and buffers in this module.

  * **recurse** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â Whether parameters and buffers of submodules should be recursively moved to the specified device.



Returns:
    

self

Return type:
    

Module

train(_mode : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Self#
    

Set the module in training mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e., whether they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
    

**mode** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
    

self

Return type:
    

Module

type(_dst_type : [dtype](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "\(in PyTorch v2.12\)") | str_) → Self#
    

Casts all parameters and buffers to `dst_type`.

Note

This method modifies the module in-place.

Parameters:
    

**dst_type** ([_type_](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.type") _or_ _string_) â the desired type

Returns:
    

self

Return type:
    

Module

xpu(_device : int | [device](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "\(in PyTorch v2.12\)") | None = None_) → Self#
    

Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on XPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
    

**device** (_int_ _,__optional_) â if specified, all parameters will be copied to that device

Returns:
    

self

Return type:
    

Module

zero_grad(_set_to_none : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → None#
    

Reset gradients of all model parameters.

See similar function under [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "\(in PyTorch v2.12\)") for more context.

Parameters:
    

**set_to_none** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")) â instead of setting to zero, set the grads to None. See [`torch.optim.Optimizer.zero_grad()`](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "\(in PyTorch v2.12\)") for details.

num_features: int#
    

eps: float#
    

momentum: float | None#
    

affine: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

track_running_stats: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

running_mean: Tensor | None#
    

running_var: Tensor | None#
    

num_batches_tracked: Tensor | None#
    

training: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

fiftyone.brain.internal.models.simple_resnet.conv_bn(_c_in_ , _c_out_)#
    

fiftyone.brain.internal.models.simple_resnet.residual(_c_)#
    

fiftyone.brain.internal.models.simple_resnet.path_iter(_nested_dict_ , _pfx =()_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
