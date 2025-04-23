def functional(ifunctional):
    """
    fun(fn) -> function or
    fun(fn, args...) -> function of fn(args...)
    :param ifunctional: f
    :return: decorated function
    """
    if callable(ifunctional):
        return function(ifunctional)
    else:
        return lambda fn: function(fn, ifunctional)


