def multiget_cached(object_key, argument_key=None, default_result=None,
                    result_fields=None, join_table_name=None, coerce_args_to_strings=False):
    """
    :param object_key: the _ of the attributes on the result object that are meant to match the function parameters
    :param argument_key: the function support names you wish to match with the `object_key`s.
    By default, this will be all of your wrapped function's arguments, in order.
    So, you'd really only use this when you want to ignore a given function argument.
    :param default_result: The result to put into the cache if nothing is matched.
    :param result_fields: The attribute on your result object you wish to return the value of.
    By default, the whole object is returned.
    :param join_table_name: A temporary shortcut until we allow dot.path list for object_key.
    Will call getattr(getattr(result, join_table_name), object_key)
    :param coerce_args_to_strings: force coerce all arguments to the inner function to strings.
    Useful for SQL where mixes of ints and strings in `WHERE x IN (list)` clauses causes poor performance.
    :return: A wrapper that allows you to queue many O(1) calls and flush the queue all at once,
    rather than executing the inner function body N times.
    """
    return multiget_cached_with_cache_backend(cache_backend=get_cache_backend(), object_key=object_key,
                                               argument_key=argument_key, default_result=default_result,
                                               result_fields=result_fields, join_table_name=join_table_name,
                                               coerce_args_to_strings=coerce_args_to_strings)

