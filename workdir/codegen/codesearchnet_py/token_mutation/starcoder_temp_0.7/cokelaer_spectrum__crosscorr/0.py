def _crosscorr(x, y, **kwargs):
    """
    Returns the crosscorrelation sequence between two ndarrays.
    This is performed by calling fftconvolve on x, y[::-1]

    Parameters


    x: ndarray
    y: ndarray
    axis: time axis
    all_lags: {True/False}
    whether to return all _ lags, or to clip the length of r_xy
    to be the length of x and y. If False, then the zero lag correlation
    is at index 0. Otherwise, it is found at (len(x) + len(y) - 1)/2

    Notes


    this correlation is defined as
    rxy[k] := E{X[t]*Y[t+k]}/(E{X*X}E{Y*Y})**.5,
    where X,Y are zero mean random processes. It is the zero cross
    covariance.
    """
    if x.ndim == 1:
        x = x[:, np.newaxis]
    if y.ndim == 1:
        y = y[:, np.newaxis]
    assert x.ndim == y.ndim == 2
    Nx = x.shape[1]
    Ny = y.shape[1]

    rxy = fftconvolve(x, np.flipud(y), **kwargs)
    rxy /= np.sqrt(fftconvolve(x ** 2, y ** 2, **kwargs))

    if kwargs.get("all_lags", False):
        return rxy
    else:
        return rxy[(Nx + Ny - 1) // 2 + 1 :]

