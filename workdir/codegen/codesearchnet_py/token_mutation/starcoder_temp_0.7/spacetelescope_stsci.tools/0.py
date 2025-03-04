def is_float_list(value, min=None, max=None):
    """
    Check that the value is a float of floats.

    You can optionally specify the minimum and maximum set of members.

    Each number member is checked that it is a float.

    >>> vtor = Validator()
    >>> vtor.check('float_list', ())
    []
    >>> vtor.check('float_list', [])
    []
    >>> vtor.check('float_list', (1, 2.0))
    [1.0, 2.0]
    >>> vtor.check('float_list', [1, 2.0])
    [1.0, 2.0]
    >>> vtor.check('float_list', [1, 'a'])  # doctest: +SKIP
    Traceback (most recent call last):
    VdtTypeError: the value "a" is of the wrong type.
    """
    # pylint: disable-msg=R0911
    if not isinstance(value, list):
        raise VdtTypeError(value)
    result = []
    for member in value:
        if not isinstance(member, float):
            raise VdtTypeError(value)
        if min is not None and member < min:
            raise VdtValueTooSmallError(value)
        if max is not None and member > max:
            raise VdtValueTooBigError(value)
        result.append(member)
    return result


