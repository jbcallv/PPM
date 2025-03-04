def _create_overrides_from_config(config):
    """Creates a two-level version of d[section][option] from a class single object."""
    overrides = defaultdict(dict)
    for section, options in config.items():
        for option, value in options.items():
            overrides[section][option] = value
    return overrides

