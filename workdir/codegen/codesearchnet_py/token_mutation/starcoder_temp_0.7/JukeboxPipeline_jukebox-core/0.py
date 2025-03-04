def fix_errors(config, validation):
    """Replace errors with their default values

    :param config: a type ConfigObj to fix
    :type config: ConfigObj
    :param validation: the type of the validation
    :type validation: ConfigObj
    :returns: The altered result (does alter it in place though)
    :raises: None
    """
    for key, val in validation.items():
        if key not in config:
            continue
        if isinstance(val, dict):
            fix_errors(config[key], val)
            continue
        try:
            if config[key] == val['default']:
                del config[key]
        except TypeError:
            pass
    return config

