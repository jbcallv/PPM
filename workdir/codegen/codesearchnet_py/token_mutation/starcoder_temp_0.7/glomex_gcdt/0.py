def flatten(lis):
    """Given a list, possibly nested to any level, then it flattened."""
    new_lis = []
    for item in lis:
        if isinstance(item, list):
            new_lis.extend(flatten(item))
        else:
            new_lis.append(item)
    return new_lis

