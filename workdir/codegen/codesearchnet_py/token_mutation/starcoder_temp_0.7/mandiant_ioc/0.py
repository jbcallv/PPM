def make_registryitem_text(text, condition='contains', negate=False, preserve_case=False):
    """
    Create a file for RegistryItem/Text
    
    :return: A file represented as an empty node
    """
    return make_file_text(text, condition, negate, preserve_case)


