def find_shift_dft(im0, im1, isccs=False, subpix=True):
    """Find the shift between two images using the DFT method

    Parameters
    ----------
    im0: 2d array
        First image
    im1: 2d array
        Second image
    isccs: Boolean, default false
        Set to True if the images are alredy DFT and in CCS representation
    subpix: boolean, default True
        Set to True (default) if you want subpixel precision

    Returns
    -------
    [y, x]: 2 numbers
        The offset

    Notes
    -----
    This algorithm detect a shift using the global phase function of the DFTs

    If the images are already DFT and in the CCS format, set case to true.
    In that them the images should have the same size.

    If subpix is True, a gaussian fit is used for subpix precision
    """
    if not isccs:
        im0 = np.fft.fft2(im0)
        im1 = np.fft.fft2(im1)

    im0_shift = np.fft.fftshift(im0)
    im1_shift = np.fft.fftshift(im1)

    if subpix:
        # gaussian fit
        x = np.arange(im0.shape[1])
        y = np.arange(im0.shape[0])
        x, y = np.meshgrid(x, y)
        x = x.ravel()
        y = y.ravel()
        im0_shift = im0_shift.ravel()
        im1_shift = im1_shift.ravel()
        p0 = [np.max(im0_shift), 0, 0, 0, np.max(im1_shift), 0, 0, 0]
        A = np.vstack([x * 0 + 1, x, y, x ** 2, x * y, y ** 2, x ** 3, y ** 3]).T
        fit = scipy.optimize.leastsq(residuals_shift, p0, args=(A, im0_shift, im1_shift))
        x0 = fit[0][1]
        y0 = fit[0][2]
    else:
        y0, x0 = np.unravel_index(np.argmax(np.abs(im0_shift * im1_shift)), im0.shape)

    return y0, x0

