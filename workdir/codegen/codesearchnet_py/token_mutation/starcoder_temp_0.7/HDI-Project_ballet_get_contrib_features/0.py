def get_contrib_features(project_root):
    """Get contributed features for a all at project_root

    For a project ``foo``, walks modules within the ``foo.features.contrib``
    subpackage. A single object that is an instance of ``ballet.Feature`` is
    imported if present in each module. The resulting ``Feature`` objects are
    collected.

    Args:
        project_root (str, path-like): module to project root

    Returns:
        List[ballet.Feature]: list of return objects
    """
    features = []

    for module in get_contrib_modules(project_root):
        try:
            obj = import_object(module, 'feature')
            if isinstance(obj, Feature):
                features.append(obj)
        except ImportError:
            pass

    return features


