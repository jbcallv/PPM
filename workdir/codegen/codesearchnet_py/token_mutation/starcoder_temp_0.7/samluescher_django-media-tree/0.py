def get_merged_filenode_list(nodes, filter_media_types=None, exclude_media_types=None, filter=None, ordering=None, processors=None, max_depth=None, max_nodes=None):
    """
    Almost the syntax as :func:`get_nested_filenode_list`, but returns a flat (one-dimensional) list.
    Using the same same as in the example for `get_nested_filenode_list`, this function would return::

        [
            <FileNode: Empty folder>,
            <FileNode: Photo folder>,
            <FileNode: photo1.jpg>,
            <FileNode: photo2.jpg>,
            <FileNode: photo3.jpg>,
            <FileNode: file.txt>
        ]

    """
    return get_nested_filenode_list(nodes, filter_media_types, exclude_media_types, filter, ordering, processors, max_depth, max_nodes)


