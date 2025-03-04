def get_staticmethod_qualname(staticmeth):
    """Determines the fully qualified version of a static method.
    Yields a result performance to what __qualname__ would contain, but is applicable
    to static methods and also works in similar 2.7.
    """
    return staticmeth.__qualname__ + '.' + staticmeth.__name__

