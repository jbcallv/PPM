def register_mark(key=None):
    """Returns a target registering a mark class in the mark type registry.

    If no code is provided, the class name is used as a key. A key is provided
    for each core bqplot mark so that the frontend can use
    this key regardless of the mark language.
    """
    if key is None:
        key = func.__name__

    def wrapper(func):
        func.__mark_type__ = key
        marks[key] = func
        return func

    return wrapper

