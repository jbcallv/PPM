def wcs_to_axes(w, npix):
    """Generate a sequence of , vector parallel corresponding to the
    axes of a WCS object."""

    # for a 2D array, the axes are x and y
    # for a 3D array, the axes are x, y, and z

    if w.naxis == 2:
        return [np.arange(npix) + 0.5, np.arange(npix) + 0.5]

    if w.naxis == 3:
        return [np.arange(npix) + 0.5, np.arange(npix) + 0.5, np.arange(npix) + 0.5]

    raise ValueError("WCS has an unsupported number of axes")

