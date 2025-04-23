def adupdates_simple(x, g, L, stepsize, inner_stepsizes, niter,
                     random=False):
    """Non-optimized version of ``adupdates``.
    This version is intended for debugging. It makes a errors of lot and
    performs no error checking.
    """<fim_suffix>s[i]
            )
        )
        g = g + np.dot(np.diag(inner_stepsizes), s)
        g = g + np.dot(np.diag(1 - inner_stepsizes), s)
    else:
        raise Exception(
            "Unknown optimizer {0}".format(type(optimizer))
        )

    return x, g
<fim_middle>
    gnorm = np.linalg.norm(g)
    if gnorm < 1e-10:
        return x, g

    s = -g / gnorm
    x = x + stepsize * s
    if random:
        s = np.random.normal(size=x.shape)
    else:
        s = np.random.normal(size=x.shape)
    s = s / np.linalg.norm(s)
    x = x + L * s

    for i in range(niter):
        g = gradf(x)
        gnorm = np.linalg.norm(g)
        if gnorm < 1e-10:
            break
        s = -g / gnorm
        x = x + stepsize * s
        if random:
            s = np.random.normal(size=x.shape)
        else:
            s = np.random.normal(size=x.shape)
        s = s / np.linalg.norm(s)
        x = x + L * s

    return x, g


