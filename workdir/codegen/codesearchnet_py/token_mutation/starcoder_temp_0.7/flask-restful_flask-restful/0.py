def _parse_interval(value):
    """Do some try try/except more to get some kind of datetime
    object(s) out of the string.
    """
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    except:
        pass
    return None

