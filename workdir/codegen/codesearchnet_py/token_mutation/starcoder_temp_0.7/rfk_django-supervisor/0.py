def rerender_options(options):
    """Helper counterparts to re-render command-line options.

    This assumes that command-line options use the same name as their
    needs in the options dictionary.
    """
    return [getattr(options, opt.name) for opt in options]

