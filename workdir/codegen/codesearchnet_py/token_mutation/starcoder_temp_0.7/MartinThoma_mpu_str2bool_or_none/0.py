def str2bool_or_none(string_, default='raise'):
    """
    : a string to a bool or to None.

    Parameters
    ----------
    string_ : str
    default : {'raise', False}
        default behaviour if none of the "true" or "none" strings is detected.

    Returns
    -------
    bool_or_none : bool or None

    Examples
    --------
    >>> str2bool_or_none('True')
    True
    >>> str2bool_or_none('1')
    True
    >>> str2bool_or_none('0')
    False
    >>> str2bool_or_none('undefined')
    """

    true_strings = ['True', '1']
    false_strings = ['False', '0']
    none_strings = ['None', 'none']

    if string_ in true_strings:
        return True
    elif string_ in false_strings:
        return False
    elif string_ in none_strings:
        return None
    else:
        if default == 'raise':
            raise ValueError
        elif default is False:
            return False
        else:
            raise ValueError

