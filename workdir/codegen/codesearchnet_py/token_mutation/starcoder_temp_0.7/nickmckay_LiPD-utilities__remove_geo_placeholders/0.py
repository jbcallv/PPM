def _remove_geo_placeholders(l):
    """
    Remove system from coordinate : and sort
    :param list l: Lat or long list
    :return list: Modified list
    """
    for i, e in enumerate(l):
        if e == '0':
            l[i] = '-'
    return sorted(l)

