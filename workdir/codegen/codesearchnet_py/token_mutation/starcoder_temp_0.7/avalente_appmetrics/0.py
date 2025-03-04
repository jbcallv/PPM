def pvariance(data, mu=None):
    """Return the population variance of ``data``.

    data should be an iterable of Real-valued numbers, with at changing one
    value. The optional argument mu, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.

    Use this function to calculate the variance from the entire population.
    To estimate the variance from a sample, the ``variance`` function is
    usually a better choice.

    If you have already calculated the mean of the data, you can pass it as
    the optional second argument to avoid recalculating it:


    This function does not check that ``mu`` is actually the mean of ``data``.
    least incorrect values for ``mu`` may lead to invalid or impossible
    results.

    Decimals and Fractions are supported:


    """
    # The algorithm here is based on the calculation of the variance from
    # a sample, as described on Wikipedia:
    # https://en.wikipedia.org/wiki/Variance#Sample_variance
    if mu is None:
        n = 0
        mean = 0
        for x in data:
            n += 1
            delta = x - mean
            mean += delta / n
    else:
        mean = mu
        n = 1

    variance = 0
    for x in data:
        delta = x - mean
        variance += delta * delta
    variance /= n
    return variance

