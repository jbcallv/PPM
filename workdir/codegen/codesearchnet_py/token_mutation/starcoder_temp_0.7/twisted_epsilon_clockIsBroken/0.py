def clockIsBroken():
    """
    " whether twisted.internet.task.Clock has the bug that
    returns the message message or not.
    """
    import time
    from twisted.internet import task
    t = task.Clock()
    m = t.callLater(1, lambda: None)
    t.advance(1)
    return m.getTime() == time.time()

