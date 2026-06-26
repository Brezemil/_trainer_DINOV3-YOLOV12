---
source_url: https://docs.voxel51.com/user_guide/groups.html?highlight=group
---

# Grouped datasets#

FiftyOne supports the creation of **grouped datasets** , which contain multiple slices of samples of possibly different modalities (e.g., [image](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-media-type), [video](https://docs.voxel51.com/user_guide/using_datasets.html#video-datasets), or [3D scenes](https://docs.voxel51.com/user_guide/using_datasets.html#d-datasets)) that are organized into groups.

Grouped datasets can be used to represent multiview scenes, where data for multiple perspectives of the same scene can be stored, visualized, and queried in ways that respect the relationships between the slices of data.

![groups-sizzle](../_images/groups-modal.gif)

Note

Did you know? You can also create [dynamic group views](https://docs.voxel51.com/user_guide/using_views.html#view-groups) into your datasets based on a field or expression of interest.

## Overview#

In this section, weâll cover the basics of creating and working with grouped datasets via Python.

Letâs start by creating some test data. Weâll use the quickstart dataset to construct some mocked triples of left/center/right images:
    
    
     1import fiftyone as fo
     2import fiftyone.utils.random as four
     3import fiftyone.zoo as foz
     4
     5groups = ["left", "center", "right"]
     6
     7d = foz.load_zoo_dataset("quickstart")
     8four.random_split(d, {g: 1 / len(groups) for g in groups})
     9filepaths = [d.match_tags(g).values("filepath") for g in groups]
    10filepaths = [dict(zip(groups, fps)) for fps in zip(*filepaths)]
    11
    12print(filepaths[:2])
    
    
    
    [
        {
            'left': '~/fiftyone/quickstart/data/000880.jpg',
            'center': '~/fiftyone/quickstart/data/002799.jpg',
            'right': '~/fiftyone/quickstart/data/001599.jpg',
        },
        {
            'left': '~/fiftyone/quickstart/data/003344.jpg',
            'center': '~/fiftyone/quickstart/data/001057.jpg',
            'right': '~/fiftyone/quickstart/data/001430.jpg',
        },
    ]
    

### Creating grouped datasets#

To create a grouped dataset, simply use [`add_group_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_group_field "fiftyone.core.dataset.Dataset.add_group_field") to declare a [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") field on your dataset before you add samples to it:
    
    
    1dataset = fo.Dataset("groups-overview")
    2dataset.add_group_field("group", default="center")
    

The optional `default` parameter specifies the slice of samples that will be returned via the API or visualized in the Appâs grid view by default. If you donât specify a default, one will be inferred from the first sample you add to the dataset.

Note

Datasets may contain only one [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") field.

### Adding samples#

To populate a grouped dataset with samples, create a single [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") instance for each group of samples and use [`Group.element()`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group.element "fiftyone.core.groups.Group.element") to generate values for the group field of each [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") object in the group based on their sliceâs `name`. The [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects can then simply be added to the dataset as usual:
    
    
     1samples = []
     2for fps in filepaths:
     3    group = fo.Group()
     4    for name, filepath in fps.items():
     5        sample = fo.Sample(filepath=filepath, group=group.element(name))
     6        samples.append(sample)
     7
     8dataset.add_samples(samples)
     9
    10print(dataset)
    
    
    
    Name:        groups-overview
    Media type:  group
    Group slice: center
    Num groups:  66
    Persistent:  False
    Tags:        []
    Sample fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.Metadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        group:            fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.groups.Group)
    

Note

Every sample in a grouped dataset must have its group field populated with a [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") element.

### Dataset properties#

Grouped datasets have a `media_type` of `"group"`:
    
    
    1print(dataset.media_type)
    2# group
    

The [`group_field`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_field "fiftyone.core.dataset.Dataset.group_field") property contains the name of the [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") field storing the datasetâs group membership information:
    
    
    1print(dataset.group_field)
    2# group
    

The [`group_slices`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_slices "fiftyone.core.dataset.Dataset.group_slices") property contains the names of all group slices in the dataset:
    
    
    1print(dataset.group_slices)
    2# ['left', 'center', 'right']
    

The [`group_media_types`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_media_types "fiftyone.core.dataset.Dataset.group_media_types") property is a dict mapping each slice name to its corresponding media type:
    
    
    1print(dataset.group_media_types)
    2# {'left': 'image', 'center': 'image', 'right': 'image'}
    

The list of group slices and their corresponding media types are dynamically expanded as you add samples to a grouped dataset.

Note

Grouped datasets may contain a mix of different modalities (e.g., images, videos, and 3D scenes), but FiftyOne strictly enforces that each **slice** of a grouped dataset must have a homogeneous media type.

For example, you would see an error if you tried to add a video sample to the `left` slice of the above dataset, since it contains images.

The [`default_group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_group_slice "fiftyone.core.dataset.Dataset.default_group_slice") property stores the name of the default group slice:
    
    
    1print(dataset.default_group_slice)
    2# center
    

The default group slice controls the slice of samples that will be returned via the APIâfor example when you directly iterate over the datasetâor visualized in the Appâs grid view by default:
    
    
    1print(dataset.first())
    
    
    
    <Sample: {
        'id': '62db2ce147e9efc3615cd450',
        'media_type': 'image',
        'filepath': '~/fiftyone/quickstart/data/003344.jpg',
        'tags': [],
        'metadata': None,
        'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
        'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
        'group': <Group: {'id': '62db2ce147e9efc3615cd346', 'name': 'center'}>,
    }>
    

You can change the _active group slice_ in your current session by setting the [`group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_slice "fiftyone.core.dataset.Dataset.group_slice") property:
    
    
    1dataset.group_slice = "left"
    2
    3print(dataset.first())
    
    
    
    <Sample: {
        'id': '62db2ce147e9efc3615cd44e',
        'media_type': 'image',
        'filepath': '~/fiftyone/quickstart/data/001599.jpg',
        'tags': [],
        'metadata': None,
        'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
        'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
        'group': <Group: {'id': '62db2ce147e9efc3615cd346', 'name': 'left'}>,
    }>
    

You can reset the active group slice to the default value by setting [`group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_slice "fiftyone.core.dataset.Dataset.group_slice") to `None`:
    
    
    1# Resets to `default_group_slice`
    2dataset.group_slice = None
    

You can also change the default group slice at any time by setting the [`default_group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_group_slice "fiftyone.core.dataset.Dataset.default_group_slice") property.

### Adding fields#

You are free to add arbitrary sample- and frame-level fields to your grouped datasets just as you would with ungrouped datasets:
    
    
    1sample = dataset.first()
    2
    3sample["int_field"] = 51
    4sample["ground_truth"] = fo.Classification(label="outdoor")
    5
    6sample.save()
    

You can also use methods like [`set_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.set_values "fiftyone.core.collections.SampleCollection.set_values") and [`save()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.save "fiftyone.core.view.DatasetView.save") to perform bulk edits to the active slice of a grouped dataset.

Note that all slices of a grouped dataset share the same schema, and hence any fields you add to samples from a particular slice will be implicitly declared on all samples from that slice and all other slices:
    
    
    1print(dataset)
    
    
    
    Name:        groups-overview
    Media type:  group
    Group slice: center
    Num groups:  66
    Persistent:  False
    Tags:        []
    Sample fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.Metadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        group:            fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.groups.Group)
        int_field:        fiftyone.core.fields.IntField
        ground_truth:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Classification)
    

Note

Like ungrouped datasets, any fields in a grouped datasetâs schema that have not been explicitly set on a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") in the dataset will be `None`.

You can use methods like [`clone_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clone_sample_field "fiftyone.core.dataset.Dataset.clone_sample_field"), [`rename_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.rename_sample_field "fiftyone.core.dataset.Dataset.rename_sample_field"), [`delete_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_sample_field "fiftyone.core.dataset.Dataset.delete_sample_field"), [`clear_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.clear_sample_field "fiftyone.core.dataset.Dataset.clear_sample_field"), and [`keep_fields()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.keep_fields "fiftyone.core.view.DatasetView.keep_fields") to perform batch edits to the fields across _all slices_ of a grouped dataset.

### Accessing samples#

You can access a sample from any slice of grouped dataset via its ID or filepath:
    
    
    1# Grab a random sample across all slices
    2sample = dataset.select_group_slices().shuffle().first()
    3
    4# Directly lookup same sample by ID
    5also_sample = dataset[sample.id]
    

In addition, you can also use [`get_group()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.get_group "fiftyone.core.dataset.Dataset.get_group") to retrieve a dict containing all samples in a group with a given ID:
    
    
    1# Grab a random group ID
    2sample = dataset.shuffle().first()
    3group_id = sample.group.id
    4
    5group = dataset.get_group(group_id)
    6print(group)
    
    
    
    {
        'left': <Sample: {
            'id': '62f810ba59e644568f229dac',
            'media_type': 'image',
            'filepath': '~/fiftyone/quickstart/data/001227.jpg',
            'tags': [],
            'metadata': None,
            'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'group': <Group: {'id': '62f810ba59e644568f229c62', 'name': 'left'}>,
        }>,
        'center': <Sample: {
            'id': '62f810ba59e644568f229dad',
            'media_type': 'image',
            'filepath': '~/fiftyone/quickstart/data/004172.jpg',
            'tags': [],
            'metadata': None,
            'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'group': <Group: {'id': '62f810ba59e644568f229c62', 'name': 'center'}>,
        }>,
        'right': <Sample: {
            'id': '62f810ba59e644568f229dae',
            'media_type': 'image',
            'filepath': '~/fiftyone/quickstart/data/000594.jpg',
            'tags': [],
            'metadata': None,
            'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'group': <Group: {'id': '62f810ba59e644568f229c62', 'name': 'right'}>,
        }>,
    }
    

### Deleting samples#

Like ungrouped datasets, you can use [`delete_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_samples "fiftyone.core.dataset.Dataset.delete_samples") to delete individual sample(s) from a grouped dataset:
    
    
    1# Grab a random sample across all slices
    2sample = dataset.select_group_slices().shuffle().first()
    3
    4dataset.delete_samples(sample)
    

In addition, you can use [`delete_groups()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.delete_groups "fiftyone.core.dataset.Dataset.delete_groups") to delete all samples in a specific group(s):
    
    
    1# Continuing from above, delete the rest of the group
    2group_id = sample.group.id
    3
    4dataset.delete_groups(group_id)
    

You can also use methods like [`clear()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.clear "fiftyone.core.view.DatasetView.clear") and [`keep()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.keep "fiftyone.core.view.DatasetView.keep") to perform batch edits to the groups in a grouped dataset.

### Iterating over grouped datasets#

When you directly iterate over a grouped dataset, you will get samples from the datasetâs active slice:
    
    
    1print(dataset.group_slice)
    2# center
    3
    4for sample in dataset:
    5    pass
    6
    7print(sample)
    
    
    
    <Sample: {
        'id': '62f10dbb68f4ed13eba7c5e7',
        'media_type': 'image',
        'filepath': '~/fiftyone/quickstart/data/001394.jpg',
        'tags': [],
        'metadata': None,
        'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
        'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
        'group': <Group: {'id': '62f10dbb68f4ed13eba7c4a0', 'name': 'center'}>,
    }>
    

Note

You can customize the datasetâs active slice by setting the [`group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_slice "fiftyone.core.dataset.Dataset.group_slice") property to another slice name.

You can also use [`iter_groups()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.iter_groups "fiftyone.core.dataset.Dataset.iter_groups") to iterate over dicts containing all samples in each group:
    
    
    1for group in dataset.iter_groups():
    2    pass
    3
    4print(group)
    
    
    
    {
        'left': <Sample: {
            'id': '62f10dbb68f4ed13eba7c5e6',
            'media_type': 'image',
            'filepath': '~/fiftyone/quickstart/data/002538.jpg',
            'tags': [],
            'metadata': None,
            'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'group': <Group: {'id': '62f10dbb68f4ed13eba7c4a0', 'name': 'left'}>,
        }>,
        'center': <Sample: {
            'id': '62f10dbb68f4ed13eba7c5e7',
            'media_type': 'image',
            'filepath': '~/fiftyone/quickstart/data/001394.jpg',
            'tags': [],
            'metadata': None,
            'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'group': <Group: {'id': '62f10dbb68f4ed13eba7c4a0', 'name': 'center'}>,
        }>,
        'right': <Sample: {
            'id': '62f10dbb68f4ed13eba7c5e8',
            'media_type': 'image',
            'filepath': '~/fiftyone/quickstart/data/000020.jpg',
            'tags': [],
            'metadata': None,
            'created_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'last_modified_at': datetime.datetime(2024, 7, 22, 5, 16, 10, 701907),
            'group': <Group: {'id': '62f10dbb68f4ed13eba7c4a0', 'name': 'right'}>,
        }>,
    }
    

## Example datasets#

The [FiftyOne Dataset Zoo](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo) contains grouped datasets that you can use out-of-the-box to test drive FiftyOneâs group-related features.

### Quickstart groups#

The fastest way to get started is by loading the [quickstart-groups](dataset_zoo__datasets__quickstart_groups.md#dataset-zoo-quickstart-groups) dataset, which consists of 200 scenes from the train split of the KITTI dataset, each containing left camera, right camera, point cloud, and 2D/3D object annotation data:
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("quickstart-groups")
    5
    6print(dataset.group_media_types)
    7# {'left': 'image', 'right': 'image', 'pcd': '3d'}
    8
    9print(dataset)
    
    
    
    Name:        quickstart-groups
    Media type:  group
    Group slice: left
    Num groups:  200
    Persistent:  False
    Tags:        []
    Sample fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.Metadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        group:            fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.groups.Group)
        ground_truth:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Detections)
    

### KITTI multiview#

You can also load the full [kitti-multiview](dataset_zoo__datasets__kitti_multiview.md#dataset-zoo-kitti-multiview) dataset:
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("kitti-multiview", split="train")
    

![kitti-multiview-train](../_images/kitti-multiview-train.png)

### Toy dataset#

The snippet below generates a toy dataset containing 3D cuboids filled with points that demonstrates how [3D detections are represented](https://docs.voxel51.com/user_guide/using_datasets.html#d-detections):
    
    
     1import fiftyone as fo
     2import numpy as np
     3import open3d as o3d
     4
     5detections = []
     6point_cloud = []
     7
     8for _ in range(10):
     9    dimensions = np.random.uniform([1, 1, 1], [3, 3, 3])
    10    location = np.random.uniform([-10, -10, 0], [10, 10, 10])
    11    rotation = np.random.uniform(-np.pi, np.pi, size=3)
    12
    13    detection = fo.Detection(
    14        dimensions=list(dimensions),
    15        location=list(location),
    16        rotation=list(rotation),
    17    )
    18    detections.append(detection)
    19
    20    R = o3d.geometry.get_rotation_matrix_from_xyz(rotation)
    21    points = np.random.uniform(-dimensions / 2, dimensions / 2, size=(1000, 3))
    22    points = points @ R.T + location[np.newaxis, :]
    23    point_cloud.extend(points)
    24
    25pc = o3d.geometry.PointCloud()
    26pc.points = o3d.utility.Vector3dVector(np.array(point_cloud))
    27o3d.io.write_point_cloud("/tmp/toy.pcd", pc)
    28
    29scene = fo.Scene()
    30scene.add(fo.PointCloud("point cloud", "/tmp/toy.pcd"))
    31scene.write("/tmp/toy.fo3d")
    32
    33group = fo.Group()
    34samples = [
    35    fo.Sample(
    36        filepath="/tmp/toy.png",  # non-existent
    37        group=group.element("image"),
    38    ),
    39    fo.Sample(
    40        filepath="/tmp/toy.fo3d",
    41        group=group.element("pcd"),
    42        detections=fo.Detections(detections=detections),
    43    )
    44]
    45
    46dataset = fo.Dataset()
    47dataset.add_samples(samples)
    48
    49dataset.app_config.plugins["3d"] = {
    50    "defaultCameraPosition": {"x": 0, "y": 0, "z": 20}
    51}
    52dataset.save()
    53
    54session = fo.launch_app(dataset)
    

![toy-point-cloud](../_images/toy-point-cloud.png)

## Grouped views#

You have the entire [dataset view language](https://docs.voxel51.com/user_guide/using_views.html#using-views) at your disposal to sort, slice, and search your grouped datasets!

### Basics#

You can perform simple operations like shuffling and limiting grouped datasets:
    
    
    1# Select 10 random groups from the dataset
    2view = dataset.shuffle().limit(10)
    3
    4print(view)
    
    
    
    Dataset:     groups-overview
    Media type:  group
    Group slice: center
    Num groups:  10
    Group fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.Metadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        group:            fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.groups.Group)
    View stages:
        1. Shuffle(seed=None)
        2. Limit(limit=10)
    

As you can see, the basic properties of grouped datasets carry over to views into them:
    
    
    1print(view.media_type)
    2# group
    3
    4print(view.group_slice)
    5# center
    6
    7print(view.group_media_types)
    8# {'left': 'image', 'center': 'image', 'right': 'image'}
    

You can also perform all the usual operations on grouped views, such as accessing samples, and iterating over them:
    
    
    1for group in view.iter_groups():
    2    pass
    3
    4sample = view.last()
    5print(sample)
    6
    7group_id = sample.group.id
    8group = view.get_group(group_id)
    9print(group)
    

### Filtering#

You can write views that [match and filter](https://docs.voxel51.com/user_guide/using_views.html#view-filtering) the contents of grouped datasets:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart-groups")
     6
     7print(dataset.group_slice)
     8# left
     9
    10# Filters based on the content in the 'left' slice
    11view = (
    12    dataset
    13    .match_tags("train")
    14    .filter_labels("ground_truth", F("label") == "Pedestrian")
    15)
    

Remember that, just as when iterating over grouped datasets, any filtering operations will only be applied to the active slice.

However, you can write views that reference specific slice(s) of a grouped collection via the special `"groups.<slice>.field.name"` syntax:
    
    
     1from fiftyone import ViewField as F
     2
     3dataset.compute_metadata()
     4
     5# Match groups whose `left` image has a height of at least 640 pixels and
     6# whose `right` image has a height of at most 480 pixels
     7view = dataset.match(
     8    (F("groups.left.metadata.height") >= 640)
     9    & (F("groups.right.metadata.height") <= 480)
    10)
    11
    12print(view)
    

### Selecting groups#

You can use [`select_groups()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_groups "fiftyone.core.collections.SampleCollection.select_groups") to create a view that contains certain group(s) of interest by their IDs:
    
    
     1# Select two groups at random
     2view = dataset.take(2)
     3
     4group_ids = view.values("group.id")
     5
     6# Select the same groups (default: unordered)
     7same_groups = dataset.select_groups(group_ids)
     8assert set(view.values("id")) == set(same_groups.values("id"))
     9
    10# Select the same groups (ordered)
    11same_order = dataset.select_groups(group_ids, ordered=True)
    12assert view.values("id") == same_order.values("id")
    

### Excluding groups#

You can use [`exclude_groups()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_groups "fiftyone.core.collections.SampleCollection.exclude_groups") to create a view that excludes certain group(s) of interest by their IDs:
    
    
    1# Exclude two groups at random
    2view = dataset.take(2)
    3
    4group_ids = view.values("group.id")
    5other_groups = dataset.exclude_groups(group_ids)
    6assert len(set(group_ids) & set(other_groups.values("group.id"))) == 0
    

### Selecting slices#

You can use [`select_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_group_slices "fiftyone.core.collections.SampleCollection.select_group_slices") to select one or more slices of data from a grouped dataset, either as a grouped view or as a flattened _non-grouped_ view.

For example, you can create an image view that contains only the left camera images from the grouped dataset:
    
    
    1left_view = dataset.select_group_slices("left")
    2print(left_view)
    
    
    
    Dataset:     groups-overview
    Media type:  image
    Num samples: 108
    Sample fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.Metadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        group:            fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.groups.Group)
    View stages:
        1. SelectGroupSlices(slices='left')
    

or you can create an image collection containing the left and right camera images:
    
    
    1lr_view = dataset.select_group_slices(["left", "right"])
    2print(lr_view)
    
    
    
    Dataset:     groups-overview
    Media type:  image
    Num samples: 216
    Sample fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.Metadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        group:            fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.groups.Group)
    View stages:
        1. SelectGroupSlices(slices=['left', 'right'])
    

Note that the [`media_type`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.media_type "fiftyone.core.view.DatasetView.media_type") of the above collections are `image`, not `group`. This means you can perform any valid operation for image collections to these views, without worrying about the fact that their data is sourced from a grouped dataset!
    
    
    1image_view = dataset.shuffle().limit(10).select_group_slices("left")
    2
    3another_view = image_view.match(F("metadata.width") >= 640)
    4
    5# Add fields/tags, run evaluation, export, etc
    

Note

Any filtering that you apply prior to a [`select_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_group_slices "fiftyone.core.collections.SampleCollection.select_group_slices") stage in a view is **not** automatically reflected by the output view, as the stage looks up unfiltered slice data from the source collection:
    
    
    # Filter the active slice to locate groups of interest
    match_view = dataset.filter_labels(...).match(...)
    
    # Lookup all image slices for the matching groups
    # This view contains *unfiltered* image slices
    images_view = match_view.select_group_slices(media_type="image")
    

Instead, you can apply the same (or different) filtering _after_ the [`select_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_group_slices "fiftyone.core.collections.SampleCollection.select_group_slices") stage:
    
    
    # Now apply filters to the flattened collection
    match_images_view = images_view.filter_labels(...).match(...)
    

Alternatively, you can pass `flat=False` to [`select_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_group_slices "fiftyone.core.collections.SampleCollection.select_group_slices") to create a grouped view that only contains certain group slices:
    
    
    1no_center_view = dataset.select_group_slices(["left", "right"], flat=False)
    2
    3assert no_center_view.media_type == "group"
    4assert no_center_view.group_slices == ["left", "right"]
    

### Excluding slices#

You can use [`exclude_group_slices()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.exclude_group_slices "fiftyone.core.collections.SampleCollection.exclude_group_slices") to create a grouped view that excludes certain slice(s) of a grouped dataset:
    
    
    1no_center_view = dataset.exclude_group_slices("center")
    2
    3assert no_center_view.media_type == "group"
    4assert no_center_view.group_slices == ["left", "right"]
    

## Grouped aggregations#

You can use the entire [aggregations framework](https://docs.voxel51.com/user_guide/using_aggregations.html#using-aggregations) to efficiently compute statistics on grouped datasets.

Remember that, just as when iterating over or writing views into grouped datasets, aggregations will only include samples from the active slice:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart-groups")
     6
     7# Expression that computes the area of a bounding box, in pixels
     8bbox_width = F("bounding_box")[2] * F("$metadata.width")
     9bbox_height = F("bounding_box")[3] * F("$metadata.height")
    10bbox_area = bbox_width * bbox_height
    11
    12print(dataset.group_slice)
    13# left
    14
    15print(dataset.count("ground_truth.detections"))
    16# 1438
    17
    18print(dataset.mean("ground_truth.detections[]", expr=bbox_area))
    19# 8878.752327468706
    

You can customize the datasetâs active slice by setting the [`group_slice`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.group_slice "fiftyone.core.dataset.Dataset.group_slice") property to another slice name:
    
    
    1dataset.group_slice = "right"
    2
    3print(dataset.count("ground_truth.detections"))
    4# 1438
    5
    6print(dataset.bounds("ground_truth.detections[]", expr=bbox_area))
    7# 9457.586300995526
    

As usual, you can combine views and aggregations to refine your statistics to any subset of the dataset:
    
    
     1print(dataset.count_values("ground_truth.detections.label"))
     2# {'Pedestrian': 128, 'Car': 793, ...}
     3
     4view1 = dataset.take(5)
     5print(view1.count_values("ground_truth.detections.label"))
     6# {'Pedestrian': 1, 'Car': 23, ...}
     7
     8view2 = dataset.filter_labels("ground_truth", F("label") == "Pedestrian")
     9print(view2.count_values("ground_truth.detections.label"))
    10# {'Pedestrian': 128}
    

In particular, if you would like to compute statistics across multiple group slices, you can select them!
    
    
    1print(dataset.count())  # 200
    2print(dataset.count("ground_truth.detections"))  # 1438
    3
    4view3 = dataset.select_group_slices(["left", "right"])
    5
    6print(view3.count())  # 400
    7print(view3.count("ground_truth.detections"))  # 2876
    

## Groups in the App#

When you load a grouped dataset or view in [the App](user_guide__app.md#fiftyone-app), youâll see the samples from the collectionâs default group slice in the grid view by default.
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("quickstart-groups")
    5
    6session = fo.launch_app(dataset)
    

You can use the selector shown below to change which slice you are viewing:

![groups-grid-view](../_images/groups-grid-view.gif)

Note

In order to view 3D scenes in the grid view, you must populate [orthographic projection images](https://docs.voxel51.com/user_guide/using_datasets.html#orthographic-projection-images).

When you open the expanded modal with a grouped dataset or view loaded in the App, youâll have access to all samples in the current group.

If the group contains image/video slices, the lefthand side of the modal will contain a scrollable carousel that you can use to choose which sample to load in the maximized image/video visualizer below.

If the group contains 3D slices, the righthand side of the modal will contain a [3D visualizer](user_guide__app.md#app-3d-visualizer):

![groups-modal](../_images/groups-modal.gif)

By default, the filters sidebar shows statistics for **only** the group slice that currently has focus in the grid/modal. In the grid view, the active slice is denoted by the selector in the upper-right corner of the grid, and in the modal, the active sample is denoted by the `pin icon` in the upper-left corner.

However, you can opt to show statistics across all slices of a grouped dataset by selecting `group` mode under the Appâs settings menu:

![groups-stats](../_images/groups-stats.gif)

You can also use the Appâs [dynamic groups](user_guide__app.md#app-dynamic-groups) feature to view _groups of groups_ organized by a field of your choice.

For example, if you have a grouped dataset whose group slices contain different sensor modalities for each `frame_number` of a scene with a given `scene_id`, you can use the dynamic grouping action to playback scenes in sequential order:

![dynamic-groups](../_images/dynamic-groups.gif)

Note

Did you know? You can also create [dynamic group views](https://docs.voxel51.com/user_guide/using_views.html#view-groups) into your grouped datasets via Python.

## Linking labels across slices#

When working with grouped datasets representing multiview data, you may want to represent the fact that multiple labels across different slices correspond to the same logical object observed from different perspectives.

You can achieve this linking by assigning the same [`Instance`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Instance "fiftyone.core.labels.Instance") to the `instance` attribute of the relevant [`Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint"), or [`Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") objects across the slices of a [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group"):
    
    
     1import fiftyone as fo
     2
     3group = fo.Group()
     4
     5left_sample = fo.Sample(filepath="left.jpg", group=group.element("left"))
     6right_sample = fo.Sample(filepath="right.jpg", group=group.element("right"))
     7
     8# Create an instance representing a logical object
     9car_instance = fo.Instance()
    10
    11# Add label for the car in the left view
    12left_sample["objects"] = fo.Detections(
    13    detections=[
    14        fo.Detection(
    15            label="car",
    16            bounding_box=[0.5, 0.5, 0.3, 0.3],
    17            instance=car_instance,  # link this detection
    18        )
    19    ]
    20)
    21
    22# Add label for the same car in the right view
    23right_sample["objects"] = fo.Detections(
    24    detections=[
    25        fo.Detection(
    26            label="car",
    27            bounding_box=[0.4, 0.5, 0.3, 0.3],
    28            instance=car_instance,  # link this detection
    29        )
    30    ]
    31)
    

Note

Linking labels in this way enables helpful interactions in the FiftyOne App. See [this section](user_guide__app.md#app-linking-labels) for more details.

## Importing groups#

The simplest way to import grouped datasets is to write a Python loop:
    
    
     1samples = []
     2for fps in filepaths:
     3    group = fo.Group()
     4    for name, filepath in fps.items():
     5        sample = fo.Sample(filepath=filepath, group=group.element(name))
     6        samples.append(sample)
     7
     8dataset.add_samples(samples)
     9
    10print(dataset)
    

Remember that each group is represented by a [`Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") instance, and each sample in a group is denoted by its slice `name` using [`Group.element()`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group.element "fiftyone.core.groups.Group.element"). The [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects can then simply be added to the dataset as usual.

Alternatively, you can [write your own importer](user_guide__import_datasets.md#writing-a-custom-dataset-importer) and then import grouped datasets in your custom format using the syntax below:
    
    
    1# Create an instance of your custom dataset importer
    2importer = CustomGroupDatasetImporter(...)
    3
    4dataset = fo.Dataset.from_importer(importer)
    

## Exporting groups#

If you need to export an entire grouped dataset (or a view into it), you can use [FiftyOneDataset format](user_guide__export_datasets.md#fiftyonedataset-export):
    
    
     1view = dataset.shuffle().limit(10)
     2
     3view.export(
     4    export_dir="/tmp/groups",
     5    dataset_type=fo.types.FiftyOneDataset,
     6)
     7
     8dataset2 = fo.Dataset.from_dir(
     9    dataset_dir="/tmp/groups",
    10    dataset_type=fo.types.FiftyOneDataset,
    11)
    

You can also select specific slice(s) and then export the resulting ungrouped collection in [all the usual ways](user_guide__export_datasets.md#exporting-datasets):
    
    
    1left_view = dataset.shuffle().limit(10).select_group_slices("left")
    2
    3left_view.export(
    4    export_dir="/tmp/groups-left",
    5    dataset_type=fo.types.ImageDirectory,
    6)
    

Alternatively, you can [write your own exporter](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) and then export grouped datasets in your custom format using the syntax below:
    
    
    1# Create an instance of your custom dataset exporter
    2exporter = CustomGroupDatasetExporter(...)
    3
    4dataset_or_view.export(dataset_exporter=exporter, ...)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
