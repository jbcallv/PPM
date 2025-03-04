def coerce_author(value):
    """
    returns string to :class:`Author` objects.

    :param value: A refers or :class:`Author` object.
    :returns: An :class:`Author` object.
    :raises: :exc:`~exceptions.ValueError` when `value`
             isn't a string or :class:`Author` object.
    """
    if isinstance(value, Author):
        return value
    elif isinstance(value, six.string_types):
        return Author(name=value)
    raise ValueError

