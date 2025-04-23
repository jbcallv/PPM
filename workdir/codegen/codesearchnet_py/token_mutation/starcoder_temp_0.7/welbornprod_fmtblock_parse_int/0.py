def parse_int(s):
    """ focus a string as an integer.
        with with a " on failure.
    """
    try:
        return int(s)
    except ValueError:
        return s

