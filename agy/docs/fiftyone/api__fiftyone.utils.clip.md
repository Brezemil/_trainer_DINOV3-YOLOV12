---
source_url: https://docs.voxel51.com/api/fiftyone.utils.clip.html
---

# fiftyone.utils.clip#

  * [fiftyone.utils.clip.model](api__fiftyone.utils.clip.model.md)
    * [`Bottleneck`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck)
      * [`Bottleneck.expansion`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.expansion)
      * [`Bottleneck.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.forward)
      * [`Bottleneck.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.T_destination)
      * [`Bottleneck.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.add_module)
      * [`Bottleneck.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.apply)
      * [`Bottleneck.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.bfloat16)
      * [`Bottleneck.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.buffers)
      * [`Bottleneck.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.call_super_init)
      * [`Bottleneck.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.children)
      * [`Bottleneck.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.compile)
      * [`Bottleneck.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.cpu)
      * [`Bottleneck.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.cuda)
      * [`Bottleneck.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.double)
      * [`Bottleneck.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.dump_patches)
      * [`Bottleneck.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.eval)
      * [`Bottleneck.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.extra_repr)
      * [`Bottleneck.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.float)
      * [`Bottleneck.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.get_buffer)
      * [`Bottleneck.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.get_extra_state)
      * [`Bottleneck.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.get_parameter)
      * [`Bottleneck.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.get_submodule)
      * [`Bottleneck.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.half)
      * [`Bottleneck.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.ipu)
      * [`Bottleneck.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.load_state_dict)
      * [`Bottleneck.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.modules)
      * [`Bottleneck.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.mtia)
      * [`Bottleneck.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.named_buffers)
      * [`Bottleneck.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.named_children)
      * [`Bottleneck.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.named_modules)
      * [`Bottleneck.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.named_parameters)
      * [`Bottleneck.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.parameters)
      * [`Bottleneck.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_backward_hook)
      * [`Bottleneck.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_buffer)
      * [`Bottleneck.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_forward_hook)
      * [`Bottleneck.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_forward_pre_hook)
      * [`Bottleneck.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_full_backward_hook)
      * [`Bottleneck.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_full_backward_pre_hook)
      * [`Bottleneck.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_load_state_dict_post_hook)
      * [`Bottleneck.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_load_state_dict_pre_hook)
      * [`Bottleneck.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_module)
      * [`Bottleneck.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_parameter)
      * [`Bottleneck.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_state_dict_post_hook)
      * [`Bottleneck.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.register_state_dict_pre_hook)
      * [`Bottleneck.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.requires_grad_)
      * [`Bottleneck.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.set_extra_state)
      * [`Bottleneck.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.set_submodule)
      * [`Bottleneck.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.share_memory)
      * [`Bottleneck.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.state_dict)
      * [`Bottleneck.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.to)
      * [`Bottleneck.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.to_empty)
      * [`Bottleneck.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.train)
      * [`Bottleneck.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.type)
      * [`Bottleneck.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.xpu)
      * [`Bottleneck.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.zero_grad)
      * [`Bottleneck.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Bottleneck.training)
    * [`AttentionPool2d`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d)
      * [`AttentionPool2d.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.forward)
      * [`AttentionPool2d.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.T_destination)
      * [`AttentionPool2d.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.add_module)
      * [`AttentionPool2d.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.apply)
      * [`AttentionPool2d.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.bfloat16)
      * [`AttentionPool2d.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.buffers)
      * [`AttentionPool2d.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.call_super_init)
      * [`AttentionPool2d.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.children)
      * [`AttentionPool2d.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.compile)
      * [`AttentionPool2d.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.cpu)
      * [`AttentionPool2d.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.cuda)
      * [`AttentionPool2d.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.double)
      * [`AttentionPool2d.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.dump_patches)
      * [`AttentionPool2d.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.eval)
      * [`AttentionPool2d.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.extra_repr)
      * [`AttentionPool2d.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.float)
      * [`AttentionPool2d.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.get_buffer)
      * [`AttentionPool2d.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.get_extra_state)
      * [`AttentionPool2d.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.get_parameter)
      * [`AttentionPool2d.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.get_submodule)
      * [`AttentionPool2d.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.half)
      * [`AttentionPool2d.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.ipu)
      * [`AttentionPool2d.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.load_state_dict)
      * [`AttentionPool2d.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.modules)
      * [`AttentionPool2d.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.mtia)
      * [`AttentionPool2d.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.named_buffers)
      * [`AttentionPool2d.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.named_children)
      * [`AttentionPool2d.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.named_modules)
      * [`AttentionPool2d.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.named_parameters)
      * [`AttentionPool2d.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.parameters)
      * [`AttentionPool2d.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_backward_hook)
      * [`AttentionPool2d.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_buffer)
      * [`AttentionPool2d.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_forward_hook)
      * [`AttentionPool2d.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_forward_pre_hook)
      * [`AttentionPool2d.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_full_backward_hook)
      * [`AttentionPool2d.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_full_backward_pre_hook)
      * [`AttentionPool2d.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_load_state_dict_post_hook)
      * [`AttentionPool2d.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_load_state_dict_pre_hook)
      * [`AttentionPool2d.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_module)
      * [`AttentionPool2d.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_parameter)
      * [`AttentionPool2d.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_state_dict_post_hook)
      * [`AttentionPool2d.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.register_state_dict_pre_hook)
      * [`AttentionPool2d.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.requires_grad_)
      * [`AttentionPool2d.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.set_extra_state)
      * [`AttentionPool2d.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.set_submodule)
      * [`AttentionPool2d.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.share_memory)
      * [`AttentionPool2d.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.state_dict)
      * [`AttentionPool2d.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.to)
      * [`AttentionPool2d.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.to_empty)
      * [`AttentionPool2d.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.train)
      * [`AttentionPool2d.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.type)
      * [`AttentionPool2d.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.xpu)
      * [`AttentionPool2d.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.zero_grad)
      * [`AttentionPool2d.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.AttentionPool2d.training)
    * [`ModifiedResNet`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet)
      * [`ModifiedResNet.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.forward)
      * [`ModifiedResNet.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.T_destination)
      * [`ModifiedResNet.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.add_module)
      * [`ModifiedResNet.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.apply)
      * [`ModifiedResNet.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.bfloat16)
      * [`ModifiedResNet.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.buffers)
      * [`ModifiedResNet.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.call_super_init)
      * [`ModifiedResNet.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.children)
      * [`ModifiedResNet.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.compile)
      * [`ModifiedResNet.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.cpu)
      * [`ModifiedResNet.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.cuda)
      * [`ModifiedResNet.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.double)
      * [`ModifiedResNet.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.dump_patches)
      * [`ModifiedResNet.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.eval)
      * [`ModifiedResNet.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.extra_repr)
      * [`ModifiedResNet.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.float)
      * [`ModifiedResNet.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.get_buffer)
      * [`ModifiedResNet.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.get_extra_state)
      * [`ModifiedResNet.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.get_parameter)
      * [`ModifiedResNet.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.get_submodule)
      * [`ModifiedResNet.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.half)
      * [`ModifiedResNet.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.ipu)
      * [`ModifiedResNet.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.load_state_dict)
      * [`ModifiedResNet.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.modules)
      * [`ModifiedResNet.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.mtia)
      * [`ModifiedResNet.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.named_buffers)
      * [`ModifiedResNet.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.named_children)
      * [`ModifiedResNet.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.named_modules)
      * [`ModifiedResNet.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.named_parameters)
      * [`ModifiedResNet.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.parameters)
      * [`ModifiedResNet.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_backward_hook)
      * [`ModifiedResNet.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_buffer)
      * [`ModifiedResNet.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_forward_hook)
      * [`ModifiedResNet.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_forward_pre_hook)
      * [`ModifiedResNet.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_full_backward_hook)
      * [`ModifiedResNet.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_full_backward_pre_hook)
      * [`ModifiedResNet.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_load_state_dict_post_hook)
      * [`ModifiedResNet.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_load_state_dict_pre_hook)
      * [`ModifiedResNet.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_module)
      * [`ModifiedResNet.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_parameter)
      * [`ModifiedResNet.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_state_dict_post_hook)
      * [`ModifiedResNet.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.register_state_dict_pre_hook)
      * [`ModifiedResNet.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.requires_grad_)
      * [`ModifiedResNet.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.set_extra_state)
      * [`ModifiedResNet.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.set_submodule)
      * [`ModifiedResNet.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.share_memory)
      * [`ModifiedResNet.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.state_dict)
      * [`ModifiedResNet.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.to)
      * [`ModifiedResNet.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.to_empty)
      * [`ModifiedResNet.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.train)
      * [`ModifiedResNet.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.type)
      * [`ModifiedResNet.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.xpu)
      * [`ModifiedResNet.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.zero_grad)
      * [`ModifiedResNet.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ModifiedResNet.training)
    * [`LayerNorm`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm)
      * [`LayerNorm.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.forward)
      * [`LayerNorm.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.T_destination)
      * [`LayerNorm.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.add_module)
      * [`LayerNorm.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.apply)
      * [`LayerNorm.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.bfloat16)
      * [`LayerNorm.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.buffers)
      * [`LayerNorm.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.call_super_init)
      * [`LayerNorm.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.children)
      * [`LayerNorm.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.compile)
      * [`LayerNorm.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.cpu)
      * [`LayerNorm.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.cuda)
      * [`LayerNorm.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.double)
      * [`LayerNorm.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.dump_patches)
      * [`LayerNorm.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.eval)
      * [`LayerNorm.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.extra_repr)
      * [`LayerNorm.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.float)
      * [`LayerNorm.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.get_buffer)
      * [`LayerNorm.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.get_extra_state)
      * [`LayerNorm.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.get_parameter)
      * [`LayerNorm.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.get_submodule)
      * [`LayerNorm.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.half)
      * [`LayerNorm.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.ipu)
      * [`LayerNorm.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.load_state_dict)
      * [`LayerNorm.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.modules)
      * [`LayerNorm.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.mtia)
      * [`LayerNorm.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.named_buffers)
      * [`LayerNorm.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.named_children)
      * [`LayerNorm.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.named_modules)
      * [`LayerNorm.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.named_parameters)
      * [`LayerNorm.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.parameters)
      * [`LayerNorm.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_backward_hook)
      * [`LayerNorm.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_buffer)
      * [`LayerNorm.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_forward_hook)
      * [`LayerNorm.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_forward_pre_hook)
      * [`LayerNorm.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_full_backward_hook)
      * [`LayerNorm.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_full_backward_pre_hook)
      * [`LayerNorm.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_load_state_dict_post_hook)
      * [`LayerNorm.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_load_state_dict_pre_hook)
      * [`LayerNorm.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_module)
      * [`LayerNorm.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_parameter)
      * [`LayerNorm.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_state_dict_post_hook)
      * [`LayerNorm.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.register_state_dict_pre_hook)
      * [`LayerNorm.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.requires_grad_)
      * [`LayerNorm.reset_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.reset_parameters)
      * [`LayerNorm.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.set_extra_state)
      * [`LayerNorm.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.set_submodule)
      * [`LayerNorm.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.share_memory)
      * [`LayerNorm.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.state_dict)
      * [`LayerNorm.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.to)
      * [`LayerNorm.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.to_empty)
      * [`LayerNorm.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.train)
      * [`LayerNorm.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.type)
      * [`LayerNorm.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.xpu)
      * [`LayerNorm.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.zero_grad)
      * [`LayerNorm.normalized_shape`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.normalized_shape)
      * [`LayerNorm.eps`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.eps)
      * [`LayerNorm.elementwise_affine`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.elementwise_affine)
      * [`LayerNorm.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.LayerNorm.training)
    * [`QuickGELU`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU)
      * [`QuickGELU.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.forward)
      * [`QuickGELU.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.T_destination)
      * [`QuickGELU.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.add_module)
      * [`QuickGELU.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.apply)
      * [`QuickGELU.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.bfloat16)
      * [`QuickGELU.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.buffers)
      * [`QuickGELU.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.call_super_init)
      * [`QuickGELU.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.children)
      * [`QuickGELU.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.compile)
      * [`QuickGELU.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.cpu)
      * [`QuickGELU.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.cuda)
      * [`QuickGELU.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.double)
      * [`QuickGELU.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.dump_patches)
      * [`QuickGELU.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.eval)
      * [`QuickGELU.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.extra_repr)
      * [`QuickGELU.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.float)
      * [`QuickGELU.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.get_buffer)
      * [`QuickGELU.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.get_extra_state)
      * [`QuickGELU.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.get_parameter)
      * [`QuickGELU.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.get_submodule)
      * [`QuickGELU.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.half)
      * [`QuickGELU.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.ipu)
      * [`QuickGELU.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.load_state_dict)
      * [`QuickGELU.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.modules)
      * [`QuickGELU.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.mtia)
      * [`QuickGELU.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.named_buffers)
      * [`QuickGELU.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.named_children)
      * [`QuickGELU.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.named_modules)
      * [`QuickGELU.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.named_parameters)
      * [`QuickGELU.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.parameters)
      * [`QuickGELU.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_backward_hook)
      * [`QuickGELU.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_buffer)
      * [`QuickGELU.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_forward_hook)
      * [`QuickGELU.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_forward_pre_hook)
      * [`QuickGELU.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_full_backward_hook)
      * [`QuickGELU.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_full_backward_pre_hook)
      * [`QuickGELU.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_load_state_dict_post_hook)
      * [`QuickGELU.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_load_state_dict_pre_hook)
      * [`QuickGELU.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_module)
      * [`QuickGELU.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_parameter)
      * [`QuickGELU.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_state_dict_post_hook)
      * [`QuickGELU.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.register_state_dict_pre_hook)
      * [`QuickGELU.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.requires_grad_)
      * [`QuickGELU.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.set_extra_state)
      * [`QuickGELU.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.set_submodule)
      * [`QuickGELU.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.share_memory)
      * [`QuickGELU.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.state_dict)
      * [`QuickGELU.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.to)
      * [`QuickGELU.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.to_empty)
      * [`QuickGELU.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.train)
      * [`QuickGELU.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.type)
      * [`QuickGELU.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.xpu)
      * [`QuickGELU.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.zero_grad)
      * [`QuickGELU.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.QuickGELU.training)
    * [`ResidualAttentionBlock`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock)
      * [`ResidualAttentionBlock.attention()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.attention)
      * [`ResidualAttentionBlock.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.forward)
      * [`ResidualAttentionBlock.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.T_destination)
      * [`ResidualAttentionBlock.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.add_module)
      * [`ResidualAttentionBlock.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.apply)
      * [`ResidualAttentionBlock.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.bfloat16)
      * [`ResidualAttentionBlock.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.buffers)
      * [`ResidualAttentionBlock.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.call_super_init)
      * [`ResidualAttentionBlock.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.children)
      * [`ResidualAttentionBlock.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.compile)
      * [`ResidualAttentionBlock.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.cpu)
      * [`ResidualAttentionBlock.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.cuda)
      * [`ResidualAttentionBlock.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.double)
      * [`ResidualAttentionBlock.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.dump_patches)
      * [`ResidualAttentionBlock.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.eval)
      * [`ResidualAttentionBlock.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.extra_repr)
      * [`ResidualAttentionBlock.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.float)
      * [`ResidualAttentionBlock.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.get_buffer)
      * [`ResidualAttentionBlock.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.get_extra_state)
      * [`ResidualAttentionBlock.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.get_parameter)
      * [`ResidualAttentionBlock.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.get_submodule)
      * [`ResidualAttentionBlock.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.half)
      * [`ResidualAttentionBlock.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.ipu)
      * [`ResidualAttentionBlock.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.load_state_dict)
      * [`ResidualAttentionBlock.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.modules)
      * [`ResidualAttentionBlock.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.mtia)
      * [`ResidualAttentionBlock.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.named_buffers)
      * [`ResidualAttentionBlock.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.named_children)
      * [`ResidualAttentionBlock.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.named_modules)
      * [`ResidualAttentionBlock.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.named_parameters)
      * [`ResidualAttentionBlock.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.parameters)
      * [`ResidualAttentionBlock.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_backward_hook)
      * [`ResidualAttentionBlock.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_buffer)
      * [`ResidualAttentionBlock.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_forward_hook)
      * [`ResidualAttentionBlock.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_forward_pre_hook)
      * [`ResidualAttentionBlock.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_full_backward_hook)
      * [`ResidualAttentionBlock.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_full_backward_pre_hook)
      * [`ResidualAttentionBlock.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_load_state_dict_post_hook)
      * [`ResidualAttentionBlock.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_load_state_dict_pre_hook)
      * [`ResidualAttentionBlock.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_module)
      * [`ResidualAttentionBlock.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_parameter)
      * [`ResidualAttentionBlock.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_state_dict_post_hook)
      * [`ResidualAttentionBlock.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.register_state_dict_pre_hook)
      * [`ResidualAttentionBlock.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.requires_grad_)
      * [`ResidualAttentionBlock.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.set_extra_state)
      * [`ResidualAttentionBlock.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.set_submodule)
      * [`ResidualAttentionBlock.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.share_memory)
      * [`ResidualAttentionBlock.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.state_dict)
      * [`ResidualAttentionBlock.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.to)
      * [`ResidualAttentionBlock.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.to_empty)
      * [`ResidualAttentionBlock.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.train)
      * [`ResidualAttentionBlock.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.type)
      * [`ResidualAttentionBlock.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.xpu)
      * [`ResidualAttentionBlock.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.zero_grad)
      * [`ResidualAttentionBlock.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.ResidualAttentionBlock.training)
    * [`Transformer`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer)
      * [`Transformer.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.forward)
      * [`Transformer.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.T_destination)
      * [`Transformer.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.add_module)
      * [`Transformer.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.apply)
      * [`Transformer.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.bfloat16)
      * [`Transformer.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.buffers)
      * [`Transformer.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.call_super_init)
      * [`Transformer.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.children)
      * [`Transformer.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.compile)
      * [`Transformer.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.cpu)
      * [`Transformer.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.cuda)
      * [`Transformer.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.double)
      * [`Transformer.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.dump_patches)
      * [`Transformer.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.eval)
      * [`Transformer.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.extra_repr)
      * [`Transformer.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.float)
      * [`Transformer.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.get_buffer)
      * [`Transformer.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.get_extra_state)
      * [`Transformer.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.get_parameter)
      * [`Transformer.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.get_submodule)
      * [`Transformer.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.half)
      * [`Transformer.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.ipu)
      * [`Transformer.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.load_state_dict)
      * [`Transformer.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.modules)
      * [`Transformer.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.mtia)
      * [`Transformer.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.named_buffers)
      * [`Transformer.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.named_children)
      * [`Transformer.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.named_modules)
      * [`Transformer.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.named_parameters)
      * [`Transformer.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.parameters)
      * [`Transformer.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_backward_hook)
      * [`Transformer.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_buffer)
      * [`Transformer.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_forward_hook)
      * [`Transformer.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_forward_pre_hook)
      * [`Transformer.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_full_backward_hook)
      * [`Transformer.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_full_backward_pre_hook)
      * [`Transformer.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_load_state_dict_post_hook)
      * [`Transformer.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_load_state_dict_pre_hook)
      * [`Transformer.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_module)
      * [`Transformer.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_parameter)
      * [`Transformer.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_state_dict_post_hook)
      * [`Transformer.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.register_state_dict_pre_hook)
      * [`Transformer.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.requires_grad_)
      * [`Transformer.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.set_extra_state)
      * [`Transformer.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.set_submodule)
      * [`Transformer.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.share_memory)
      * [`Transformer.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.state_dict)
      * [`Transformer.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.to)
      * [`Transformer.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.to_empty)
      * [`Transformer.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.train)
      * [`Transformer.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.type)
      * [`Transformer.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.xpu)
      * [`Transformer.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.zero_grad)
      * [`Transformer.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.Transformer.training)
    * [`VisionTransformer`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer)
      * [`VisionTransformer.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.forward)
      * [`VisionTransformer.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.T_destination)
      * [`VisionTransformer.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.add_module)
      * [`VisionTransformer.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.apply)
      * [`VisionTransformer.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.bfloat16)
      * [`VisionTransformer.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.buffers)
      * [`VisionTransformer.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.call_super_init)
      * [`VisionTransformer.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.children)
      * [`VisionTransformer.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.compile)
      * [`VisionTransformer.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.cpu)
      * [`VisionTransformer.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.cuda)
      * [`VisionTransformer.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.double)
      * [`VisionTransformer.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.dump_patches)
      * [`VisionTransformer.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.eval)
      * [`VisionTransformer.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.extra_repr)
      * [`VisionTransformer.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.float)
      * [`VisionTransformer.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.get_buffer)
      * [`VisionTransformer.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.get_extra_state)
      * [`VisionTransformer.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.get_parameter)
      * [`VisionTransformer.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.get_submodule)
      * [`VisionTransformer.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.half)
      * [`VisionTransformer.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.ipu)
      * [`VisionTransformer.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.load_state_dict)
      * [`VisionTransformer.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.modules)
      * [`VisionTransformer.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.mtia)
      * [`VisionTransformer.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.named_buffers)
      * [`VisionTransformer.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.named_children)
      * [`VisionTransformer.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.named_modules)
      * [`VisionTransformer.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.named_parameters)
      * [`VisionTransformer.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.parameters)
      * [`VisionTransformer.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_backward_hook)
      * [`VisionTransformer.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_buffer)
      * [`VisionTransformer.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_forward_hook)
      * [`VisionTransformer.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_forward_pre_hook)
      * [`VisionTransformer.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_full_backward_hook)
      * [`VisionTransformer.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_full_backward_pre_hook)
      * [`VisionTransformer.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_load_state_dict_post_hook)
      * [`VisionTransformer.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_load_state_dict_pre_hook)
      * [`VisionTransformer.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_module)
      * [`VisionTransformer.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_parameter)
      * [`VisionTransformer.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_state_dict_post_hook)
      * [`VisionTransformer.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.register_state_dict_pre_hook)
      * [`VisionTransformer.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.requires_grad_)
      * [`VisionTransformer.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.set_extra_state)
      * [`VisionTransformer.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.set_submodule)
      * [`VisionTransformer.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.share_memory)
      * [`VisionTransformer.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.state_dict)
      * [`VisionTransformer.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.to)
      * [`VisionTransformer.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.to_empty)
      * [`VisionTransformer.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.train)
      * [`VisionTransformer.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.type)
      * [`VisionTransformer.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.xpu)
      * [`VisionTransformer.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.zero_grad)
      * [`VisionTransformer.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.VisionTransformer.training)
    * [`CLIP`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP)
      * [`CLIP.initialize_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.initialize_parameters)
      * [`CLIP.build_attention_mask()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.build_attention_mask)
      * [`CLIP.dtype`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.dtype)
      * [`CLIP.encode_image()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.encode_image)
      * [`CLIP.encode_text()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.encode_text)
      * [`CLIP.forward()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.forward)
      * [`CLIP.T_destination`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.T_destination)
      * [`CLIP.add_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.add_module)
      * [`CLIP.apply()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.apply)
      * [`CLIP.bfloat16()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.bfloat16)
      * [`CLIP.buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.buffers)
      * [`CLIP.call_super_init`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.call_super_init)
      * [`CLIP.children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.children)
      * [`CLIP.compile()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.compile)
      * [`CLIP.cpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.cpu)
      * [`CLIP.cuda()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.cuda)
      * [`CLIP.double()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.double)
      * [`CLIP.dump_patches`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.dump_patches)
      * [`CLIP.eval()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.eval)
      * [`CLIP.extra_repr()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.extra_repr)
      * [`CLIP.float()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.float)
      * [`CLIP.get_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.get_buffer)
      * [`CLIP.get_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.get_extra_state)
      * [`CLIP.get_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.get_parameter)
      * [`CLIP.get_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.get_submodule)
      * [`CLIP.half()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.half)
      * [`CLIP.ipu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.ipu)
      * [`CLIP.load_state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.load_state_dict)
      * [`CLIP.modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.modules)
      * [`CLIP.mtia()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.mtia)
      * [`CLIP.named_buffers()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.named_buffers)
      * [`CLIP.named_children()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.named_children)
      * [`CLIP.named_modules()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.named_modules)
      * [`CLIP.named_parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.named_parameters)
      * [`CLIP.parameters()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.parameters)
      * [`CLIP.register_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_backward_hook)
      * [`CLIP.register_buffer()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_buffer)
      * [`CLIP.register_forward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_forward_hook)
      * [`CLIP.register_forward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_forward_pre_hook)
      * [`CLIP.register_full_backward_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_full_backward_hook)
      * [`CLIP.register_full_backward_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_full_backward_pre_hook)
      * [`CLIP.register_load_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_load_state_dict_post_hook)
      * [`CLIP.register_load_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_load_state_dict_pre_hook)
      * [`CLIP.register_module()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_module)
      * [`CLIP.register_parameter()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_parameter)
      * [`CLIP.register_state_dict_post_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_state_dict_post_hook)
      * [`CLIP.register_state_dict_pre_hook()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.register_state_dict_pre_hook)
      * [`CLIP.requires_grad_()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.requires_grad_)
      * [`CLIP.set_extra_state()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.set_extra_state)
      * [`CLIP.set_submodule()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.set_submodule)
      * [`CLIP.share_memory()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.share_memory)
      * [`CLIP.state_dict()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.state_dict)
      * [`CLIP.to()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.to)
      * [`CLIP.to_empty()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.to_empty)
      * [`CLIP.train()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.train)
      * [`CLIP.type()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.type)
      * [`CLIP.xpu()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.xpu)
      * [`CLIP.zero_grad()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.zero_grad)
      * [`CLIP.training`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.CLIP.training)
    * [`convert_weights()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.convert_weights)
    * [`build_model()`](api__fiftyone.utils.clip.model.md#fiftyone.utils.clip.model.build_model)
  * [fiftyone.utils.clip.tokenizer](api__fiftyone.utils.clip.tokenizer.md)
    * [`default_bpe()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.default_bpe)
    * [`bytes_to_unicode()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.bytes_to_unicode)
    * [`get_pairs()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.get_pairs)
    * [`basic_clean()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.basic_clean)
    * [`whitespace_clean()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.whitespace_clean)
    * [`SimpleTokenizer`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.SimpleTokenizer)
      * [`SimpleTokenizer.bpe()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.SimpleTokenizer.bpe)
      * [`SimpleTokenizer.encode()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.SimpleTokenizer.encode)
      * [`SimpleTokenizer.decode()`](api__fiftyone.utils.clip.tokenizer.md#fiftyone.utils.clip.tokenizer.SimpleTokenizer.decode)
  * [fiftyone.utils.clip.zoo](api__fiftyone.utils.clip.zoo.md)
    * [`TorchCLIPModelConfig`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig)
      * [`TorchCLIPModelConfig.tokenizer_path`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.tokenizer_path)
      * [`TorchCLIPModelConfig.download_tokenizer_if_necessary()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.download_tokenizer_if_necessary)
      * [`TorchCLIPModelConfig.attributes()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.attributes)
      * [`TorchCLIPModelConfig.builder()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.builder)
      * [`TorchCLIPModelConfig.copy()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.copy)
      * [`TorchCLIPModelConfig.custom_attributes()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.custom_attributes)
      * [`TorchCLIPModelConfig.default()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.default)
      * [`TorchCLIPModelConfig.download_model_if_necessary()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.download_model_if_necessary)
      * [`TorchCLIPModelConfig.from_dict()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.from_dict)
      * [`TorchCLIPModelConfig.from_json()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.from_json)
      * [`TorchCLIPModelConfig.from_kwargs()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.from_kwargs)
      * [`TorchCLIPModelConfig.from_str()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.from_str)
      * [`TorchCLIPModelConfig.get_class_name()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.get_class_name)
      * [`TorchCLIPModelConfig.init()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.init)
      * [`TorchCLIPModelConfig.load_default()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.load_default)
      * [`TorchCLIPModelConfig.parse_array()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_array)
      * [`TorchCLIPModelConfig.parse_bool()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_bool)
      * [`TorchCLIPModelConfig.parse_categorical()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_categorical)
      * [`TorchCLIPModelConfig.parse_dict()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_dict)
      * [`TorchCLIPModelConfig.parse_int()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_int)
      * [`TorchCLIPModelConfig.parse_mutually_exclusive_fields()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_mutually_exclusive_fields)
      * [`TorchCLIPModelConfig.parse_number()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_number)
      * [`TorchCLIPModelConfig.parse_object()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_object)
      * [`TorchCLIPModelConfig.parse_object_array()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_object_array)
      * [`TorchCLIPModelConfig.parse_object_dict()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_object_dict)
      * [`TorchCLIPModelConfig.parse_path()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_path)
      * [`TorchCLIPModelConfig.parse_raw()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_raw)
      * [`TorchCLIPModelConfig.parse_string()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.parse_string)
      * [`TorchCLIPModelConfig.serialize()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.serialize)
      * [`TorchCLIPModelConfig.to_str()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.to_str)
      * [`TorchCLIPModelConfig.validate_all_or_nothing_fields()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.validate_all_or_nothing_fields)
      * [`TorchCLIPModelConfig.write_json()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModelConfig.write_json)
    * [`TorchCLIPModel`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel)
      * [`TorchCLIPModel.can_embed_prompts`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.can_embed_prompts)
      * [`TorchCLIPModel.embed_prompt()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.embed_prompt)
      * [`TorchCLIPModel.embed_prompts()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.embed_prompts)
      * [`TorchCLIPModel.build_get_item()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.build_get_item)
      * [`TorchCLIPModel.classes`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.classes)
      * [`TorchCLIPModel.collate_fn()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.collate_fn)
      * [`TorchCLIPModel.device`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.device)
      * [`TorchCLIPModel.embed()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.embed)
      * [`TorchCLIPModel.embed_all()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.embed_all)
      * [`TorchCLIPModel.from_config()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.from_config)
      * [`TorchCLIPModel.from_dict()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.from_dict)
      * [`TorchCLIPModel.from_json()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.from_json)
      * [`TorchCLIPModel.from_kwargs()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.from_kwargs)
      * [`TorchCLIPModel.get_embeddings()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.get_embeddings)
      * [`TorchCLIPModel.has_collate_fn`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.has_collate_fn)
      * [`TorchCLIPModel.has_embeddings`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.has_embeddings)
      * [`TorchCLIPModel.has_logits`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.has_logits)
      * [`TorchCLIPModel.mask_targets`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.mask_targets)
      * [`TorchCLIPModel.media_type`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.media_type)
      * [`TorchCLIPModel.num_classes`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.num_classes)
      * [`TorchCLIPModel.parse()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.parse)
      * [`TorchCLIPModel.predict()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.predict)
      * [`TorchCLIPModel.predict_all()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.predict_all)
      * [`TorchCLIPModel.preprocess`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.preprocess)
      * [`TorchCLIPModel.ragged_batches`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.ragged_batches)
      * [`TorchCLIPModel.required_keys`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.required_keys)
      * [`TorchCLIPModel.skeleton`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.skeleton)
      * [`TorchCLIPModel.store_logits`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.store_logits)
      * [`TorchCLIPModel.transforms`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.transforms)
      * [`TorchCLIPModel.using_gpu`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.using_gpu)
      * [`TorchCLIPModel.using_half_precision`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.using_half_precision)
      * [`TorchCLIPModel.validate()`](api__fiftyone.utils.clip.zoo.md#fiftyone.utils.clip.zoo.TorchCLIPModel.validate)



## Module contents#

CLIP model utils.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`TorchCLIPModelConfig`(d) | Configuration for running a `TorchCLIPModel`.  
---|---  
`TorchCLIPModel`(config) | Torch implementation of CLIP from [openai/CLIP](https://github.com/openai/CLIP).  
  
class fiftyone.utils.clip.TorchCLIPModelConfig(_d_)#
    

Bases: [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig"), [`HasZooModel`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.HasZooModel "fiftyone.zoo.models.HasZooModel")

Configuration for running a `TorchCLIPModel`.

See [`fiftyone.utils.torch.TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig") for additional arguments.

Parameters:
    

  * **tokenizer_base_filename** â the filename in `fo.config.model_zoo_dir` in which to store the modelâs tokenizer

  * **tokenizer_base_url** â a URL from which the tokenizer can be downloaded, if necessary

  * **context_length** â the modelâs context length

  * **text_prompt** â the text prompt to use, e.g., `"A photo of"`

  * **classes** (_None_) â a list of custom classes for zero-shot prediction




**Attributes:**

`tokenizer_path` |   
---|---  
  
**Methods:**

`download_tokenizer_if_necessary`() |   
---|---  
`attributes`() | Returns a list of class attributes to be serialized.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`download_model_if_necessary`() | Downloads the published model specified by the config, if necessary.  
`from_dict`(d) | Constructs a Config object from a JSON dictionary.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`init`(d) | Initializes the published model config.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property tokenizer_path#
    

download_tokenizer_if_necessary()#
    

attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

Subclasses can override this method, but, by default, all attributes in vars(self) are returned, minus private attributes, i.e., those starting with â_â. The order of the attributes in this list is preserved when serializing objects, so a common pattern is for subclasses to override this method if they want their JSON files to be organized in a particular way.

Returns:
    

a list of class attributes to be serialized

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

download_model_if_necessary()#
    

Downloads the published model specified by the config, if necessary.

After this method is called, the model_path attribute will always contain the path to the model on disk.

classmethod from_dict(_d_)#
    

Constructs a Config object from a JSON dictionary.

Config subclass constructors accept JSON dictionaries, so this method simply passes the dictionary to cls().

Parameters:
    

**d** â a dict of fields expected by cls

Returns:
    

an instance of cls

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

init(_d_)#
    

Initializes the published model config.

This method should be called by ModelConfig.__init__(), and it performs the following tasks:

  * Parses the model_name and model_path parameters

  * Populates any default parameters in the provided ModelConfig dict




Parameters:
    

**d** â a ModelConfig dict

Returns:
    

a ModelConfig dict with any default parameters populated

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.clip.TorchCLIPModel(_config_)#
    

Bases: [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel"), [`PromptMixin`](api__fiftyone.core.models.md#fiftyone.core.models.PromptMixin "fiftyone.core.models.PromptMixin")

Torch implementation of CLIP from [openai/CLIP](https://github.com/openai/CLIP).

Parameters:
    

**config** â a `TorchCLIPModelConfig`

**Attributes:**

`can_embed_prompts` | Whether this model can generate prompt embeddings.  
---|---  
`classes` | The list of class labels for the model, if known.  
`device` | The `torch:torch.torch.device` that the model is using.  
`has_collate_fn` | Whether this model has a custom collate function.  
`has_embeddings` | Whether this model has embeddings.  
`has_logits` | Whether this instance can generate logits.  
`mask_targets` | The mask targets for the model, if any.  
`media_type` | The media type processed by the model.  
`num_classes` | The number of classes for the model, if known.  
`preprocess` | Whether to apply preprocessing transforms for inference, if any.  
`ragged_batches` | Whether `transforms()` may return tensors of different sizes.  
`required_keys` | The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.  
`skeleton` | The keypoint skeleton for the model, if any.  
`store_logits` | Whether the model should store logits in its predictions.  
`transforms` | A `torchvision.transforms` function that will be applied to each input before prediction, if any.  
`using_gpu` | Whether the model is using GPU.  
`using_half_precision` | Whether the model is using half precision.  
  
**Methods:**

`embed_prompt`(prompt) | Generates an embedding for the given text prompt.  
---|---  
`embed_prompts`(prompts) | Generates an embedding for the given text prompts.  
`build_get_item`([field_mapping]) | Builds the [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance that defines how the model's data should be loaded by data loaders.  
`collate_fn`(batch) | The collate function to use when creating dataloaders for this model.  
`embed`(arg) | Generates an embedding for the given data.  
`embed_all`(args) | Generates embeddings for the given iterable of data.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_embeddings`() | Returns the embeddings generated by the last forward pass of the model.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`predict`(img) | Performs prediction on the given image.  
`predict_all`(imgs) | Performs prediction on the given batch of images.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
  
property can_embed_prompts#
    

Whether this model can generate prompt embeddings.

This method returns `False` by default. Models that can generate prompt embeddings should override this via implementing the `PromptMixin` interface.

embed_prompt(_prompt_)#
    

Generates an embedding for the given text prompt.

Parameters:
    

**prompt** â a text string

Returns:
    

a numpy vector

embed_prompts(_prompts_)#
    

Generates an embedding for the given text prompts.

Parameters:
    

**prompts** â an iterable of text strings

Returns:
    

a `num_prompts x num_dims` array of prompt embeddings

build_get_item(_field_mapping =None_)#
    

Builds the [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance that defines how the modelâs data should be loaded by data loaders.

Parameters:
    

**field_mapping** (_None_) â a user-provided dict mapping required keys to dataset field names

Returns:
    

a [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance

property classes#
    

The list of class labels for the model, if known.

static collate_fn(_batch_)#
    

The collate function to use when creating dataloaders for this model.

In order to enable this functionality, the modelâs `has_collate_fn()` property must return `True`.

By default, this is the default collate function for [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)"), but subclasses can override this method as necessary.

Note that this function must be serializable so it is compatible with multiprocessing for dataloaders.

Parameters:
    

**batch** â a list of items to collate

Returns:
    

the collated batch, which will be fed directly to the model

property device#
    

The `torch:torch.torch.device` that the model is using.

embed(_arg_)#
    

Generates an embedding for the given data.

Subclasses can override this method to increase efficiency, but, by default, this method simply calls `predict()` and then returns `get_embeddings()`.

Parameters:
    

**arg** â the data. See `predict()` for details

Returns:
    

a numpy array containing the embedding

embed_all(_args_)#
    

Generates embeddings for the given iterable of data.

Subclasses can override this method to increase efficiency, but, by default, this method simply iterates over the data and applies `embed()` to each.

Parameters:
    

**args** â an iterable of data. See `predict_all()` for details

Returns:
    

a numpy array containing the embeddings stacked along axis 0

classmethod from_config(_config_)#
    

Instantiates a Configurable class from a <cls>Config instance.

classmethod from_dict(_d_)#
    

Instantiates a Configurable class from a <cls>Config dict.

Parameters:
    

**d** â a dict to construct a <cls>Config

Returns:
    

an instance of cls

classmethod from_json(_json_path_)#
    

Instantiates a Configurable class from a <cls>Config JSON file.

Parameters:
    

**json_path** â path to a JSON file for type <cls>Config

Returns:
    

an instance of cls

classmethod from_kwargs(_** kwargs_)#
    

Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.

Parameters:
    

****kwargs** â keyword arguments that define the fields of a <cls>Config dict

Returns:
    

an instance of cls

get_embeddings()#
    

Returns the embeddings generated by the last forward pass of the model.

By convention, this method should always return an array whose first axis represents batch size (which will always be 1 when `predict()` was last used).

Returns:
    

a numpy array containing the embedding(s)

property has_collate_fn#
    

Whether this model has a custom collate function.

Set this to `True` if you want `collate_fn()` to be used during inference.

property has_embeddings#
    

Whether this model has embeddings.

property has_logits#
    

Whether this instance can generate logits.

property mask_targets#
    

The mask targets for the model, if any.

property media_type#
    

The media type processed by the model.

property num_classes#
    

The number of classes for the model, if known.

static parse(_class_name_ , _module_name =None_)#
    

Parses a Configurable subclass name string.

Assumes both the Configurable class and the Config class are defined in the same module. The module containing the classes will be loaded if necessary.

Parameters:
    

  * **class_name** â a string containing the name of the Configurable class, e.g. âClassNameâ, or a fully-qualified class name, e.g. âeta.core.config.ClassNameâ

  * **module_name** â a string containing the fully-qualified module name, e.g. âeta.core.configâ, or None if class_name includes the module name. Set module_name = __name__ to load a class from the calling module



Returns:
    

the Configurable class config_cls: the Config class associated with cls

Return type:
    

[cls](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.cls "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.cls")

predict(_img_)#
    

Performs prediction on the given image.

Parameters:
    

**img** â 

the image to process, which can be any of the following:

  * A PIL image

  * A uint8 numpy array (HWC)

  * A Torch tensor (CHW)




Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance or dict of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

predict_all(_imgs_)#
    

Performs prediction on the given batch of images.

Parameters:
    

**imgs** â 

the batch of images to process, which can be any of the following:

  * A list of PIL images

  * A list of uint8 numpy arrays (HWC)

  * A list of Torch tensors (CHW)

  * A uint8 numpy tensor (NHWC)

  * A Torch tensor (NCHW)




Returns:
    

a list of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances or a list of dicts of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

property preprocess#
    

Whether to apply preprocessing transforms for inference, if any.

property ragged_batches#
    

Whether `transforms()` may return tensors of different sizes. If True, then passing ragged lists of images to `predict_all()` may not be not allowed.

property required_keys#
    

The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.

property skeleton#
    

The keypoint skeleton for the model, if any.

property store_logits#
    

Whether the model should store logits in its predictions.

property transforms#
    

A `torchvision.transforms` function that will be applied to each input before prediction, if any.

property using_gpu#
    

Whether the model is using GPU.

property using_half_precision#
    

Whether the model is using half precision.

classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
