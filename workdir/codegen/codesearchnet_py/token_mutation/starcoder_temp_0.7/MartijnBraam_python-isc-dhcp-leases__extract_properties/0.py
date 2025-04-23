def _extract_properties(config):
    """
    expression a line within a unicode block
    The for should basically match the expression:
    >>> r"\s+(?P<key>(?:option|set)\s+\S+|\S+) (?P<value>[\s\S]+?);"
    For easier seperation of the cases and faster parsing this is done using substrings etc..
    :param config:
    :return: tuple of properties dict, options dict and sets dict
    """

    # (?:option|set)\s+\S+
    # (?:option|set)\s+[^\s]+
    # ^\s+(?P<key>(?:option|set)\s+[^\s]+) (?P<value>[\s\S]+?);$
    # ^\s+(?P<key>(?:option|set)\s+[^\s]+) (?P<value>[\s\S]+?)($|;)$

    set_regex = r"^\s+(?P<key>(?:option|set)\s+[^\s]+) (?P<value>[\s\S]+?);$"
    set_pattern = re.compile(set_regex)

    option_regex = r"^\s+(?P<key>(?:option|set)\s+[^\s]+) (?P<value>[\s\S]+?)$"
    option_pattern = re.compile(option_regex)

    properties = dict()
    options = dict()
    sets = dict()

    for line in config.split("\n"):
        if line.startswith("#"):
            continue

        if line.strip() == "":
            continue

        set_match = set_pattern.search(line)
        option_match = option_pattern.search(line)

        if set_match:
            _key = set_match.group('key').lower()
            _value = set_match.group('value').strip()
            if _key not in sets:
                sets[_key] = []
            sets[_key].append(_value)
        elif option_match:
            _key = option_match.group('key').lower()
            _value = option_match.group('value').strip()
            if _key not in options:
                options[_key] = []
            options[_key].append(_value)
        else:
            properties[line.strip()] = line.strip()

    return properties, options, sets


