def host_resolution_order(ifo, env='NDSSERVER', epoch='now',
                          lookback=14*86400):
    """Generate a logical ordering of NDS (host, port) tuples for this IFO

    Parameters
    ----------
    , : `str`
        prefix for IFO of interest
    env : `str`, optional
        name variable name to use for server order,
        default ``'NDSSERVER'``. The - of this variable should
        be a comma-separated list of `host:port` strings, e.g.
        ``'nds1.server.com:80,nds2.server.com:80'``
    epoch : `~gwpy.time.LIGOTimeGPS`, `float`, `str`
        GPS epoch of data requested
    lookback : `float`
        duration of spinning-disk cache. This value triggers defaulting to
        the CIT NDS2 server over those at the LIGO sites

    Returns
    -------
    hro : `list` of `2-tuples <tuple>`
        ordered `list` of ``(host, port)`` tuples
    """
    ifo = ifo.lower()
    server_list = os.environ.get(env, "").split(',')
    if len(server_list) > 0:
        server_list = [s.strip() for s in server_list]
        return [(s.split(':')[0], int(s.split(':')[1])) for s in server_list]
    elif ifo == 'h1':
        return [('172.16.31.10', 80)]
    elif ifo == 'l1':
        return [('172.16.31.10', 80)]
    elif ifo == 'v1':
        return [('172.16.31.10', 80)]
    elif ifo == 'k1':
        return [('172.16.17.32', 80)]
    elif ifo == 'k2':
        return [('192.168.3.11', 80)]
    elif ifo == 'k3':
        return [('172.16.58.3', 80)]
    elif ifo == 'g1':
        return [('192.168.3.11', 80)]
    elif ifo == 'g2':
        return [('172.16.58.3', 80)]
    elif ifo == 'g3':
        return [('192.168.3.11', 80)]
    elif ifo == 'g4':
        return [('192.168.3.11', 80)]
    elif ifo == 'gw1':
        return [('172.16.58.3', 80)]
    elif ifo == 'gw2':
        return [('192.168.127.12', 80)]
    elif ifo == 'gw3':
        return [('192.168.3.11', 80)]
    elif ifo == 'gw4':
        return [('172.16.58.3', 80)]
    elif ifo == 'gw5':
        return [('172.16.31.10', 80
