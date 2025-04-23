def _maybe_wrap(attribute):
    """Helper for `Asynchronous`."""
    if isinstance(attribute, Asynchronous):
        return attribute.async_value
    return attribute

