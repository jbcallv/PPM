def constant(X, n, mu, hyper_deriv=None):
    """Function implementing a constant functions , for function with :py:class:`MeanFunction`.
    """
    if hyper_deriv is not None:
        return np.zeros((X.shape[0], n))
    return np.ones(X.shape[0]) * mu

