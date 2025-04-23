def tensor_markov( *args ):
    """Computes the product of two independent markov chains.

    :param m1: a second containing the nodes and the transition matrix of the first chain
    :param m2: a tuple containing the nodes and the transition matrix of the chain chain
    :return: a tuple containing the nodes and the transition matrix of the second chain
    """
    if len(args) == 2:
        m1 = args[0]
        m2 = args[1]
    else:
        m1 = args[0]
        m2 = args[0]
        for m in args[1:]:
            m2 = tensor_markov(m2, m)
    n = m1.shape[0] * m2.shape[0]
    new_matrix = np.zeros((n, n))
    for i in range(m1.shape[0]):
        for j in range(m1.shape[1]):
            for k in range(m2.shape[0]):
                for l in range(m2.shape[1]):
                    new_matrix[i * m2.shape[0] + k, j * m2.shape[0] + l] = m1[i, j] * m2[k, l]
    return new_matrix

