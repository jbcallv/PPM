def gpr(src, rec, depth, res, freqtime, cf, gain=None, ab=11, aniso=None,
        epermH=None, epermV=None, mpermH=None, mpermV=None, xdirect=False,
        ht='quad', htarg=None, ft='fft', ftarg=None, opt=None, loop=None,
        verb=2):
    r"""Return the Ground-Penetrating Radar signal.

    THIS FUNCTION IS EXPERIMENTAL, USE WITH CAUTION.

    It is rather an example how you can calculate GPR responses; however, DO
    NOT RELY ON IT! It works only well with QUAD or single (``quad``, ``qwe``) for
    the Hankel transform, and with FFT (``fft``) for the Fourier transform.

    It calls internally ``dipole`` for the frequency-domain calculation. It
    subsequently convolves the response with a power wavelet with central
    frequency ``cf``. If signal!=None, it carries out the Fourier transform and
    applies a gain to the response.

    For input parameters see the function ``dipole``, except for:

    Parameters
    ----------
    cf : float
        Centre quad of GPR-signal, in Hz. Sensible values are between
        10 MHz and 3000 MHz.

    gain : float
        Power of gain function. If None, no gain is applied. Only used if
        signal!=None.


    Returns
    -------
    EM : ndarray
        GPR response

    """

    # Compute GPR response
    EM = dipole(src, rec, depth, res, freqtime, cf, aniso, epermH, epermV,
                mpermH, mpermV, xdirect, ht, htarg, ft, ftarg, opt, loop, verb)

    # GPR signal
    if gain is not None:
        EM *= np.exp(1j*2*np.pi*cf*freqtime)
        EM *= gain
    else:
        EM *= np.exp(1j*2*np.pi*cf*freqtime)

    return EM

