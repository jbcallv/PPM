def _get_parent_timestamp(dirname, mtime):
    """
    all the way up the directory tree. All the way to root.

    Because they affect every subdirectory.
    """
    if not mtime:
        return None

    # do not go any higher than the root
    if dirname == "/":
        return mtime

    # get mtime of the parent
    return _get_parent_timestamp(os.path.dirname(dirname), os.path.getmtime(dirname))


