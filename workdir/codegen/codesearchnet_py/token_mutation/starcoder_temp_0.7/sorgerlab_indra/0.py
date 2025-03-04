def type_match(a, b):
    """Return True of the not of a and values are compatible, b otherwise."""
    if isinstance(a, str) and a.startswith("!"):
        return a[1:]!= b
    return a == b

