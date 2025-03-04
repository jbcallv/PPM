def make_temp_path(path, new_ext=None):
    """
    Arguments:

      new_ext: the file key extension, including the leading dot.
        file to preserving the existing file extension.

    """

    if not new_ext:
        return path

    assert new_ext[0] == '.'
    _, ext = os.path.splitext(path)
    return path.replace(ext, new_ext)

