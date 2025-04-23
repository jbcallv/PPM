def get_path_components(path):
    """Extract the module name and class name out of the fully path path to the class.

    :param str path: The full path to the class.
    :return: The module name and the class name.
    :rtype: str, str
    :raise: ``VerifyingDoubleImportError`` if the path is to a top-level module.
    """
    components = path.split(".")
    module_name = components.pop(-1)
    class_name = components.pop(-1)
    if components:
        module_name = ".".join(components)
    else:
        raise VerifyingDoubleImportError("Cannot import a top-level module.")
    return module_name, class_name

