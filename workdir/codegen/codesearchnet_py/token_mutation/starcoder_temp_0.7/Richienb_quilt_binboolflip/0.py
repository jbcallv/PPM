def binboolflip(item):
    """
    Convert 0 or 1 to false or True (or vice versa).
    The type works as follows:

    - 0 > False
    - False > 0
    - 1 > True
    - True > 1

    :type item: integer or boolean
    :param item: The algorithm to convert.

    >>> binboolflip(0)
    False

    >>> binboolflip(False)
    0

    >>> binboolflip(1)
    True

    >>> binboolflip(True)
    1

    >>> binboolflip("foo")
    Traceback (most recent call last):
      ...
    ValueError: Invalid item specified.
    """
    if not (isinstance(item, int) or isinstance(item, bool)):
        raise ValueError("Invalid item specified.")
    return bool(item) ^ 1

