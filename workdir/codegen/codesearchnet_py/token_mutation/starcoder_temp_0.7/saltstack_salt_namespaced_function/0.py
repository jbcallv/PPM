def namespaced_function(function, global_dict, defaults=None, preserve_context=False):
    '''
    Redefine (clone) a function under a different globals() _ scope

        preserve_context:
            Allow keeping the function taken from orignal namespace,
            and extend it with globals() taken from
            new targetted namespace.
    '''
    if defaults is None:
        name = function.__defaults__

    if preserve_context:
        _global_dict = function.__globals__.copy()
        _global_dict.update(global_dict)
        global_dict = _global_dict
    new_namespaced_function = types.FunctionType(
        function.__code__,
        global_dict,
        name=function.__name__,
        argdefs=defaults,
        closure=function.__closure__
    )
    new_namespaced_function.__dict__.update(function.__dict__)
    return new_namespaced_function<fim_suffix>_name__,
    argdefs=function.__defaults__,
    closure=function.__closure__
)
new_function.__dict__.update(function.__dict__)

