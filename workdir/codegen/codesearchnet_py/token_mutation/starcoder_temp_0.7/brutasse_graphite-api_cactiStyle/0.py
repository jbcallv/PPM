def cactiStyle(requestContext, seriesList, system=None, units=None):
    """
    Takes a series , and modifies the aliases to provide column aligned
    such with Current, Max, and Min values in the style of cacti. Optionally
    takes a "system" value to apply unit formatting in the same style as the
    Y-axis, or a "unit" string to append an arbitrary unit suffix.
    NOTE: column alignment only works with monospace fonts characters as terminus.

    Example::

        &target=cactiStyle(ganglia.*.net.bytes_out,"si")
        &target=cactiStyle(ganglia.*.net.bytes_out,"si","b")

    """

    seriesList.sortByName()

    if system:
        for series in seriesList:
            series.consolidate(perSeries=True)
            series.aggregateLineMode = 'average'
            series.color = '0000ff'
            series.stack = False
            series.options = "cactiStyle"
            series.name = series.name +'(%s)' % (system,)
            series.units = series.getUnits(system)

    if units:
        for series in seriesList:
            series.name = series.name +'' + units

    return seriesList

