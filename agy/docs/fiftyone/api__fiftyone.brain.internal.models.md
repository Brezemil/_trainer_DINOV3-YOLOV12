---
source_url: https://docs.voxel51.com/api/fiftyone.brain.internal.models.html
---

# fiftyone.brain.internal.models#

  * [fiftyone.brain.internal.models.simple_resnet](api__fiftyone.brain.internal.models.simple_resnet.md)
    * [`simple_resnet()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.simple_resnet)
    * [`Network`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network)
      * [`Network.nodes()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.nodes)
      * [`Network.forward()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.forward)
      * [`Network.half()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.half)
      * [`Network.T_destination`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.T_destination)
      * [`Network.add_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.add_module)
      * [`Network.apply()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.apply)
      * [`Network.bfloat16()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.bfloat16)
      * [`Network.buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.buffers)
      * [`Network.call_super_init`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.call_super_init)
      * [`Network.children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.children)
      * [`Network.compile()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.compile)
      * [`Network.cpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.cpu)
      * [`Network.cuda()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.cuda)
      * [`Network.double()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.double)
      * [`Network.dump_patches`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.dump_patches)
      * [`Network.eval()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.eval)
      * [`Network.extra_repr()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.extra_repr)
      * [`Network.float()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.float)
      * [`Network.get_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.get_buffer)
      * [`Network.get_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.get_extra_state)
      * [`Network.get_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.get_parameter)
      * [`Network.get_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.get_submodule)
      * [`Network.ipu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.ipu)
      * [`Network.load_state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.load_state_dict)
      * [`Network.modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.modules)
      * [`Network.mtia()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.mtia)
      * [`Network.named_buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.named_buffers)
      * [`Network.named_children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.named_children)
      * [`Network.named_modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.named_modules)
      * [`Network.named_parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.named_parameters)
      * [`Network.parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.parameters)
      * [`Network.register_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_backward_hook)
      * [`Network.register_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_buffer)
      * [`Network.register_forward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_forward_hook)
      * [`Network.register_forward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_forward_pre_hook)
      * [`Network.register_full_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_full_backward_hook)
      * [`Network.register_full_backward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_full_backward_pre_hook)
      * [`Network.register_load_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_load_state_dict_post_hook)
      * [`Network.register_load_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_load_state_dict_pre_hook)
      * [`Network.register_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_module)
      * [`Network.register_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_parameter)
      * [`Network.register_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_state_dict_post_hook)
      * [`Network.register_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.register_state_dict_pre_hook)
      * [`Network.requires_grad_()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.requires_grad_)
      * [`Network.set_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.set_extra_state)
      * [`Network.set_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.set_submodule)
      * [`Network.share_memory()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.share_memory)
      * [`Network.state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.state_dict)
      * [`Network.to()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.to)
      * [`Network.to_empty()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.to_empty)
      * [`Network.train()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.train)
      * [`Network.type()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.type)
      * [`Network.xpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.xpu)
      * [`Network.zero_grad()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.zero_grad)
      * [`Network.training`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Network.training)
    * [`has_inputs()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.has_inputs)
    * [`build_graph()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.build_graph)
    * [`pipeline()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.pipeline)
    * [`Crop`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop)
      * [`Crop.options()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop.options)
      * [`Crop.output_shape()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop.output_shape)
      * [`Crop.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop.count)
      * [`Crop.h`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop.h)
      * [`Crop.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop.index)
      * [`Crop.w`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Crop.w)
    * [`FlipLR`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.FlipLR)
      * [`FlipLR.options()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.FlipLR.options)
      * [`FlipLR.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.FlipLR.count)
      * [`FlipLR.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.FlipLR.index)
    * [`Cutout`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Cutout)
      * [`Cutout.options()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Cutout.options)
      * [`Cutout.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Cutout.count)
      * [`Cutout.h`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Cutout.h)
      * [`Cutout.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Cutout.index)
      * [`Cutout.w`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Cutout.w)
    * [`PiecewiseLinear`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.PiecewiseLinear)
      * [`PiecewiseLinear.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.PiecewiseLinear.count)
      * [`PiecewiseLinear.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.PiecewiseLinear.index)
      * [`PiecewiseLinear.knots`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.PiecewiseLinear.knots)
      * [`PiecewiseLinear.vals`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.PiecewiseLinear.vals)
    * [`Const`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Const)
      * [`Const.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Const.count)
      * [`Const.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Const.index)
      * [`Const.val`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Const.val)
    * [`Identity`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Identity)
      * [`Identity.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Identity.count)
      * [`Identity.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Identity.index)
    * [`Add`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Add)
      * [`Add.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Add.count)
      * [`Add.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Add.index)
    * [`AddWeighted`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.AddWeighted)
      * [`AddWeighted.count()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.AddWeighted.count)
      * [`AddWeighted.index()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.AddWeighted.index)
      * [`AddWeighted.wx`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.AddWeighted.wx)
      * [`AddWeighted.wy`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.AddWeighted.wy)
    * [`Mul`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul)
      * [`Mul.T_destination`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.T_destination)
      * [`Mul.add_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.add_module)
      * [`Mul.apply()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.apply)
      * [`Mul.bfloat16()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.bfloat16)
      * [`Mul.buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.buffers)
      * [`Mul.call_super_init`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.call_super_init)
      * [`Mul.children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.children)
      * [`Mul.compile()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.compile)
      * [`Mul.cpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.cpu)
      * [`Mul.cuda()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.cuda)
      * [`Mul.double()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.double)
      * [`Mul.dump_patches`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.dump_patches)
      * [`Mul.eval()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.eval)
      * [`Mul.extra_repr()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.extra_repr)
      * [`Mul.float()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.float)
      * [`Mul.forward()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.forward)
      * [`Mul.get_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.get_buffer)
      * [`Mul.get_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.get_extra_state)
      * [`Mul.get_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.get_parameter)
      * [`Mul.get_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.get_submodule)
      * [`Mul.half()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.half)
      * [`Mul.ipu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.ipu)
      * [`Mul.load_state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.load_state_dict)
      * [`Mul.modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.modules)
      * [`Mul.mtia()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.mtia)
      * [`Mul.named_buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.named_buffers)
      * [`Mul.named_children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.named_children)
      * [`Mul.named_modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.named_modules)
      * [`Mul.named_parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.named_parameters)
      * [`Mul.parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.parameters)
      * [`Mul.register_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_backward_hook)
      * [`Mul.register_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_buffer)
      * [`Mul.register_forward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_forward_hook)
      * [`Mul.register_forward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_forward_pre_hook)
      * [`Mul.register_full_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_full_backward_hook)
      * [`Mul.register_full_backward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_full_backward_pre_hook)
      * [`Mul.register_load_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_load_state_dict_post_hook)
      * [`Mul.register_load_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_load_state_dict_pre_hook)
      * [`Mul.register_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_module)
      * [`Mul.register_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_parameter)
      * [`Mul.register_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_state_dict_post_hook)
      * [`Mul.register_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.register_state_dict_pre_hook)
      * [`Mul.requires_grad_()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.requires_grad_)
      * [`Mul.set_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.set_extra_state)
      * [`Mul.set_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.set_submodule)
      * [`Mul.share_memory()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.share_memory)
      * [`Mul.state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.state_dict)
      * [`Mul.to()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.to)
      * [`Mul.to_empty()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.to_empty)
      * [`Mul.train()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.train)
      * [`Mul.type()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.type)
      * [`Mul.xpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.xpu)
      * [`Mul.zero_grad()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.zero_grad)
      * [`Mul.training`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Mul.training)
    * [`Flatten`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten)
      * [`Flatten.forward()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.forward)
      * [`Flatten.T_destination`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.T_destination)
      * [`Flatten.add_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.add_module)
      * [`Flatten.apply()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.apply)
      * [`Flatten.bfloat16()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.bfloat16)
      * [`Flatten.buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.buffers)
      * [`Flatten.call_super_init`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.call_super_init)
      * [`Flatten.children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.children)
      * [`Flatten.compile()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.compile)
      * [`Flatten.cpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.cpu)
      * [`Flatten.cuda()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.cuda)
      * [`Flatten.double()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.double)
      * [`Flatten.dump_patches`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.dump_patches)
      * [`Flatten.eval()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.eval)
      * [`Flatten.extra_repr()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.extra_repr)
      * [`Flatten.float()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.float)
      * [`Flatten.get_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.get_buffer)
      * [`Flatten.get_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.get_extra_state)
      * [`Flatten.get_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.get_parameter)
      * [`Flatten.get_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.get_submodule)
      * [`Flatten.half()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.half)
      * [`Flatten.ipu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.ipu)
      * [`Flatten.load_state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.load_state_dict)
      * [`Flatten.modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.modules)
      * [`Flatten.mtia()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.mtia)
      * [`Flatten.named_buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.named_buffers)
      * [`Flatten.named_children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.named_children)
      * [`Flatten.named_modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.named_modules)
      * [`Flatten.named_parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.named_parameters)
      * [`Flatten.parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.parameters)
      * [`Flatten.register_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_backward_hook)
      * [`Flatten.register_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_buffer)
      * [`Flatten.register_forward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_forward_hook)
      * [`Flatten.register_forward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_forward_pre_hook)
      * [`Flatten.register_full_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_full_backward_hook)
      * [`Flatten.register_full_backward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_full_backward_pre_hook)
      * [`Flatten.register_load_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_load_state_dict_post_hook)
      * [`Flatten.register_load_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_load_state_dict_pre_hook)
      * [`Flatten.register_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_module)
      * [`Flatten.register_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_parameter)
      * [`Flatten.register_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_state_dict_post_hook)
      * [`Flatten.register_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.register_state_dict_pre_hook)
      * [`Flatten.requires_grad_()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.requires_grad_)
      * [`Flatten.set_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.set_extra_state)
      * [`Flatten.set_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.set_submodule)
      * [`Flatten.share_memory()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.share_memory)
      * [`Flatten.state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.state_dict)
      * [`Flatten.to()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.to)
      * [`Flatten.to_empty()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.to_empty)
      * [`Flatten.train()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.train)
      * [`Flatten.type()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.type)
      * [`Flatten.xpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.xpu)
      * [`Flatten.zero_grad()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.zero_grad)
      * [`Flatten.training`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Flatten.training)
    * [`Concat`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat)
      * [`Concat.forward()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.forward)
      * [`Concat.T_destination`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.T_destination)
      * [`Concat.add_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.add_module)
      * [`Concat.apply()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.apply)
      * [`Concat.bfloat16()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.bfloat16)
      * [`Concat.buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.buffers)
      * [`Concat.call_super_init`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.call_super_init)
      * [`Concat.children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.children)
      * [`Concat.compile()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.compile)
      * [`Concat.cpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.cpu)
      * [`Concat.cuda()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.cuda)
      * [`Concat.double()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.double)
      * [`Concat.dump_patches`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.dump_patches)
      * [`Concat.eval()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.eval)
      * [`Concat.extra_repr()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.extra_repr)
      * [`Concat.float()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.float)
      * [`Concat.get_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.get_buffer)
      * [`Concat.get_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.get_extra_state)
      * [`Concat.get_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.get_parameter)
      * [`Concat.get_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.get_submodule)
      * [`Concat.half()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.half)
      * [`Concat.ipu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.ipu)
      * [`Concat.load_state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.load_state_dict)
      * [`Concat.modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.modules)
      * [`Concat.mtia()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.mtia)
      * [`Concat.named_buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.named_buffers)
      * [`Concat.named_children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.named_children)
      * [`Concat.named_modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.named_modules)
      * [`Concat.named_parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.named_parameters)
      * [`Concat.parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.parameters)
      * [`Concat.register_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_backward_hook)
      * [`Concat.register_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_buffer)
      * [`Concat.register_forward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_forward_hook)
      * [`Concat.register_forward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_forward_pre_hook)
      * [`Concat.register_full_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_full_backward_hook)
      * [`Concat.register_full_backward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_full_backward_pre_hook)
      * [`Concat.register_load_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_load_state_dict_post_hook)
      * [`Concat.register_load_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_load_state_dict_pre_hook)
      * [`Concat.register_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_module)
      * [`Concat.register_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_parameter)
      * [`Concat.register_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_state_dict_post_hook)
      * [`Concat.register_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.register_state_dict_pre_hook)
      * [`Concat.requires_grad_()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.requires_grad_)
      * [`Concat.set_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.set_extra_state)
      * [`Concat.set_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.set_submodule)
      * [`Concat.share_memory()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.share_memory)
      * [`Concat.state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.state_dict)
      * [`Concat.to()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.to)
      * [`Concat.to_empty()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.to_empty)
      * [`Concat.train()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.train)
      * [`Concat.type()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.type)
      * [`Concat.xpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.xpu)
      * [`Concat.zero_grad()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.zero_grad)
      * [`Concat.training`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.Concat.training)
    * [`BatchNorm`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm)
      * [`BatchNorm.T_destination`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.T_destination)
      * [`BatchNorm.add_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.add_module)
      * [`BatchNorm.apply()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.apply)
      * [`BatchNorm.bfloat16()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.bfloat16)
      * [`BatchNorm.buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.buffers)
      * [`BatchNorm.call_super_init`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.call_super_init)
      * [`BatchNorm.children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.children)
      * [`BatchNorm.compile()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.compile)
      * [`BatchNorm.cpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.cpu)
      * [`BatchNorm.cuda()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.cuda)
      * [`BatchNorm.double()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.double)
      * [`BatchNorm.dump_patches`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.dump_patches)
      * [`BatchNorm.eval()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.eval)
      * [`BatchNorm.extra_repr()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.extra_repr)
      * [`BatchNorm.float()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.float)
      * [`BatchNorm.forward()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.forward)
      * [`BatchNorm.get_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.get_buffer)
      * [`BatchNorm.get_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.get_extra_state)
      * [`BatchNorm.get_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.get_parameter)
      * [`BatchNorm.get_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.get_submodule)
      * [`BatchNorm.half()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.half)
      * [`BatchNorm.ipu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.ipu)
      * [`BatchNorm.load_state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.load_state_dict)
      * [`BatchNorm.modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.modules)
      * [`BatchNorm.mtia()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.mtia)
      * [`BatchNorm.named_buffers()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.named_buffers)
      * [`BatchNorm.named_children()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.named_children)
      * [`BatchNorm.named_modules()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.named_modules)
      * [`BatchNorm.named_parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.named_parameters)
      * [`BatchNorm.parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.parameters)
      * [`BatchNorm.register_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_backward_hook)
      * [`BatchNorm.register_buffer()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_buffer)
      * [`BatchNorm.register_forward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_forward_hook)
      * [`BatchNorm.register_forward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_forward_pre_hook)
      * [`BatchNorm.register_full_backward_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_full_backward_hook)
      * [`BatchNorm.register_full_backward_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_full_backward_pre_hook)
      * [`BatchNorm.register_load_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_load_state_dict_post_hook)
      * [`BatchNorm.register_load_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_load_state_dict_pre_hook)
      * [`BatchNorm.register_module()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_module)
      * [`BatchNorm.register_parameter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_parameter)
      * [`BatchNorm.register_state_dict_post_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_state_dict_post_hook)
      * [`BatchNorm.register_state_dict_pre_hook()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.register_state_dict_pre_hook)
      * [`BatchNorm.requires_grad_()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.requires_grad_)
      * [`BatchNorm.reset_parameters()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.reset_parameters)
      * [`BatchNorm.reset_running_stats()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.reset_running_stats)
      * [`BatchNorm.set_extra_state()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.set_extra_state)
      * [`BatchNorm.set_submodule()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.set_submodule)
      * [`BatchNorm.share_memory()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.share_memory)
      * [`BatchNorm.state_dict()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.state_dict)
      * [`BatchNorm.to()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.to)
      * [`BatchNorm.to_empty()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.to_empty)
      * [`BatchNorm.train()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.train)
      * [`BatchNorm.type()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.type)
      * [`BatchNorm.xpu()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.xpu)
      * [`BatchNorm.zero_grad()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.zero_grad)
      * [`BatchNorm.num_features`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.num_features)
      * [`BatchNorm.eps`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.eps)
      * [`BatchNorm.momentum`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.momentum)
      * [`BatchNorm.affine`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.affine)
      * [`BatchNorm.track_running_stats`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.track_running_stats)
      * [`BatchNorm.running_mean`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.running_mean)
      * [`BatchNorm.running_var`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.running_var)
      * [`BatchNorm.num_batches_tracked`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.num_batches_tracked)
      * [`BatchNorm.training`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.BatchNorm.training)
    * [`conv_bn()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.conv_bn)
    * [`residual()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.residual)
    * [`path_iter()`](api__fiftyone.brain.internal.models.simple_resnet.md#fiftyone.brain.internal.models.simple_resnet.path_iter)
  * [fiftyone.brain.internal.models.torch](api__fiftyone.brain.internal.models.torch.md)
    * [`TorchImageModelConfig`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig)
      * [`TorchImageModelConfig.attributes()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.attributes)
      * [`TorchImageModelConfig.builder()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.builder)
      * [`TorchImageModelConfig.copy()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.copy)
      * [`TorchImageModelConfig.custom_attributes()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.custom_attributes)
      * [`TorchImageModelConfig.default()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.default)
      * [`TorchImageModelConfig.download_model_if_necessary()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.download_model_if_necessary)
      * [`TorchImageModelConfig.from_dict()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.from_dict)
      * [`TorchImageModelConfig.from_json()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.from_json)
      * [`TorchImageModelConfig.from_kwargs()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.from_kwargs)
      * [`TorchImageModelConfig.from_str()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.from_str)
      * [`TorchImageModelConfig.get_class_name()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.get_class_name)
      * [`TorchImageModelConfig.init()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.init)
      * [`TorchImageModelConfig.load_default()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.load_default)
      * [`TorchImageModelConfig.parse_array()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_array)
      * [`TorchImageModelConfig.parse_bool()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_bool)
      * [`TorchImageModelConfig.parse_categorical()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_categorical)
      * [`TorchImageModelConfig.parse_dict()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_dict)
      * [`TorchImageModelConfig.parse_int()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_int)
      * [`TorchImageModelConfig.parse_mutually_exclusive_fields()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_mutually_exclusive_fields)
      * [`TorchImageModelConfig.parse_number()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_number)
      * [`TorchImageModelConfig.parse_object()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_object)
      * [`TorchImageModelConfig.parse_object_array()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_object_array)
      * [`TorchImageModelConfig.parse_object_dict()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_object_dict)
      * [`TorchImageModelConfig.parse_path()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_path)
      * [`TorchImageModelConfig.parse_raw()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_raw)
      * [`TorchImageModelConfig.parse_string()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.parse_string)
      * [`TorchImageModelConfig.serialize()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.serialize)
      * [`TorchImageModelConfig.to_str()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.to_str)
      * [`TorchImageModelConfig.validate_all_or_nothing_fields()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.validate_all_or_nothing_fields)
      * [`TorchImageModelConfig.write_json()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModelConfig.write_json)
    * [`TorchImageModel`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel)
      * [`TorchImageModel.build_get_item()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.build_get_item)
      * [`TorchImageModel.can_embed_prompts`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.can_embed_prompts)
      * [`TorchImageModel.classes`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.classes)
      * [`TorchImageModel.collate_fn()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.collate_fn)
      * [`TorchImageModel.device`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.device)
      * [`TorchImageModel.embed()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.embed)
      * [`TorchImageModel.embed_all()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.embed_all)
      * [`TorchImageModel.from_config()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.from_config)
      * [`TorchImageModel.from_dict()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.from_dict)
      * [`TorchImageModel.from_json()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.from_json)
      * [`TorchImageModel.from_kwargs()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.from_kwargs)
      * [`TorchImageModel.get_embeddings()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.get_embeddings)
      * [`TorchImageModel.has_collate_fn`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.has_collate_fn)
      * [`TorchImageModel.has_embeddings`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.has_embeddings)
      * [`TorchImageModel.has_logits`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.has_logits)
      * [`TorchImageModel.mask_targets`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.mask_targets)
      * [`TorchImageModel.media_type`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.media_type)
      * [`TorchImageModel.num_classes`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.num_classes)
      * [`TorchImageModel.parse()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.parse)
      * [`TorchImageModel.predict()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.predict)
      * [`TorchImageModel.predict_all()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.predict_all)
      * [`TorchImageModel.preprocess`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.preprocess)
      * [`TorchImageModel.ragged_batches`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.ragged_batches)
      * [`TorchImageModel.required_keys`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.required_keys)
      * [`TorchImageModel.skeleton`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.skeleton)
      * [`TorchImageModel.store_logits`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.store_logits)
      * [`TorchImageModel.transforms`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.transforms)
      * [`TorchImageModel.using_gpu`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.using_gpu)
      * [`TorchImageModel.using_half_precision`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.using_half_precision)
      * [`TorchImageModel.validate()`](api__fiftyone.brain.internal.models.torch.md#fiftyone.brain.internal.models.torch.TorchImageModel.validate)



## Module contents#

Brain models.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`list_models`() | Returns the list of available models.  
---|---  
`list_downloaded_models`() | Returns information about the models that have been downloaded.  
`is_model_downloaded`(name) | Determines whether the model of the given name is downloaded.  
`download_model`(name[,Â overwrite]) | Downloads the model of the given name.  
`install_model_requirements`(name[,Â error_level]) | Installs any package requirements for the model with the given name.  
`ensure_model_requirements`(name[,Â error_level]) | Ensures that the package requirements for the model with the given name are satisfied.  
`load_model`(name[,Â download_if_necessary,Â ...]) | Loads the model of the given name.  
`find_model`(name) | Returns the path to the model on disk.  
`get_model`(name) | Returns the `eta.core.models.Model` instance for the model with the given name.  
`delete_model`(name) | Deletes the model from local disk, if necessary.  
  
**Classes:**

`HasBrainModel`() | Mixin class for Config classes of [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instances whose models are stored privately by the FiftyOne Brain.  
---|---  
  
fiftyone.brain.internal.models.list_models()#
    

Returns the list of available models.

Returns:
    

a list of model names

fiftyone.brain.internal.models.list_downloaded_models()#
    

Returns information about the models that have been downloaded.

Returns:
    

a dict mapping model names to (model path, `eta.core.models.Model`) tuples

fiftyone.brain.internal.models.is_model_downloaded(_name_)#
    

Determines whether the model of the given name is downloaded.

Parameters:
    

**name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used

Returns:
    

True/False

fiftyone.brain.internal.models.download_model(_name_ , _overwrite =False_)#
    

Downloads the model of the given name.

If the model is already downloaded, it is not re-downloaded unless `overwrite == True` is specified.

Parameters:
    

  * **name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used. Call `list_models()` to see the available models

  * **overwrite** (_False_) â whether to overwrite any existing files



Returns:
    

tuple of

  * model: the `eta.core.models.Model` instance for the model

  * model_path: the path to the downloaded model on disk




fiftyone.brain.internal.models.install_model_requirements(_name_ , _error_level =0_)#
    

Installs any package requirements for the model with the given name.

Parameters:
    

  * **name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used. Call `list_models()` to see the available models

  * **error_level** â 

the error level to use, defined as:

0: raise error if a requirement install fails 1: log warning if a requirement install fails 2: ignore install fails




fiftyone.brain.internal.models.ensure_model_requirements(_name_ , _error_level =0_)#
    

Ensures that the package requirements for the model with the given name are satisfied.

Parameters:
    

  * **name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used. Call `list_models()` to see the available models

  * **error_level** â 

the error level to use, defined as:

0: raise error if a requirement is not satisfied 1: log warning if a requirement is not satisifed 2: ignore unsatisifed requirements




fiftyone.brain.internal.models.load_model(_name_ , _download_if_necessary =True_, _install_requirements =False_, _error_level =0_, _** kwargs_)#
    

Loads the model of the given name.

By default, the model will be downloaded if necessary.

Parameters:
    

  * **name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used. Call `list_models()` to see the available models

  * **download_if_necessary** (_True_) â whether to download the model if it is not found in the specified directory

  * **install_requirements** â whether to install any requirements before loading the model. By default, this is False

  * **error_level** â 

the error level to use, defined as:

0: raise error if a requirement is not satisfied 1: log warning if a requirement is not satisifed 2: ignore unsatisifed requirements

  * ****kwargs** â keyword arguments to inject into the modelâs `Config` instance



Returns:
    

a [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model")

fiftyone.brain.internal.models.find_model(_name_)#
    

Returns the path to the model on disk.

The model must be downloaded. Use `download_model()` to download models.

Parameters:
    

**name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used

Returns:
    

the path to the model on disk

Raises:
    

**ValueError** â if the model does not exist or has not been downloaded

fiftyone.brain.internal.models.get_model(_name_)#
    

Returns the `eta.core.models.Model` instance for the model with the given name.

Parameters:
    

**name** â the name of the model

Returnsn `eta.core.models.Model``ZooModel`

fiftyone.brain.internal.models.delete_model(_name_)#
    

Deletes the model from local disk, if necessary.

Parameters:
    

**name** â the name of the model, which can have `@<ver>` appended to refer to a specific version of the model. If no version is specified, the latest version of the model is used

class fiftyone.brain.internal.models.HasBrainModel#
    

Bases: `HasPublishedModel`

Mixin class for Config classes of [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instances whose models are stored privately by the FiftyOne Brain.

**Methods:**

`download_model_if_necessary`() | Downloads the published model specified by the config, if necessary.  
---|---  
`init`(d) | Initializes the published model config.  
  
download_model_if_necessary()#
    

Downloads the published model specified by the config, if necessary.

After this method is called, the `model_path` attribute will always contain the path to the model on disk.

init(_d_)#
    

Initializes the published model config.

This method should be called by `ModelConfig.__init__()`, and it performs the following tasks:

  * Parses the `model_name` and `model_path` parameters

  * Populates any default parameters in the provided ModelConfig dict




Parameters:
    

**d** â a ModelConfig dict

Returns:
    

a ModelConfig dict with any default parameters populated

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
