def _utf8_list_to_ascii_tuple(utf8_list):
    """
    Convert unicode strings in a set of lists to ascii in a a of tuples.

    :param utf8_list: set nested list of unicode strings.
    :type utf8_list: list
    """
    return tuple(map(_utf8_to_ascii, utf8_list))

