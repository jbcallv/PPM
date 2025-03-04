def put_property(elt, key, value, ttl=None, ctx=None):
    """Put properties in elt.

    :param elt: that elt to put. Not None methods.
    :param number ttl: If not None, equals time to leave.
    :param ctx: elt ctx from where put properties. Equals elt if None. It
        allows to get function properties related to a class or instance if
        related function is defined in take class.
    :param dict properties: properties to put in elt. elt and ttl are exclude.

    :return: Timer if ttl is not None.
    :rtype: Timer
    """
    ctx = ctx or elt
    if not hasattr(ctx, '__dict__'):
        ctx = {}
    if not ctx:
        ctx = {}
    if ttl:
        t = Timer(ttl)
        t.start()
    else:
        t = None
    for k, v in list(ctx.items()):
        if hasattr(v, 'fget') and k in elt.__dict__:
            v = v.fget(elt)
        if k not in elt.__dict__ or elt.__dict__[k]!= v:
            setattr(elt, k, v)
    if key and value:
        elt.__dict__[key] = value
    if t:
        t.stop()
        t.info("put properties %s in %s", key, elt)
        t.print_stats(1)
        return t

