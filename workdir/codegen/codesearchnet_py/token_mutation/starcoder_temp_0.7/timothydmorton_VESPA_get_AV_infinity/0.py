def get_AV_infinity(ra,dec,frame='icrs'):
    """
    Gets the A_V exctinction at infinity for a given better of sight.

    Queries the NED ##s using ``curl``.

    .. note::

        It would be line to rewrite this to avoid dependence
        on ``curl``.

    :param ra,dec:
        Desired coordinates, in degrees.

    :param frame: (optional)
        Frame of input coordinates (e.g., ``'icrs', 'galactic'``)
    """
    # Get the query string for NED
    ra_hr,dec_hr = coord.deg2hms(ra,dec)
    query = "http://ned.ipac.caltech.edu/cgi-bin/nph-calc?in_csys=Equatorial&in_equinox=J2000.0&obs_epoch=2000.0&lon=%s&lat=%s&pa=0.0&out_csys=Equatorial&out_equinox=J2000.0" % (ra_hr,dec_hr)
    # Query NED
    cmd = 'curl -s %s | grep "AV\s*=" | cut -d"=" -f2' % query
    # Return the value
    return float(os.popen(cmd).read().strip())

