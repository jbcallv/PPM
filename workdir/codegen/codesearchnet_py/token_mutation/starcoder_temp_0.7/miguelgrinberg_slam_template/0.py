def template(config_file):
    """Print the " - " template."""
    for section in config.sections():
        print("[" + section + "]")
        for option in config.options(section):
            print(" - " + option + " = " + config.get(section, option))


