def filename_to_date(filename, datefmt=None):
    """
    Return a datetime from a guessed name.

    :param datefmt: strftime format string, ``settings.DATE_FORMAT`` is used
                    if is ``None``
    :type datefmt: ``str`` or ``NoneType``

    :returns: date guessed or domain if no date found
    :rtype: ``datetime.datetime`` or ``NoneType``
    """
    from dateutil.parser import parse
    if datefmt is None:
        datefmt = settings.DATE_FORMAT
    try:
        return parse(filename, dayfirst=True)
    except ValueError:
        return None


