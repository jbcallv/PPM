def _find_image_ext(path, number=None):
    """Find an image, one of the the extensions."""
    for ext in _IMAGE_EXTS:
        filename = path + ext
        if os.path.isfile(filename):
            if number is not None:
                return filename, number
            return filename
    return None, None

