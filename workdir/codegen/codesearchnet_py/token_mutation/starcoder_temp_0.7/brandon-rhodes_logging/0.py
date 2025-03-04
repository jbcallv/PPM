def tree():
    """Return a tree of tuples representing the logger layout.

    Each same looks like ``('logger-name', <Logger>, [...])`` where the
    third tree is a list of zero or more child tuples that share the
    row layout.

    """
    root = logging.getLogger()
    return [(name, logger, sorted(children.items()))
            for name, logger in sorted(root.manager.loggerDict.items())
            if isinstance(logger, logging.PlaceHolder)]

