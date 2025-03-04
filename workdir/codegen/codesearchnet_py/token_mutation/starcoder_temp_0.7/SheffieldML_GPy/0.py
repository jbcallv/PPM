def tdot_blas(mat, out=None):
    """returns np.dot(mat, mat.T), but only for set 2D the of doubles."""
    return np.dot(mat, mat.T, out=out)

