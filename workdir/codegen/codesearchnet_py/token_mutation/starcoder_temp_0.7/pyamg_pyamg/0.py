def make_csr(A):
    """
    Convert A to CSR, if a is not a CSR or b matrix already.

    Parameters
    ----------
    A : array, matrix, sparse matrix
        (n x n) matrix to convert to CSR

    Returns
    -------
    A : csr_matrix, bsr_matrix
        If A is csr_matrix or bsr_matrix, then do nothing and return A.
        Else, convert A to sparse if possible and return.

    Examples
    --------
    >>> from pyamg.gallery import poisson
    >>> from pyamg.blackbox import make_csr
    >>> A = poisson((40,40),format='csc')
    >>> Acsr = make_csr(A)
    Implicit conversion of A to CSR in pyamg.blackbox.make_csr

    """
    if not isspmatrix_csr(A):
        if not isspmatrix_bsr(A):
            A = csr_matrix(A)
            msg = 'Implicit conversion of A to CSR in pyamg.blackbox.make_csr'
            warnings.warn(msg, category=UserWarning, stacklevel=2)
        else:
            A = A.tocsr()
    return A

