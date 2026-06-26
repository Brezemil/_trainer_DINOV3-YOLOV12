---
source_url: https://docs.voxel51.com/api/fiftyone.core.plots.manager.html
---

# fiftyone.core.plots.manager#

Session plot manager.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PlotManager`(session) | Class that manages communication between a [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") and one or more [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances.  
---|---  
  
class fiftyone.core.plots.manager.PlotManager(_session_)#
    

Bases: `object`

Class that manages communication between a [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") and one or more [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances.

Each plot can be linked to either the view, samples, frames, or labels of a session:

  * **View links:** When a plot has `link_type == "view"`, then, when the sessionâs view changes, the plot is updated based on the content of the view

  * **Sample links:** When points are selected in a plot with `link_type == "samples"`, a view containing the corresponding samples is loaded in the App. Conversely, when the sessionâs view changes, the corresponding points are selected in the plot

  * **Frame links:** When points are selected in a plot with `link_type == "frames"`, a view containing the corresponding frames is loaded in the App. Conversely, when the sessionâs view changes, the corresponding points are selected in the plot

  * **Label links:** When points are selected in a plot with `link_type == "labels"`, a view containing the corresponding labels is loaded in the App. Conversely, when the sessionâs view changes, the points in the plot corresponding to all labels in the view are selected in the plot




Parameters:
    

**session** â a [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session")

**Methods:**

`summary`() | Returns a string summary of this manager.  
---|---  
`keys`() | Returns an iterator over the names of plots in this manager.  
`items`() | Returns an iterator over the `(name, plot)` pairs in this manager.  
`values`() | Returns an iterator over the plots in this manager.  
`attach`(plot[,Â name,Â connect,Â overwrite]) | Attaches a plot to this manager.  
`remove`(name) | Removes the plot from this manager.  
`clear`() | Removes all plots from this manager.  
`pop`(name) | Removes the plot from this manager and returns it.  
`connect`() | Connects this manager to its session and all plots.  
`disconnect`() | Disconnects this manager from its session and all plots.  
`sync`() | Syncs all connected plots with the session's current view.  
`freeze`() | Freezes all connected plots, replacing them with static images.  
  
**Attributes:**

`is_connected` | Whether this manager is currently connected to its plots.  
---|---  
`is_disconnected` | Whether this manager is currently disconnected from its plots.  
`has_view_links` | Whether this manager has plots linked to views.  
`has_sample_links` | Whether this manager has plots linked to samples.  
`has_frame_links` | Whether this manager has plots linked to frames.  
`has_label_links` | Whether this manager has plots linked to labels.  
  
summary()#
    

Returns a string summary of this manager.

Returns:
    

a string summary

keys()#
    

Returns an iterator over the names of plots in this manager.

Returns:
    

an iterator over plot names

items()#
    

Returns an iterator over the `(name, plot)` pairs in this manager.

Returns:
    

an iterator that emits `(name, ResponsivePlot)` tuples

values()#
    

Returns an iterator over the plots in this manager.

Returns:
    

an iterator that emits [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances

property is_connected#
    

Whether this manager is currently connected to its plots.

property is_disconnected#
    

Whether this manager is currently disconnected from its plots.

property has_view_links#
    

Whether this manager has plots linked to views.

property has_sample_links#
    

Whether this manager has plots linked to samples.

property has_frame_links#
    

Whether this manager has plots linked to frames.

property has_label_links#
    

Whether this manager has plots linked to labels.

attach(_plot_ , _name =None_, _connect =True_, _overwrite =True_)#
    

Attaches a plot to this manager.

Parameters:
    

  * **plot** â a [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot")

  * **name** (_None_) â an optional name for the plot

  * **connect** (_True_) â whether to immediately connect the plot

  * **overwrite** (_True_) â whether to overwrite an existing plot of the same name




remove(_name_)#
    

Removes the plot from this manager.

Parameters:
    

**name** â the name of a plot

clear()#
    

Removes all plots from this manager.

pop(_name_)#
    

Removes the plot from this manager and returns it.

Parameters:
    

**name** â the name of a plot

Returns:
    

the [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot")

connect()#
    

Connects this manager to its session and all plots.

disconnect()#
    

Disconnects this manager from its session and all plots.

sync()#
    

Syncs all connected plots with the sessionâs current view.

freeze()#
    

Freezes all connected plots, replacing them with static images.

Only applicable in notebook contexts.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
