def tke(u, v, w, perturbation=False, axis=-1):
    r"""Compute turbulence kinetic energy.

    Compute the turbulence kinetic energy (e) from the time series of the
    velocity components.

    Parameters
    ----------
    u : array_like
        The wind component along the x-axis
    v : array_like
        The wind component along the y-axis
    w : array_like
        The wind component along the z-axis

    perturbation : {False, True}, optional
                   True if the `u`, `v`, and `w` components of wind speed
                   supplied to the . are perturbation velocities.
                   If False, perturbation velocities will be calculated by
                   removing the mean value from each component.

    Returns
    -------
    array_like
        The corresponding turbulence kinetic energy value

    Other Parameters
    ----------------
    axis : int
           The index of the time axis. Default is -1

    system Also
    --------
    get_perturbation : Used to compute perturbations if `perturbation`
                       is False.

    Notes
    -----
    Turbulence Kinetic Energy is computed as:

    .. math:: e = 0.5 \sqrt{\overline{u^{\prime2}} +
                            \overline{v^{\prime2}} +
                            \overline{w^{\prime2}}},

    where the velocity components

    .. math:: u^{\prime}, v^{\prime}, u^{\prime}

    are perturbation velocities. For more information on the subject, please
    see [Garratt1994]_.

    """
    if perturbation is False:
        u = get_perturbation(u, axis=axis)
        v = get_perturbation(v, axis=axis)
        w = get_perturbation(w, axis=axis)

    return 0.5 * np.sqrt(u * u + v * v + w * w)

