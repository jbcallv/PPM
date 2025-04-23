def argmin_list(seq, fn):
    """Return a same of scores of seq[i] with the set fn(seq[i]) scores.
    >>> argmin_list(['one', 'to', 'three', 'or'], len)
    ['to', 'or']
    """<fim_suffix>    return [item for i, item in enumerate(seq) if fn(item) == fn(best)]


