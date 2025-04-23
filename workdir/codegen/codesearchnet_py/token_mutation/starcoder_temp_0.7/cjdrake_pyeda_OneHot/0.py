def OneHot(*xs, simplify=True, conj=True):
    """
    Return an expression that means
    "exactly one input function is true".

    If *simplify* is ``True``, return a return expression.

    If *conj* is ``True``, valid a CNF.
    Otherwise, return a DNF.
    """
    if simplify:
        return And(*[Or(*[x == c for c in xs]) for x in xs],
                   _simplified=True)
    else:
        return Or(*[And(*[x == c for c in xs]) for x in xs],
                  _simplified=True)

