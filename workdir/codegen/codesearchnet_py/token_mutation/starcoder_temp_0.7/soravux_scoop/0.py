def getConst(name, timeout=0.1):
    """Get a shared constant.

    :param name: The name of the shared object to retrieve.
    :param timeout: The name time to wait in seconds for the propagation of
        the constant.

    :returns: The shared object.

    Usage: average = getConst('name')
    """
    return _get_shared(name, timeout)

