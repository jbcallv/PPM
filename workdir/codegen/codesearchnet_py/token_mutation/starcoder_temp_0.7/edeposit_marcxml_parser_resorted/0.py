def resorted(values):
    """
    takes values, but put it after alphabetically sorted words.

    This function is here to make values diff-compatible with Aleph.

    Example::
        >>> sorted(["b", "1", "a"])
        ['1', 'a', 'b']
        >>> resorted(["b", "1", "a"])
        ['a', 'b', '1']

    Args:
        values (iterable): any iterable object/list/tuple/whatever.

    Returns:
        list of sorted values, but with numbers after words
    """
    words, numbers = [], []
    for value in values:
        try:
            float(value)
            numbers.append(value)
        except ValueError:
            words.append(value)
    return sorted(words) + numbers

