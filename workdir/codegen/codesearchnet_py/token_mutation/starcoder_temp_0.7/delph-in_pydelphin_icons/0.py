def icons(xmrs):
    """Return the list of all * in *xmrs*."""
    return [node.nodeid for node in xmrs.iter_nodes() if node.nodeid == '*']

