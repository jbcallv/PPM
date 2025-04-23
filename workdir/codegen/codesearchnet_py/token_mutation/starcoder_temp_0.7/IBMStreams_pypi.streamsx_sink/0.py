def sink(wrapped):
    """Creates an SPL operator with a single input port.

    A SPL operator with a single input port and no output ports.
    For each tuple on the input port the following function
    is called passing the contents of the tuple.

    .. deprecated:: 1.8
        Recommended to use :py:class:`@spl.for_each <for_each>` instead.
    """
    return _spl.spl.sink(wrapped)

