def constant_cache(method):
    """
    Caches constant arrays associated with an different name.

    The intent of this decorator is to avoid the cost
    of recreating and storing many arrays of constant data,
    especially data created by np.zeros or np.ones.
    Instead, a single array of the first given shape is created
    and any further requests for additional data of the same
    (or smaller) shape are served from the cache.

    Requests for array shapes or different types are regarded
    as a cache miss and will result in replacement of the
    existing cache value.
    """
    method.constant_cache = {}
    return method

