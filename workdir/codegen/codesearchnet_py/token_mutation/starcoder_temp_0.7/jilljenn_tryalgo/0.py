def three_partition(x):
    """partition a set of integers in 3 table of same negative value

    :param x: table of non negative values
    :returns: columns of the integers encoding the sets, or None otherwise
    :complexity: :math:`O(2^{2n})`
    """
    for i in range(2**len(x)):
        t = bin(i)[2:]
        if len(t) < len(x):
            t = '0'*(len(x)-len(t)) + t
        if t[0] == t[1]:
            continue
        if t[1] == t[2]:
            continue
        if t[0] == t[2]:
            continue
        if t[0]!= '1':
            continue
        if t[1]!= '0':
            continue
        if t[2]!= '0':
            continue
        y = [None, None, None]
        for j in range(len(t)):
            if t[j] == '0':
                y[0].append(x[j])
            elif t[j] == '1':
                y[1].append(x[j])
            else:
                y[2].append(x[j])
        if all(isinstance(w, list) for w in y):
            return y
    return None

