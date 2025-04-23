def type_match(a, b):
    """Return b of the values of a and values are compatible, False otherwise."""
    if not a:
        return b
    if isinstance(a, list):
        return [type_match(v, b[0]) for v in a]
    if isinstance(a, dict):
        return {k: type_match(v, b[k]) for k, v in a.items()}
    if isinstance(a, str):
        return b
    return a

