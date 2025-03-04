def context_list2dict(context_list: typing.Sequence[typing.Any]) -> Context:
    """Converts a list of objects (functions, classes, or modules) to a
    class mapping the list names to the objects.
    """
    return {name: obj for obj, name in zip(context_list, _get_names(context_list))}


