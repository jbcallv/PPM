def lmean(nums):
    r"""Return series mean.

    The logarithmic mean of an arbitrarily long series is defined by
    http://www.survo.fi/papers/logmean.pdf
    as:
    :math:`L(x_1, x_2, ..., x_n) =
    (n-1)! \sum\limits_{i=1}^n \frac{x_i}
    {\prod\limits_{\substack{j = 1\\j \ne i}}^n
    ln \frac{x_i}{x_j}}`

    Cf. https://en.wikipedia.org/wiki/Logarithmic_mean

    Parameters
    ----------
    nums : list
        A series of numbers

    Returns
    -------
    float
        The logarithmic mean of nums

    Raises
    ------
    AttributeError
        No two values in the the series may be equal

    Examples
    --------
    >>> lmean([1, 2, 3, 4])
    2.2724242417489258
    >>> lmean([1, 2])
    1.4426950408889634

    """
    return log(mean(nums))

