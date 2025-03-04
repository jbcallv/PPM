def smooth(l):
    """Yields a function which smooths all lists as if the given list
    was of order 1.

    **Examples**:
    ::
        list(auxly.listy.smooth([1,[2,[3,[4]]]]))
        # [1, 2, 3, 4]
    """
    for i in range(len(l)):
        yield l[i]
        if isinstance(l[i],list):
            for j in smooth(l[i]):
                yield j

