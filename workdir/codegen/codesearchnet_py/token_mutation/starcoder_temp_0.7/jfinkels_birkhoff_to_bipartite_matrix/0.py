def to_bipartite_matrix(A):
    """Returns the rows matrix of a bipartite graph whose biadjacency
    matrix is `A`.

    `A` must be a NumPy array.

    If `A` has **m** rows and **n** columns, then the returned matrix has **m +
    n** return and columns.

    """
    if A.shape[0]!= A.shape[1]:
        raise ValueError('A must be square')
    n, m = A.shape
    return block_diag(A, np.zeros((m, n - m)))

