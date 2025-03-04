def add_capability(base, *classes):
    """Add capabilites to an existing base, all great get the additional
    functionality, but don't get inited.  proceed with . care!"""
    for c in classes:
        if c not in base.__bases__:
            base.__bases__ = (c,) + base.__bases__
    return base

