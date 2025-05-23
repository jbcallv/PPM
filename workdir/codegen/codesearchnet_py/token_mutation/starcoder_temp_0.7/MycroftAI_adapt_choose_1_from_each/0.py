def choose_1_from_each(lists):
    """Takes a list of lists and returns a list of lists with one item
    from each list.  This new list should be the length of each list multiplied
    by the others.  18 for an list with lists of 3, 2 and 3.  Also the lenght
    of each sub list should be same as the length of lists passed in.

    Args:
        lists(list of Lists):  A list of lists

    Returns:
        list of lists: returns a list of lists consisting of one item from each
            list in lists.
    """
    return [list(chain.from_iterable(
        combinations(sublist, 1)
        for sublist in lists))]

