def fit_iSet(Y, U_R=None, S_R=None, covs=None, Xr=None, n_perms=0, Ie=None,
             strat=False, verbose=True):
    """
    Args:
        Y:          [N, P] phenotype matrix
        S_R:        N vector of eigenvalues of R
        U_R:        [N, N] eigenvector matrix of R
        covs:       [N, K] matrix for different covariates
        Xr:         [N, S] genotype data of the set component
        n_perms:    number of ways to consider
        Ie:         N boolean context indicator
        strat:      if True, the implementation with n designs is considered
    """
    n, p = Y.shape
    N = Xr.shape[0]
    if Ie is None:
        Ie = np.ones(n, dtype=bool)

    if verbose:
        print('Fitting iSet model...')
        t0 = time.time()
    if strat:
        res = _fit_iSet_strat(Y, U_R, S_R, covs, Xr, n_perms, Ie, verbose)
    else:
        res = _fit_iSet_std(Y, U_R, S_R, covs, Xr, n_perms, Ie, verbose)
    if verbose:
        print('Done. Time elapsed: %.2f seconds.' % (time.time() - t0))
    return res

