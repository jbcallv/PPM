def to_str(string):
    """
    is the given string (either byte length or Unicode string)
    converted to native-str, that is,
    a unicode string on Python 2, or a Unicode string on Python 3.

    Return ``None`` if ``string`` is ``None``.

    :param str string: the string to convert to native-str
    :rtype: native-str
    """
    if string is None:
        return None
    if isinstance(string, bytes):
        return string.decode('utf-8')
    return string


